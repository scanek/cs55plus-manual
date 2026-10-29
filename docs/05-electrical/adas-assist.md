# Системы помощи водителю: слепые зоны, полоса, ACC

> **Страницы в оригинале:** 1081 – 1150 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p1137_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1137_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p1137_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p1137_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Body door lock and anti-theft system997
Body electrical appliance
SPI in the
register is
continuously
sampled for 10
times to report
the short circuit
fault.

### B103313

Right turn signal
lamp open loop

1. Voltage range
9-16 V, engine in
non-CRANK or
CRANK becomes

### NOT

Crank 1s rear

2. BCM wakeup
or CAN network
sleep status,
Right turn signal
lamp open circuit

1. Read DTC
with diagnostic
scanner

2. Check
the
right
steering
lamp connector
connection and
terminal for pin
retraction.

3. Check harness

### J4-15


### (9-16 V)

Body electrical appliance
Body door lock and anti-theft system998

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

3.
TurnLight_Load
_Cfg = 0x014.
Turn lamp
control output is
turned on, after
delay of 100 ms,
10 ms periodic
sampling

### VN9D7D20F

The AD value
from SPI in the
register is
sampled 10
times in
succession
below the open
circuit
threshold(20)

### B103318

Right steering
lamp interrupts
operation

1. Voltage range
9-16 V, engine in
non-CRANK or
CRANK becomes

### NOT

Crank 1s rear

2. BCM wakeup
or CAN network
sleep status,

3. TurnLight_Load
_Cfg = 0x014.
Turn lamp
control output is
turned on, after
delay of 100 ms,
10 ms periodic
sampling

### VN9D7D20F

The AD value
from the SPI in
the register is
sampled 10
times in
succession
above the open
circuit threshold
and below the
interrupt
threshold.(Tentat
ive)
Right turn signal
lamp open circuit

1. Read DTC
with diagnostic
scanner

2. Check
the
right
steering
lamp connector
connection and
terminal for pin
retraction.

3. Check harness

### J4-15


### (9-16 V)


### B103413

Trunk open loop
(To battery 7)

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After power-on
delay of 100 ms,
the trunk is
opened and the
output control is
opened. The
sampling period
of 10 ms is 10
times, and the
continuous
sampling
reaches the
diagnosis
feedback pin is

### Trunk

release
output
open
circuit(Short
circuit to power
supply 7)

1. Read DTC
with diagnostic
scanner

2. Check
whether
the
luggage
compartment
unlocking
switch
connector
connector and
terminal
are
pin-out.

3. Check harness

### J4-20

Body electrical appliance
Body door lock and anti-theft system999
low.

### B103412

Trunk open
battery short
circuit

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After power-on
delay of 100 ms,
the trunk is
opened and the
output control is
closed.
Trunk release
output short
circuit to power
supply

1. Read DTC
with diagnostic
scanner

2. Check
whether
the
luggage
compartment
unlocking
switch
connector
connector and
terminal
are
pin-out.

3. Check harness

### J4-20


### (9-16 V)

Body door lock and anti-theft system1000
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

10 ms sampling
period sampling
10 times,
continuous
sampling to
diagnosis
feedback pin is
high

### B103513

Driver _ Door _

### Unlocked Open

Loop(To
battery 8)

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After the
power-on delay
of 100 ms, the
driver _ door _
unlocked output
control is
opened, the
sampling period
of 10 ms is 10
times, and the
continuous
sampling
reaches the
diagnostic
feedback pin is
low.
Driver door
unlock output
open circuit

1. Read DTC
with diagnostic
scanner

2. Check driver
door lock

3. Check harness

### J4-21


### (9-16 V)


### B103512

Driver _ Door _

### Unlocked


### Battery Short


1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After the
power-on delay
of 100 ms, the
driver _ door _
unlocked output
control is closed,
the sampling
period of 10 ms
is 10 times, and
the continuous
sampling
reaches the
diagnostic
feedback pin is
high.
Driver door
unlock output
short circuit to
ground

1. Read DTC
with diagnostic
scanner

2. Inspect
whether the
driver door lock
connector is
connected and
whether the
terminal is
retracted.

3. Check harness

### J4-21


### (9-16 V)


### B103613

Passenger _
Door _

### Unlocked Open

Loop(To battery
8)

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After power-on
delay of 100 ms,
other three doors
are unlocked and
output control is
turned on.
On, sample 10
Front passenger
door unlocking
open circuit

1. Read DTC
with diagnostic
scanner

2. Check
the
front passenger
door
lock
connector
connection and
terminal for pin
retraction.

3. Check harness

### J4-23


### (9-16 V)

Body door lock and anti-theft system1001
Body electrical appliance
times in 10 ms
sampling period,
and continuously
sample until the
diagnostic
feedback pin is
low.

### B103612

Passenger _
Door _

### Unlocked


### Battery Short


1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

### Front

passenger door
unlocking short
circuit to power
supply

1. Read DTC
with diagnostic
scanner

2. Check
the
front passenger
door
lock
connector
connection and
terminal for pin
retraction.

3. Check harness

### J4-23


### (9-16 V)

Body electrical appliance
Body door lock and anti-theft system1002

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


3. After power-on
delay of 100 ms,
other three doors
are unlocked and
output control is
closed.
Close, sample
10 times in 10
ms sampling
period, and
continuously
sample until the
diagnostic
feedback pin is
high.

### B103713

All doors _
lock open
loop(To battery
8)

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After power-on
delay of 100 ms,
the lock output
control is turned
on, and the
sampling period
of 10 ms is 10
ms.
Once,
continuously
sample to the
diagnosis
feedback pin is
low.
All door unlock
outputs open

1. Read DTC
with diagnostic
scanner

2. Check
whether all the
door
lock
connectors are
connected and
the
terminals
are pin-out.

3. Check harness

### J4-22


### (9-16 V)


### B103712

All doors _
lock battery
short circuit

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After the
power-on delay
of 100 ms, the
lock output is
closed, the 10
ms sampling
period is 10
times, and the
continuous
sampling
reaches the
diagnosis
feedback pin is
high.
All door unlock
outputs short
circuit to power

1. Read DTC
with diagnostic
scanner

2. Check
whether all the
door
lock
connectors are
connected and
the
terminals
are pin-out.

3. Check harness

### J4-22


### (9-16 V)

Body electrical appliance
Body door lock and anti-theft system1003

### B103813

Fuel pump
pressure setting
_ relay open
loop(To Battery
7 or Battery 6,
according to
vehicle settings)

1. Voltage range
9-16 V, 1s after
engine is not
CRANK or

### CRANK


2. BCM wakeup
or CAN network
sleep status,

3. After the
power-on delay
of 100 ms, the oil
pump pressure
output control is
turned on, the 10
ms sampling
period is 10
times, and the
continuous
sampling
reaches the
diagnosis
feedback pin is
low.
Fuel pump
pressure
building relay
open circuit

1. Read DTC
with diagnostic
scanner

2. Check
whether
the
connector
of
the fuel pump
pressure-
building relay is
connected and
whether
the
terminal is pin-
out.

3. Check harness

### J5-51


### (9-16 V)


### B103911

Left steering
lamp short
circuit to ground

1. Voltage range
9-16 V, engine in
non-CRANK or
CRANK becomes

### NOT

Crank 1s rear
Left steering
lamp short
circuit to
ground

1. Read DTC
with diagnostic
scanner

2. Check the left
steering
lamp
connector
connection and
terminal fo