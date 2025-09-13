#!/usr/bin/env python3
"""
OLED Display for Clover Selfcheck on Raspberry Pi 5
Shows system status on SSD1306 OLED display as a ROS node.
"""

import os
import sys
import time
import subprocess
import threading
import re
from datetime import datetime
# ROS
try:
    import rospy
except Exception:
    rospy = None
import shutil
import socket
# PIL may be absent on first boot; import lazily inside class

# Try different OLED libraries (prefer luma by default; override with OLED_BACKEND)
OLED_LIBRARY = None
OLED_BACKEND = os.environ.get('OLED_BACKEND', 'auto').lower()

# Try Luma first unless explicitly forced to adafruit
if OLED_BACKEND in ('auto', 'luma'):
    try:
        from luma.core.interface.serial import i2c
        from luma.oled.device import ssd1306
        OLED_LIBRARY = "luma"
    except ImportError:
        OLED_LIBRARY = None

# If not found, try Adafruit
if OLED_LIBRARY is None and OLED_BACKEND in ('auto', 'adafruit'):
    try:
        import board
        import busio
        import adafruit_ssd1306
        OLED_LIBRARY = "adafruit"
    except ImportError:
        OLED_LIBRARY = None

if OLED_LIBRARY is None:
    print("No OLED library available. Install either adafruit-circuitpython-ssd1306 or luma.oled")

# Check if running as service, use appropriate Python path
if os.path.exists('/home/pi/catkin_ws/devel/setup.bash'):
    # Running on actual Clover system
    PYTHON_PATH = '/usr/bin/python3'
else:
    # Development environment
    PYTHON_PATH = 'python3'

