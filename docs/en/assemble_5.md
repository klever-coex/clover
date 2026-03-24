# Clover 5 Assembly

## Contents
1. [Wiring Diagram](#wiring-diagram)
2. [Frame Assembly](#frame-assembly)
3. [Motor Installation](#motor-installation)
4. [ESC Installation](#esc-installation)
5. [Aluminum Standoffs Installation](#aluminum-standoffs-installation)
6. [Flight Controller Installation](#flight-controller-installation)
7. [Raspberry Pi Installation](#raspberry-pi-installation)
8. [Installing Guards, Legs, and LED Strip](#installing-guards-legs-and-led-strip)

## Fastener Sizes

> **Success** Fasteners of various sizes are used during assembly. Installing screws or standoffs of the wrong size may result in damage to the quadcopter.

<div align="center"> <table class="type_table">
  <tr>
    <td id="cell1"><div align="center"><strong>Cell 1</strong><br><img src="../assets/assembling_clever5/fasteners/nut_press.png" width="20"/><br>Press Nut M3</div></td>
    <td id="cell2"><div align="center"><strong>Cell 2</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.png" width="20"/><br>Nylon Nut M3</div></td>
    <td id="cell3"><div align="center"><strong>Cell 3</strong><br><img src="../assets/assembling_clever5/fasteners/hts-m2,5.png" width="35"/><br>Nylon Standoff M2.5</div></td>
    <td id="cell4"><div align="center"><strong>Cell 4</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.png" width="16"/><br>Nylon Nut M2.5</div></td>
    <td id="cell5"><div align="center"><strong>Cell 5</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.png" width="12"/><br>Nylon Nut M2</div></td>
  </tr>
  <tr>
    <td id="cell6"><div align="center"><strong>Cell 6</strong><br><img src="../assets/assembling_clever5/fasteners/m3x40.png" width="150" height="30"/><br>Screw M3x40</div></td>
    <td id="cell7"><div align="center"><strong>Cell 7</strong><br><img src="../assets/assembling_clever5/fasteners/m3x12.png" width="95" height="30"/><br>Screw M3x12</div></td>
    <td id="cell8"><div align="center"><strong>Cell 8</strong><br><img src="../assets/assembling_clever5/fasteners/m3x8.png" width="70" height="30"/><br>Screw M3x8</div></td>
    <td id="cell9"><div align="center"><strong>Cell 9</strong><br><img src="../assets/assembling_clever5/fasteners/m3x6.png" width="45" height="30"/><br>Screw M3x6</div></td>
    <td id="cell10"><div align="center"><strong>Cell 10</strong><br><img src="../assets/assembling_clever5/fasteners/m3x4.png" width="35" height="30"/><br>Screw M3x4</div></td>
  </tr>
  <tr>
    <td id="cell11"><div align="center"><strong>Cell 11</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_40.png" width="130" height="15"/><br>Aluminum Standoff M3x40</div></td>
    <td id="cell12"><div align="center"><strong>Cell 12</strong><br><img src="../assets/assembling_clever5/fasteners/dumper.png" width="50"/><br>Damper Standoff M3</div></td>
    <td id="cell13"><div align="center"><strong>Cell 13</strong><br><img src="../assets/assembling_clever5/fasteners/m3x10.png" width="80" height='30'/><br>Screw M3x10</div></td>
    <td id="cell14"><div align="center"><strong>Cell 14</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_10.png" width="40" height="15"/><br>Aluminum Standoff M3x10</div></td>
    <td id="cell15"><div align="center"><strong>Cell 15</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_40.png" width="100" height="15"/><br>Aluminum Standoff M3x30</div></td>
  </tr>
  <tr>
    <td id="cell16"><div align="center"><strong>Cell 16</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x6.png" width="50" height="20"/><br>Screw M2x6</div></td>
    <td id="cell17"><div align="center"><strong>Cell 17</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x4.png" width="50" height="25"/><br>Screw M2.5x4</div></td>
    <td id="cell18"><div align="center"><strong>Cell 18</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x6.png" width="60" height="25"/><br>Screw M2.5x6</div></td>
    <td id="cell19"><div align="center"><strong>Cell 19</strong><br><img src="../assets/assembling_clever5/fasteners/m1,4x3.png" width="35"/><br>Self-tapping Screw M1.4x4</div></td>
    <td id="cell20"><div align="center"><strong>Cell 20</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x4.png" width="35" height="20"/><br>Screw M2x3</div></td>
  </tr>
  <tr>
    <td id="cell21"><div align="center"><strong>Cell 21</strong><br><img src="../assets/assembling_clever5/fasteners/htp-30.png" width="100" height="15"/><br>Nylon Standoff M3x30</div></td>
    <td id="cell22"><div align="center"><strong>Cell 22</strong><br><img src="../assets/assembling_clever5/fasteners/htp-20.png" width="70" height="15"/><br>Nylon Standoff M3x20</div></td>
    <td id="cell23"><div align="center"><strong>Cell 23</strong><br><img src="../assets/assembling_clever5/fasteners/htp-40.png" width="130" height="15"/><br>Nylon Standoff M3x40</div></td>
    <td id="cell24"><div align="center"><strong>Cell 24</strong><br><img src="../assets/assembling_clever5/fasteners/m1,4x10.png" width="60"/><br>Self-tapping Screw M1.4x10</div></td>
    <td id="cell25"><div align="center"><strong>Cell 25</strong><br><img src="../assets/assembling_clever5/fasteners/tpu-spacer.png" width="60"/><br>TPU Foot</div></td>
  </tr>
</table></div>

## Wiring Diagram

<div align="center"><img src="../assets/assembling_clever5/en/layout.png" width=700 class="zoom border center"></div>

## Frame Assembly

1. Align the 4 arms between the middle and bottom plates.

    <div align="center"><img src="../assets/assembling_clever5/en/frame/frame_step_1.png" width=700 class="zoom border center"></div>

2. Install M3x12 screws (<a href="#cell7">Cell 7</a>) and M3x40 screws (<a href="#cell6">Cell 6</a>) from the bottom plate side: M3x12 (<a href="#cell7">Cell 7</a>) in the outer arm holes, M3x40 (<a href="#cell6">Cell 6</a>) in the central holes of the bottom plate.

    <div align="center"><img src="../assets/assembling_clever5/en/frame/frame_step_2.png" width=700 class="zoom border center"></div>

3. Install M3 press nuts (<a href="#cell1">Cell 1</a>) on the middle plate and secure them with screws.

    <div align="center"><img src="../assets/assembling_clever5/en/frame/frame_step_3.png" width=700 class="zoom border center"></div>

## Motor Installation

1. Install the motors into the corresponding holes on the arm using **M3x8 screws** (<a href="#cell8">Cell 8</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/motor.png" width=700 class="zoom border center"></div>

> **Caution** Ensure that the motors are secured with M3x8 screws; otherwise, a short circuit between the windings may occur.

## ESC Installation
1. Install the Electronic Speed Controller (ESC) over the M3x40 screws (<a href="#cell6">Cell 6</a>) on the middle plate. The battery power connector should face backward.

    <div align="center"><img src="../assets/assembling_clever5/en/esc_step_1.png" width=700 class="zoom border center"></div>

2. Connect the MR30 connectors from the ESC to the motors, route the wires as shown in the figure, and then secure them to the arms using zip ties (plastic cable ties).

    <div align="center"><img src="../assets/assembling_clever5/en/esc_step_2.png" width=700 class="zoom border center"></div>

## Aluminum Standoffs Installation

1. Install M3x40 aluminum standoffs (<a href="#cell11">Cell 11</a>) on the middle plate using M3 damper standoffs (<a href="#cell12">Cell 12</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/aluminium_40_step_1.png" width=700 class="zoom border center"></div>

2. Tighten the damper standoffs from the bottom plate side.

    <div align="center"><img src="../assets/assembling_clever5/en/aluminium_40_step_2.png" width=700 class="zoom border center"></div>

## Flight Controller Installation

1. Before installing the flight controller, thread M3 nylon nuts (<a href="#cell2">Cell 2</a>) onto the M3x40 screws (<a href="#cell6">Cell 6</a>), then install the flight controller with the arrow pointing forward.
Install nylon nuts to secure the flight controller.

    <div align="center"><img src="../assets/assembling_clever5/en/flight_controller_step_1.png" width=700 class="zoom border center"></div>

2. Install the 6-pin cable between the flight controller and the ESC.

    <div align="center"><img src="../assets/assembling_clever5/en/flight_controller_step_2.png" width=700 class="zoom border center"></div>

3. View with the cable installed.

    <div align="center"><img src="../assets/assembling_clever5/en/flight_controller_step_3.png" width=700 class="zoom border center"></div>

## Raspberry Pi Installation

1. Install M2.5 standoffs (<a href="#cell3">Cell 3</a>) on the polycarbonate mounting plate using M2.5x4 screws (<a href="#cell17">Cell 17</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_1.png" width=700 class="zoom border center"></div>

2. Tighten the screws. Use an H1.5/HEX1.5 bit.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_2.png" width=700 class="zoom border center"></div>

3. Place the Raspberry Pi 5 on top of the M2.5 standoffs.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_3.png" width=700 class="zoom border center"></div>

4. Secure the Raspberry Pi 5 board using M2.5x4 screws (<a href="#cell17">Cell 17</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_4.png" width=700 class="zoom border center"></div>

5. Remove the films from the thermal pads and place them in the positions highlighted in the image. Install the cooling heatsink on the Raspberry Pi by inserting the locking clips through the heatsink into the Raspberry Pi. Connect the cooling system to the port marked in the image.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_5.png" width=700 class="zoom border center"></div>

6. Raspberry Pi with heatsink assembled.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_6.png" width=700 class="zoom border center"></div>

7. Install 30mm nylon standoffs (<a href="#cell21">Cell 21</a>) on the plate with the Raspberry Pi using M3x8 screws (<a href="#cell8">Cell 8</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_7.png" width=700 class="zoom border center"></div>

8. View with nylon standoffs installed.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_8.png" width=700 class="zoom border center"></div>

9. Install the assembled plate with the Raspberry Pi onto the bottom part of the quadcopter into the damper standoffs, secure with M3x4 screws (<a href="#cell10">Cell 10</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_9.png" width=700 class="zoom border center"></div>

10. Connect the data cable to the Raspberry Pi. The connection is made to the outer row of the header, starting from the 4th port relative to the SD card port (black wire in port 14, see pinout). The other end connects to the UART 4 port on the flight controller (black wire is located in the far right corner).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_10.png" width=700 class="zoom border center"></div>
    <div align="center"><img src="../assets/assembling_clever5/en/RPI_pinout.png" width=400 class="zoom border center"></div>

11. Install the camera on the small mounting plate with the tab towards the top clip and secure it using two M1.4x4 self-tapping screws (<a href="#cell19">Cell 19</a>) in the top left and bottom right corners. Assembly bit: PH1.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_11.png" width=700 class="zoom border center"></div>

12. Install 20mm nylon standoffs (<a href="#cell22">Cell 22</a>) on the small mounting plate and secure with M3x6 screws (<a href="#cell9">Cell 9</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_12.png" width=700 class="zoom border center"></div>

13. Install the small mounting plate with the camera onto the gripper plate using M3x6 screws (<a href="#cell9">Cell 9</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_13.png" width=700 class="zoom border center"></div>

14. Install the laser rangefinder on the gripper plate using M2x6 screws (<a href="#cell16">Cell 16</a>) and M2 nylon nuts (<a href="#cell5">Cell 5</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_14.png" width=700 class="zoom border center"></div>

15. Connect the laser rangefinder cable.

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_15.png" width=700 class="zoom border center"></div>

16. Install the gripper plate on the quadcopter using M3x8 screws (<a href="#cell8">Cell 8</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_16.png" width=700 class="zoom border center"></div>

17. Connect the rangefinder cable to the UART 1 port on the flight controller (black wire in the far left pin).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_17.png" width=700 class="zoom border center"></div>

18. Install the screen on the drone canopy using M2.5x6 screws (<a href="#cell18">Cell 18</a>) and M2.5 nylon nuts (<a href="#cell4">Cell 4</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_18.png" width=700 class="zoom border center"></div>

19. Install the UBEC on the plate with the Raspberry Pi using double-sided tape. Connect the UBEC to the ESC via the XT30 connector. Connect the first UBEC wire to the Raspberry Pi as indicated in the picture (pins 4 and 6, see pinout above).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_19.png" width=700 class="zoom border center"></div>

20. Connect the receiver to the SBUS/CRSF (UART 6) port on the flight controller (black wire in the far left pin).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_20.png" width=700 class="zoom border center"></div>

21. Install the canopy over the aluminum standoffs and secure the receiver with a zip tie into the highlighted holes in the image. Route the wires into the wire cutout in the canopy. Connect the screen to the Raspberry Pi; the red wire connects to the far left pin of the inner row of the header relative to the SD card (red - pin 1, black - pin 9).

    <div align="center"><img src="../assets/assembling_clever5/en/RPI_step_21.png" width=700 class="zoom border center"></div>

## Installing Guards, Legs, and LED Strip

1. Thread the strap into the top plate, then secure it to the aluminum standoffs using M3x8 screws (<a href="#cell8">Cell 8</a>), and secure the power connector using M2.5x6 screws (<a href="#cell18">Cell 18</a>). Assembly bit for the plate - H2.0/HEX2.0, for the connector - H1.5/HEX1.5.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_1.png" width=700 class="zoom border center"></div>

2. Arrange the guard bridges in a square at the bottom, then place the bottom guard arcs on the corners, secure with M3x10 screws (<a href="#cell13">Cell 13</a>) from the top, and 40mm nylon standoffs (<a href="#cell23">Cell 23</a>) from the bottom.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_2.png" width=700 class="zoom border center"></div>

3. Secure the top arcs and bridges in reverse order using M3x8 screws (<a href="#cell8">Cell 8</a>); the bridges should face inward and the arcs outward.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_3.png" width=700 class="zoom border center"></div>

4. Install and secure M3 press nuts (<a href="#cell1">Cell 1</a>) into the holes at the ends of the arms.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_4.png" width=700 class="zoom border center"></div>

5. Install the guard from the bottom side and secure it using M3x10 screws (<a href="#cell13">Cell 13</a>).

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_5.png" width=700 class="zoom border center"></div>

6. Screw M3x6 screws (<a href="#cell9">Cell 9</a>) into all holes on one side of the small leg, and secure them with 10mm aluminum standoffs (<a href="#cell14">Cell 14</a>) on the other side. Place a TPU foot (<a href="#cell25">Cell 25</a>) over the standoff in the bottom hole.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_6.png" width=700 class="zoom border center"></div>

7. Place the small leg on the arm as shown in the image and secure with M3x6 screws (<a href="#cell9">Cell 9</a>). Do the same for the other legs.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_7.png" width=700 class="zoom border center"></div>

8. Stick the LED strip onto the circumference, then install it into the hooks on the legs and secure the wires with a zip tie. Connect the power to the second free UBEC, and connect the signal wire to GPIO 9 (pin 21).

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_8.png" width=700 class="zoom border center"></div>

9. Install the propellers according to the classic rotation direction, as shown in the image.

    <div align="center"><img src="../assets/assembling_clever5/en/other_step_9.png" width=700 class="zoom border center"></div>


> **Caution** Check that no components remain unsecured. Before the first power-on, ensure that the propellers do not touch the canopy or wires.
