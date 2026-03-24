# Сборка Клевера 5 FPV

## Содержание
1. [Схема подключения электроники](#схема-подключения-электроники)
2. [Сборка рамы](#сборка-рамы)
3. [Установка моторов](#установка-моторов)
4. [Установка ESC](#установка-esc)
5. [Установка полетного контроллера](#установка-полетного-контроллера)
6. [Установка видеопередатчика](#установка-видеопередатчика)
7. [Сборка квадрокоптера](#сборка-квадрокоптера)

## Размер крепежа

> **Success** При сборке применяются крепёжные элементы разных типоразмеров. Установка винтов или стоек несоответствующего размера может привести к повреждению квадрокоптера.

<div align="center"> <table class="type_table">
  <tr>
    <td id="cell1"><div align="center"><strong>Ячейка 1</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/nut_press.png" width="20"/><br>Гайка запрессовочная М3</div></td>
    <td id="cell2"><div align="center"><strong>Ячейка 2</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/nut_nylon.png" width="20"/><br>Гайка нейлоновая М3</div></td>
    <td id="cell3"><div align="center"><strong>Ячейка 3</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/hts-m2,5.png" width="35"/><br>Стойка нейлоновая M2.5</div></td>
    <td id="cell4"><div align="center"><strong>Ячейка 4</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/nut_nylon.png" width="16"/><br>Гайка нейлоновая М2.5</div></td>
    <td id="cell5"><div align="center"><strong>Ячейка 5</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/nut_nylon.png" width="12"/><br>Гайка нейлоновая М2</div></td>
  </tr>
  <tr>
    <td id="cell6"><div align="center"><strong>Ячейка 6</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m3x40.png" width="150" height="30"/><br>Винт M3x40</div></td>
    <td id="cell7"><div align="center"><strong>Ячейка 7</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m3x12.png" width="95" height="30"/><br>Винт M3x12</div></td>
    <td id="cell8"><div align="center"><strong>Ячейка 8</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m3x8.png" width="70" height="30"/><br>Винт M3x8</div></td>
    <td id="cell9"><div align="center"><strong>Ячейка 9</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m3x6.png" width="45" height="30"/><br>Винт M3x6</div></td>
    <td id="cell10"><div align="center"><strong>Ячейка 10</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m3x4.png" width="35" height="30"/><br>Винт M3x4</div></td>
  </tr>
  <tr>
    <td id="cell11"><div align="center"><strong>Ячейка 11</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/aluminium_40.png" width="130" height="15"/><br>Стойка алюминиевая M3x40</div></td>
    <td id="cell12"><div align="center"><strong>Ячейка 12</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/dumper.png" width="50"/><br>Стойка демпферная М3</div></td>
    <td id="cell13"><div align="center"><strong>Ячейка 13</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m3x10.png" width="80" height='30'/><br>Винт M3x10</div></td>
    <td id="cell14"><div align="center"><strong>Ячейка 14</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/aluminium_10.png" width="40" height="15"/><br>Стойка алюминиевая M3x10</div></td>
    <td id="cell15"><div align="center"><strong>Ячейка 15</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/aluminium_40.png" width="100" height="15"/><br>Стойка алюминиевая M3x30</div></td>
  </tr>
  <tr>
    <td id="cell16"><div align="center"><strong>Ячейка 16</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m2,5x6.png" width="50" height="20"/><br>Винт M2x6</div></td>
    <td id="cell17"><div align="center"><strong>Ячейка 17</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m2,5x4.png" width="50" height="25"/><br>Винт M2.5x4</div></td>
    <td id="cell18"><div align="center"><strong>Ячейка 18</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m2,5x6.png" width="60" height="25"/><br>Винт M2.5x6</div></td>
    <td id="cell19"><div align="center"><strong>Ячейка 19</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m1,4x3.png" width="35"/><br>Саморез M1.4x4</div></td>
    <td id="cell20"><div align="center"><strong>Ячейка 20</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m2,5x4.png" width="35" height="20"/><br>Винт M2x3</div></td>
  </tr>
  <tr>
    <td id="cell21"><div align="center"><strong>Ячейка 21</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/htp-30.png" width="100" height="15"/><br>Стойка нейлоновая M3x30</div></td>
    <td id="cell22"><div align="center"><strong>Ячейка 22</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/htp-20.png" width="70" height="15"/><br>Стойка нейлоновая M3x20</div></td>
    <td id="cell23"><div align="center"><strong>Ячейка 23</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/htp-40.png" width="130" height="15"/><br>Стойка нейлоновая M3x40</div></td>
    <td id="cell24"><div align="center"><strong>Ячейка 24</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/m1,4x10.png" width="60"/><br>Саморез M1.4x10</div></td>
    <td id="cell25"><div align="center"><strong>Ячейка 25</strong><br><img src="../assets/assembling_clever5_fpv/fasteners/tpu-spacer.png" width="60"/><br>Ножка из TPU</div></td>
  </tr>
</table></div>

## Схема подключения электроники

<div align="center"><img src="../assets/assembling_clever5_fpv/ru/layout.png" width=700 class="zoom border center"></div>

## Сборка рамы

1. Совместите 4 луча между средней и нижней декой, между ними установите проставку.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/frame/frame_step_1.png" width=700 class="zoom border center"></div>

2. Установите винты M3x12 (<a href="#cell7">Ячейка 7</a>) и M3x40 (<a href="#cell6">Ячейка 6</a>) со стороны нижней деки, M3x12 (<a href="#cell7">Ячейка 7</a>) в крайние отверстия лучей, M3x40 (<a href="#cell6">Ячейка 6</a>) в центральные отверстия нижней деки.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/frame/frame_step_2.png" width=700 class="zoom border center"></div>

3. На средней деке установите запрессовочные гайки М3 (<a href="#cell1">Ячейка 1</a>) и зафиксируйте их винтами.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/frame/frame_step_3.png" width=700 class="zoom border center"></div>

## Установка моторов

1. Установите накладки на лучи, так, как показано на изображении.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/arm_guard_step_4.png" width=700 class="zoom border center"></div>

2. Установите моторы в соответствующие отверстия в луче с помощью **винтов М3х10** (<a href="#cell13">Ячейка 13</a>).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/motor_step_5.png" width=700 class="zoom border center"></div>

> **Caution** Убедитесь, что моторы закреплены с помощью винтов М3х10, в противном случае может возникнуть короткое замыкание между обмотками.

## Установка ESC
1. Установите регулятор оборотов (ESC) поверх винтов M3x40 (<a href="#cell6">Ячейка 6</a>) на средней деке. Контакты питания аккумулятора должны быть направлены назад.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/esc_step_6.png" width=700 class="zoom border center"></div>

2. Приклейте защитные кожухи и проденьте в них провода моторов. Припаяйте силовые провода и конденсатор на контакты питания ESC, также припаяйте моторы на контакты моторов (см. изобр. ниже).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/esc_step_7.png" width=700 class="zoom border center"></div>

3. Наденьте на силовые провода защитный кожух, после чего припаяйте разъём питания XT60. Защелкните защитный кожух на разъёме питания.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/xt60_step_8.png" width=700 class="zoom border center"></div>

## Установка полетного контроллера

1. Установите полётный контроллер стрелкой вперед, после чего установите нейлоновые гайки M3 (<a href="#cell2">Ячейка 2</a>) для фиксации полетного контроллера.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/fcu_step_9.png" width=700 class="zoom border center"></div>

2. Установите 6-пиновый шлейф между полетным контроллером и регулятором оборотов (ESC).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/fcu_to_esc_step_10.png" width=700 class="zoom border center"></div>

## Установка видеопередатчика

1. Установите винты M3x10 (<a href="#cell13">Ячейка 13</a>) c нижней стороны деки, с верхней стороны установите видеопередатчик (VTX) и зафиксируйте нейлоновыми гайками M3 (<a href="#cell2">Ячейка 2</a>).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/vtx_step_11.png" width=700 class="zoom border center"></div>

2. Вид с установленным видеопередатчиком (VTX).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/vtx_step_12.png" width=700 class="zoom border center"></div>

## Сборка квадрокоптера

1. Установите алюминиевые стойки M3х30 (<a href="#cell15">Ячейка 15</a>) сверху, снизу зафиксируйте винтами M3x6 (<a href="#cell9">Ячейка 9</a>).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/aluminium_30_step_13.png" width=700 class="zoom border center"></div>

2. Вид с установленными алюминиевыми стойками.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/aluminium_30_step_14.png" width=700 class="zoom border center"></div>

3. Установите маунт камеры на передние стойки, так, как показано на изображении снизу.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/camera_mount_step_15.png" width=700 class="zoom border center"></div>

4. Установите видеокамеру в маунт на винты М2х3 (<a href="#cell20">Ячейка 20</a>) и зафиксируйте в удобном для вас наклоне камеры.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/camera_step_16.png" width=700 class="zoom border center"></div>

5. Подключите шлейф камеры в разъём для курсовой камеры в полетном контроллере, так, как показано на изображении.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/camera_step_17.png" width=700 class="zoom border center"></div>

6. Установите в маунт для антенны разъём и затяните ключом для пропеллеров (ключ на 8), после чего подключите разъём антенны в видеопередатчик и установите на задние стойки.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/backward_mount_step_18.png" width=700 class="zoom border center"></div>

7. Установите радиоприемник ELRS и подключите при помощи шлейфа в порт SBUS/CRSF на полётном контроллере.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/elrs_rx_step_19.png" width=700 class="zoom border center"></div>

8. Установите защитные накладки сзади, для этого заведите крючок за стойку около полётного контроллера и защёлкните клипсу на задней стойке.
    
    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/backward_guard_step_20.png" width=700 class="zoom border center"></div>

9. Установите LED модули, для этого приклейте их на двухсторонний скотч на внутренние стороны лучей (см. изобр. ниже).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/led_step_21.jpg" width=700 class="zoom border center"></div>

10. Подключите LED модули в хаб, как показано на изображении. Подключите хаб в разъём LED/Buzzer на полётном контроллере.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/led_hub_step_22.png" width=700 class="zoom border center"></div>

11. Уложите провода от LED модулей, как показано на изображении.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/led_hub_step_23.png" width=700 class="zoom border center"></div>

12. Протяните стропу для аккумулятора в посадочные пазы, установите верхнюю деку используя винты М3х6 (<a href="#cell9">Ячейка 9</a>).

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/top_plate_step_24.png" width=700 class="zoom border center"></div>

13. Установите боковую защиту на центральные стойки, защёлкните на клипсы защиты.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/side_guard_step_25.png" width=700 class="zoom border center"></div>

14. Накрутите антенну видеосвязи на разъём сзади.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/vtx_antenna_step_26.png" width=700 class="zoom border center"></div>

15. Установите пропеллеры в соответствии с обратным вращением, как представлено на изображении.

    <div align="center"><img src="../assets/assembling_clever5_fpv/ru/props_step_27.png" width=700 class="zoom border center"></div>

> **Caution** Проверьте, что ни один из компонентов не остался незакрепленным. Перед первым включением убедитесь, что пропеллеры не задевают кожух и провода.