class CloverStatusDisplay:
    def __init__(self):
        # Initialize OLED display
        self.display_available = False
        self.device = None
        self.Image = None
        self.ImageDraw = None
        self.ImageFont = None

        if OLED_LIBRARY is None:
            print("No OLED library available")
            return

        try:
            if OLED_LIBRARY == "adafruit":
                # Using Adafruit library (recommended for RPi5)
                i2c_bus = busio.I2C(board.SCL, board.SDA)
                self.device = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c_bus, addr=0x3C)
                self.device.contrast(255)
                self.display_available = True
                print("OLED initialized with Adafruit library")
            elif OLED_LIBRARY == "luma":
                # Using Luma library (fallback)
                serial = i2c(port=1, address=0x3C)
                self.device = ssd1306(serial, rotate=0)
                self.device.contrast(255)
                self.display_available = True
                print("OLED initialized with Luma library")
        except Exception as e:
            print(f"OLED display not available: {e}")
            self.display_available = False
            return

        # Try import PIL lazily
        try:
            from PIL import Image, ImageDraw, ImageFont  # noqa
            self.Image = Image
            self.ImageDraw = ImageDraw
            self.ImageFont = ImageFont
        except Exception as e:
            print(f"PIL not available: {e}")
            self.display_available = False
            return

        # Fonts
        try:
            self.font_small = self.ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
            self.font_normal = self.ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
            self.font_large = self.ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
        except Exception:
            self.font_small = self.ImageFont.load_default()
            self.font_normal = self.ImageFont.load_default()
            self.font_large = self.ImageFont.load_default()

        # Padding for better layout
        self.pad_top = 4
        self.pad_bottom = 4
        self.pad_side = 2

        # Status mapping for display
        self.status_map = {
            'rpi_model': 'RPi5',
            'gpio': 'GPIO',
            'libcamera': 'CAM',
            'i2c': 'I2C',
            'spi': 'SPI',
            'uart': 'UART',
            'service_/mavros/state': 'FCU',
            'service_/navigate': 'NAV',
            'service_/get_telemetry': 'TEL',
            'service_/led/set_effect': 'LED',
            'topic_/main_camera/image_raw': 'IMG',
            'rangefinder': 'RNG'
        }

        # Status cache
        self.statuses = {}
        self.service_status = "NO"
        self.last_update = None
        self.last_temp_c = None
        self.boot_active = True
        self._start_ts = time.time()

        # Start display with boot screen
        self.show_boot_screen()

    def _display_image(self, img):
        """Universal method to display image on OLED"""
        if not self.display_available:
            return

        try:
            if OLED_LIBRARY == "adafruit":
                # Clear display first
                self.device.fill(0)
                self.device.show()

                # Convert PIL image to display format
                self.device.image(img)
                self.device.show()
            elif OLED_LIBRARY == "luma":
                self.device.display(img)
        except Exception as e:
            print(f"Display error: {e}")

    def _text_size(self, font, text):
        try:
            bbox = font.getbbox(text)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]
        except Exception:
            return font.getsize(text)

    def _draw_center(self, draw, y, text, font):
        tw, th = self._text_size(font, text)
        x = max(self.pad_side, (self.device.width - tw) // 2)
        draw.text((x, y), text, font=font, fill=255)

    def _read_cpu_times(self):
        try:
            with open('/proc/stat', 'r') as f:
                parts = f.readline().split()
                if parts[0] != 'cpu':
                    return None
                vals = list(map(int, parts[1:]))
                user, nice, system, idle, iowait, irq, softirq, steal = (vals + [0]*10)[:8]
                idle_all = idle + iowait
                non_idle = user + nice + system + irq + softirq + steal
                total = idle_all + non_idle
                return idle_all, total
        except Exception:
            return None

    def _get_cpu_usage_percent(self):
        try:
            t1 = self._read_cpu_times()
            if not t1:
                return None
            time.sleep(0.1)
            t2 = self._read_cpu_times()
            if not t2:
                return None
            idle_d = t2[0] - t1[0]
            total_d = t2[1] - t1[1]
            if total_d <= 0:
                return None
            usage = (total_d - idle_d) * 100.0 / total_d
            return int(round(usage))
        except Exception:
            return None

    def _get_loadavg_text(self):
        try:
            a, b, c = os.getloadavg()
            return f"{a:.2f} {b:.2f} {c:.2f}"
        except Exception:
            return ""

    def _get_mem_usage_percent(self):
        try:
            meminfo = {}
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    parts = line.split(':')
                    if len(parts) < 2:
                        continue
                    key = parts[0]
                    val = parts[1].strip().split()[0]
                    meminfo[key] = int(val)
            total = meminfo.get('MemTotal')
            avail = meminfo.get('MemAvailable')
            if not total or avail is None:
                return None
            used = total - avail
            return int(round(used * 100.0 / total))
        except Exception:
            return None

    def _get_disk_usage_percent(self):
        try:
            total, used, free = shutil.disk_usage('/')
            return int(round(used * 100.0 / total))
        except Exception:
            return None

    def _get_ip_text(self):
        try:
            out = subprocess.check_output(['hostname', '-I'], text=True).strip()
            ip = out.split()[0] if out else ''
            return ip
        except Exception:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 80))
                ip = s.getsockname()[0]
                s.close()
                return ip
            except Exception:
                return ""

    def show_boot_screen(self):
        """Show boot screen with Clover logo"""
        if not self.display_available:
            return

        self.render_splash()

    def _find_container_id(self):
        """Find running Clover container id by name, label or ancestor image."""
        # 1) By explicit name (default: clover)
        try:
            name = os.environ.get("CLOVER_CONTAINER_NAME", "clover")
            ps = subprocess.run(["docker", "ps", "-q", "-f", f"name=^{name}$"], capture_output=True, text=True, timeout=2)
            cid = ps.stdout.strip()
            if cid:
                return cid.splitlines()[0]
        except Exception:
            pass

        # 2) By label (if container started with --label clover=1)
        try:
            ps = subprocess.run(["docker", "ps", "-q", "-f", "label=clover=1"], capture_output=True, text=True, timeout=2)
            cid = ps.stdout.strip()
            if cid:
                return cid.splitlines()[0]
        except Exception:
            pass

        # 3) By ancestor image
        try:
            image = os.environ.get("CLOVER_IMAGE", "serhio11/clover:latest")
            ps = subprocess.run(["docker", "ps", "-q", "-f", f"ancestor={image}"], capture_output=True, text=True, timeout=2)
            cid = ps.stdout.strip()
            if cid:
                return cid.splitlines()[0]
        except Exception:
            pass

        return ""

    def run_selfcheck(self):
        """Run selfcheck and parse results"""
        try:
            # Prefer running selfcheck inside Docker container if available
            # Container is started with --name clover and label clover=1
            env = os.environ.copy()
            env['ROS_LOG_DIR'] = '/tmp'

            # Check if container is running
            cid = self._find_container_id()

            if cid:
                base_env = "source /opt/ros/noetic/setup.bash 2>/dev/null || true; " \
                           "[ -f /home/pi/catkin_ws/devel/setup.bash ] && source /home/pi/catkin_ws/devel/setup.bash || true; "

                # Try fast path: rosrun selfcheck (no heavy launch include)
                exec_script1 = base_env + "timeout 25 rosrun clover selfcheck.py 2>&1 || true"
                cmd = ["docker", "exec", cid, "bash", "-lc", exec_script1]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, env=env)

                output_try1 = (result.stdout or '') + (result.stderr or '')
                need_fallback = False
                if result.returncode not in (0, 124):  # 124 is timeout from coreutils timeout
                    need_fallback = True
                if 'RLException' in output_try1 or 'rosrun:' in output_try1 or 'not found' in output_try1.lower():
                    need_fallback = True

                # Fallback: full launch with include (may take longer)
                if need_fallback:
                    exec_script2 = base_env + "timeout 40 roslaunch clover selfcheck.launch with_aruco:=false --screen 2>&1 || true"
                    cmd = ["docker", "exec", cid, "bash", "-lc", exec_script2]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=45, env=env)
            else:
                # No Docker: probe statuses directly via ROS (fast, no external processes)
                statuses = {}
                if rospy:
                    def topic_ok(name, timeout=0.8):
                        try:
                            rospy.wait_for_message(name, rospy.AnyMsg, timeout=timeout)
                            return True
                        except Exception:
                            return False

                    def service_ok(name, timeout=0.8):
                        try:
                            rospy.wait_for_service(name, timeout=timeout)
                            return True
                        except Exception:
                            return False

                    # Camera image
                    statuses['topic_/main_camera/image_raw'] = 'OK' if topic_ok('main_camera/image_raw', 1.0) else 'NO'
                    # MAVROS state (topic)
                    statuses['service_/mavros/state'] = 'OK' if topic_ok('mavros/state', 1.0) else 'NO'
                    # Core Clover services
                    statuses['service_/navigate'] = 'OK' if service_ok('navigate', 1.0) else 'NO'
                    statuses['service_/get_telemetry'] = 'OK' if service_ok('get_telemetry', 1.0) else 'NO'
                    # Rangefinder topic
                    statuses['rangefinder'] = 'OK' if topic_ok('rangefinder/range', 1.0) else 'NO'

                self.last_update = datetime.now()
                return statuses

            # Parse output (selfcheck prints lines like "FCU: ...", "Main camera: ...", "... OK")
            output = result.stdout + result.stderr
            statuses = {}

            # strip ANSI escape sequences
            ansi_re = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")

            mapping = {
                'FCU': ['service_/mavros/state'],
                'Main camera': ['topic_/main_camera/image_raw'],
                'Simple offboard node': ['service_/navigate', 'service_/get_telemetry'],
                'Rangefinder': ['rangefinder'],
            }

            for raw in output.split('\n'):
                line = ansi_re.sub('', raw).strip()
                if not line or ':' not in line:
                    continue
                name, msg = line.split(':', 1)
                name = name.strip()
                msg = msg.strip().lower()

                # Determine status heuristically
                if re.search(r'\bok\b', msg):
                    st = 'OK'
                elif any(w in msg for w in ['no ', 'failed', 'failure', 'cannot', 'error']):
                    st = 'FAIL'
                else:
                    st = 'WARN'

                # Map to our keys
                if name in mapping:
                    for k in mapping[name]:
                        statuses[k] = st

            # Fallback: if camera status not resolved, probe locally via ROS
            if 'topic_/main_camera/image_raw' not in statuses and rospy:
                try:
                    rospy.wait_for_message('main_camera/image_raw', rospy.AnyMsg, timeout=1.0)
                    statuses['topic_/main_camera/image_raw'] = 'OK'
                except Exception:
                    statuses.setdefault('topic_/main_camera/image_raw', 'NO')

            self.last_update = datetime.now()
            return statuses

        except subprocess.TimeoutExpired:
            print("Selfcheck timeout")
            return {}
        except Exception as e:
            print(f"Selfcheck error: {e}")
            return {}

    def get_service_status(self):
        """Check clover.service status"""
        try:
            # Prefer Docker container status
            if self._find_container_id():
                return "DOCKER"

            # Fallbacks: systemd services or roscore
            result = subprocess.run(["systemctl", "is-active", "clover.service"], capture_output=True, text=True)
            if result.stdout.strip() == "active":
                return "ROS"

            result = subprocess.run(["pgrep", "roscore"], capture_output=True, text=True)
            if result.returncode == 0:
                return "CORE"

            result = subprocess.run(["systemctl", "is-active", "roscore.service"], capture_output=True, text=True)
            if result.stdout.strip() == "active":
                return "CORE"
            return "NO"
        except Exception:
            return "NO"

    def render_splash(self):
        if not self.display_available:
            return
        img = self.Image.new("1", (self.device.width, self.device.height))
        d = self.ImageDraw.Draw(img)
        # Title and subtitle minimalistic with padding and centering
        title_y = self.pad_top + 4
        self._draw_center(d, title_y, "CLOVER", self.font_large)
        self._draw_center(d, title_y + 22, "Starting...", self.font_normal)
        self._display_image(img)

    def render_status(self):
        """Render status screen"""
        if not self.display_available:
            return

        img = self.Image.new("1", (self.device.width, self.device.height))
        draw = self.ImageDraw.Draw(img)

        # Top header: IP (left) and Temperature (right)
        title_y = self.pad_top

        # Read temperature
        temp_text = self._get_cpu_temp_text()
        if temp_text:
            tw, th = self._text_size(self.font_small, temp_text)
            draw.text((self.device.width - tw - self.pad_side, title_y), temp_text, font=self.font_small, fill=255)

        # IP address on the left top
        ip_text = self._get_ip_text()
        if ip_text:
            draw.text((self.pad_side, title_y), ip_text, font=self.font_small, fill=255)

        # Separator under header
        header_h = 0
        if ip_text:
            header_h = max(header_h, self._text_size(self.font_small, ip_text)[1])
        if temp_text:
            header_h = max(header_h, self._text_size(self.font_small, temp_text)[1])
        if header_h == 0:
            header_h = self._text_size(self.font_small, "A")[1]
        line_y = title_y + header_h + 1
        draw.line((self.pad_side, line_y, self.device.width - 1 - self.pad_side, line_y), fill=255)

        # Centered system metrics (no service/system line)
        y = line_y + 6
        cpu_pct = self._get_cpu_usage_percent()
        cpu_text = f"CPU: {cpu_pct}%" if cpu_pct is not None else "CPU: --%"
        self._draw_center(draw, y, cpu_text, self.font_large)
        # Draw Mem/Disk above bottom
        mem = self._get_mem_usage_percent()
        dsk = self._get_disk_usage_percent()
        stats_line = f"Mem: {mem}%  Disk: {dsk}%" if (mem is not None and dsk is not None) else ""
        if stats_line:
            stats_h = self._text_size(self.font_normal, stats_line)[1]
            y_stats = self.device.height - self.pad_bottom - stats_h - 10
            self._draw_center(draw, y_stats, stats_line, self.font_normal)

        # Draw Load at the bottom
        load_text = self._get_loadavg_text()
        if load_text:
            load_line = f"Load: {load_text}"
            load_h = self._text_size(self.font_normal, load_line)[1]
            y_load = self.device.height - self.pad_bottom - load_h
            self._draw_center(draw, y_load, load_line, self.font_normal)

        self._display_image(img)

    def render_detailed(self):
        """Render detailed view (cycle through all statuses)"""
        if not self.display_available:
            return

        img = self.Image.new("1", (self.device.width, self.device.height))
        draw = self.ImageDraw.Draw(img)

        # Title (smaller to fit more lines)
        title = "SYSTEM STATUS"
        title_y = self.pad_top
        self._draw_center(draw, title_y, title, self.font_small)
        th_title = self._text_size(self.font_small, title)[1]
        draw.line((self.pad_side, title_y + th_title + 2, self.device.width - 1 - self.pad_side, title_y + th_title + 2), fill=255)

        # Second screen: list FCU, IMG, NAV, TEL, RNG with YES/NO/ERROR (compact)
        y = title_y + th_title + 3
        bottom_limit = self.device.height - self.pad_bottom - 1

        ordered_keys = [
            'service_/mavros/state',
            'topic_/main_camera/image_raw',
            'service_/navigate',
            'service_/get_telemetry',
            'rangefinder',
        ]
        shown_any = False
        for key in ordered_keys:
            display_name = self.status_map.get(key, key)
            st = self.statuses.get(key)
            if st == 'OK':
                status_text = 'YES'
            elif st == 'FAIL':
                status_text = 'ERROR'
            else:
                status_text = 'NO'
            text = f"{display_name}: {status_text}"
            draw.text((self.pad_side + 2, y), text, font=self.font_small, fill=255)
            shown_any = True
            y += 8
            if y > bottom_limit:
                break

        if not shown_any:
            self._draw_center(draw, y, "No data", self.font_normal)

        self._display_image(img)

    def update_loop(self):
        """Background thread to update status"""
        while True:
            try:
                # Run selfcheck
                self.statuses = self.run_selfcheck()
                self.service_status = self.get_service_status()
                # exit splash after first successful cycle or after timeout
                if self.boot_active and (self.statuses is not None or self.service_status in ("DOCKER","ROS","CORE","NO") or (time.time() - self._start_ts) > 10):
                    self.boot_active = False

                # Wait before next update
                if rospy and not rospy.is_shutdown():
                    rospy.sleep(10.0)
                else:
                    time.sleep(10)

            except Exception as e:
                print(f"Update error: {e}")
                if rospy and not rospy.is_shutdown():
                    rospy.sleep(10.0)
                else:
                    time.sleep(10)

    def display_loop(self):
        """Main display loop"""
        mode = 0  # 0: status, 1: detailed

        while True:
            try:
                # Splash until первый апдейт или таймаут
                if self.boot_active:
                    self.render_splash()
                    if rospy and not rospy.is_shutdown():
                        rospy.sleep(0.3)
                    else:
                        time.sleep(0.3)
                    continue
                if mode == 0:
                    self.render_status()
                else:
                    self.render_detailed()

                # Switch modes every 10 seconds
                if rospy and not rospy.is_shutdown():
                    rospy.sleep(10.0)
                else:
                    time.sleep(10)
                mode = (mode + 1) % 2

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Display error: {e}")
                if rospy and not rospy.is_shutdown():
                    rospy.sleep(1.0)
                else:
                    time.sleep(1)

    def _get_cpu_temp_text(self):
        """Read CPU temperature and format as text."""
        try:
            t = None
            try:
                with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                    t = float(f.read().strip()) / 1000.0
            except Exception:
                pass
            if t is None:
                try:
                    out = subprocess.check_output(['vcgencmd', 'measure_temp'], text=True).strip()
                    if out.startswith('temp=') and out.endswith("'C"):
                        t = float(out.split('=')[1].split("'" )[0])
                except Exception:
                    pass
            self.last_temp_c = t
            return f"{t:.1f}C" if t is not None else ""
        except Exception:
            return ""

    def run(self):
        """Start display service"""
        if not self.display_available:
            print("No OLED display, exiting")
            return

        # Start update thread
        update_thread = threading.Thread(target=self.update_loop, daemon=True)
        update_thread.start()

        # Wait a bit for first update
        time.sleep(2)

        # Run display loop
        try:
            self.display_loop()
        finally:
            try:
                if OLED_LIBRARY == "adafruit":
                    self.device.fill(0)
                    self.device.show()
                elif OLED_LIBRARY == "luma":
                    self.device.clear()
                    self.device.hide()
            except:
                pass

def main():
    """Main entry point"""
    if rospy:
        try:
            rospy.init_node('display_selfcheck', anonymous=False)
        except Exception:
            # allow running without ROS
            pass

    display = CloverStatusDisplay()

    # If no display available, just exit gracefully
    if not display.display_available:
        # Keep running as service but do nothing
        while True:
            if rospy and rospy.is_shutdown():
                break
            if rospy and not rospy.is_shutdown():
                rospy.sleep(60.0)
            else:
                time.sleep(60)
    else:
        display.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1) 
