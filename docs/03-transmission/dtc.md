# Коды неисправностей (DTC) трансмиссии

> **Страницы в оригинале:** 616 – 677 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p617_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p617_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p617_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p617_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p618_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p618_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p618_2.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p618_2.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p619_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p619_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p619_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p619_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Electronic shift

### System

System overview
Gearshift control assembly (hereinafter referred to as ESL): It is a handle type electronic gearshift. It adopts
position Hall sensor element. When the gearshift lever moves to different positions, it realizes the ON/OFF
signals of different position Hall sensor elements. Then the single-chip microcomputer judges the current
position of gearshift lever according to the activated sensor element, and finally converts it into CAN signal,
which is input into TCU. TCU makes logical judgment according to the current state of the vehicle to realize
gearshift. Electronic gearshift actuator controller assembly (hereinafter referred to as ACM) and electronic
gearshift actuator assembly (hereinafter referred to as ARC): ACM is located at the original clutch pedal
bracket in the cab, responsible for vehicle communication and ARC control; ARC is located on the
transmission case (directly below the engine thermostat). Its torque output hole fits with the gearbox
gearshift shaft in a clearance manner. The motor drives to achieve torque output and complete gear
switching. Position sensor is set in ARC to feed back gear information.
Electronic shift
Inspection of part
Inspection of part structure principle
Electronic shift control assembly ESL
Serial number

### Name


### Quantity

Gearshift base assembly
Handle ball assembly
Electronic shift actuator controller assembly ACM
Serial number

### Name


### Part

Fixing hole
Electronic gear shift actuator controller
assembly(ACM)
Complete vehicle harness interface
Electronic gear shift actuator controller
assembly(ACM)
ARC harness interface
Electronic gear shift actuator controller
assembly(ACM)
Interface definition
•
Complete vehicle harness interface
Electronic shift
Inspection of part
Pin number

### Pin

definition(Description
)
Signal type
Signal range
Test conditions

### Remarks


### KL30

-

### 12V

-
-

### KL30

-

### 12V

-
-

### GND

-

### 0V

-
-

### GND

-

### 0V

-
-

### NC

-
-
-
-

### NC

-
-
-
-

### KL15

-

### 12V

-
-

### NC

-
-
-
-

### CAN_L


### Bus

-
-
-

### CAN_H


### Bus

-
-
-

### NC

-
-
-
-

### NC

-
-
-
-
•
ARC harness interface
Pin number

### Pin

definition(Description
)
Signal type
Signal range
Test conditions

### Remarks

Motor+

### PWM


### 12V

-
-

### NC

-
-
-
-

### NC

-
-
-
-
Motor-

### PWM


### 12V

-

### NC

-
-
-
-
5V_Sensor
-

### 5V

-
-
Electronic shift
Inspection of part

### GND

-

### 0V

-
-
Position_Sensor1

### PWM


### 5V

-
-

### NC

-
-
-
-

### NC

-
-
-
-

### NC

-
-
-
-

### NC

-
-
-
-
Electronic gearshift actuator assembly ARC
Serial number

### Name


### Part

Fixing hole
Electronic gearshift actuator
assembly(ARC)
ACM harness interface
Electronic gearshift actuator
assembly(ARC)
Gear shift shaft mating hole
Electronic gearshift actuator
assembly(ARC)
Interface definition
•
ACM harness interface
Pin number

### Pin

definition(Description
)
Signal type
Signal range
Test conditions

### Remarks


### F


### NC

-
-
-
-

### E

Motor-
Power PWM

### 12V

-
-

### D

Motor+
Power PWM

### 12V

-
-

### C


### GND

-

### 0V

-
-

### B

Position_Sensor

### PWM


### 5V

-
-

### A

5V_Sensor
-

### 5V

-
-
Electronic shift

### Common

Common methods
Calibration procedure of electronic gear shift actuator controller (ACM) self-learning
diagnostic scanner

### Warning

Please put the vehicle into P gear during self-learning, keep the vehicle level during the
whole process, and do not start the engine.
1.

1. Connect diagnostic scanner in power-off state.
2.
2.Power on the complete vehicle (Ignition on).
3.
3.Turn on the diagnostic scanner, enter the current model catalog, and select: Shift gear execution control module ACM→ diagnostic
data version? Special function →ACM self-learning.
4.

