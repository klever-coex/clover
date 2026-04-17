# RPi Wi-Fi Setup via NetworkManager

## Contents
1. [Changing the password or SSID (network name)](#changing-the-password-or-ssid-network-name)
2. [Switching the adapter to client mode](#switching-the-adapter-to-client-mode)
3. [Switching the adapter to access point mode](#switching-the-adapter-to-access-point-mode)
4. [How RPi networking works with NetworkManager](#how-rpi-networking-works-with-networkmanager)

You can configure networking on Raspberry Pi through `NetworkManager` and its text interface `nmtui`.

`NetworkManager` is a system service that manages network interfaces and stores connection profiles. In this case, the service is responsible for Wi-Fi settings on Raspberry Pi, while `nmtui` provides a convenient text interface for changing these settings without manually editing several configuration files.

With `NetworkManager`, you can switch the Raspberry Pi Wi-Fi adapter between two main operating modes:

1. **Client mode (Mode = Client)** - Raspberry Pi connects to an existing Wi-Fi network.
2. **Access point mode (Mode = Access Point)** - Raspberry Pi creates a Wi-Fi network that you can connect to.

Connect to Raspberry Pi locally or over [SSH](ssh.md), then start the configuration interface:

```bash
sudo nmtui
```

## Changing the password or SSID (network name)

1. Run `sudo nmtui`.
2. Select `Edit a connection`.

<div align="center">
  <img src="../assets/network/general.webp" width=350 class="zoom border center">
  <p>Figure 1 - Main nmtui menu with the Edit a connection item</p>
</div>

3. Select the `clover` access point profile and press `Edit` (see Figure 2). If there is no such profile, create it through `Add` -> `Wi-Fi`.

<div align="center">
  <img src="../assets/network/edit_net.webp" width=350 class="zoom border center">
  <p>Figure 2 - Selecting a connection profile before editing</p>
</div>

4. In the profile edit window, change the `SSID` and `Password` fields, as shown in Figure 3:
   * `SSID` - to change the Wi-Fi network name;
   * `Password` - to change the password.

<div align="center">
  <img src="../assets/network/edit_clover.webp" width=350 class="zoom border center">
  <p>Figure 3 - Changing SSID and password in the access point profile</p>
</div>

> **Caution** The Wi-Fi password must be at least 8 characters long.
> If you changed the `SSID` field, after reactivation you will need to reconnect using the new network name.

5. Press `OK`, then `Back`.
6. To apply the changes, run the command below and wait for NetworkManager to restart:

```bash
sudo systemctl restart NetworkManager
```

## Switching the adapter to client mode

> **Note** In **client mode**, Raspberry Pi connects to an existing Wi-Fi network.

1. Run `sudo nmtui`.
2. Select `Edit a connection`.

<div align="center">
  <img src="../assets/network/general.webp" width=350 class="zoom border center">
  <p>Figure 4 - Main nmtui menu for opening the connection list</p>
</div>

3. Create a new profile by selecting `Add` (see Figure 5).

<div align="center">
  <img src="../assets/network/client_1.webp" width=350 class="zoom border center">
  <p>Figure 5 - Adding a new connection profile</p>
</div>

4. In the `New Connection` window, select `Wi-Fi` (see Figure 6).

<div align="center">
  <img src="../assets/network/client_2.webp" width=350 class="zoom border center">
  <p>Figure 6 - Choosing Wi-Fi as the connection type</p>
</div>

5. In the `Edit Connection` window, select `Security` and change the security protocol to `WPA & WPA2 Personal` or another protocol that matches your router settings, as shown in Figure 7.

<div align="center">
  <img src="../assets/network/client_3.webp" width=350 class="zoom border center">
  <p>Figure 7 - Configuring security settings for the client mode profile</p>
</div>

6. Enter `SSID` and `Password`, then press `OK` (see Figure 8).

<div align="center">
  <img src="../assets/network/client_4.webp" width=350 class="zoom border center">
  <p>Figure 8 - Entering the network name and password for client mode</p>
</div>

7. Exit `nmtui` by pressing `Back`, then `Quit`. Run the following command and wait for reboot:

```bash
sudo reboot
```

8. Run `sudo nmtui`.
9. Open `Activate a connection`, select the profile you created (if you did not rename the network, it is usually `Wi-Fi connection 1`), and press `Activate`.

<div align="center">
  <img src="../assets/network/client_5.webp" width=350 class="zoom border center">
  <p>Figure 9 - Activating the created client mode profile</p>
</div>

> **Success** Wait for the reboot to finish. After that, Raspberry Pi will connect to your Wi-Fi network.

## Switching the adapter to access point mode

> **Note** In **access point mode**, Raspberry Pi creates a Wi-Fi network that you can connect to.

1. Run `sudo nmtui`.
2. Select `Activate a connection`.

<div align="center">
  <img src="../assets/network/activate.webp" width=350 class="zoom border center">
  <p>Figure 10 - Opening the list of active connections</p>
</div>

3. Select the created client profile and press `Deactivate`, as shown in Figure 11.

<div align="center">
  <img src="../assets/network/deactivate.webp" width=350 class="zoom border center">
  <p>Figure 11 - Deactivating the active client profile to return to access point mode</p>
</div>

> **Success** Wait for the reboot. The standard `clover-XXXX` network will appear again.

## How RPi networking works with NetworkManager

`NetworkManager` stores connection profiles and applies them to the required interface. For Wi-Fi, this is convenient because all main settings can be changed from the single `nmtui` interface instead of editing several configuration files by hand.

For client mode, a profile with `Mode = Client` and `IPv4 CONFIGURATION = Automatic` is usually enough. In this case, Raspberry Pi connects to an existing network and receives an address over DHCP.

For access point mode, you need a profile with `Mode = Access Point` and `IPv4 CONFIGURATION = Shared`. In this mode, Raspberry Pi creates its own Wi-Fi network and assigns addresses to connected devices.

`NetworkManager` profile files are usually stored in `/etc/NetworkManager/system-connections/`. In most cases, you do not need to edit them manually - it is more convenient to use the `nmtui` text interface.

When using `NetworkManager`, it is better to keep Wi-Fi and routing settings in one place. If the `wlan0` network interface is configured at the same time through `NetworkManager` and manually through `dhcpcd.conf`, `wpa_supplicant.conf`, or a separate `dnsmasq` configuration file, configuration conflicts, unstable operation, or loss of connectivity may occur.
