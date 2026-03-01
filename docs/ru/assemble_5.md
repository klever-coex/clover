# Сборка Клевера 5

## Содержание
1. [Схема подключения электроники](#схема-подключения-электроники)
2. [Сборка рамы](#сборка-рамы)
3. [Установка ESC](#установка-esc)
4. [Установка алюминиевых стоек](#установка-алюминиевых-стоек)
5. [Установка полетного контроллера](#установка-полетного-контроллера)
6. [Установка Raspberry Pi](#установка-raspberry-pi)
7. [Установка защиты, ножек и LED ленты](#установка-защиты-ножек-и-led-ленты)

## Размер крепежа

> **Важно!** При сборке применяются крепёжные элементы разных типоразмеров. Установка винтов или стоек несоответствующего размера может привести к повреждению квадрокоптера.

<div align="center"> <table class="type_table">
  <tr>
    <td id="cell1"><div align="center"><strong>Ячейка 1</strong><br><img src="../assets/assembling_clever5/fasteners/nut_press.png" width="20"/><br>Гайка запрессовочная М3</div></td>
    <td id="cell2"><div align="center"><strong>Ячейка 2</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.png" width="20"/><br>Гайка нейлоновая М3</div></td>
    <td id="cell3"><div align="center"><strong>Ячейка 3</strong><br><img src="../assets/assembling_clever5/fasteners/hts-m2,5.png" width="35"/><br>Стойка нейлоновая M2.5</div></td>
    <td id="cell4"><div align="center"><strong>Ячейка 4</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.png" width="16"/><br>Гайка нейлоновая М2.5</div></td>
    <td id="cell5"><div align="center"><strong>Ячейка 5</strong><br><img src="../assets/assembling_clever5/fasteners/nut_nylon.png" width="12"/><br>Гайка нейлоновая М2</div></td>
  </tr>
  <tr>
    <td id="cell6"><div align="center"><strong>Ячейка 6</strong><br><img src="../assets/assembling_clever5/fasteners/m3x40.png" width="150" height="30"/><br>Винт M3x40</div></td>
    <td id="cell7"><div align="center"><strong>Ячейка 7</strong><br><img src="../assets/assembling_clever5/fasteners/m3x12.png" width="95" height="30"/><br>Винт M3x12</div></td>
    <td id="cell8"><div align="center"><strong>Ячейка 8</strong><br><img src="../assets/assembling_clever5/fasteners/m3x8.png" width="70" height="30"/><br>Винт M3x8</div></td>
    <td id="cell9"><div align="center"><strong>Ячейка 9</strong><br><img src="../assets/assembling_clever5/fasteners/m3x6.png" width="45" height="30"/><br>Винт M3x6</div></td>
    <td id="cell10"><div align="center"><strong>Ячейка 10</strong><br><img src="../assets/assembling_clever5/fasteners/m3x4.png" width="35" height="30"/><br>Винт M3x4</div></td>
  </tr>
  <tr>
    <td id="cell11"><div align="center"><strong>Ячейка 11</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_40.png" width="130" height="15"/><br>Стойка алюминиевая M3x40</div></td>
    <td id="cell12"><div align="center"><strong>Ячейка 12</strong><br><img src="../assets/assembling_clever5/fasteners/dumper.png" width="50"/><br>Стойка демпферная М3</div></td>
    <td id="cell13"><div align="center"><strong>Ячейка 13</strong><br><img src="../assets/assembling_clever5/fasteners/m3x10.png" width="80" height='30'/><br>Винт M3x10</div></td>
    <td id="cell14"><div align="center"><strong>Ячейка 14</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_10.png" width="40" height="15"/><br>Стойка алюминиевая M3x10</div></td>
    <td id="cell15"><div align="center"><strong>Ячейка 15</strong><br><img src="../assets/assembling_clever5/fasteners/aluminium_40.png" width="100" height="15"/><br>Стойка алюминиевая M3x30</div></td>
  </tr>
  <tr>
    <td id="cell16"><div align="center"><strong>Ячейка 16</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x6.png" width="50" height="20"/><br>Винт M2x6</div></td>
    <td id="cell17"><div align="center"><strong>Ячейка 17</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x4.png" width="50" height="25"/><br>Винт M2.5x4</div></td>
    <td id="cell18"><div align="center"><strong>Ячейка 18</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x6.png" width="60" height="25"/><br>Винт M2.5x6</div></td>
    <td id="cell19"><div align="center"><strong>Ячейка 19</strong><br><img src="../assets/assembling_clever5/fasteners/m1,4x3.png" width="35"/><br>Саморез M1.4x4</div></td>
    <td id="cell20"><div align="center"><strong>Ячейка 20</strong><br><img src="../assets/assembling_clever5/fasteners/m2,5x4.png" width="35" height="20"/><br>Винт M2x3</div></td>
  </tr>
  <tr>
    <td id="cell21"><div align="center"><strong>Ячейка 21</strong><br><img src="../assets/assembling_clever5/fasteners/htp-30.png" width="100" height="15"/><br>Стойка нейлоновая M3x30</div></td>
    <td id="cell22"><div align="center"><strong>Ячейка 22</strong><br><img src="../assets/assembling_clever5/fasteners/htp-20.png" width="70" height="15"/><br>Стойка нейлоновая M3x20</div></td>
    <td id="cell23"><div align="center"><strong>Ячейка 23</strong><br><img src="../assets/assembling_clever5/fasteners/htp-40.png" width="130" height="15"/><br>Стойка нейлоновая M3x40</div></td>
    <td id="cell24"><div align="center"><strong>Ячейка 24</strong><br><img src="../assets/assembling_clever5/fasteners/m1,4x10.png" width="60"/><br>Саморез M1.4x10</div></td>
    <td id="cell25"><div align="center"><strong>Ячейка 25</strong><br><img src="../assets/assembling_clever5/fasteners/tpu-spacer.png" width="60"/><br>Ножка из TPU</div></td>
  </tr>
</table></div>

## Схема подключения электроники

<div align="center"><img src="../assets/assembling_clever5/ru/layout.png" width=700 class="zoom border center"></div>

## Сборка рамы

1. Совместите 4 луча между средней и нижней декой.

<div align="center"><img src="../assets/assembling_clever5/ru/frame/frame_step_1.png" width=700 class="zoom border center"></div>

2. Установите винты M3x12 (<a href="#cell7">Ячейка 7</a>) и M3x40 (<a href="#cell6">Ячейка 6</a>) со стороны нижней деки, M3x12 (<a href="#cell7">Ячейка 7</a>) в крайние отверстия лучей, M3x40 (<a href="#cell6">Ячейка 6</a>) в центральные отверстия нижней деки.

<div align="center"><img src="../assets/assembling_clever5/ru/frame/frame_step_2.png" width=700 class="zoom border center"></div>

3. На средней деке установите запрессовочные гайки М3 (<a href="#cell1">Ячейка 1</a>) и зафиксируйте их винтами.

<div align="center"><img src="../assets/assembling_clever5/ru/frame/frame_step_3.png" width=700 class="zoom border center"></div>

## Установка моторов

1. Установите моторы в соответствующие отверстия в луче с помощью **винтов М3х8** (<a href="#cell8">Ячейка 8</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/motor.png" width=700 class="zoom border center"></div>

> **Важно!** Убедитесь, что моторы закреплены с помощью винтов М3х8, в противном случае может возникнуть короткое замыкание между обмотками.

## Установка ESC

1. Установите регулятор оборотов (ESC) поверх винтов M3x40 (<a href="#cell6">Ячейка 6</a>) на средней деке. Разъем питания аккумулятора должен быть направлен назад.

<div align="center"><img src="../assets/assembling_clever5/ru/esc_step_1.png" width=700 class="zoom border center"></div>

2. Подсоедините к моторам разъемы MR30 от регулятора оборотов (ESC), уложите провода так, как показано на рисунке, после чего закрепите их на лучах с помощью пластиковых хомутов.

<div align="center"><img src="../assets/assembling_clever5/ru/esc_step_2.png" width=700 class="zoom border center"></div>

## Установка алюминиевых стоек

1. Установите алюминиевые стойки M3x40 (<a href="#cell11">Ячейка 11</a>) на среднюю деку с помощью демпферных стоек М3 (<a href="#cell12">Ячейка 12</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/aluminium_40_step_1.png" width=700 class="zoom border center"></div>

2. Закрутите демпферные стойки со стороны нижней деки.

<div align="center"><img src="../assets/assembling_clever5/ru/aluminium_40_step_2.png" width=700 class="zoom border center"></div>

## Установка полетного контроллера

1. Перед установкой полетного контроллера, накрутите нейлоновые гайки M3 (<a href="#cell2">Ячейка 2</a>) на винты M3x40 (<a href="#cell6">Ячейка 6</a>), после чего установите полетный контроллер стрелкой вперед.
Установите нейлоновые гайки для фиксации полетного контроллера.

<div align="center"><img src="../assets/assembling_clever5/ru/flight_controller_step_1.png" width=700 class="zoom border center"></div>

2. Установите 6-пиновый шлейф между полетным контроллером и регулятором оборотов (ESC).

<div align="center"><img src="../assets/assembling_clever5/ru/flight_controller_step_2.png" width=700 class="zoom border center"></div>

3. Вид с установленным шлейфом.

<div align="center"><img src="../assets/assembling_clever5/ru/flight_controller_step_3.png" width=700 class="zoom border center"></div>

## Установка Raspberry Pi

1. Установите на монтажную деку из поликарбоната стойки M2.5 (<a href="#cell3">Ячейка 3</a>) с помощью винтов M2.5x4 (<a href="#cell17">Ячейка 17</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_1.png" width=700 class="zoom border center"></div>

2. Закрутите винты. Используйте биту H1.5/HEX1.5.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_2.png" width=700 class="zoom border center"></div>

3. Установите Raspberry pi 5 поверх стоек M2.5.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_3.png" width=700 class="zoom border center"></div>

4. Зафиксируйте плату Raspberry Pi 5 с помощью винтов М2.5х4 (<a href="#cell17">Ячейка 17</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_4.png" width=700 class="zoom border center"></div>

5. Снимите пленки с термопрокладок и установите их на выделенные позиции на изображении. Установите радиатор охлаждения на Raspberry pi, для этого вставьте фиксирующие клипсы через радиатор в Raspberry pi. Подключите систему охлаждения в порт отмеченный на изображении.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_5.png" width=700 class="zoom border center"></div>

6. Raspberry Pi с радиатором в сборе.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_6.png" width=700 class="zoom border center"></div>

7. Установите нейлоновые стойки 30мм (<a href="#cell21">Ячейка 21</a>) на деку с Raspberry pi с помощью винтов M3x8 (<a href="#cell8">Ячейка 8</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_7.png" width=700 class="zoom border center"></div>

8. Вид с установленными нейлоновыми стойками.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_8.png" width=700 class="zoom border center"></div>

9. Установите собранную деку c Raspberry pi на нижнюю часть квадрокоптера в демпферные стойки, зафиксируйте на винты M3x4 (<a href="#cell10">Ячейка 10</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_9.png" width=700 class="zoom border center"></div>

10. Подключите к Raspberry шлейф передачи данных. Подключение производится во внешнюю линию гребенки, начиная с 4 порта относительно порта SD карты(черный провод в 14 порту, см. pinout). Подключение ответной части производится в порт UART 4 на полетном контроллере(черный провод распологается в крайнем правом углу).
    
<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_10.png" width=700 class="zoom border center"></div>
<div align="center"><img src="../assets/assembling_clever5/ru/RPI_pinout.png" width=400 class="zoom border center"></div>

11. На малую монтажную деку установите камеру так, как показано на изображении ниже, после чего зафиксируйте ее с помощью 2х саморезов М1.4х4 (<a href="#cell19">Ячейка 19</a>), в верхнем левом и нижнем правом углах. Бита для сборки PH1.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_11.png" width=700 class="zoom border center"></div>

12. На малую монтажную деку установите нейлоновые стойки 20мм (<a href="#cell22">Ячейка 22</a>) и зафиксируйте винтами M3x6 (<a href="#cell9">Ячейка 9</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_12.png" width=700 class="zoom border center"></div>

13. Установите малую монтажную деку с камерой на деку захвата с помощью винтов M3x6 (<a href="#cell9">Ячейка 9</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_13.png" width=700 class="zoom border center"></div>

14. Установите лазерный дальномер на деку захвата с помощью винтов M2x6 (<a href="#cell16">Ячейка 16</a>) и нейлоновых гаек M2 (<a href="#cell5">Ячейка 5</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_14.png" width=700 class="zoom border center"></div>

15. Подключите шлейф лазерного дальномера.

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_15.png" width=700 class="zoom border center"></div>

16. Установите деку захвата на квадрокоптер с помощью винтов M3x8 (<a href="#cell8">Ячейка 8</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_16.png" width=700 class="zoom border center"></div>

17. Подключите шлейф дальномера в порт UART 1 на полетном контроллере(черный провод в левом крайнем пину).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_17.png" width=700 class="zoom border center"></div>

18. Установите экран на кожух дрона при помощи винтов M2.5x6 (<a href="#cell18">Ячейка 18</a>) и нейлоновых гаек M2.5 (<a href="#cell4">Ячейка 4</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_18.png" width=700 class="zoom border center"></div>

19. Установите UBEC на деку с Raspberry pi применив двухсторонний скотч. Подключите UBEC к регулятору оборотов (ESC) через разъем XT30. Подключите первый провод UBEC в Raspberry pi как указано на картинке(4 и 6 пины, см. pinout выше).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_19.png" width=700 class="zoom border center"></div>

20. Подключите приемник в порт SBUS/CRSF (UART 6) на полетном контроллере(черный провод в левом крайнем пину).

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_20.png" width=700 class="zoom border center"></div>

21. Установите кожух поверх алюминиевых стоек и закрепите приемник на пластиковый хомут, в выделенные отверстия на изображении. Уложите провода в вырез для проводов. Подключите экран к Raspberry pi, красный провод подключается в левый крайний пин внутренней части гребенки, относительно SD карты(красный - 1 пин, чёрный - 9 пин). 

<div align="center"><img src="../assets/assembling_clever5/ru/RPI_step_21.png" width=700 class="zoom border center"></div>

## Установка защиты, ножек и LED ленты

1. Проденьте ремешок в верхнюю деку, после чего закрепите ее на винты M3x8 (<a href="#cell8">Ячейка 8</a>) в алюминиевые стойки, закрепите разъем питания с помощью винтов M2.5x6 (<a href="#cell18">Ячейка 18</a>). Бита для сборки деки - H2.0/HEX2.0, для разъема - H1.5/HEX1.5.

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_1.png" width=700 class="zoom border center"></div>

2. Расположите снизу в виде квадрата перемычки защиты, после чего на углы выложите нижние дуги защиты, зафиксируйте на винты M3x10 (<a href="#cell13">Ячейка 13</a>) сверху, снизу нейлоновые стойки 40мм (<a href="#cell23">Ячейка 23</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_2.png" width=700 class="zoom border center"></div>

3. Зафиксируйте винтами M3x8 (<a href="#cell8">Ячейка 8</a>) верхние дуги и перемычки в обратном порядке, должно получится так, что перемычки направлены внутрь, а дуги наружу.

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_3.png" width=700 class="zoom border center"></div>

4. Установите и зафиксируйте запрессовочные гайки М3 (<a href="#cell1">Ячейка 1</a>) в отверстия по краям лучей.

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_4.png" width=700 class="zoom border center"></div>

5. Установите с нижней стороны защиту и зафиксируйте её на винты M3x10 (<a href="#cell13">Ячейка 13</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_5.png" width=700 class="zoom border center"></div>

6. С одной стороны маленькой ножки вкрутите винты M3x6 (<a href="#cell9">Ячейка 9</a>) во все отверстия, с другой стороны зафиксируйте их на алюминиевыми стойками 10мм (<a href="#cell14">Ячейка 14</a>). В нижнем отверстии поверх стойки наденьте ножку из TPU (<a href="#cell25">Ячейка 25</a>).

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_6.png" width=700 class="zoom border center"></div>

7. Разместите маленькую ножку на луче, как показано на изображении и зафиксируйте винтами M3x6 (<a href="#cell9">Ячейка 9</a>). Выполните тоже самое для остальных ножек.

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_7.png" width=700 class="zoom border center"></div>

8. Наклейте LED ленту на окружность (Пластиковое кольцо для крепежа LED ленты) после чего установите в крючки на ножках и зафиксируйте провода пластиковым хомутом. Подключите питание во второй свободный UBEC, а сигнальный провод подключите в 9 GPIO (21 пин).

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_8.png" width=700 class="zoom border center"></div>

9. Установите пропеллеры в соответствии с классическим вращением, как представлено на изображении.

<div align="center"><img src="../assets/assembling_clever5/ru/other_step_9.png" width=700 class="zoom border center"></div>


> **Готово** Проверьте, что ни один из компонентов не остался незакрепленным. Перед первым включением убедитесь, что пропеллеры не задевают кожух и провода.