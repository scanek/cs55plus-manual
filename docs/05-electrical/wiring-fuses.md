# Предохранители, реле и жгуты проводов

> **Страницы в оригинале:** 1316 – 1554 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p1348_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1348_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1348_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1348_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1354_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1354_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1355_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1355_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1357_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1357_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1358_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1358_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Parallel auxiliary system1124
Body electrical appliance
F, 14 cycle times
received
140msec signal
If the obvious deviation
is less than 40 or more
than 80, check whether
the terminal resistance
controller is damaged,
and observe whether the
fault is eliminated after
replacing the controller.
(48)

### Check

the
functional status of the
associated controller

### B212F06

Production line mode
activation
Production mode is

### ACTIVE

Production mode is not
closed
Using a diagnostic
scanner, diagnose 2E by
Service shuts down
production mode.

### B213178

Radar never calibrated
Calibration not completed Radar has not been
calibrated
Power on/off the vehicle
again
SDA calibration with
diagnostic scanner
If the calibration still fails,
read the data stream
with a diagnostic
scanner and check
whether the angle and
displacement are out of
tolerance; Check
whether the radar is
blocked and whether the
bracket is deformed or
damaged.
Replace radar and
recalibrate

### B213278

Abnormal radar
calibration status
Calibration not completed Calibration has been
performed, but the
calibration status is not
normal.
Power on/off the vehicle
again
SDA calibration with
diagnostic scanner
If the calibration still fails,
read the data stream
with a diagnostic
scanner and check
whether the angle and
displacement are out of
tolerance; Check
whether the radar is
blocked and whether the
bracket is deformed or
damaged.
Replace radar and
recalibrate

### B212578

Radar calibration error
Calibration error detected Incorrect calibration
Power on/off the vehicle
again
SDA calibration with
diagnostic scanner
If the calibration still fails,
read the data stream
with a diagnostic
scanner and check
whether the angle and
displacement are out of
tolerance; Check
whether the radar is
blocked and whether the
bracket is deformed or
damaged.
Replace radar and
recalibrate

### B212604

System internal error:
Radar blinding detected
Blind spot detected
Radar is blocked
Power on/off the vehicle
again
Check whether the radar
is covered by ice or other
things.
Parallel auxiliary system1125
Body electrical appliance
B21a586
Radar DA_core abnormal DA core does not meet
specifications
Wheel speed, yaw rate
signal, longitudinal
acceleration, front wheel
angle invalid.
DAcore Unreliable tire
size data detected
DAcore detected
unreliable yaw rate
compensation data.
If any value exceeds the
allowable range
Timer - Timer
>1000 ms.
Power on/off the vehicle
again

### Check

whether
the
instrument
fault
is
cleared
(3)

### Check

whether the vehicle is
normal (4) Replace ECU
Parallel auxiliary system1126
Body electrical appliance

### B212981

Radar VMC abnormal
The correlation signal
detected by VMC is
abnormal signal.
Received message
overload
Transmission line is
affected by
electromagnetic
interference
The variantcode read by
the VMCs is empty or
out of rangeThe corridor
information received
from the RPMs is
unknown/incorrect
Power on/off the vehicle
again

### Check

whether
the
instrument
fault
is
cleared
(3)

### Check

whether the vehicle is
normal (4) Replace ECU

### B213000

Radar internal fault
Driving test mode active
Bosch driving test mode
is not disabled
Workflow of standard
maintenance action for
internal ECU
occurrence/fault.
DTC is present/active.
Perform SW update and
new variable
coding/calibration (if
required
Yes).
Via diagnostic tester
ECU hard reset.
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Switch off ignition and
wait
ECU is off (sleep
mode).
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Unplug the ECU itself
or the corresponding
power fuse, and
perform ECU power
reset.
Start the engine and
wait for 5 seconds.
Erasing and reading
out fault memory
If the DTC is still
present/active.
Replace ECU

### B213100

Radar internal fault
MMIC plant data does not
exist
Internal accident/fault
detected
Workflow of standard
maintenance action for
internal ECU
occurrence/fault.
DTC is present/active.
Perform SW update and
new variable
coding/calibration (if
required
Yes).
Via diagnostic tester
ECU hard reset.
Start the engine and
wait for 5 seconds.
Erasing and reading out
Parallel auxiliary system1127
Body electrical appliance
fault memory
If the DTC is still
present/active.
Parallel auxiliary system1128
Body electrical appliance
Switch off ignition and
wait
ECU is off (sleep
mode).
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Unplug the ECU itself
or the corresponding
power fuse, and
perform ECU power
reset.
Start the engine and
wait for 5 seconds.
Erasing and reading
out fault memory
If the DTC is still
present/active.

12. Replace ECUs

### B213200

Radar internal fault
MMIC (monolithic
microwave integrated
circuit) internal
hardware fault
Internal accident/fault
detected
Workflow of standard
maintenance action for
internal ECU
occurrence/fault.
DTC is present/active.
Perform SW update and
new variable
coding/calibration (if
required
Yes).
Via diagnostic tester
ECU hard reset.
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Switch off ignition and
wait
ECU is off (sleep
mode).
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Unplug the ECU itself
or the corresponding
power fuse, and
perform ECU power
reset.
Start the engine and
wait for 5 seconds.
Erasing and reading
out fault memory
If the DTC is still
present/active.

13. Replace ECUs

### B213300

Radar internal fault
Application data integrity
check failed
Internal accident/fault
detected
Workflow of standard
maintenance action for
internal ECU
occurrence/fault.
DTC is present/active.
Parallel auxiliary system1129
Body electrical appliance
Perform SW update and
new variable
coding/calibration (if
required
Yes).
Via diagnostic tester
ECU hard reset.
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Switch off ignition and
wait
ECU is off (sleep
mode).
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Unplug the ECU itself
or the corresponding
power fuse, and
perform ECU power
reset.
Start the engine and
wait for 5 seconds.
Erasing and reading
out fault memory
If the DTC is still
present/active.

14. Replace ECUs

### B213400

Radar ADC module self-
test fault
Radar ADC module self-
test fails
Internal accident/fault
detected
Workflow of standard
maintenance action for
internal ECU
occurrence/fault.
DTC is present/active.
Perform SW update and
new variable
coding/calibration (if
required
Yes).
Via diagnostic tester
ECU hard reset.
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Switch off ignition and
wait
ECU is off (sleep
mode).
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Unplug the ECU itself
or the corresponding
power fuse, and
perform ECU power
Parallel auxiliary system1130
Body electrical appliance
reset.
Parallel auxiliary system1131
Body electrical appliance
Start the engine and
wait for 5 seconds.
Erasing and reading
out fault memory
If the DTC is still
present/active.

15. Replace ECUs

### B213500

Radar internal power
management fault
The ASIC watchdog is
faulty,
and
the
operating system 10 ms
task is abnormal to give
feedback
to
the
watchdog.
Internal accident/fault
detected
Workflow of standard
maintenance action for
internal ECU
occurrence/fault.
DTC is present/active.
Perform SW update and
new variable
coding/calibration (if
required
Yes).
Via diagnostic tester
ECU hard reset.
Start the engine and
wait for 5 seconds.
Erasing and reading out
fault memory
If the DTC is still
present/active.
Switch off ignition and
wait
ECU is