# Первоначальная настройка

## Установка QGroundControl

**QGroundControl** – программное обеспечение, необходимое для прошивки, настройки и калибровки полетного контроллера Клевера.

<img src="../assets/qgc.webp" alt="QGroundControl" class="zoom">

Для настройки используйте QGroundControl версии 5.1.4. Скачайте установщик для Windows, Linux или macOS на странице [релиза QGroundControl v5.1.4](https://github.com/mavlink/QGroundControl/releases/tag/v5.1.4). Если установщик предложит поставить дополнительные драйверы, согласитесь с установкой.

См. также [основную документацию по QGroundControl](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/).

## Загрузка прошивки в полетный контроллер

Скачайте прошивку PX4 для полётного контроллера. Актуальные версии:

- Для `micoair_h743-v2` — **1.16.0**, файл [`micoair_h743-v2_default.px4`](https://github.com/PX4/PX4-Autopilot/releases/download/v1.16.0/micoair_h743-v2_default.px4).
- Для `pixracer_R15` — **1.13.3**, файл [`px4fmu-v4_default.px4`](https://github.com/PX4/PX4-Autopilot/releases/download/v1.13.3/px4fmu-v4_default.px4).

Инструкция по прошивке:

1. Отключите полетный контроллер от компьютера (если он подключен).
2. Запустите программу QGroundControl.
3. Перейдите в панель *Vehicle Configuration* (кликнув на логотип QGroundControl в левом верхнем углу) и выберите меню *Firmware*.
4. Подключите полетный контроллер к компьютеру по USB.
5. Выберите в появившемся меню справа *PX4 Flight Stack*.

   <img src="../assets/qgc-firmware.webp" alt="QGroundControl firmware upload" class="zoom">

6. Для выбора и загрузки файла прошивки:

   * Выберите *Advanced settings*.
   * В выпадающем меню выберите *Custom firmware file...*
   * Нажмите *OK* и выберите скаченный файл прошивки.

Дождитесь, пока QGroundControl загрузит прошивку и выполнит перезагрузку полетного контроллера.

> **Warning** Не отключайте полетный контроллер от компьютера в процессе загрузки прошивки.


## Настройка полетного контроллера

> **Hint** Все дальнейшие настройки и калибровки полетного контроллера могут быть выполнены без проводов с применением [доступа к полетному контроллеру по Wi-Fi через Raspberry Pi](gcs_bridge.md).

<img src="../assets/qgc-requires-setup.webp" alt="QGroundControl overview" class="zoom">

1. Параметры, нуждающиеся в настройке: *Airframe*, *Radio*, *Sensors*, *Flight Modes*.
2. Текущая прошивка контроллера.
3. Текущий полетный режим.
4. Сообщения об ошибках.

### Выбор рамы

<img src="../assets/qgc-frame-apply-clover4.webp" alt="QGroundControl frame selection" class="zoom">

1. Выберите меню *Airframe*.
2. Выберите тип рамы *Quadrotor*.
3. Для Клевера 4 выберите подтип рамы *COEX Clover 4*. Для Клевера 5 – *Generic Quadrotor*.
4. Переместитесь в начало списка и нажмите кнопку *Apply and Restart*, подтвердите нажатием *Apply*.
5. Дождитесь применения настроек и перезагрузки полетного контроллера.

### Параметры

Для настройки параметров полетного контроллера войдите во вкладку *Vehicle Configuration* и выберите меню *Parameters*. Вы можете использовать поле *Search* для поиска параметров по имени. Рекомендуемые параметры для Клевера приведены в дальнейшей документации.

<img src="../assets/qgc-parameters.webp" alt="QGroundControl parameters" class="zoom">

После установки параметра необходимо нажать кнопку *Save*. При необходимости – перезагрузить полетный контроллер, нажав кнопку *Tools*, затем *Reboot vehicle*.


#### Файлы с параметрами

Вы можете загрузить настроенный пресет через меню во вкладке *Parameters*, для этого нажмите на кнопку *Tools*, после чего в всплывающем окне выберете *Load from file...* и выберете файл ``.params``.  

- Параметры для clover-4 - [clover-4.params](https://drive.google.com/file/d/1lPq6y8CVDUKBxo5hVujcWUJAfzTqqCx1/view?usp=sharing)  
- Параметры для clover-5 - [clover-5.params](https://drive.google.com/file/d/1z8tDCJZqSyJtySgBizllgdF7DIC28A9C/view?usp=sharing)


#### Настройка PID-регуляторов


##### Усредненные коэффициенты PID для Клевера 5

* `MC_PITCHRATE_P` = 0.176  
* `MC_PITCHRATE_I` = 0.213  
* `MC_PITCHRATE_D` = 0.0018  
* `MC_ROLLRATE_P` = 0.176  
* `MC_ROLLRATE_I` = 0.213  
* `MC_ROLLRATE_D` = 0.0018  
* `MC_YAWRATE_P` = 0.25  
* `MC_YAWRATE_I` = 0.09  
* `MPC_XY_P` = 1.8  
* `MPC_Z_P` = 1.5  
* `MPC_XY_VEL_P_ACC` = 3.45  
* `MPC_XY_VEL_D_ACC` = 0.15  
* `MPC_XY_VEL_I_ACC` = 1.0  
* `MPC_Z_VEL_P_ACC` = 5.5  
* `MPC_Z_VEL_I_ACC` = 2.3  
* `MPC_THR_HOVER` = 0.4  
* `MPC_ACC_DOWN_MAX` = 2.0  

##### Усредненные коэффициенты PID для Клевера 4

* `MC_PITCHRATE_P` = 0.072
* `MC_PITCHRATE_I` = 0.037
* `MC_PITCHRATE_D` = 0.0021
* `MC_PITCH_P` = 8.5
* `MC_ROLLRATE_P` = 0.072
* `MC_ROLLRATE_I` = 0.037
* `MC_ROLLRATE_D` = 0.0021
* `MC_ROLL_P` = 8.5
* `MPC_XY_VEL_P_ACC` = 2.2
* `MPC_XY_VEL_D_ACC` = 0.26
* `MPC_XY_P` = 0.9
* `MPC_Z_VEL_P_ACC` = 4.8
* `MPC_Z_P` = 1.2


> **Hint** Необходимо учитывать, что для идеального полета параметры PID-регуляторов подбираются вручную для каждого конкретного собранного квадрокоптера. Вы можете узнать больше об этом в статье "[Настройка PID-регуляторов](pid_tuning.md)".

**Далее**: [Калибровка датчиков](calibration.md).
