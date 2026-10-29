# Снятие, установка и обслуживание КПП

> **Страницы в оригинале:** 566 – 615 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p587_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p587_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p590_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p590_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p592_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p592_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p602_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p602_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p480_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p480_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p603_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p603_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры


### Automatic

DTC diagnosis and test
Low-side current too high
fault
0x01
Low-side current too low
fault
0x02
Channel unexpected
shutdown fault
0x48
MOS tube discharge
current fault
0x49
Possible causes
Fault code
Inspection strategy
Setting conditions(Control
strategy)
Faulty position

### P0755

Hardware circuit check
After ignition, the TCU detects
that the high side of the on-off
valve 2 is short to power
supply, the above fault lasts for
0.1 s or longer, and the
software makes fault judgment.
· Harness
· Switch valve 2

### · TCU

After ignition, the TCU detects
high-side open circuit fault of
on-off valve2, the above fault
lasts for 0.1 s or longer, and
the software makes fault
judgment.
After ignition, the TCU detects
the high-end short-circuit fault
of on-off valve2 to ground, the
above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.
After ignition, the TCU detects
open circuit fault of high-side
power supply of on-off valve 2,
the above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.
Diagnostic process
Test conditions
Details/Results/Measures

1. Check fault code
A. Connect the diagnostic
scanner.
B. Test the automatic
transmission system with a
diagnostic scanner.
Is there any fault code other
than P0755 fault code?
- > Yes
Reference: Fault code list

### Automatic

DTC diagnosis and test
- > No
Go to step 2.

2. Check whether the switch solenoid valve 2 fault continues to occur.
A. Connect diagnostic scanner
B. After clearing the fault code, fault P0755 continues to appear.
-> Yes
Contact transmission after-sales technical support
-> No
Step3

3. Check the circuit between switch solenoid valve 2 and TCU.

3. Check TCU
A. Dismantle TCU
B. Install the TCU of this vehicle on a vehicle
in good condition. Is the vehicle in normal
state after installing TCU?
- > Yes
Reference: Troubleshooting according to DTC
- > No
replacing

### TCU


### DTC P 1245, P 1256, P 1247

Fault code
Fault code

### Description


### FTB


### Definition


### P1245

Solenoid valve high end 1
fault
Short circuit fault to
power supply
0x04
Solenoid valve high
side 1, 2, 3 fault
through automatic
transmission wire
. High end of solenoid
valve 1 is the high end
of solenoid valve of shift
solenoid valve 1/clutch
1/switch valve 1, and
T10, T8 and T9 of TCU
plug and through-
cylinder connector
12,19,20
High end of solenoid
valve 2 is the high end of
solenoid valve of shift
Open circuit fault
0x05
Short circuit to ground
fault
0x03

### P1246

Solenoid valve high end 2
fault
Short circuit fault to
power supply
0x04
Open circuit fault
0x05
Short circuit to ground
fault
0x03

### P1247

Solenoid valve high end 3
fault
Short circuit fault to
power supply
0x04

### Automatic

DTC diagnosis and test
solenoid valve 2/clutch
2/switch valve 2, and
TCU plug

### Automatic

DTC diagnosis and test
Open circuit fault
0x05
T33, T48, T47 and
through-cylinder
connector 11,21,13
Short circuit to ground
fault
0x03
Solenoid valve 3 high-
end main pressure and
lubricating
High end of slide
solenoid valve. T44,
T45 of TCU plug and
through-cylinder
connector 10,9
Possible causes
Fault code
Inspection strategy
Setting conditions(Control
strategy)
Faulty position

### P1245

Hardware circuit check
After ignition, the TCU detects
the short circuit fault of the high
end of the solenoid valve to the
power supply, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.
· Harness
· Solenoid Valve High Side 1, 2,

### · TCU

After ignition, the TCU detects
the open circuit fault of
solenoid valve high end 1, the
above fault lasts for 0.1 s or
longer, and the software
makes fault judgment.
After ignition, the TCU detects
the fault of solenoid valve high
end 1 short circuit to ground,
the above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.

### P1246

