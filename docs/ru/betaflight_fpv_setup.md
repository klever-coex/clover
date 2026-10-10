# Настройка FPV в Betaflight для MicoAir743v2

> **Success** Документация описывает базовую настройку FPV-квадрокоптера на полётном контроллере **MicoAir743v2** в **Betaflight Configurator** после прошивки контроллера Betaflight.
> [Документация по прошивке с PX4 на Betaflight](firmware_Betaflight_MicoAir743v2.md)

<p/>

> **Caution** Перед настройкой и особенно перед проверкой моторов **обязательно снимите пропеллеры**.

## Содержание
1. [Подключение и подготовка](#подключение-и-подготовка)
2. [Калибровка и базовая конфигурация](#калибровка-и-базовая-конфигурация)
3. [Настройка портов](#настройка-портов)
4. [Настройка приёмника и режимов](#настройка-приёмника-и-режимов)
5. [Настройка моторов](#настройка-моторов)
6. [Настройка OSD](#настройка-osd)
7. [Настройка видеопередатчика](#настройка-видеопередатчика)
8. [Настройка LED-ленты](#настройка-led-ленты)
9. [Финальная проверка](#финальная-проверка)

## Подключение и подготовка

1. Подключите полётный контроллер к компьютеру по USB и откройте **Betaflight Configurator**.
2. Убедитесь, что включён режим **Enable Expert Mode**, чтобы были доступны все необходимые вкладки.
3. Если после подключения появляется предупреждение о некалиброванном акселерометре, сначала выполните калибровку, а затем продолжайте настройку.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_1.webp" width="700" class="zoom border center"></div>

## Калибровка и базовая конфигурация

1. Откройте вкладку **Setup** и нажмите **Calibrate Accelerometer**. Во время калибровки рама должна лежать неподвижно на ровной поверхности.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_2.webp" width="700" class="zoom border center"></div>

2. Перейдите во вкладку **Configuration**.
3. В разделе **System configuration** оставьте включённым **Accelerometer**, если планируется режим стабилизации, и отключите ненужные датчики, если они не используются.
4. В поле **Craft name** укажите имя квадрокоптера, в поле **Pilot name** при необходимости укажите имя пилота.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_3.webp" width="700" class="zoom border center"></div>

5. В разделе **Other Features** включите:
   - **AIRMODE**
   - **DISPLAY**
   - **LED_STRIP**
   - **OSD**

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_4.webp" width="700" class="zoom border center"></div>

6. Нажмите **Save and Reboot**.

## Настройка портов

1. Откройте вкладку **Ports**.
2. Настройте порты следующим образом:
   - **UART2**: выключите **MSP** и в разделе **Peripherals** выберите **VTX (IRC Tramp)**.
   - **UART3**: если подключён GPS, в разделе **Sensor Input** выберите **GPS** и скорость **57600**.
   - **UART6**: включите **Serial RX** для приёмника.
   - **UART7**: если используется телеметрия ESC, выберите **ESC**.
3. Нажмите **Save and Reboot**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_5.webp" width="700" class="zoom border center"></div>

> **Caution** Если у вас приёмник, GPS или VTX подключены к другим UART, выставляйте настройки в соответствии с фактическим подключением.

## Настройка приёмника и режимов

### Приёмник

1. Откройте вкладку **Receiver**.
2. В поле **Receiver Mode** выберите **Serial (via UART)**.
3. В поле **Serial Receiver Provider** выберите **CRSF**.
4. Проверьте, что стики корректно двигаются во вкладке Preview.
5. Для карты каналов используйте **AETR1234**.
6. При необходимости выполните привязку приёмника кнопкой **Bind Receiver**.
7. Нажмите **Save**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_6.webp" width="700" class="zoom border center"></div>

### Режимы

1. Откройте вкладку **Modes**.
2. Настройте режимы, как показано на скриншотах:
   - **ARM** на **AUX1**, диапазон примерно `1700-2100`
   - **ANGLE** на **AUX3**, диапазон примерно `1300-1700`
   - **HORIZON** на **AUX3**, диапазон примерно `1700-2100`
   - **FAILSAFE** на **AUX4**, диапазон примерно `1700-2100`
   - **BEEPER** на **AUX4**, диапазон примерно `1700-2100`
3. Нажмите **Save**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_7.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_8.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_9.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_10.webp" width="700" class="zoom border center"></div>

> **Caution** Значения AUX-каналов могут отличаться в зависимости от вашей аппаратуры. После настройки обязательно проверьте переключатели в реальном времени.

## Настройка моторов

> **Caution** Не проверяйте моторы с установленными пропеллерами.

1. Откройте вкладку **Motors**.
2. Для схемы квадрокоптера выберите **QUAD X**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_11.webp" width="700" class="zoom border center"></div>

3. В разделе **ESC/Motor Features** выставьте:
   - **ESC/Motor protocol**: `DSHOT600`
   - **ESC_SENSOR**: включено
   - **Bidirectional DShot**: включено
   - **Motor poles**: `14`
   - **Motor Idle (% static)**: `5.5`

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_12.webp" width="700" class="zoom border center"></div>

4. Включите **Motor direction is reversed**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_13.webp" width="700" class="zoom border center"></div>

5. Для настройки направления вращения нажмите **Motor direction**.
6. Подтвердите предупреждение, что пропеллеры сняты, и выберите способ настройки.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_14.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_15.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_16.webp" width="700" class="zoom border center"></div>

7. Для настройки порядка моторов нажмите **Reorder motors**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_17.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_18.webp" width="700" class="zoom border center"></div>

8. Если моторы вращаются не в ту сторону, измените направление через мастер настройки или по одному мотору.

## Настройка OSD

1. Откройте вкладку **OSD**.
2. Для аналоговой видеосистемы выберите формат видеосвязи **Auto**.
3. В разделе **Units** выберите **Metric**.
4. Настройте таймеры:
   - **Timer 1**: `Last armed time`
   - **Timer 2**: `On/Armed time`
5. В разделе **Alarms** можно использовать значения как на примере:
   - **RSSI**: `20`
   - **Capacity**: `2200`
   - **Altitude**: `100`
   - **Link Quality**: `60`

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_19.webp" width="700" class="zoom border center"></div>

6. Включите и разместите на экране основные элементы OSD:
   - **Craft name**
   - **Battery voltage**
   - **Disarmed**
   - **Fly mode**
   - **GPS latitude**
   - **GPS longitude**
   - **Throttle position**
   - **Timer 1**
   - **Timer 2**
   - **VTX channel**
   - **Warnings**
7. После размещения элементов нажмите **Save**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_20.webp" width="700" class="zoom border center"></div>

## Настройка видеопередатчика

> **Caution** Перед подачей питания подключите антенну к видеопередатчику. Не включайте видеопередатчик без антенны: это может привести к его повреждению. Используйте только разрешённые в вашем регионе частоты и мощность передатчика.

1. Откройте вкладку **Video Transmitter**.
2. Если таблица VTX ещё не загружена, нажмите **Load from file**.
3. Выберите файл VTX-таблицы.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_21.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_22.webp" width="700" class="zoom border center"></div>

4. После загрузки таблицы проверьте параметры:
   - **Band**: `RACEBAND`
   - **Channel**: `Channel 5`
   - **Power**: `25`
   - **Pit Mode**: по необходимости
   - **Low Power Disarm**: `Off`
5. Убедитесь, что таблица частот и уровней мощности загрузилась корректно.
6. Нажмите **Save**.

## Настройка LED-ленты

1. Убедитесь, что функция **LED_STRIP** уже включена во вкладке **Configuration**.
2. Откройте вкладку **LED Strip**.
3. Разметьте используемые светодиоды на сетке.
4. Нажмите **Wire Ordering Mode** и задайте порядок светодиодов.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_23.webp" width="700" class="zoom border center"></div>

5. В поле **Function** выберите **Color**.
6. При необходимости в **Color modifier** выберите режим, например **Throttle**.
7. Назначьте цвета на свое усмотрение и нажмите **Save**.

    <div align="center"><img src="../assets/betaflight_fpv_setup/step_24.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_25.webp" width="700" class="zoom border center"></div>
    <div align="center"><img src="../assets/betaflight_fpv_setup/step_26.webp" width="700" class="zoom border center"></div>

## Финальная проверка

1. Проверьте, что во вкладке **Setup** модель квадрокоптера повторяет реальные движения рамы.
2. Убедитесь, что стики и переключатели корректно отображаются во вкладке **Receiver**.
3. Проверьте, что при переключении режимов во вкладке **Modes** активируются нужные диапазоны.
4. Проверьте направление вращения моторов без пропеллеров.
5. Убедитесь, что OSD отображается в очках или видеошлеме.

После этого можно переходить к установке пропеллеров и аккуратному первому тестовому запуску.
