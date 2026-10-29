# Подушки безопасности и преднатяжители (SRS)

> **Страницы в оригинале:** 1251 – 1315 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Содержание и процедуры

Parallel auxiliary system1098
Body electrical appliance
(2) ECU internal voltage
too low
Power on the vehicle
again and wait for 5

### Second

Clear DTC

### Read


### DTC

if
not
present

### DTC:


### MPC

reusable If DTC still
present/active:
Replacing MPC

### B220C45

ECU software fault
The ignition switch is on
ECU software abnormal
Abnormal operation of
controller software
Turn off ignition switch
Power on the vehicle
again and wait for 5

### Second

Clear DTC

### Read


### DTC

if
not
present

### DTC:


### MPC

reusable If DTC still
present/active:
Replacing MPC

### B220D54

ECU software temporary
fault
The ignition switch is on
ECU software abnormal
Abnormal operation of
controller software
Turn off ignition switch
Power on the vehicle
again and wait for 5

### Second

Clear DTC

### Read


### DTC

if
not
present

### DTC:


### MPC

reusable If DTC still
present/active:
Replacing MPC

### B220E60

ECU temperature
exceeds maximum
value fault
The ignition switch is on
ECU internal temperature
is too high
Controller temperature
too high
Turn off ignition switch
Take appropriate heat
dissipation
measures(If interior
A/C is turned on)
Power on the vehicle
again and wait for 5

### Second

Clear DTC

### Read


### DTC

if
not
present

### DTC:


### MPC

reusable If DTC still
present/active:
Replacing MPC

### B220F32

MPC calibration input
parameter fault
The ignition switch is on
Controller calibration
error
Controller internal
calibration parameter is
abnormal.

### Recalibrate

Power on the vehicle
again and wait for 5

### Second

Clear DTC

### Read


### DTC

if
not
present

### DTC:


### MPC

reusable If DTC still
present/active:
Replacing MPC
Fault symptom diagnosis

### Check

and
confirm
test
equipmen
t
Parallel auxiliary system1099
Body electrical appliance
Confirm the user's problem and whether the instrument displays the lane assist system fault information.
Check whether the switch function is normal. Click the alarm mode of "Early Warning, Rectification, Early Warning + Rectification" in
"Vehicle Center - Driving Assistance" of the host to confirm whether the switch can be normally switched. If it is not switched, the
system has fault.
Read the version information of lane departure and current DTC with KT 700 diagnostic scanner.
Carry out corresponding troubleshooting according to the fault code prompt. If it is necessary to check the camera installation
deviation, remove the inner rearview mirror and beauty cover, visually inspect the lane departure controller assembly for obvious
mechanical or electrical damage and whether the front windshield camera installation position is broken.
There is strong correlation between lane departure controller assembly and adaptive cruise controller assembly, so special attention
should be paid to the state of adaptive cruise controller.

### Warning

If the relevant systems such as EMS, EPBi, TCU and EPS are replaced or the software is updated for some reasons, the correct
operation must be carried out according to the repair/maintenance methods of the corresponding system, the fault code of the lane
assist system shall be cleared, and the vehicle shall confirm that the function of the lane assist system is normal.
Appearance check list
Mechanical part
Electrical part
Lane departure controller assembly
Controller harness and connector
Lane departure controller mounting bracket

### Fuse

Front gear glass
Lane departure controller assembly
Fault diagnosis table

### Fault

sympto
m

### Fault

cause

### Solution

Three modes of "Warning, Rectification,

::: warning ВНИМАНИЕ
Warning + Rectification" cannot be
:::

switched through the vehicle center of the
vehicle machine - driving assistance -
1、 lane departure controller has fault

2. Lane departure controller is short-
circuited or open-circuited with the CAN
bus of the vehicle.

1. Use the diagnostic scanner to read the
fault code and check the associated
system according to the prompt.

2. If the diagnostic scanner cannot
communicate with the controller, check
whether the harness is normal or whether
the BDC is correctly configured.
The instrument prompts that the camera is
blocked and the lane departure fault lamp
is yellow.

1. Lane deviation controller field of view is
blocked by foreign objects.

2. The glass at the lane departure controller
field of view is broken.

3. The camera of lane departure controller
has dust.

1. Clean the front windshield.

2. Replace front windshield

3. Clean lens
Diagnostic scanner cannot connect lane
departure controller
Fuse of 1、 lane departure controller blows;
Poor contact of 2、 connector;

3. BDC configuration is incorrect.
1、 Replace fuse;
2、 Check connector

3. Reconfigure BDC or replace BDC
The instrument prompts lane assist system
fault, and the lane departure fault lamp is
yellow.
1、 associated system causes lane assist
system fault;
2、 lane departure controller fault
1、 Maintenance association system
according to diagnostic scanner DTC;

2. Replace lane departure controller
assembly
The instrument prompts LAS is not
calibrated, and the lane departure fault
lamp is yellow.

1. Camera angle out of range

2. Bracket damage

1. Enter FC calibration lane deviation with
diagnostic scanner

2. Reinstall and calibrate

3. If the above is not available, refer to
after-sales calibration of lane assist
system for calibration method of lane
departure controller assembly.
The diagnostic scanner prompts to interrupt
the contact with Private CAN.
Adaptive Cruise Control model is incorrectly
configured
Re-model the adaptive cruise control
The instrument
prompts that the
camera is blocked.
Diagnostic scanner KT 700, multimeter
Parallel auxiliary system1100
Body electrical appliance
The instrument prompts that the camera is blocked
and the lane departure fault lamp is yellow. Fault
cause
The lane deviation controller field of view is blocked by foreign objects.
Broken glass at lane departure controller field of view.
Parallel auxiliary system1101
Body electrical appliance
The camera of the lane departure
controller has dust. Solution
Clean the front windscreen.
Replace the front windscreen.
Clean the lens.
Fault cause of
steering wheel not
vibrating during
alarm
1.Enter the interface of incall System Setting - Vehicle Center - Train Assistance, and confirm whether the warning mode has selected the
sound reminder mode; If yes, select Vibration Mode or Sound + Vibration Mode.

2. If the reminder mode has vibration, the steering wheel still does not vibrate during alarm. Use diagnostic scanner KT 700 to check
whether the system has current fault:
With a diagnostic scanner, enter the S 203 front camera FC/LAS, read the current fault code, confirm whether there is fault, if there is fault,
perform troubleshooting according to relevant troubleshooting methods of DTCs.
Use diagnostic scanner to enter S203EPS, read current fault code, confirm whether there is fault, if there is fault, perform troubleshooting
according to relevant troubleshooting methods of DTCs.
Removal and installation
Lane assist control and lane assist camera
Disassembly and assembly tool
8 mm socket and ratchet wrench
Plastic skid

### Removal


1. Use a pry piece to pry outwards along the edge of the beauty cover, and remove the partial plastic cover plate of the beauty cover
shown in Figure 1.

2. Use 8 mm socket and ratchet wrench to remove the bolt shown in the figure and remove the inner rearview mirror;
Parallel auxiliary system1102
Body electrical appliance

3. Gently pry along the edge of the beauty cover with a pry piece, and remove the beauty cover after the peripheral buckle loosens.

4. Dismantle controller;
First remove the controller harness connector (5); Then remove the controller (4): Hold the two ends of the controller, first pull the
controller downward to open the metal spring. When the metal spring is wide enough for the controller, pull the controller downward with
a little force to release the controller. Be care