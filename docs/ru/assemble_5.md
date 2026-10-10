# Сборка Клевера 5 КОД

## Содержание
1. [Схема подключения электронных компонентов](#схема-подключения-электронных-компонентов)
2. [Сборка рамы](#сборка-рамы)
3. [Установка бесколлекторных электродвигателей](#установка-бесколлекторных-электродвигателей)
4. [Установка регулятора оборотов](#установка-регулятора-оборотов)
5. [Установка алюминиевых стоек](#установка-алюминиевых-стоек)
6. [Установка полетного контроллера](#установка-полетного-контроллера)
7. [Установка одноплатного компьютера Raspberry Pi 5](#установка-одноплатного-компьютера-raspberry-pi-5)
8. [Установка защиты, ножек и светодиодной ленты](#установка-защиты-ножек-и-светодиодной-ленты)

## Крепежные элементы

> **Success** Используйте крепежные элементы только в соответствии с настоящей инструкцией. Установка винтов или стоек несоответствующего размера может привести к повреждению квадрокоптера.

<div align="center"> <table class="type_table">
  <tr>
    <td id="cell1"><div align="center"><strong>Ячейка 1</strong><br><img src="../assets/assembling_clever5/fasteners/nut_press.webp" width="20"/><br>Гайка запрессовочная М3</div></td>
    <td id="cell2"><div align="center"><strong>Ячейка 2</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.webp" width="20"/><br>Гайка нейлоновая М3</div></td>
    <td id="cell3"><div align="center"><strong>Ячейка 3</strong><br><img src="../assets/assembling_clever5/fasteners/hts-m2,5.webp" width="35"/><br>Стойка нейлоновая M2.5х6</div></td>
    <td id="cell4"><div align="center"><strong>Ячейка 4</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.webp" width="16"/><br>Гайка нейлоновая М2.5</div></td>
    <td id="cell5"><div align="center"><strong>Ячейка 5</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.webp" width="12"/><br>Гайка нейлоновая М2</div></td>
  </tr>
  <tr>
    <td id="cell6"><div align="center"><strong>Ячейка 6</strong><br><img src="../assets/assembling_clever5/fasteners/m3x40.webp" width="150" height="30"/><br>Винт M3x40</div></td>
    <td id="cell7"><div align="center"><strong>Ячейка 7</strong><br><img src="../assets/assembling_clever5/fasteners/m3x12.webp" width="95" height="30"/><br>Винт M3x12</div></td>
    <td id="cell8"><div align="center"><strong>Ячейка 8</strong><br><img src="../assets/assembling_clever5/fasteners/m3x8.webp" width="70" height="30"/><br>Винт M3x8</div></td>
    <td id="cell9"><div align="center"><strong>Ячейка 9</strong><br><img src="../assets/assembling_clever5/fasteners/m3x6.webp" width="45" height="30"/><br>Винт M3x6</div></td>
    <td id="cell10"><div align="center"><strong>Ячейка 10</strong><br><img src="../assets/assembling_clever5/fasteners/m3x4.webp" width="35" height="30"/><br>Винт M3x4</div></td>
  </tr>
  <tr>
    <td id="cell11"><div align="center"><strong>Ячейка 11</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_40.webp" width="130" height="15"/><br>Стойка алюминиевая M3x40</div></td>
    <td id="cell12"><div align="center"><strong>Ячейка 12</strong><br><img src="../assets/assembling_clever5/fasteners/dumper.webp" width="50"/><br>Стойка антивибрационная</div></td>
    <td id="cell13"><div align="center"><strong>Ячейка 13</strong><br><img src="../assets/assembling_clever5/fasteners/m3x10.webp" width="80" height='30'/><br>Винт M3x10</div></td>
    <td id="cell14"><div align="center"><strong>Ячейка 14</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_10.webp" width="40" height="15"/><br>Стойка алюминиевая M3x10</div></td>
    <td id="cell15"><div align="center"><strong>Ячейка 15</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_40.webp" width="100" height="15"/><br>Стойка алюминиевая M3x30</div></td>
  </tr>
  <tr>
    <td id="cell16"><div align="center"><strong>Ячейка 16</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x6.webp" width="50" height="20"/><br>Винт M2x6</div></td>
    <td id="cell17"><div align="center"><strong>Ячейка 17</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x4.webp" width="50" height="25"/><br>Винт M2.5x4</div></td>
    <td id="cell18"><div align="center"><strong>Ячейка 18</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x6.webp" width="60" height="25"/><br>Винт M2.5x6</div></td>
    <td id="cell19"><div align="center"><strong>Ячейка 19</strong><br><img src="../assets/assembling_clever5/fasteners/m1,4x3.webp" width="35"/><br>Саморез M1.4x4</div></td>
    <td id="cell20"><div align="center"><strong>Ячейка 20</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x4.webp" width="35" height="20"/><br>Винт M2x3</div></td>
  </tr>
  <tr>
    <td id="cell21"><div align="center"><strong>Ячейка 21</strong><br><img src="../assets/assembling_clever5/fasteners/htp-30.webp" width="100" height="15"/><br>Стойка нейлоновая M3x30</div></td>
    <td id="cell22"><div align="center"><strong>Ячейка 22</strong><br><img src="../assets/assembling_clever5/fasteners/htp-20.webp" width="70" height="15"/><br>Стойка нейлоновая M3x20</div></td>
    <td id="cell23"><div align="center"><strong>Ячейка 23</strong><br><img src="../assets/assembling_clever5/fasteners/htp-40.webp" width="130" height="15"/><br>Стойка нейлоновая M3x40</div></td>
    <td id="cell24"><div align="center"><strong>Ячейка 24</strong><br><img src="../assets/assembling_clever5/fasteners/m1,4x10.webp" width="60"/><br>Саморез M1.4x10</div></td>
    <td id="cell25"><div align="center"><strong>Ячейка 25</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x25.webp" width="120"/><br>Винт М2.5х25</div></td>
  </tr>
</table></div>

## Схема подключения электронных компонентов

> **Success** Подключайте электронные компоненты согласно приведенной схеме.

<div align="center"><img src="../assets/assembling_clever5/ru/layout.webp" width=700 class="zoom border center"></div>

## Сборка рамы

1. Совместите четыре луча между верхней и нижней декой рамы.

    <div align="center"><img src="../assets/assembling_clever5/ru/frame/frame_step_1.webp" width=700 class="zoom border center"></div>

2. Установите винты M3x12 (<a href="#cell7">Ячейка 7</a>) в крайние отверстия лучей. Установите винты M3x40 (<a href="#cell6">Ячейка 6</a>) в центральные отверстия нижней деки.

    <div align="center"><img src="../assets/assembling_clever5/ru/frame/frame_step_2.webp" width=700 class="zoom border center"></div>

3. Установите запрессовочные гайки М3 (<a href="#cell1">Ячейка 1</a>) в предусмотренные отверстия нижней деки. Закрутите ранее установленные винты до надежной фиксации нижней деки и лучей рамы.

    <div align="center"><img src="../assets/assembling_clever5/ru/frame/frame_step_3.webp" width=700 class="zoom border center"></div>

## Установка бесколлекторных электродвигателей

1. Установите электродвигатели в предусмотренные отверстия лучей и закрепите их **винтами М3х8** (<a href="#cell8">Ячейка 8</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/motor.webp" width=700 class="zoom border center"></div>

> **Caution** Убедитесь, что винты надежно закреплены и не выступают в область обмоток электродвигателей. Использование винтов неправильной длины может привести к повреждению обмоток и короткому замыканию.

## Установка регулятора оборотов

1. Установите регулятор оборотов (ESC) поверх винтов M3x40 (<a href="#cell6">Ячейка 6</a>) на средней деке. Разъем питания аккумулятора должен быть направлен назад.

    <div align="center"><img src="../assets/assembling_clever5/ru/esc_step_1.webp" width=700 class="zoom border center"></div>

2. Подсоедините разъемы MR30 электродвигателей к регулятору оборотов (ESC). Уложите провода, как показано на изображении, и закрепите их на лучах пластиковыми хомутами.

    <div align="center"><img src="../assets/assembling_clever5/ru/esc_step_2.webp" width=700 class="zoom border center"></div>

## Установка алюминиевых стоек

1. Установите алюминиевые стойки M3x40 (<a href="#cell11">Ячейка 11</a>) на нижнюю деку с использованием антивибрационных стоек (<a href="#cell12">Ячейка 12</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/aluminium_40_step_1.webp" width=700 class="zoom border center"></div>

2. Закрутите антивибрационные стойки со стороны нижней деки и надежно зафиксируйте их.

    <div align="center"><img src="../assets/assembling_clever5/ru/aluminium_40_step_2.webp" width=700 class="zoom border center"></div>

## Установка полетного контроллера

1. Закрутите нейлоновые гайки M3 (<a href="#cell2">Ячейка 2</a>) на установленные винты M3x40 (<a href="#cell6">Ячейка 6</a>). Установите полетный контроллер стрелкой вперед и зафиксируйте его нейлоновыми гайками М3 (<a href="#cell2">Ячейка 2</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/flight_controller_step_1.webp" width=700 class="zoom border center"></div>

2. Установите 8-пиновый шлейф между полетным контроллером и регулятором оборотов (ESC).

    <div align="center"><img src="../assets/assembling_clever5/ru/flight_controller_step_2.webp" width=700 class="zoom border center"></div>

3. Вид с установленным шлейфом.

    <div align="center"><img src="../assets/assembling_clever5/ru/flight_controller_step_3.webp" width=700 class="zoom border center"></div>

## Установка одноплатного компьютера Raspberry Pi 5

1. Установите на пластиковую монтажную деку нейлоновые стойки M2.5 (<a href="#cell3">Ячейка 3</a>) с помощью винтов M2.5x4 (<a href="#cell17">Ячейка 17</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_1.webp" width=700 class="zoom border center"></div>

2. Закрутите винты. Используйте биту H1.5/HEX1.5.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_2.webp" width=700 class="zoom border center"></div>

3. Установите Raspberry Pi 5 на установленные стойки M2.5х6.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_3.webp" width=700 class="zoom border center"></div>

4. Зафиксируйте Raspberry Pi 5 винтами М2.5х4 (<a href="#cell17">Ячейка 17</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_4.webp" width=700 class="zoom border center"></div>

5. Снимите защитные пленки с обеих сторон термопрокладок. Установите термопрокладки на позиции, выделенные красными рамками на изображении. Установите радиатор охлаждения на Raspberry Pi 5. Для этого вставьте фиксирующие клипсы через радиатор в предусмотренные отверстия Raspberry Pi 5. Подключите систему охлаждения в предусмотренный разъем, расположенный под защитной крышкой.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_5.webp" width=700 class="zoom border center"></div>

6. Raspberry Pi с радиатором в сборе.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_6.webp" width=700 class="zoom border center"></div>

7. Установите нейлоновые стойки 30мм (<a href="#cell21">Ячейка 21</a>) на деку с Raspberry Pi 5 с помощью винтов M3x8 (<a href="#cell8">Ячейка 8</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_7.webp" width=700 class="zoom border center"></div>

8. Вид с установленными нейлоновыми стойками.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_8.webp" width=700 class="zoom border center"></div>

9. Установите собранную деку c Raspberry Pi 5 на антивибрационные стойки собранной рамы конструктора. Зафиксируйте деку винтами M3x4 (<a href="#cell10">Ячейка 10</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_9.webp" width=700 class="zoom border center"></div>

10. Подключите к Raspberry Pi 5 шлейф телеметрии. Подключение выполните во внешнюю линию гребенки, начиная с пина 8 (GPIO 14). Черный провод подключите к пину 14 (Ground) (см. pinout). Ответную часть шлейфа подключите к порту UART4 полетного контроллера (черный провод — в крайний правый угол).
    
    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_10.webp" width=700 class="zoom border center"></div>
    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_pinout.webp" width=400 class="zoom border center"></div>

11. Установите камеру компьютерного зрения на малую монтажную деку. Зафиксируйте камеру саморезами М1.4х4 (<a href="#cell19">Ячейка 19</a>) в предусмотренных отверстиях. Используйте биту PH1.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_11.webp" width=700 class="zoom border center"></div>

12. На малую монтажную деку установите нейлоновые стойки M3x20 (<a href="#cell22">Ячейка 22</a>) и зафиксируйте их винтами M3x6 (<a href="#cell9">Ячейка 9</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_12.webp" width=700 class="zoom border center"></div>

13. Установите малую монтажную деку с камерой компьютерного зрения на деку захвата с помощью винтов M3x6 (<a href="#cell9">Ячейка 9</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_13.webp" width=700 class="zoom border center"></div>

14. Установите лазерный дальномер на деку захвата с помощью винтов M2x6 (<a href="#cell16">Ячейка 16</a>) и нейлоновых гаек M2 (<a href="#cell5">Ячейка 5</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_14.webp" width=700 class="zoom border center"></div>

15. Подключите шлейф лазерного дальномера.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_15.webp" width=700 class="zoom border center"></div>

16. Установите деку захвата на раму конструктора с помощью винтов M3x8 (<a href="#cell8">Ячейка 8</a>). Подключите шлейф камеры к компьютеру согласно схеме подключения.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_16.webp" width=700 class="zoom border center"></div>

17. Подключите шлейф дальномера к порту UART1 полетного контроллера (вставьте черный провод в крайний левый пин). Протяните кабель через отверстие в кожухе полетного контроллера.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_17.webp" width=700 class="zoom border center"></div>

18. Установите экран на кожух полетного контроллера при помощи винтов M2.5x6 (<a href="#cell18">Ячейка 18</a>) и нейлоновых гаек M2.5 (<a href="#cell4">Ячейка 4</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_18.webp" width=700 class="zoom border center"></div>

19. Установите UBEC на деку с Raspberry Pi 5 с помощью двухсторонней клейкой ленты. Подключите UBEC к регулятору оборотов (ESC) через разъем XT30. Подключите первый провод UBEC в Raspberry Pi 5 в пины 4 (5V power) и 6 (Ground) (см. pinout выше).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_19.webp" width=700 class="zoom border center"></div>

20. Подключите приемник в порт SBUS/CRSF (UART6) полетного контроллера — вставьте черный провод в левый крайний пин.

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_20.webp" width=700 class="zoom border center"></div>

21. Установите кожух полетного контроллера на алюминиевые стойки. Закрепите приемник пластиковым хомутом в предусмотренных отверстиях. Уложите провода в вырез для проводов. Подключите экран к Raspberry Pi 5: красный провод подключите к пину 1 (3V3), черный — к пину 9 (Ground) (см. pinout выше).

    <div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_21.webp" width=700 class="zoom border center"></div>

## Установка защиты, ножек и светодиодной ленты

1. Проденьте ремешок аккумуляторной батареи через предусмотренные отверстия карбоновой монтажной деки. Установите деку на алюминиевые стойки и закрепите ее винтами M3x8 (<a href="#cell8">Ячейка 8</a>). Используйте H2.0/HEX2.0.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_1.webp" width=700 class="zoom border center"></div>

2. Расположите перемычки защиты в форме квадрата. Установите на углы нижние дуги защиты. Закрепите элементы винтами M3x10 (<a href="#cell13">Ячейка 13</a>) сверху и нейлоновыми стойками M3x40 (<a href="#cell23">Ячейка 23</a>) снизу.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_2.webp" width=700 class="zoom border center"></div>

3. Зафиксируйте винтами M3x8 (<a href="#cell8">Ячейка 8</a>) верхние дуги и перемычки защиты. Расположите элементы так, чтобы перемычки были направлены внутрь, а дуги — наружу.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_3.webp" width=700 class="zoom border center"></div>

4. Установите запрессовочные гайки М3 (<a href="#cell1">Ячейка 1</a>) в предусмотренные отверстия по краям лучей.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_4.webp" width=700 class="zoom border center"></div>

5. Установите собранную защиту с нижней стороны конструктора и зафиксируйте ее винтами M3x10 (<a href="#cell13">Ячейка 13</a>).

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_5.webp" width=700 class="zoom border center"></div>

6. С одной стороны маленькой ножки вкрутите винты M3x6 (<a href="#cell9">Ячейка 9</a>) в предусмотренные отверстия. С другой стороны установите алюминиевые стойки 10мм (<a href="#cell14">Ячейка 14</a>). Установите антискользящую проставку поверх алюминиевой стойки. Повторите действия для сборки остальных ножек.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_6.webp" width=700 class="zoom border center"></div>

7. Установите маленькую ножку на луч и зафиксируйте ее винтами M3x6 (<a href="#cell9">Ячейка 9</a>). Повторите действия с остальными ножками.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_7.webp" width=700 class="zoom border center"></div>

8. Наклейте светодиодную (LED) ленту на пластиковое кольцо для LED-ленты. Установите кольцо в предусмотренные крючки на ножках и зафиксируйте провода пластиковым хомутом. Подключите питание LED-ленты ко второму свободному UBEC. Подключите сигнальный провод к пину 21 (GPIO 9).

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_8.webp" width=700 class="zoom border center"></div>

9. Установите пропеллеры в соответствии с направлениями вращения, указанными на изображении.

    <div align="center"><img src="../assets/assembling_clever5/ru/other_step_9.webp" width=700 class="zoom border center"></div>

> **Caution** Проверьте, что ни один из компонентов не остался незакрепленным. Перед первым включением убедитесь, что пропеллеры не задевают кожух и провода.