4. The diagnostic scanner interface displays "Do you enter into ACM self-learning?" , click "Yes."
5.

5. Wait for "P gear calibration succeeds" in the diagnostic scanner interface, and click "OK."
6.

6. Wait until "ACM self-learning ends" appears on the diagnostic scanner interface, and click "Exit."
7.
Self-learning completed.
Manual unlocking P gear
If the transmission cannot shift out of P gear due to ACM fault and trailer or other operation is required by
unlocking front wheels, you can manually unlock P gear as follows:
Pull up the handbrake, keep the vehicle level, and power off the complete vehicle;
Use an 8 mm open-end wrench to clamp the transmission shift shaft between the ARC shift shaft fitting hole 3 and the
transmission case, and rotate it clockwise (top view) by about 18° (from gray position to blue position in the following figure) to
realize manual unlocking.

### Warn

ing
If the hand brake fails, use a wedge block to fix the tire when unlocking
gear P to prevent the vehicle from slipping.
ARC internal resistance is large, and manual unlocking process requires
a little force.
When there is no ARC/ACM fault, the complete vehicle will be powered
on or powered off to automatically shift the transmission into P gear.
Electronic shift
DTC Diagnostic608
DTC Diagnostic
Electronic shift control assembly ESL
P 119216: Low KL30 voltage
Fault triggering conditions
•
The shifter is not in sleep mode.
•
KL30 supply voltage < 6.0 V is detected.
Possible fault causes
•
Battery voltage is below the limit.
•
The power supply harness is disconnected or in poor contact.
Failure mode
•
Respond according to 4.2.1 Product Function Definition.
Diagnostic process
•
Check whether the battery voltage is lower than the limit value.
•
Check whether the voltage at the ESL harness terminal is lower than the limit value.
P 119217: High KL30 voltage
Fault triggering conditions
•
The shifter is not in sleep mode.
•
KL30 supply voltage > 18 V is detected.
Possible fault causes
•
Battery voltage is higher than the limit.
•
The power supply harness is disconnected or in poor contact.
Failure mode
•
Respond according to 4.2.1 Product Function Definition.
Diagnostic process
•
Check whether the battery voltage is higher than the limit value.
•
Check whether the voltage at the ESL harness terminal is higher than the limit value.
U007388: Bus off
Fault triggering conditions
•
ESL is not in sleep mode.
•
KL15 1s after power-on.
•
Power supply voltage: 6.5 V-18 V.
•
Bus-Off counter reaches NBusOffCount=5.

### ESL

harness
terminal

### Harness

connector
Electronic shift
DTC Diagnostic609
Possible fault causes
•
Can network fault.
Failure mode
•
Shift request cannot be issued.
•
ESL gear indicator lamp goes out.
Diagnostic process
•
Check CAN interface connector.
•
Check CAN network terminal resistance.
•
After the above inspection, CAN communication fault still exists, and replace ESL. After replacement, clear the fault code, read it
again, and check whether the fault code reappears.
U010187: Lost communication with TCUs
Fault triggering conditions
•
ESL is not in sleep mode.
•
KL15 1s after power-on.
•
Power supply voltage: 6.5 V-18 V.
•
CAN Bus-Off not detected.
•
Id=0x 338 > 1s detected.
Possible fault causes
•
The ESL harness end is disconnected or in poor contact.
•
TCU fault.
Failure mode
•
When the duration is ≤1s, the ESL gear indicator lamp remains in the front gear state when the TCU message is lost.
•
When the duration is > 1s, the ESL gear indicator lamp goes out.
Diagnostic process
•
Inspect whether the ESL harness end is disconnected or in poor contact.
•
Check whether the TCU_ 338 message on the CAN line is sent normally.
U2F3A86: Unreliable data received from TCUs
Fault triggering conditions
•
ESL is not in sleep mode.
•
KL15 1s after power-on.
•
Power supply voltage: 6.5 V-18 V.
•
CAN Bus-Off not detected.
•
TCU_GearForDisplay= 0xE=Unreliable or TCU_GearForDisplay=0xF =Invalid detected.
Possible fault causes
•
Can line is disturbed.
•
TCU fault.
Failure mode
•
When the duration is ≤1s, the ESL gear indicator lamp remains in the gear state when the TCU message is reliable.
•
When the duration is > 1s,