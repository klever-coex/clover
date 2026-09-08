# Radio Controller Setup

## Contents
1. [Hardware overview](#hardware-overview)
2. [Radio controller setup](#radio-controller-setup)
3. [Binding the radio controller to the receiver](#binding-the-radio-controller-to-the-receiver)

## Hardware overview

<div align="center"><img src="../assets/radio/rc_pocket_front_part.webp" width=900 class="zoom border center"><p>Figure 1 - Radio controller, front view</p></div>

<div align="center"><img src="../assets/radio/rc_pocket_back_part.webp" width=900 class="zoom border center"><p>Figure 2 - Radio controller, rear view</p></div>

## Radio controller setup

1. Remove the black rubber grips from the back of the radio controller.
2. Insert the batteries, observing the correct polarity.
3. Put the rubber grips back in place.
4. Turn on the radio controller by holding the **POWER** button.

> **Caution** If warning messages appear on the radio controller screen, check the positions of the switches and the throttle stick. Before power-on, they must be in their default positions.

<div align="center"><img src="../assets/radio/warn.webp" width=350 class="zoom border center"><p>Figure 3 - Warning shown when switches or sticks are in the wrong position</p></div>

After you return the switches and sticks to their default positions, the main menu will open.

<div align="center"><img src="../assets/radio/main_menu_no_signal.webp" width=350 class="zoom border center"><p>Figure 4 - Radio controller main menu without a receiver link</p></div>

## Binding the radio controller to the receiver

### Radio controller setup (transmitter)

1. Turn on the radio controller by holding the **POWER** button.
2. Press **SYS** and open the **ExpressLRS** menu, as shown in Figure 5.

    <div align="center"><img src="../assets/radio/rx/elrs_step_1.webp" width=350 class="zoom border center"><p>Figure 5 - Opening the ExpressLRS menu for transmitter setup</p></div>

3. Open the **WiFi Connectivity** tab and enable **Enable WiFi**, as shown in Figures 6 and 7.

  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_1.webp" width=350 class="zoom border center">
  </div>
  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_2.webp" width=350 class="zoom border center">
  </div>
  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_3.webp" width=350 class="zoom border center">
    <p>Figure 6 - Opening WiFi Connectivity settings</p>
    <p>Figure 7 - Enabling WiFi on the ExpressLRS transmitter</p>
  </div>

4. Connect from a PC or smartphone to the **ExpressLRS TX** network. The default password is **expresslrs**. An example is shown in Figure 8.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_step_4.webp" width=350 class="zoom border center"><p>Figure 8 - Connecting to the ExpressLRS TX network</p></div>

5. Open a browser and go to `10.0.0.1`. The start page is shown in Figure 9.

    > **Note** Pay attention to the firmware version. If it is lower than 3.3.1, update it with [ExpressLRS Web Flasher](https://expresslrs.github.io/web-flasher/).

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_tx.webp" width=350 class="zoom border center"><p>Figure 9 - ExpressLRS transmitter web interface</p></div>

6. Enter a unique **Binding Phrase** and press **SAVE**, as shown in Figure 10.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_settings.webp" width=700 class="zoom border center"><p>Figure 10 - Entering the Binding Phrase in the transmitter settings</p></div>

7. In the pop-up window, press **REBOOT**, as shown in Figure 11.

    <div align="center"><img src="../assets/radio/bind_phrase/reboot.webp" width=350 class="zoom border center"><p>Figure 11 - Rebooting the transmitter after saving settings</p></div>

### Receiver setup

1. Put the receiver into **WiFi** mode by powering the flight controller connected to the ELRS receiver and waiting 60 seconds. After that, the receiver LED will blink continuously.

2. Connect from a PC or smartphone to the **ExpressLRS RX** network. The default password is **expresslrs**. An example is shown in Figure 12.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_step_5.webp" width=350 class="zoom border center"><p>Figure 12 - Connecting to the ExpressLRS RX network</p></div>

3. Open a browser and go to `10.0.0.1`. The start page is shown in Figure 13.

    > **Note** Pay attention to the firmware version. If it is lower than 3.0.0, update it with [ExpressLRS Web Flasher](https://expresslrs.github.io/web-flasher/).

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_rx.webp" width=350 class="zoom border center"><p>Figure 13 - ExpressLRS receiver web interface</p></div>

4. Enter the **same** unique **Binding Phrase** that was used on the transmitter, then press **SAVE & REBOOT**, as shown in Figure 14.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_settings_2.webp" width=700 class="zoom border center"><p>Figure 14 - Entering the Binding Phrase in the receiver settings</p></div>

5. In the pop-up window, press **REBOOT**, as shown in Figure 15.

    <div align="center"><img src="../assets/radio/bind_phrase/reboot.webp" width=350 class="zoom border center"><p>Figure 15 - Rebooting the receiver after saving settings</p></div>

6. Setup is complete. After reboot, the link should appear as shown in Figure 16.

    <div align="center"><img src="../assets/radio/main_menu.webp" width=350 class="zoom border center"><p>Figure 16 - Radio controller main menu after setup through Bind Phrase</p></div>

### Alternative method: Bind mode

1. Put the receiver into **bind** mode by powering the flight controller connected to the ELRS receiver on and off three times.

> **Note** When the receiver enters bind mode, the LED on the receiver starts blinking twice with a pause.

2. On the radio controller, press **SYS** and open the **ExpressLRS** menu, as shown in Figure 17.

<div align="center"><img src="../assets/radio/rx/elrs_step_1.webp" width=350 class="zoom border center"><p>Figure 17 - Opening the ExpressLRS menu</p></div>

3. Set **TX Power** to **100mW**, as shown in Figure 18.

<div align="center"><img src="../assets/radio/rx/elrs_step_2.webp" width=350 class="zoom border center"><p>Figure 18 - Setting transmitter power to 100mW</p></div>

4. Press **Bind** and wait until binding finishes, as shown in Figure 19.

<div align="center"><img src="../assets/radio/rx/elrs_step_3.webp" width=350 class="zoom border center"><img src="../assets/radio/rx/elrs_bind.webp" width=350 class="zoom border center"><p>Figure 19 - Starting binding from the ExpressLRS menu</p></div>

5. Press **RTN**. The receiver link indicator will appear in the main menu, as shown in Figure 20.

<div align="center"><img src="../assets/radio/main_menu.webp" width=350 class="zoom border center"><p>Figure 20 - Radio controller main menu after successful binding</p></div>
