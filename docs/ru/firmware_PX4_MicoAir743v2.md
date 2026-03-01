# Прошивка MicoAir743v2 с Betaflight на PX4

> Документация описывает безопасную процедуру перепрошивки полётного контроллера **MicoAir743v2** между PX4 и Betaflight через DFU/bootloader. 
> [Документация по прошивке с PX4 на Betaflight](firmware_Betaflight_MicoAir743v2.md)

> [!WARNING]
> Данная инструкция подходит **только для полётного контроллера MicoAir743v2**.  
> Если у вас **Pixracer / COEX Pix / Pixhawk**, используйте документацию по прошивке PX4 для Pixracer:  
> [PX4 firmware in Pixracer](firmware_Pixracer.md)

<div align="center">
  <img src="../assets/flight_controller_firmware/MicoAir743v2.png" width="350" class="zoom border center">
  <br/>
  <sub>MicoAir743v2 flight controller</sub>
</div>

## Содержание
1. [Ссылки на ПО и прошивку](#ссылки-на-по-и-прошивку)
2. [Вход в DFU / bootloader mode](#вход-в-dfu--bootloader-mode)
3. [Прошивка с Betaflight на PX4](#прошивка-с-betaflight-на-px4)

## Ссылки на ПО и прошивку

- **QGroundControl (QGC)** - официальный релиз‑раздел: [github.com/mavlink/qgroundcontrol/releases](https://github.com/mavlink/qgroundcontrol/releases)
- **STM32CubeProgrammer** (Google Drive): [drive.google.com (STM32CubeProgrammer)](https://drive.google.com/file/d/1Iku7s-Pmpvm8ctj7OK7KDgX6tYp3GB6a/view?usp=drive_link)
- **Прошивка PX4** для MicoAir743v2: [drive.google.com (PX4 firmware)](https://drive.google.com/file/d/1jzP9aq3Xnf23IBPEMmOuu_WSnmtp5k30/view?usp=drive_link)
- **Бутлоадер PX4** для MicoAir743v2: [drive.google.com (PX4 bootloader)](https://drive.google.com/file/d/1uBthl71j38G7UHf_kAU8f30lo4woI9I8/view?usp=drive_link)

## Вход в DFU / bootloader mode

1. Зажмите кнопку **BOOT** на контроллере.
2. Не отпуская BOOT, подключите USB к ПК.
3. В системе устройство должно определиться как DFU/STM32 Bootloader.

## Прошивка с Betaflight на PX4

> [!WARNING]
> **Установка программатора (STM32CubeProgrammer)**  
> Перед прошивкой скачайте и установите STM32CubeProgrammer.

1. Переведите полётный контроллер в режим **DFU** (зажмите кнопку BOOT и подключите по проводу USB к компьютеру). Откройте STM32CubeProgrammer, нажмите на кнопку выбора протокола подключения (UART).
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_1.png" width=700 class="zoom border center"></div>

2. Выберите протокол USB.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_2.png" width=700 class="zoom border center"></div>

3. Обновите порт, для этого нажмите на кнопку справа от выбора порта.
После чего автоматически выберется нужный порт (Если не выбрался, значит полётный контроллер не в режиме DFU, повторите первый пункт).
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_3.png" width=700 class="zoom border center"></div>

4. Нажмите кнопку "Connect".
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_4.png" width=700 class="zoom border center"></div>

5. Выполните полную очистку, для этого нажмите кнопку с ластиком в левом нижнем углу, во всплывающем окне подтвердите действия. Дождитесь окончания очистки.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_5.png" width=700 class="zoom border center"></div>

6. Нажмите **Open file** и выберите файл "MicoAir743v2_PX4-1.15.x_bootloader.bin".
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_6.png" width=700 class="zoom border center"></div>

7. Для загрузки бутлоадера нажмите кнопку "Download" и дождитесь окончания загрузки.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_7.png" width=700 class="zoom border center"></div>

8. Нажмите кнопку "Disconnect".
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_8.png" width=700 class="zoom border center"></div>

9. Выйдите или закройте STM32CubeProgrammer.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_9.png" width=700 class="zoom border center"></div>

10. Откройте QGroundControl и нажмите на логотип в верхнем левом углу.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_10.png" width=700 class="zoom border center"></div>

11. Во всплывающем списке выберите "Vehicle Configuration".
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_11.png" width=700 class="zoom border center"></div>

12. Нажмите на кнопку "Firmware" после чего переподключите полётный контроллер к компьютеру **без зажатой кнопки BOOT**.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_12.png" width=700 class="zoom border center"></div>

13. В окне "Firmware Setup" поставьте галочку "Advanced settings".
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_13.png" width=700 class="zoom border center"></div>

14. В списке снизу выберите "Custom firmware file..." и нажмите кнопку OK.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_14.png" width=700 class="zoom border center"></div>

15. Дождитесь окончания прошивки.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_15.png" width=700 class="zoom border center"></div>

16. Далее можете приступить к настройке полётного контроллера.
<div align="center"><img src="../assets/flight_controller_firmware/PX4/step_16.png" width=700 class="zoom border center"></div>
