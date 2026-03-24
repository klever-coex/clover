# Настройка аппаратуры управления (Radio)

## Содержание
1. [Обзор аппаратуры](#обзор-аппаратуры)
2. [Настройка аппаратуры](#настройка-аппаратуры)
3. [Создание модели дрона](#создание-модели-дрона)
4. [Загрузка модели](#загрузка-модели)
5. [Сопряжение аппаратуры управления с приемником](#сопряжение-аппаратуры-управления-с-приемником)
6. [Сопряжение аппаратуры управления с приемником через Bind Phrase](#сопряжение-аппаратуры-управления-с-приемником-через-bind-phrase)

## Обзор аппаратуры

<div align="center"><img src="../assets/radio/rc_pocket_front_part.png" width=900 class="zoom border center"></div>

<div align="center"><img src="../assets/radio/rc_pocket_back_part.png" width=900 class="zoom border center"></div>

## Настройка аппаратуры

1. Снимите черные резиновые накладки с задней стороны аппаратуры управления.
2. Вставьте АКБ, соблюдая полярность.
3. Наденьте резиновые накладки обратно.
4. Включите аппаратуру, зажав кнопку **POWER**.

> **Caution** Если на экране аппаратуры появляются сообщения с предупреждением (картинка WARN), тогда проверьте положение тумблеров и стика газа (Throttle), они должны быть в нулевом положении.  

<div align="center"><img src="../assets/radio/rc_pocket.png" width=700 class="zoom border center"></div>

<div align="center"><img src="../assets/radio/main_menu_no_signal.jpg" width=350 class="zoom border center"></div>

## Создание модели дрона

1. Нажмите кнопку **MDL**.
2. Выберите пустое поле и зажмите **колесо (энкодер)**.

    <div align="center"><img src="../assets/radio/steps_model/step_1.jpg" width=350 class="zoom border center"></div>

3. Выберите пункт **CREATE MODEL**.
4. Нажмите кнопку **PAGE >**.
5. С помощью **колеса (энкодера)** выберите пункт **«Model name»** и дайте имя вашему дрону.

    <div align="center"><img src="../assets/radio/steps_model/step_2.jpg" width=350 class="zoom border center"></div>

6. Вернитесь в меню с помощью кнопки **RTN**.
7. С помощью **колеса (энкодера)** спуститесь ниже и включите внутренний передатчик сигнала.

  <div align="center">
    <img src="../assets/radio/steps_model/step_3.jpg" width=350 class="zoom border center">
    <img src="../assets/radio/steps_model/step_4.jpg" width=350 class="zoom border center">
  </div>

8. Перейдите на страницу **MIXES** и включите дополнительные свитчи на аппаратуре:

  <div align="center">
    <img src="../assets/radio/steps_model/step_6.jpg" width=350 class="zoom border center">
    <img src="../assets/radio/steps_model/step_7.jpg" width=350 class="zoom border center">
  </div>
   <div align="center"><img src="../assets/radio/steps_model/step_5.jpg" width=350 class="zoom border center"></div>

9. У вас должны быть настроены все свитчи от SA до S1, после чего нажмите кнопку **RTN**. На этом основная настройка модели дрона закончена.

## Загрузка модели

1. Скачайте файл модели дрона на ПК [`model05.yml`](https://drive.google.com/file/d/19Ab9sWPvaOvIavkEXPXzDXCRajpBcO7e/view?usp=sharing).
2. Включите аппаратуру > подключите кабель type-C в верхний USB порт > выберите в меню вариант подключения **USB Storage (SD)**.
3. В появившемся окне перейдите в папку **MODELS** и скопируйте в неё файл `model05.yml`.

    <div align="center"><img src="../assets/radio/steps_model/step_8.png"  height=300 class="zoom border center"><img src="../assets/radio/steps_model/step_9.png" height=300 class="zoom border center"></div>

## Сопряжение аппаратуры управления с приемником

1. Переведите приемник в режим **bind**, трижды подключив и отключив питание полетного контроллера, к которому подключен приемник ELRS.

  > **Note** При переходе приемника в режим сопряжения, светодиод на приемнике начнет **мигать дважды с паузой**.

2. Нажмите кнопку **SYS** и перейдите в меню **ExpressLRS**.

    <div align="center"><img src="../assets/radio/rx/elrs_step_1.jpg" width=350 class="zoom border center"></div>

3. Выставьте **TX Power** на **100mW**.

    <div align="center"><img src="../assets/radio/rx/elrs_step_2.jpg" width=350 class="zoom border center"></div>

4. Нажмите кнопку **bind**, дождитесь сопряжения.

    <div align="center"><img src="../assets/radio/rx/elrs_step_3.jpg" width=350 class="zoom border center"><img src="../assets/radio/rx/elrs_bind.jpg" width=350 class="zoom border center"></div>

5. После чего зажмите кнопку **RTN**, и в основном меню появится индикатор связи с приемником.

    <div align="center"><img src="../assets/radio/main_menu.jpg" width=350 class="zoom border center"></div>

## Сопряжение аппаратуры управления с приемником через Bind Phrase

### Настройка аппаратуры (передатчика)

1. Включите аппаратуру, зажав кнопку **POWER**.
2. Нажмите кнопку **SYS** и перейдите в меню **ExpressLRS**.

    <div align="center"><img src="../assets/radio/rx/elrs_step_1.jpg" width=350 class="zoom border center"></div>

3. Перейдите во вкладку **WiFi Connectivity** и активируйте подключение **Enable WiFi**.

  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_1.jpg" width=350 class="zoom border center">
  </div>
  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_2.jpg" width=350 class="zoom border center">
  </div>
  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_3.jpg" width=350 class="zoom border center">
  </div>

4. Подключитесь с компьютера или смартфона к появившейся сети **ExpressLRS TX**. Пароль по умолчанию: **expresslrs**.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_step_4.png" width=350 class="zoom border center"></div>

5. Откройте браузер и перейдите по адресу `10.0.0.1`.

    > **Note** **Обратите внимание на версию прошивки:** если она меньше 3.3.1, то её следует обновить через [ExpressLRS Web Flasher](https://expresslrs.github.io/web-flasher/).

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_tx.png" width=350 class="zoom border center"></div>

6. Введите уникальную **Binding Phrase** и нажмите **SAVE**.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_settings.png" width=700 class="zoom border center"></div>

7. В появившемся окне нажмите кнопку **REBOOT**.

    <div align="center"><img src="../assets/radio/bind_phrase/reboot.png" width=350 class="zoom border center"></div>

### Настройка приемника

1. Переведите приемник в режим **WiFi**, подав питание на полетный контроллер, к которому подключен приемник ELRS и подождав 60 секунд, после чего приемник будет непрерывно моргать.

2. Подключитесь с компьютера или смартфона к появившейся сети **ExpressLRS RX**. Пароль по умолчанию: **expresslrs**.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_step_5.png" width=350 class="zoom border center"></div>

3. Откройте браузер и перейдите по адресу `10.0.0.1`.

    > **Note** **Обратите внимание** на версию прошивки: если она меньше 3.0.0, то её следует обновить через ["ExpressLRS Web Flasher"](https://expresslrs.github.io/web-flasher/).

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_rx.png" width=350 class="zoom border center"></div>

4. Введите **ТАКУЮ ЖЕ** уникальную **Binding Phrase**, как и на передатчике, и нажмите **SAVE & REBOOT**.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_settings_2.png" width=700 class="zoom border center"></div>

5. В появившемся окне нажмите кнопку **REBOOT**.

    <div align="center"><img src="../assets/radio/bind_phrase/reboot.png" width=350 class="zoom border center"></div>

6. Настройка завершена.

    <div align="center"><img src="../assets/radio/main_menu.jpg" width=350 class="zoom border center"></div>
