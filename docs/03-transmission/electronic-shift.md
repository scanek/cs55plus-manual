# Электронный селектор переключения передач

> **Страницы в оригинале:** 531 – 565 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p536_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p536_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p537_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p537_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Automatic transmission
DTC diagnosis and test518
Clutch 1 pressure data flow is normal
-> Yes
Go to Step 3
-> No
Contact transmission after-sales technical support

3. Check TCU power supply circuit
A. Turn the ignition switch to "LOCK" position and disconnect the battery negative
cable.
B. Disconnect TCU harness plug.
C. Connect the battery negative harness.
D. Turn the ignition switch to "ON" position.
E. Measure the voltage between T15 and T32 of TCU harness plug and reliable
grounding point.
Standard voltage: 11--Whether 14 V circuit check is normal?
? Yes
Go to step 7.
? No
Overhaul open circuit fault between terminals T15 and T32 of TCU harness plug and
engine compartment electrical center C01 and indoor electrical center P01 respectively.

4. Check grounding circuit of TCU
A. Turn the ignition switch to "LOCK" position and disconnect the battery negative
cable.
B. Disconnect TCU harness plug.
C. Measure the resistance between T5 and T7 of TCU harness plug and reliable
grounding point.
Standard resistance: Is the resistance less than 5Ω normal?
? Yes
Go to Step 7
? No
Overhaul open circuit fault between terminal T5 and T7 of TCU harness plug and
grounding point G 310.
Confirm the system is normal.

5. Check TCU
A. Dismantle TCU
B. Install the TCU of this vehicle on a vehicle in good condition.
Is the vehicle in normal state after installing TCU?
- > Yes
Reference: Troubleshooting according to DTC
- > No replacing TCU
Automatic transmission
DTC diagnosis and test519

### DTC P0845

Fault code
Fault code

### Description


### FTB


### Definition


### P0845

Clutch 2 sensor
Voltage signal too low
0x16
Even pressure sensor is
connected with terminals
BC1, BD4 and BD2 of
TCU connector through
cylinder connector
18,19,20.
Voltage signal too high
0x17

2. Possible causes
Fault code
Inspection strategy
Setting conditions(Control
strategy)
Faulty position

### P0845

Hardware circuit check
After ignition, the software
detects that the voltage of even
clutch pressure sensor is less
than 0.125 V, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.
· Harness
· Clutch 2 pressure sensor

### · TCU

After ignition, the software
detects that the voltage of even
clutch pressure sensor is
greater than 4.875 V, the above
fault lasts for 0.1 s or longer,
and the software makes fault
judgment.
Diagnostic process
Test conditions
Details/Results/Measures

1. Check fault code
A. Connect the diagnostic scanner.
B. Test the automatic transmission
system with a diagnostic scanner. Is
there any fault code other than
P0845 fault code?
- > Yes
Reference: Fault code list
- > No
Go to step 2.

2. Check clutch 2 pressure data flow
A. Read automatic transmission data stream "clutch 2
pressure" with diagnostic scanner. Is the data flow
normal
-> Yes
Go to Step 3
-> No
Contact transmission after-sales technical support

3. Check TCU power supply circuit
A. Turn the ignition switch to "LOCK" position and disconnect the battery negative
cable.
B. Disconnect TCU harness plug.
C. Connect the battery negative harness.
D. Turn the ignition switch to "ON" position.
E. Measure the voltage between T15 and T32 of TCU harness plug and reliable
grounding point.
Standard voltage: 11--Whether 14 V circuit check is normal?
Automatic transmission
DTC diagnosis and test520
? Yes
Go to step 7.
? No
Overhaul open circuit fault between terminals T15 and T32 of TCU harness plug and
engine compartment electrical center C01 and indoor electrical center P01 respectively.

4. Check grounding circuit of TCU
A. Turn the ignition switch to "LOCK" position and disconnect the battery negative
cable.
B. Disconnect TCU harness plug.
C. Measure the resistance between T5 and T7 of TCU harness plug and reliable
grounding point.
Standard resistance: Is the resistance less than 5Ω normal?
? Yes
Go to Step 7
? No
Overhaul open circuit fault between terminal T5 and T7 of TCU harness plug and
grounding point G 310.
Confirm the system is normal.

