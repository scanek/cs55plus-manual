# Обшивки стоек, потолок и элементы салона

> **Страницы в оригинале:** 1611 – 1650 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p1635_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1635_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1635_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1635_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1636_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1636_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1636_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1636_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1636_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1636_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1637_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1637_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

DTC Diagnostic
Fault code table1372
Power supply gear OFF
50 ms
The voltage is within
the normal working
range of 9-16 V
4.Without using 28
service to suspend
communication

### B1B0049

Internal fault
ECU internal key
hardware and software
error
ECU internal key
hardware and software
error
Return to repair shop for
repair

### B1B0050

Internal fault with life
cycle counter function
ECU internal key
hardware and software
error
ECU internal key
hardware and software
error
Return to repair shop for
repair

### B002201

Can controller related
failure
Can drive communication
exceeds
500ms
Problem with CAN
controller hardware

1. If history fault, try to
clear error 2.If it is
always the current
reason
Obstacle, replacement

### B1B0111

Driver side acceleration
sensor short circuit to
ground
Sensor positive
connected to ground for
duration in the same
power cycle
About 2.7 seconds, or
the sensor positive
electrode is connected
to the ground before
power-on. This fault can
be found after power-on
initialization.
Sensor wiring problem
Check the sensor wiring
to ensure that the
sensor is connected
properly.

### B1B012B

Driver side acceleration
sensor wiring

### Wire

the
positive
electrodes of the two
sensors before power-
on. This fault will be
found immediately after
power-on initialization.
Sensor wiring problem
Check the sensor wiring
to ensure that the
sensor is connected
properly.

### B1B0155

Driver side acceleration
sensor not configured
The controller sensor is
not equipped, but the
vehicle is equipped with
this sensor.
The sensor is not
configured in the
software configuration.

### Make

sure
that
the
sensor
has
been
configured
in
the
software
configuration.

### After

re-power-on
initialization, the fault will
become history fault.

### B1B014A

Driver side acceleration
sensor initialization error
Wrong sensor type
Connecting sensor of
wrong type
Replace correct type
sensor

### B1B0181

Driver side acceleration
sensor receives invalid
data
Unstable communication
between controller and
sensor(Poor contact)
Poor contact between
controller and sensor
connecting wire
Check the sensor wiring
to ensure that the
sensor is connected
properly.

### B1B0112

Positive electrode of
driver side acceleration
sensor is connected to
power supply.
In the same power-on
cycle,
the
sensor
positive is connected to
the power supply for 3 to
4 seconds, or the sensor
positive is connected to
the
ground
before
power-on, and the fault
can
be
found
after
power-on initialization.
Sensor wiring problem
Check the sensor wiring
to
ensure
that
the
sensor
is
connected
normally. In the same
power-on cycle, the fault
will be relieved after 2 to
3 seconds. The fault will
be relieved immediately
after power-on again.

### B1B0113

Driver side acceleration
sensor open circuit
Sensor disconnection
Sensor wiring problem
Make sure the sensor
is connected properly,
and release the fault
after 3 to 4 seconds.

### B1B0129

Driver side acceleration
sensor error due to
signal enhancement or
algorithm sensor
watchdog error
The acceleration signal
is too strong and
exceeds the range for a
certain time.(0.13
seconds to 5 seconds)
The acceleration signal
is too strong and
exceeds the range for a
certain time.(0.13
seconds to 5 seconds)
Replace both sensor and
controller

### B1B0196

Driver side acceleration
sensor internal error
Sensor has internal fault
or abnormal connection
during
sensor
initialization
Sensor has internal fault
or abnormal connection
during
sensor
initialization
Power off the controller
and replace it with a new
sensor. Power on the
controller and clear the
DTC Diagnostic
Fault code table1373
error within the power-
on period.

### B1B0211

