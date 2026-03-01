border# RC Transmitter Setup (Radio)

## Contents
1. [Transmitter Overview](#transmitter-overview)
2. [Transmitter Setup](#transmitter-setup)
3. [Creating a Drone Model](#creating-a-drone-model)
4. [Loading the Model](#loading-the-model)
5. [Binding Transmitter to Receiver](#binding-transmitter-to-receiver)
6. [Binding via Bind Phrase](#binding-via-bind-phrase)

## Transmitter Overview

<div align="center"><img src="../assets/radio/en/rc_pocket_front_part.png" width="900" class="zoom border center"></div>

<div align="center"><img src="../assets/radio/en/rc_pocket_back_part.png" width="900" class="zoom border center"></div>

## Transmitter Setup

1. Remove the black rubber grips from the back of the transmitter.
2. Insert the batteries, observing correct polarity.
3. Put the rubber grips back on.
4. Turn on the transmitter by holding the **POWER** button.

> **Important!** If you see a warning message on the screen (WARN image), check the position of the switches and the throttle stick—they must be in their zero (default) positions.

<div align="center"><img src="../assets/radio/rc_pocket.png" width="700" class="zoom border center"></div>

<div align="center"><img src="../assets/radio/main_menu_no_signal.jpg" width="350" class="zoom border center"></div>

## Creating a Drone Model

1. Press the **MDL** button.
2. Select an empty slot and press the **scroll wheel (encoder)**.

<div align="center"><img src="../assets/radio/steps_model/step_1.jpg" width="350" class="zoom border center"></div>

3. Select **CREATE MODEL**.
4. Press the **PAGE >** button.
5. Use the **scroll wheel (encoder)** to select **«Model name»** and name your drone.

<div align="center"><img src="../assets/radio/steps_model/step_2.jpg" width="350" class="zoom border center"></div>

6. Return to the menu using the **RTN** button.
7. Scroll down with the **scroll wheel** and turn on the Internal RF (radio frequency module).

<div align="center">
    <img src="../assets/radio/steps_model/step_3.jpg" width="350" class="zoom border center">
    <img src="../assets/radio/steps_model/step_4.jpg" width="350" class="zoom border center">
</div>

8. Go to the **MIXES** page and set up the aux switches on your transmitter:

<div align="center">
    <img src="../assets/radio/steps_model/step_6.jpg" width="350" class="zoom border center">
    <img src="../assets/radio/steps_model/step_7.jpg" width="350" class="zoom border center">
</div>
<div align="center"><img src="../assets/radio/steps_model/step_5.jpg" width="350" class="zoom border center"></div>

9. You should have all switches configured from SA to S1. Once done, press **RTN**. The basic model setup is complete.

## Loading the Model

1. Download the drone model file to your PC [`model05.yml`](https://drive.google.com/file/d/19Ab9sWPvaOvIavkEXPXzDXCRajpBcO7e/view?usp=sharing).
2. Turn on the transmitter > plug the Type-C cable into the top USB port > select **USB Storage (SD)** from the popup menu.
3. In the opened file explorer, go to the **MODELS** folder and copy the `model05.yml` file into it.

<div align="center">
    <img src="../assets/radio/steps_model/step_8.png" height="300" class="zoom border center">
    <img src="../assets/radio/steps_model/step_9.png" height="300" class="zoom border center">
</div>

## Binding Transmitter to Receiver

1. Put the receiver into **bind mode** by powering the flight controller (to which the ELRS RX is connected) on and off three times.

> **Important!** When the receiver enters bind mode, its LED will start doing a **double blink with a pause**.

2. Press the **SYS** button and navigate to the **ExpressLRS** LUA script.

<div align="center"><img src="../assets/radio/rx/elrs_step_1.jpg" width="350" class="zoom border center"></div>

3. Set **TX Power** to **100mW**.

<div align="center"><img src="../assets/radio/rx/elrs_step_2.jpg" width="350" class="zoom border center"></div>

4. Press **[Bind]** and wait for the pairing to complete.

<div align="center">
    <img src="../assets/radio/rx/elrs_step_3.jpg" width="350" class="zoom border center">
    <img src="../assets/radio/rx/elrs_bind.jpg" width="350" class="zoom border center">
</div>

5. Afterwards, hold the **RTN** button, and the connection telemetry icon will appear on the main screen.

<div align="center"><img src="../assets/radio/main_menu.jpg" width="350" class="zoom border center"></div>

## Binding via Bind Phrase

### Transmitter Setup (TX)

1. Turn on the transmitter by holding **POWER**.
2. Press **SYS** and navigate to the **ExpressLRS** menu.

<div align="center"><img src="../assets/radio/rx/elrs_step_1.jpg" width="350" class="zoom border center"></div>

3. Go to the **WiFi Connectivity** tab and turn on **Enable WiFi**.

<div align="center"><img src="../assets/radio/bind_phrase/elrs_step_1.jpg" width="350" class="zoom border center"></div>
<div align="center"><img src="../assets/radio/bind_phrase/elrs_step_2.jpg" width="350" class="zoom border center"></div>
<div align="center"><img src="../assets/radio/bind_phrase/elrs_step_3.jpg" width="350" class="zoom border center"></div>

4. From your PC or smartphone, connect to the newly appeared network **ExpressLRS TX**. Default password: **expresslrs**.

<div align="center"><img src="../assets/radio/bind_phrase/elrs_step_4.png" width="350" class="zoom border center"></div>

5. Open your browser and go to `10.0.0.1`.

> **Note on firmware version:** If it's lower than 3.3.1, you should update it via [ExpressLRS Web Flasher](https://expresslrs.github.io/web-flasher/).

<div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_tx.png" width="350" class="zoom border center"></div>

6. Enter your unique **Binding Phrase** and click **SAVE**.

<div align="center"><img src="../assets/radio/bind_phrase/elrs_settings.png" width="700" class="zoom border center"></div>

7. In the prompt window, click **REBOOT**.

<div align="center"><img src="../assets/radio/bind_phrase/reboot.png" width="350" class="zoom border center"></div>

### Receiver Setup (RX)

1. Put the receiver into **WiFi mode** by powering the flight controller and waiting for 60 seconds. The RX LED will start blinking rapidly and continuously.

2. Connect your PC or smartphone to the **ExpressLRS RX** network. Default password: **expresslrs**.

<div align="center"><img src="../assets/radio/bind_phrase/elrs_step_5.png" width="350" class="zoom border center"></div>

3. Open a browser and navigate to `10.0.0.1`.

> **Note on firmware version:** If it's lower than 3.0.0, you should update it via [ExpressLRS Web Flasher](https://expresslrs.github.io/web-flasher/).

<div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_rx.png" width="350" class="zoom border center"></div>

4. Enter the **EXACT SAME** unique **Binding Phrase** you used on the transmitter, then click **SAVE & REBOOT**.

<div align="center"><img src="../assets/radio/bind_phrase/elrs_settings_2.png" width="700" class="zoom border center"></div>

5. In the prompt window, click **REBOOT**.

<div align="center"><img src="../assets/radio/bind_phrase/reboot.png" width="350" class="zoom border center"></div>

6. Setup is complete.

<div align="center"><img src="../assets/radio/main_menu.jpg" width="350" class="zoom border center"></div>
