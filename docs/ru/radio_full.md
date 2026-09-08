# Подробная настройка аппаратуры управления (Radio)

## Содержание
1. [Обзор аппаратуры](#обзор-аппаратуры)
2. [Настройка аппаратуры](#настройка-аппаратуры)
3. [Создание модели дрона](#создание-модели-дрона)
4. [Загрузка модели](#загрузка-модели)
5. [Сопряжение аппаратуры управления с приемником через Bind Phrase](#сопряжение-аппаратуры-управления-с-приемником-через-bind-phrase)
6. [Сопряжение аппаратуры управления с приемником](#сопряжение-аппаратуры-управления-с-приемником)

## Обзор аппаратуры

<div align="center"><img src="../assets/radio/rc_pocket_front_part.webp" width=900 class="zoom border center"><p>Рисунок 1 – Аппаратура управления, вид спереди</p></div>

<div align="center"><img src="../assets/radio/rc_pocket_back_part.webp" width=900 class="zoom border center"><p>Рисунок 2 – Аппаратура управления, вид сзади</p></div>

## Настройка аппаратуры

1. Снимите черные резиновые накладки с задней стороны аппаратуры управления.
2. Вставьте АКБ, соблюдая полярность.
3. Наденьте резиновые накладки обратно.
4. Включите аппаратуру, зажав кнопку **POWER**.

> **Caution** Если на экране аппаратуры появляются сообщения с предупреждением (картинка WARN), тогда проверьте положение тумблеров и стика газа (Throttle), они должны быть в нулевом положении.  

<div align="center"><img src="../assets/radio/warn.webp" width=350 class="zoom border center"><p>Рисунок 3 – Предупреждение при неверном положении стиков или тумблеров</p></div>

После установки тумблеров и стиков в нулевое положение вы попадете в главное меню.

<div align="center"><img src="../assets/radio/main_menu_no_signal.webp" width=350 class="zoom border center"><p>Рисунок 4 – Главное меню аппаратуры без связи с приемником</p></div>

## Создание модели дрона

1. Нажмите кнопку **MDL**.
2. Выберите пустое поле и зажмите **колесо (энкодер)**, как показано на рисунке 5.

    <div align="center"><img src="../assets/radio/steps_model/step_1.webp" width=350 class="zoom border center"><p>Рисунок 5 – Выбор пустой модели</p></div>

3. Выберите пункт **CREATE MODEL**.
4. Нажмите кнопку **PAGE >**.
5. С помощью **колеса (энкодера)** выберите пункт **«Model name»** и дайте имя вашему дрону, как показано на рисунке 6.

    <div align="center"><img src="../assets/radio/steps_model/step_2.webp" width=350 class="zoom border center"><p>Рисунок 6 – Задание имени модели</p></div>

6. Вернитесь в меню с помощью кнопки **RTN**.
7. С помощью **колеса (энкодера)** спуститесь ниже и включите внутренний передатчик сигнала, как показано на рисунке 7.

  <div align="center">
    <img src="../assets/radio/steps_model/step_3.webp" width=350 class="zoom border center">
    <img src="../assets/radio/steps_model/step_4.webp" width=350 class="zoom border center">
    <p>Рисунок 7 – Включение внутреннего передатчика сигнала</p>
  </div>

8. Перейдите на страницу **MIXES** и включите дополнительные свитчи на аппаратуре, как показано на рисунках 8 и 9:

  <div align="center">
    <img src="../assets/radio/steps_model/step_6.webp" width=350 class="zoom border center">
    <img src="../assets/radio/steps_model/step_7.webp" width=350 class="zoom border center">
    <p>Рисунок 8 – Настройка дополнительных свитчей в меню MIXES</p>
  </div>
   <div align="center"><img src="../assets/radio/steps_model/step_5.webp" width=350 class="zoom border center"><p>Рисунок 9 – Экран со списком настроенных свитчей</p></div>

9. У вас должны быть настроены все свитчи от SA до S1, после чего нажмите кнопку **RTN**. На этом основная настройка модели дрона закончена.

## Загрузка модели

1. Скачайте файл модели дрона на ПК [`model05.yml`](https://drive.google.com/file/d/19Ab9sWPvaOvIavkEXPXzDXCRajpBcO7e/view?usp=sharing).
2. Включите аппаратуру > подключите кабель type-C в верхний USB порт > выберите в меню вариант подключения **USB Storage (SD)**.
3. В появившемся окне перейдите в папку **MODELS** и скопируйте в неё файл `model05.yml`, как показано на рисунке 10.

    <div align="center"><img src="../assets/radio/steps_model/step_8.webp"  height=300 class="zoom border center"><img src="../assets/radio/steps_model/step_9.webp" height=300 class="zoom border center"><p>Рисунок 10 – Копирование файла модели в папку MODELS</p></div>

## Сопряжение аппаратуры управления с приемником через Bind Phrase

### Настройка аппаратуры (передатчика)

1. Включите аппаратуру, зажав кнопку **POWER**.
2. Нажмите кнопку **SYS** и перейдите в меню **ExpressLRS**, как показано на рисунке 11.

    <div align="center"><img src="../assets/radio/rx/elrs_step_1.webp" width=350 class="zoom border center"><p>Рисунок 11 – Переход в меню ExpressLRS для настройки передатчика</p></div>

3. Перейдите во вкладку **WiFi Connectivity** и активируйте подключение **Enable WiFi**, как показано на рисунках 12 и 13.

  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_1.webp" width=350 class="zoom border center">
  </div>
  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_2.webp" width=350 class="zoom border center">
  </div>
  <div align="center">
    <img src="../assets/radio/bind_phrase/elrs_step_3.webp" width=350 class="zoom border center">
    <p>Рисунок 12 – Переход к настройкам WiFi Connectivity</p>
    <p>Рисунок 13 – Включение WiFi на передатчике ExpressLRS</p>
  </div>

4. Подключитесь с компьютера или смартфона к появившейся сети **ExpressLRS TX**. Пароль по умолчанию: **expresslrs**. Пример подключения показан на рисунке 14.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_step_4.webp" width=350 class="zoom border center"><p>Рисунок 14 – Подключение к сети ExpressLRS TX</p></div>

5. Откройте браузер и перейдите по адресу `10.0.0.1`. Стартовый экран показан на рисунке 15.

    > **Note** **Обратите внимание на версию прошивки:** если она меньше 3.3.1, то её следует обновить через [ExpressLRS Web Flasher](https://expresslrs.github.io/web-flasher/).

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_tx.webp" width=350 class="zoom border center"><p>Рисунок 15 – Веб-интерфейс передатчика ExpressLRS</p></div>

6. Введите уникальную **Binding Phrase** и нажмите **SAVE**, как показано на рисунке 16.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_settings.webp" width=700 class="zoom border center"><p>Рисунок 16 – Ввод Binding Phrase в настройках передатчика</p></div>

7. В появившемся окне нажмите кнопку **REBOOT**, как показано на рисунке 17.

    <div align="center"><img src="../assets/radio/bind_phrase/reboot.webp" width=350 class="zoom border center"><p>Рисунок 17 – Перезагрузка передатчика после сохранения настроек</p></div>

### Настройка приемника

1. Переведите приемник в режим **WiFi**, подав питание на полетный контроллер, к которому подключен приемник ELRS и подождав 60 секунд, после чего приемник будет непрерывно моргать.

2. Подключитесь с компьютера или смартфона к появившейся сети **ExpressLRS RX**. Пароль по умолчанию: **expresslrs**. Пример подключения показан на рисунке 18.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_step_5.webp" width=350 class="zoom border center"><p>Рисунок 18 – Подключение к сети ExpressLRS RX</p></div>

3. Откройте браузер и перейдите по адресу `10.0.0.1`. Стартовый экран показан на рисунке 19.

    > **Note** **Обратите внимание** на версию прошивки: если она меньше 3.0.0, то её следует обновить через ["ExpressLRS Web Flasher"](https://expresslrs.github.io/web-flasher/).

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_logo_rx.webp" width=350 class="zoom border center"><p>Рисунок 19 – Веб-интерфейс приемника ExpressLRS</p></div>

4. Введите **ТАКУЮ ЖЕ** уникальную **Binding Phrase**, как и на передатчике, и нажмите **SAVE & REBOOT**, как показано на рисунке 20.

    <div align="center"><img src="../assets/radio/bind_phrase/elrs_settings_2.webp" width=700 class="zoom border center"><p>Рисунок 20 – Ввод Binding Phrase в настройках приемника</p></div>

5. В появившемся окне нажмите кнопку **REBOOT**, как показано на рисунке 21.

    <div align="center"><img src="../assets/radio/bind_phrase/reboot.webp" width=350 class="zoom border center"><p>Рисунок 21 – Перезагрузка приемника после сохранения настроек</p></div>

6. Настройка завершена. После перезагрузки связь должна появиться, как на рисунке 22.

    <div align="center"><img src="../assets/radio/main_menu.webp" width=350 class="zoom border center"><p>Рисунок 22 – Главное меню аппаратуры после настройки через Bind Phrase</p></div>

## Сопряжение аппаратуры управления с приемником

Альтернативный способ — сопряжение через режим **bind** приемника.

1. Переведите приемник в режим **bind**, трижды подключив и отключив питание полетного контроллера, к которому подключен приемник ELRS.

  > **Note** При переходе приемника в режим сопряжения, светодиод на приемнике начнет **мигать дважды с паузой**.

2. Нажмите кнопку **SYS** и перейдите в меню **ExpressLRS**, как показано на рисунке 23.

    <div align="center"><img src="../assets/radio/rx/elrs_step_1.webp" width=350 class="zoom border center"><p>Рисунок 23 – Переход в меню ExpressLRS</p></div>

3. Выставьте **TX Power** на **100mW**, как показано на рисунке 24.

    <div align="center"><img src="../assets/radio/rx/elrs_step_2.webp" width=350 class="zoom border center"><p>Рисунок 24 – Установка мощности передатчика 100mW</p></div>

4. Нажмите кнопку **bind**, дождитесь сопряжения, как показано на рисунке 25.

    <div align="center"><img src="../assets/radio/rx/elrs_step_3.webp" width=350 class="zoom border center"><img src="../assets/radio/rx/elrs_bind.webp" width=350 class="zoom border center"><p>Рисунок 25 – Запуск сопряжения в меню ExpressLRS</p></div>

5. После чего зажмите кнопку **RTN**, и в основном меню появится индикатор связи с приемником, как на рисунке 26.

    <div align="center"><img src="../assets/radio/main_menu.webp" width=350 class="zoom border center"><p>Рисунок 26 – Главное меню аппаратуры после успешного сопряжения</p></div>