Copilot side acceleration
sensor short circuit to
ground
Sensor positive
connected to ground for
duration in the same
power cycle
About 2.7 seconds, or
the sensor positive
electrode is connected
to the ground before
power-on. This fault can
be found after power-on
initialization.
Sensor wiring problem
Check the sensor wiring
to ensure that the
sensor positive
connection is normal.

### B1B022B

Passenger's side
peripheral front
acceleration sensor
wiring

### Connect

the
positive
electrodes of the two
sensors before power-
on. This fault will be
found immediately after
power-on initialization.
Sensor wiring problem
Check the sensor wiring
to ensure that the
sensor positive
connection is normal.
DTC Diagnostic
Fault code table1374

### B1B0255

The co-driver side
acceleration sensor is
not configured.
The controller sensor is
not equipped, but the
vehicle is equipped with
this sensor.
The sensor is not
configured in the
software configuration.

### Make

sure
that
the
sensor
has
been
configured
in
the
software
configuration.

### After

re-power-on
initialization, the fault will
become history fault.

### B1B024A

Co-driver side
acceleration sensor
initialization error
Wrong sensor type
Connecting sensor of
wrong type
Replace correct type
sensor

### B1B0281

The co-driver side
acceleration sensor
receives invalid data.
Unstable communication
between controller and
sensor(Poor contact)
Poor contact between
controller and sensor
connecting wire
Check the sensor wiring
to ensure that the
sensor is connected
properly.

### B1B0212

The positive electrode of
the co-driver side
acceleration sensor is
connected to the power
supply.
In the same power-on
cycle,
the
sensor
positive is connected to
the power supply for 3 to
4 seconds, or the sensor
positive is connected to
the
ground
before
power-on, and the fault
can
be
found
after
power-on initialization.
Sensor wiring problem
Check the sensor wiring
to
ensure
that
the
sensor
is
connected
normally. In the same
power-on cycle, the fault
will be relieved after 2 to
3 seconds. The fault will
be relieved immediately
after power-on again.

### B1B0213

Front passenger side
acceleration sensor
open circuit
Disconnecting sensor
. Sensor wiring problem
Make sure the sensor
is connected properly,
and release the fault
after 3 to 4 seconds.

### B1B0229

Passenger side
acceleration sensor
error due to signal
enhancement or
algorithm sensor
watchdog error
The acceleration signal
is too strong and
exceeds the range for a
certain time.(0.13
seconds to 5 seconds)
The acceleration signal
is too strong and
exceeds the range for a
certain time.(0.13
seconds to 5 seconds)
Replace both sensor and
controller

### B1B0296

Co-driver side
acceleration sensor
internal error
Sensor has internal fault
or abnormal connection
during
sensor
initialization
Sensor has internal fault
or abnormal connection
during
sensor
initialization
Power off the controller
and replace it with a new
transmitter. Power on
the controller and clear
the error within the
power-on period.

### B1B0311

Driver front sensor short
circuit to ground
Sensor wiring problem
Sensor wiring problem
Check the sensor wiring
to ensure that the
sensor positive
connection is normal.

### B1B032B

Front acceleration sensor
wiring
Sensor wiring problem
Sensor wiring problem
Check the sensor wiring
to ensure that the
sensor positive
connection is normal.

### B1B0355

Driver front sensor
configuration error
The sensor is not
configured in the
software configuration.
The sensor is not
configured in the
software configuration.

### Make

sure
that
the
sensor
has
been
configured
in
the
software
configuration.

### After

re-power-on
initialization, the fault will
become history fault.

### B1B034A

Driver front acceleration
sensor initialization error
Connecting sensor of
wrong type
Connecting sensor of
wrong type
Replace correct type
sensor

### B1B0381

Invalid data received by
driver front acceleration
sensor
Poor contact between
controller and sensor
connecting wire
Poor contact between
controller and sensor
connecting wire
Check the sensor wiring
to ensure that the
sensor is connected
properly.

### B1B0312

Positive pole of driver's
front acceleration sensor
is connected to power
supply.
Sensor wiring problem
Sensor wiring problem
Check the sensor wir