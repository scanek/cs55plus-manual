# Система бесключевого доступа (PEPS)

> **Страницы в оригинале:** 1021 – 1050 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p1021_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1021_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Body door lock and anti-theft system938
Body electrical appliance
Function structure of door signal lamp switch
Door signal lamp consists of switch button, waterproof
rubber, mounting screw, connector, etc. Schematic diagram
and pin definition of PIN
Front hood lock and status switch
The front cover lock is located at the front end of the front cover, as shown in the figure.
Body electrical appliance
Body door lock and anti-theft system938
When the front cover is closed, the lock pin of the front cover is hit against the lock bolt by the weight of the front cover.
Unlock the front cover by pulling the front cover unlocking handle on the instrument panel
to drive the unlocking cable and stop block to complete level 1 unlocking. Lift the front
cover to expose the gap, extend the hand into it and toggle the secondary unlocking
handle to unlock the front cover.
Common methods
Method of release after anti-theft triggering

1. Press the unlock button of the smart key;

2. Bring the smart key and press the PE switch.
Replacement method of key battery

1. Open the rear lid of the key;

2. Then open the upper battery cover.

3. Replace battery
Fault symptom diagnosis
IBCM Common fault diagnosis

### Function


### Fault

symptom
Fault cause

### Solution


### Remarks

Remote control function
Failure of all functions of
remote controller
No matching remote
control
Too far from the
vehicle, or
Re-online key
configuration or
diagnostic
scanner manual
key configuration
Enter the vehicle
for operation or
leave the area
Replace the battery
for the key.
PCB in remote
control
Reinstall the plate
once
Charge the battery

### Replace

the
remote controller
and re-learn the
keyless
system
menu through the
diagnostic
scanner.
First note that the power
supply must be OFF
Status.
Strong interference
near the vehicle
Source. (Transmitter,
etc.)
The remote
controller has no
power, check
Battery in remote
control
Does the
voltage >2.9 V
Contact between
remote controller and
battery

### Bad

Body electrical appliance
Body door lock and anti-theft system939
Vehicle battery
power

### Foot

Remote control
damaged
Body door lock and anti-theft system940
Body electrical appliance

### Function


### Fault

symptom
Fault cause

### Solution


### Remarks

Keyless entry function
Keyless entry failure
Smart key has fault
Front left/right door
handle
When pressing
the door handle
button, observe
the
Switch short or
open
Front left/right
door handle
Does the indicator
light flash,
If there is flashing,
confirm the key.
Antenna short
circuit or open
circuit
Keyless control
module damage
Vehicle battery
power
Normal; If there is
no flicker, please
Handle according to
remote control
failure
Read with
diagnostic scanner
IBCM fault code,

### Foot

IBCM Problem
Keyless control
module and
BCM Direct CAN
Is there a
problem with the
watchman handle
antenna
Read with
diagnostic scanner
IBCM fault code,
Bus short or open
See if IBCM is
present

### Fault

Charge the battery
Replace body
intelligent control
Device assembly

::: tip ПРИМЕЧАНИЕ
Note: Replace body
:::

intelligent control
The device needs to re-
learn the smart key
Key, re-match anti-theft.
One-button start
Vehicle cannot be started 1
First observe
starter motor
Refer to
diagnostic scanner
fault generation
Does it turn, if it
starts
Press the engine
related fault block
after rotating the
motor.
Code processing
method
Check whether the
key is normal
Check engine
control module
Except, keyless
system positive

### Constant


### Observe

whether there is
relevant fault
prompt on the
instrument.
Whether the block
has fault code
Check battery
voltage and
charge
Check whether the
circuit is open
If prompted,
Please refer to
diagnostic scanner
fault
Or short circuit
Replace body
intelligent control
Code handling
method
Observe if the
indicator on the
key flashes, if
any

### Device


::: tip ПРИМЕЧАНИЕ
Note: To replace the
:::

body intelligent
controller, it is necessary
to re-learn the smart key
and re-perform anti-theft
Body door lock and anti-theft system941
Body electrical appliance
Flicker normally
to confirm that the
key is normal; If
there is no flicker,
please
matching.
Handle according to
remote control
failure
Check start
request signal

### Normal

Vehicle battery
power

