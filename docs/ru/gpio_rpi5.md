# Работа с GPIO на Raspberry Pi 5

## Содержание
1. [Работа с цифровым вводом и выводом через gpiozero](#работа-с-цифровым-вводом-и-выводом-через-gpiozero)
2. [Аппаратный ШИМ на Raspberry Pi 5](#аппаратный-шим-на-raspberry-pi-5)
3. [Подключение и управление сервоприводом](#подключение-и-управление-сервоприводом)

GPIO (General-Purpose Input/Output) – это тип пинов, напряжение на которых можно программно изменять. На Raspberry Pi 5 часть GPIO-пинов поддерживает аппаратный <abbr title="Широтно-импульсная модуляция">ШИМ</abbr> (<abbr title="Pulse-width modulation">PWM</abbr>), которым удобно управлять через библиотеку `rpi_hardware_pwm`.

> **Note** Используйте [схему распиновки](https://pinout.xyz), чтобы понять, какие пины на Raspberry Pi 5 поддерживают GPIO и аппаратный ШИМ.

<div align="center"><img src="../assets/magnet_grip/gpio_servo.webp" width=350 class="zoom border center"><p>Рисунок 1 – Схема распиновки Raspberry Pi</p></div>

> **Success** В отличие от статьи [Работа с GPIO](gpio.md), здесь рассматриваются GPIO на Raspberry Pi 5. Для цифрового ввода и вывода удобно использовать библиотеку `gpiozero`, а для аппаратного ШИМа на поддерживаемых пинах – `rpi_hardware_pwm`.

## Работа с цифровым вводом и выводом через gpiozero

Для цифрового ввода и вывода на Raspberry Pi 5 удобно использовать библиотеку `gpiozero`. Она подходит для случаев, когда нужно включить или выключить нагрузку, считать состояние пина или обработать нажатие кнопки.

> **Info** Нумерация GPIO в примерах ниже использует GPIO-номера пинов, а не физические номера на гребенке Raspberry Pi.

Установите библиотеки `lgpio` и `gpiozero`:

```bash
sudo apt update
sudo apt install python3-lgpio python3-gpiozero
```

Пример работы с библиотекой `gpiozero`:

```python
from time import sleep
from gpiozero import InputDevice, OutputDevice

# Создаем объект для работы с выходом на GPIO17
out_pin = OutputDevice(17)

# Создаем объект для чтения состояния GPIO27
in_pin = InputDevice(27)


# Подаем сигнал на GPIO17
out_pin.on()
sleep(2)

# Отключаем сигнал на GPIO17
out_pin.off()

# Считываем состояние GPIO27
level = in_pin.value
print(f"Input level: {level}")
```

## Аппаратный ШИМ на Raspberry Pi 5

Библиотека `rpi_hardware_pwm` работает только с аппаратными ШИМ-каналами Raspberry Pi.

Для Raspberry Pi 5 можно использовать следующие GPIO-номера пинов:

| GPIO | Физический пин | Канал `HardwarePWM` |
| --- | --- | --- |
| GPIO12 | 32 | 0 |
| GPIO13 | 33 | 1 |

## Подключение и управление сервоприводом

Сервопривод обычно управляется сигналом с частотой 50 Гц. Обычно управляющий сигнал для сервопривода имеет диапазон значений от 1000 до 2000 мкс.

* `1000` мкс — начальное положение;
* `1500` мкс — среднее положение;
* `2000` мкс — конечное положение.

Подключите:

* сигнальный провод сервопривода к `GPIO13`;
* питание сервопривода к внешнему источнику 5 В или через BEC;
* землю внешнего питания обязательно объедините с `GND` Raspberry Pi.

Пример кода для управления сервоприводом:

```python
from rpi_hardware_pwm import HardwarePWM
import time


# Частота управления сервоприводом обычно составляет 50 Гц
SERVO_PWM_HZ = 50

# DUTY - это коэффициент заполнения ШИМ-сигнала в процентах
# При частоте 50 Гц период равен 20 мс:
# 0.5 мс -> 2.5%
# 1.5 мс -> 7.5%
# 2.5 мс -> 12.5%
# Эти импульсы обычно соответствуют положениям 0°, 90° и 180°.
DUTY_0 = 2.5
DUTY_90 = 7.5
DUTY_180 = 12.5

# Создаем объект для работы с аппаратным ШИМ на GPIO13 (PWM1)
pwm = HardwarePWM(pwm_channel=1, hz=SERVO_PWM_HZ, chip=0)


def set_servo_angle(duty_cycle):
    # Применяем новое значение к ШИМ-сигналу
    duty_cycle = max(DUTY_0, min(DUTY_180, duty_cycle))
    pwm.change_duty_cycle(duty_cycle)


def servo_demo(wait_s=2):
    try:
        # Запускаем ШИМ и сразу ставим сервопривод в положение 0°
        pwm.start(DUTY_0)
        time.sleep(1)

        print("0°")
        set_servo_angle(DUTY_0)
        time.sleep(wait_s)

        # Переводим сервопривод в 90°
        print("90°")
        set_servo_angle(DUTY_90)
        time.sleep(wait_s)

        # Переводим сервопривод в 180°
        print("180°")
        set_servo_angle(DUTY_180)
        time.sleep(wait_s)
    finally:
        # При явной остановке отключаем ШИМ
        pwm.stop()


if __name__ == "__main__":
    servo_demo()
```

> **Note** После вызова `pwm.stop()` управляющий сигнал пропадает, поэтому редуктор перестает удерживать позицию и может изменить своё положение.