5. Check TCU
A. Dismantle TCU
B. Install the TCU of this vehicle on a vehicle in good condition.
Is the vehicle in normal state after installing TCU?
- > Yes
Reference: Troubleshooting according to DTC
- > No replacing TCU

### DTC P2831 P2836 P283B P2840

Fault code
Fault code

### Description


### FTB


### Definition


### P2831

Shift fork 1st (gear 5/7)
displacement sensor
Voltage signal too low
0x16
The fork position sensor
passes through
terminals 32,33,34,35 of
cylinder connector and
B_J1, B_J3, B_H1 of
TCU harness plug AB.
B_J2 terminal connection

### P2831

Voltage signal too high
0x17

### P2836

Shift fork 2 (gear 2/6)
displacement sensor
Voltage signal too low
0x16

### P2836

Voltage signal too high
0x17

### P283B

Shift fork 3rd (gear 4/R)
displacement sensor
Voltage signal too low
0x16

### P283B

Voltage signal too high
0x17

### P2840

Shift fork 4 (gear 1/3)
displacement sensor
Voltage signal too low
0x16

### P2840

Voltage signal too high
0x17
Possible causes
Fault code
Inspection strategy
Setting conditions(Control
strategy)
Faulty position
Automatic transmission
DTC diagnosis and test521

### P2831

Hardware circuit check
After ignition, the software
detects that the voltage of shift
fork (gear 5/7) displacement
sensor is less than 0.125 V, the
above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.
· harness
After ignition, the software
detects that the displacement
sensor of shift fork 5/7 (gear
5/7) is greater than 4.875 V, the
above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.

### P2836

After ignition, the software
detects that the voltage of shift
fork 2-6 (gear 2-6)
displacement sensor is less
than 0.125 V, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.
· Fork displacement sensor
After ignition, the software
detects that the displacement
sensor of shift fork 2-6 (gear 2-

6) is greater than 4.875 V, the
above fault lasts for 0.1 s or
longer, and the software makes
fault judgment.

### P283B

After ignition, the software
detects that the voltage of
displacement sensor of shifting
fork 4- R (gear 4- R) is less
than 0.125 V, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.

### · TCU

After ignition, the software
detects that the shifting fork
(gear 4- R) displacement
sensor is greater than 4.875 V,
the above fault lasts for 0.1 s or
longer, and the DTCs make
fault judgment.

### P2840

After ignition, the software
detects that the voltage of shift
fork 1-3 (gear 1-3)
displacement sensor is less
than 0.125 V, the above fault
lasts for 0.1 s or longer, and the
software makes fault judgment.
After ignition, the software
detects that the shift fork 1-3
(gear 1-3) displacement sensor
is greater than 4.875 V, the
above fault lasts for 0.1 s or
longer, and the DTCs make
fault judgment.
Diagnostic process
Test conditions
Details/Results/Measures

1. Check fault code
Automatic transmission
DTC diagnosis and test522
A. Connect the diagnostic scanner.
B. Test the automatic transmission system with a diagnostic scanner.
Is there P 2831, P 2836, P283B, P 2840
Fault code other than fault code
- > Yes
Reference: Fault code list
- > No
Go to step 2.

2. Check the position of shift fork 1, 2, 3 and 4.
A. Connect diagnostic scanner
B. Turn ignition switch to "ON" position
C. Read data stream "shift fork 1,2,3,4 position" with diagnostic scanner
Whether the data flow is normal
Automatic transmission
DTC diagnosis and test523
-> Yes
Contact transmission after-sales technical support
-> No
Go to Step 3

3. Check power supply circuit of TCU
A. Turn the ignition switch to "LOCK" position and
disconnect the battery negative cable.
B. Disconnect TCU harness plug.
C. Connect the battery negative harness.
D. Turn the ignition switch to "ON" position.
E. Measure the voltage between T15 and T32 of TCU
harness plug and reliable grounding point.
Standard voltage: 11--Whether 14 V
circuit check is normal?
? Yes
Go to step 7.
? N