### Foot

Can bus short
circuit or open

### Road

Inspection and maintenance
Test conditions
Maintenance method

1. Test steps and methods
A. Check whether the resistance of start/stop switch is normal;
B. Check whether both ends of harness are in normal contact;
C. Check whether the appearance of BDC is normal.
A. Replace the start/stop switch and re-verify whether the function
is normal;
B. Reinsert connector harness; if the harness and connector are
damaged, replace it;
C. Replace BDC and re-verify whether the function is normal.
Body electrical appliance
Body door lock and anti-theft system942
DTC Diagnostic

### BDC


### Serial

number
Fault code

### Meaning


### Triggering

conditions

### Possible

fault
cause
s

### Maintenan

ce steps

### Remarks


### B104D17

Circuit voltage
exceeds
threshold

1. BCM is in
wake-up mode
or
network
sleep mode.
2.The engine is
in non-CRANK
3.The actual
voltage on the
battery input pin
is higher than the
defined 16.5 V.
Power supply 1
output voltage
too high

1. Read DTC
with diagnostic
scanner
2.Check whether
the battery is
within the 9-16 V
range.

3. Check
connecting
harness

### (J5-49)


### (9-16 V)

4.Duration
500 ms

### B104D16

Circuit voltage
below threshold

1. BCM is in
wake-up mode
or
network
sleep mode.
2.The engine is
in non-CRANK
3.Actual voltage
on battery input
pin is lower than
definition 8.5 V
Power supply 1
output voltage
too low

1. Read DTC
with diagnostic
scanner
2.Check whether
the battery is
within the 9-16 V
range.

3. Check
connecting
harness

### (J5-49)


### (9-16 V)

4.Duration
500 ms

### U101088

DiagCAN
interface
Bus-off

1. Battery voltage
is
9-16 V, and
BCMs
1.
Harness/conne
ctor fault;

1. Read DTC
with diagnostic
scanner

### Awake


2. Controller
fault;

2. Check CAN
line

2. After power-on
for 1S

3. Bus off
counter value
NBusOffCount>=

3. External
interference(Suc
h as illegal
peripherals)
Connection (J2-
39/

### J2-40)


### (1.5-3.5 V)


3. Check whether
there is exterior
Set access OBD

4. Test terminal
resistance
Is 120 ohm left
Right, if obvious
100 or less
Above 140, check
Check terminal
resistance control
Is the device
damaged, more
Observe after
replacing
controller
Is the fault
Body electrical appliance
Body door lock and anti-theft system943
eliminated

### U101288

PCAN interface
Bus- off

1. Battery voltage
is
9-16 V, and
BCMs
1.
Harness/conne
ctor fault;

1. Read DTC
with diagnostic
scanner

### Awake


2. Controller
fault;

2. Check CAN
line

2. After power-on
for 1S

3. Bus off counter

3. External
interference(Suc
h as illegal
peripherals)
Connection(J5-

### 2/J5-3)


### (1.5-3.5 V)


### Value

NBusOffCount>=

3. Check whether
there is exterior
Set access OBD

4. Test terminal
resistance
Is 120 ohm left
Right, if obvious
100 or less
Above 140, check
Body door lock and anti-theft system944
Body electrical appliance

### Serial

number
Fault code

### Meaning


### Triggering

conditions

### Possible

fault
cause
s

### Maintenan

ce steps

### Remarks

Check whether
the
terminal
resistance
controller
is
damaged, and
observe
whether
the
fault
is
eliminated after
replacing
the
controller.

### U101988

BCAN Bus-off

1. Battery voltage
is
1.
Harness/connect
or

1. Read with
diagnostic
scanner
9-16 V, and
BCMs
Fault;
Fault code

### Awake


2. Controller fault; 2. Check CAN
line
2, 1S after power-
on

3. Bus off
counter value
NBusOffCount>=

3. External
interference(Suc
h as illegal
peripherals)
Connection (J3-
63/

### J3-64)


### (1.5-3.5 V)


3. Check whether
there is exterior
Set access OBD

4. Test terminal
resistance
Is 120 ohm left
Right, if obvious
100 or less
Above 140, check
Check terminal
resistance control
Is the device
damaged, more
Obser