# Flashing MicoAir743v2 from PX4 to Betaflight

> **Success** This doc walks you through a safe way to re-flash the **MicoAir743v2** flight controller between PX4 and Betaflight via DFU/bootloader.  
> [How to flash from Betaflight to PX4](firmware_PX4_MicoAir743v2.md)

<p/>

> **Caution** This guide is **ONLY** for the **MicoAir743v2** flight controller.  
> If you’ve got a **Pixracer / COEX Pix / Pixhawk**, use the Pixracer PX4 flashing guide instead:  
> [PX4 firmware on Pixracer](firmware_Pixracer.md)

<div align="center">
  <img src="../assets/flight_controller_firmware/MicoAir743v2.png" width="350" class="zoom border center">
  <br/>
  <sub>MicoAir743v2 flight controller</sub>
</div>

## Contents
1. [Software & firmware links](#software--firmware-links)
2. [Entering DFU / bootloader mode](#entering-dfu--bootloader-mode)
3. [Flashing PX4 to Betaflight](#flashing-px4-to-betaflight)

## Software & firmware links

- **Betaflight Configurator** (official releases): [github.com/betaflight/betaflight-configurator/releases](https://github.com/betaflight/betaflight-configurator/releases)
- **STM32CubeProgrammer** (Google Drive): [drive.google.com (STM32CubeProgrammer)](https://drive.google.com/file/d/1Iku7s-Pmpvm8ctj7OK7KDgX6tYp3GB6a/view?usp=drive_link)
- **Betaflight firmware** for MicoAir743v2: [drive.google.com (Betaflight firmware)](https://drive.google.com/file/d/1gaLgiCqa-gUa-vJtmGSQhVh7zwCFcqFN/view?usp=drive_link)

## Entering DFU / bootloader mode

1. Hold the **BOOT** button on the FC.
2. While holding **BOOT**, plug the USB cable into your PC.
3. Your system should detect it as **DFU / STM32 Bootloader**.

## Flashing PX4 to Betaflight

> **Caution** **Programmer setup (STM32CubeProgrammer)**  
> Before flashing, download and install STM32CubeProgrammer.

1. Put the flight controller into **DFU** (hold **BOOT** and plug it in via USB). Open STM32CubeProgrammer and click the connection protocol selector (UART).
    <div align="center"><img src="../assets/flight_controller_firmware/PX4/step_1.png" width=700 class="zoom border center"></div>

2. Select the **USB** protocol.
    <div align="center"><img src="../assets/flight_controller_firmware/PX4/step_2.png" width=700 class="zoom border center"></div>

3. Refresh ports (click the button to the right of the port selector). It should auto-pick the right one.  
If it doesn’t, the FC is not in DFU mode — redo step 1.
    <div align="center"><img src="../assets/flight_controller_firmware/PX4/step_3.png" width=700 class="zoom border center"></div>

4. Click "Connect".
    <div align="center"><img src="../assets/flight_controller_firmware/PX4/step_4.png" width=700 class="zoom border center"></div>

5. Do a full wipe: click the eraser icon in the bottom-left, confirm in the popup, and wait until it’s done.
    <div align="center"><img src="../assets/flight_controller_firmware/PX4/step_5.png" width=700 class="zoom border center"></div>

6. Click **Open file** and select `MicoAir743v2_Betaflight-4.5.2.hex`.
    <div align="center"><img src="../assets/flight_controller_firmware/PX4/step_6.png" width=700 class="zoom border center"></div>

7. Click "Download" to flash the firmware and wait until it finishes.
    <div align="center"><img src="../assets/flight_controller_firmware/Betaflight/step_7.png" width=700 class="zoom border center"></div>

8. Click "Disconnect".
    <div align="center"><img src="../assets/flight_controller_firmware/Betaflight/step_8.png" width=700 class="zoom border center"></div>

9. Open Betaflight Configurator and start setting things up.
    <div align="center"><img src="../assets/flight_controller_firmware/Betaflight/step_9.png" width=700 class="zoom border center"></div>