Hardware circuit check
After ignition, the TCU detects
the short circuit fault of the high
end of the solenoid valve to the
power supply, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.
After ignition, the TCU detects
the open circuit fault of high
end 2 of solenoid valve, the
above fault lasts for 0.1 s or
longer, and the software
makes fault judgment.

### Automatic

DTC diagnosis and test
After ignition, the TCU detects
the fault of solenoid valve high
end 2 short circuit to ground,
the above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.

### P1247

Hardware circuit check
After ignition, the TCU detects
the short circuit fault of the high
end of the solenoid valve to the
power supply, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.

### Automatic

DTC diagnosis and test
After ignition, the TCU detects
the open circuit fault of high
end 3 of solenoid valve, the
above fault lasts for 0.1 s or
longer, and the software
makes fault judgment.
After ignition, the TCU detects
the short circuit fault of solenoid
valve high end 3 to ground, the
above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.
Diagnostic process
Test conditions
Details/Results/Measures

1. Check fault code
A. Connect the diagnostic scanner.
B. Test the automatic transmission system
with a diagnostic scanner.
Are there any DTCs other than P 1245, P

### 1246, P 1247?

- > Yes
Reference: Fault code list
- > No
Go to step 2.

2. Check whether the feedback current of solenoid valve related to high-end 1,2,3,4 of solenoid valve is normal.
A. Connect diagnostic scanner
B. Turn ignition switch to "ON" position
C. Read
data flow
"main
pressure,
lubrication, gearshift 1/2, on-off valve
1/2, clutch 1/2 solenoid valve feedback
current" according to solenoid valve low
side shunt.
Whether the data flow is normal
-> Yes
Go to Step 3
-> No
Contact transmission after-sales technical
support

3. Check the circuit between solenoid valve 1, 2, 3, 4 and TCU.

4. Check TCU
A. Remove TCU

### Automatic

DTC diagnosis and test
B. Install the TCU of this vehicle on a vehicle
in good condition. Is the vehicle in normal
state after installing TCU?
- > Yes
Reference: Troubleshooting according to DTC
- > No
replacing

### TCU


### DTC P1213 P1214 P1216 P1217 P1218

Fault code
Fault code

### Description


### FTB


### Definition


### P1213

Sensor 5V power supply
1 fault
Short circuit to power
supply
0x12
PRND sensor is 5 V
supply
Electrical, port connected
to TCU

### P1213

Voltage too high
0x17
BE2, BE4; Oil
t
t

### P1213

High current
0x19
The sensor supplies
t

### 5V

d
TCU connection port is

### T42


### P1214

Short circuit to power
supply
0x12
Sensor 5V power supply
2 f
lt
B; Input shaft 1/2 speed
i
The supply voltage of the
d
i
i 8V
d

### P1214

Voltage too high
0x17
TCU connection ports are
ti
l

### P1214

High current
0x19

### T43, T53


### P1216

Sensor 8V power supply
1 fault
Short circuit to power
supply
0x12

### P1216

Voltage too high
0x17

### P1216

High current
0x19

### P1217

Sensor 8V power supply
fault
Short circuit to power
supply
0x12

### P1217

Voltage too high
0x17

### P1217

High current
0x19

### P1218

Sensor 8V power supply
fault
Sensor 8V voltage fault
0x0
Possible causes
Fault code
Inspection strategy
Setting conditions(Control
strategy)
Faulty position

### P1213

Hardware circuit check
After ignition, the TCU detects
that the sensor 5V power
supply 1 is shorted to the
power supply, and the software
makes fault judgment.
· Harness

### · TCU


### Automatic

DTC diagnosis and test
After ignition, TCU detects
sensor 5V power supply 1 fault
voltage
is
too
high,
and
software makes fault judgment.
After ignition, TCU detects
sensor 5V power supply 1 fault
current
is
too
high,
and
software makes fault judgment.

### P1214

After ignition, the TCU detects
that the sensor 5V power
supply 2 is short to power
supply,
and
the
software
makes fault judgment.
After ignition, TCU detects
sensor 5V power supply 2 fault
voltage
is
too
high,
and
software makes fault judgme