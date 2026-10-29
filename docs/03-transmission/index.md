# Обзор 7-ступенчатой роботизированной КПП (7DCT)

> **Страницы в оригинале:** 476 – 485 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p477_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p477_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p478_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p478_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p480_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p480_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p480_2.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p480_2.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p483_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p483_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p483_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p483_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры


### Automatic Sion

Automatic transmission............................................................................................................. 463
Automatic transmission ...................................................................................................... 464
Specifications ........................................................................................................... 464
Composition and position distribution........................................................................ 465
System overview ...................................................................................................... 466
Inspection of part structure principle ......................................................................... 467
Common methods .................................................................................................... 475
DTC diagnosis and test ............................................................................................ 478
Fault symptom diagnosis .......................................................................................... 561
Removal and installation ........................................................................................... 566
Spare parts atlas ...................................................................................................... 577
Electronic shift control assembly
............................................ 578
Torque specification .................................................................................................. 578
Composition and position distribution........................................................................ 579
System overview ...................................................................................................... 580
Inspection of part structure principle ......................................................................... 581
Common methods .................................................................................................... 584
DTC Diagnostic ........................................................................................................ 585
Fault symptom diagnosis .......................................................................................... 602
Removal and installation ........................................................................................... 604
Spare parts atlas ...................................................................................................... 607
Mechanical shift control system .......................................................................................... 608
Torque specification .................................................................................................. 608
Composition and position distribution........................................................................ 609
System functional principle introduction .................................................................... 610
Inspection of part structure principle ......................................................................... 611
Common methods .................................................................................................... 613
Fault symptom diagnosis .......................................................................................... 614
Removal and installation ........................................................................................... 616
Spare parts atlas ...................................................................................................... 619
Drive shaft .......................................................................................................................... 620
Specifications ........................................................................................................... 620
Composition and position distribution........................................................................ 622
System functional principle introduction .................................................................... 624
Inspection of part structure principle ......................................................................... 625
Fault symptom diagnosis .......................................................................................... 627
Removal and installation ........................................................................................... 637
Spare parts atlas ...................................................................................................... 640
Automatic transmission
Specification 464
Automatic transmission
specification
Transmission specification

### TM047FDB

Gear ratio
1st gear
4.214
2nd gear
3.105
3rd gear
1.724
4th gear
1.268
5th gear
1.270
6th gear
1.049
7th gear
0.891
Reverse gear
3.664
Final reduction ratio

### 3.842(1/3/4/R)

3.042(2/5/6/7)
Dead weight
Approx. 80 kg
Automatic transmission fluid rating

### 4.8±0.1L

Automatic transmission fluid specification
Castrol BOT 351C4
Automatic transmission
Composition and position distribution 465
Composition and position distribution
Dual-clutch automatic transmission DF 727 is a dual-clutch automatic transmission with seven-gear
automatic transmission. Dual clutch automatic transmission mainly includes dual clutch, power train, shift
train, hydraulic system and electronic control system. The hydraulic control system is based on the hydraulic
pressure generated by the oil pump. The dual-clutch automatic transmission control unit sends signals to the
solenoid valve. The hydraulic control system controls the dual clutch and valve body module according to
the driving conditions of the vehicle to realize gear shift without power interruption. Dual clutch automatic
transmission includes 1 dual clutch, 4 synchronizers, 1 differential
Serial number

### Name


### Purpose

Dual clutch
Transmit and cut off power to realize no
power interruption during gearshift

### Synchronizer

Shift gear
Differential mechanism
Complete vehicle steering
Automatic transmission
System overview 466
System overview
Actuator worksheet

### Gear

VBS3(Shift pressure
control solenoid
valve)
VBS4(Shift pressure
control solenoid
valve)
SOL1(Gear selector
switch solenoid
valve)
SOL2(Gear selector
switch solenoid
valve)

### REV

1st
2nd
3rd
4th
5th
6th
7th
TCU control function automatic shift
control
In each shift mode, the TCU controls the shift solenoid valve (PWM1, PWM2, PWM3) to open or close
according to the engine speed signal, input shaft speed signal, output shaft speed signal, vehicle speed
signal, accelerator pedal signal and brake pedal position signal, and operates the pressure control solenoid
valves VBS3, VBS4, SOL1 and SOL2 linearly to control the hydraulic pressure in the hydraulic control
system to realize the automatic change of the transmission between various gears.
Driver adaptive mode control
During driving, the automatic transmission is always in adaptive mode. There is no switch available for the
driver to select the drive mode. Once specific conditions appear, TCU will select suitable gear shifting
mode for driving state and automatically shift mode to improve smooth gear shifting.
Self-diagnosis function
TCU communicates with engine control module through monitoring sensor and electronic components. If
transmission-related fault is detected, TCU self-diagnosis function will illuminate fault indicator on
combination instrument to remind driver to repair timely and store in TCU memory in the form of fault code.
Fault protection function
In case of automatic transmission system fault, TCU will output a control signal to realize fault protection
function. This control can only make the vehicle operate within the minimum distance. If the shift solenoid
valve or clutch pressure control solenoid valve fails, the TCU will cancel some gears. When brake fault is
detected, crawling function will be canceled.
Automatic transmission
Inspection 