# Круговой обзор 360° и парктроники

> **Страницы в оригинале:** 1051 – 1080 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Содержание и процедуры

Body electrical appliance
Body door lock and anti-theft system967

### U100387

When LIN3 RLS
communication
arrives

1. Battery voltage

### 8-18 V,


2. Bcm is in
wakeup state,
and after LIN
wakeup is
delayed for 1s,
BCM cannot be
in tTimeout (1s).
Bcm cannot
communicate
with LINs
within the time
of tTimeout.

1. Read DTC
with diagnostic
scanner

2. Check
whether

### BCM

and rain sensor
connector
are
connected and
whether
the
terminal is pin-
out.

3. Check harness

### (J3-32)


### (9-11 V)

Body door lock and anti-theft system968
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


### Communication

with RLS within
time
3.And automatic
wiper
AutoWiper_Cfg
exists.

### U100701

Sunroof system
failure

1. Battery voltage

### 8-18 V,


2. Bcm is in
wakeup state,
and Lin wakes
up and delays
1s start.

3. One of the
response errors
Sunroof_ECUErr
o r=0x01,
Sunroof_H
allError=0x01 or
Sunroof_RelayEr
r or=0x01 is
received
continuously
more than the
defined
maximum
number of times
(five).
Any of the
following errors
detected,
Sunroof_ECUErr
o r,
Sunroof_Respon
se
_Error ,
Sunroof_HallErr
or
, and
Sunroof_RelayE
rr orSignal

1. Read DTC
with diagnostic
scanner

2. Check
whether

### BCM

and
sunroof
module
connector
are
connected and
whether
the
terminal is pin-
out.

3. Check harness

### (J3-57)


### (9-11 V)


### U100709

Sunroof switch
failure

1. Battery voltage

### 8-18 V,


2. The BCM is
awake and the
LIN wakes up
with a delay of
1S.

3. The error
number of
received
Sunroof_Switch
Er ror=0x01
error signal
reaches five
frames.

### Receive

Sunroof_Switch
Er ror signal

1. Read DTC
with diagnostic
scanner

2. Check
whether

### BCM

and
sunroof
switch
connector
are
connected and
whether
the
terminal is pin-
out.

3. Check harness

### (J3-57)


### (9-11 V)


### U100801

Sunroof curtain
system failure

1. Battery voltage

### 8-18 V,


2. Bcm is in
wakeup state,
and Lin wakes
up and delays
1s start.

3. Continuous
response error
Sunshade_ECU
Err or=0x01,

### Sunshade


### Either

_HallError=0x01
or
Sunshade_Relay
Er ror=0x01
signal exceeds
the defined
maximum
number of times
(5 times).
Any of the
following signals
are detected:
Sunshade_ECU
Err or,
Sunshade_Resp
ons e_Error,
Sunshade_HallE
rr or, and
Sunshade_Relay
Er rorSignal

1. Read DTC
with diagnostic
scanner

2. Check
whether BCM
and sunroof
curtain
connector are
connected and
whether the
terminal is pin-
out.

3. Check harness

### (J3-57)


### (9-11 V)

Body door lock and anti-theft system969
Body electrical appliance

### U100809

Sunroof curtain
switch fails

1. Battery voltage

### 8-18 V,


### Received

Sunshade_Switc
hE rror signal
receives
Sunshade_Switc
hE rror signal

1. Read DTC
with diagnostic
scanner

2. Check
whether

### BCM

and
sunroof
curtain
switch
connector
are
connected and
whether
the
terminal is pin-
out.
Body electrical appliance
Body door lock and anti-theft system970

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


2. The BCM is
awake and the
LIN wakes up
with a delay of
1S.

3. The error
number of
received
Sunshade_Switc
hE rror=0x01
error signal
reaches five
frames.

3. Check harness

### (J3-57)


### (9-11 V)


### U10004B


### RLS

overtemperature

1. Battery voltage

### 8-18 V,


2. Bcm is in
wakeup state,
and Lin wakes
up and delays
1s start.

3. The error
number of
received
RLS_Error_statu
s_
over_temperatur
e= 0x01 error
signal reaches
five frames.

### Receive

RLS_Error_statu
s_
ove_temperature
signal

1. Read DTC
with diagnostic
scanner

2. Check
the
connection
of
rain
sensor
connector and
terminal for pin
withdrawal.

3. Check harness

### (J3-32)


### (9-11 V)


### U100046

Rain sensor
calibration error

1. Battery voltage

### 9~16 V,


2. The BCM is
awake and the
LIN wakes up
with a delay of
1S.

3. The error
number of
received
RLS_Error_calibr
a
tion_rain_sensor
=0 x01 error
signal reaches
five frames.

### Received

RLS_Error

1. Read DTC
with diagnostic
scanner

2. Check
the
connection
of
rain
sensor
connector and
terminal for pin
withdrawal.

3. Check harness

### (J3-32)


### (9-11 V)


### U100017

RLS overvoltage

1. Battery voltage

### 9~16 V,


2. The BCM is
awake and the
LIN wakes up
with a delay of
1S.

3. Received
RLS_Error_statu
s_
over_voltage=0x
0 1 error signal
error
Number of times
reaches 5 frames

### Receive

RLS_Error_statu
s_ over_voltage
signal

1. Read DTC
with diagnostic
scanner

2. Check
the
connection
of
rain
sensor
connector and
terminal for pin
withdrawal.

3. Check harness

### (J3-32)


### (9-11 V)

Body electrical appliance
Body door lock and anti-theft system971

### U101883

EMSImmo

### Verification


### Request


1. Battery voltage

### 6.5-18 V,


2. The BCM is
awake,

3. The
received

### EMS


### Immo

calculation

### Checksum

is
inconsistent with
the

### BCM

calculation
Can bus
transmission is
abnormal

1. Read DTC
with diagnostic
scanner

2. Disconnect
battery and
power on
again

3. Check
whether the
battery level is

### 9-16 V


4. Test harness
connection

### (J3-63/J3-64)


### (1.5-3.5 V)


### U101987

No verification
request received
from EMSImmo

1. Battery voltage

### 6.5-18 V,


### Configuration

word error

1. Read DTC
with diagnostic
scanner

2. Check
whether the
configuration
word is correct
Body door lock and anti-theft system972
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


2. After the BCM
is awake and
the power mode
is On for 2
seconds,

3. No verification
request received
from EMSImmo

3. Disconnect
battery and
power on
again

4. Check
whether the
battery level is

### 9-16 V


5. Test harness
connection

### (J3-63/J3-64)


### (1.5-3.5 V)


### U101A87

No verification
results received
from EMSImmo

1. Battery voltage

### 6.5-18 V,


2. The BCM is
awake and the
power
supply
mode is On.

3. No verification
result
of
EMSImmo
is
received
within
3.5 seconds
Can bus
transmission is
abnormal

1. Read DTC
with diagnostic
scanner

2. Disconnect
battery and
power on
again

3. Check
whether the
battery level is

### 9-16 V


4. Test harness
connection

### (J3-63/J3-64)


### (1.5-3.5 V)


### U103D87


### IBS

communication
loss

1. Battery voltage
is

### 8-18 V,


2. The BCM is
awake,

3. Lin wakeup
delay
After 1S, no
message is
received within
1s. 0x34
IBS_LIN_10x35
IBS_LIN_20x36
IBS_LIN_30x37
IBS_LIN_44.
The vehicle is
equipped with

### IBS

node.(IBS_Cfg=
0x01)

### LIN2

transmission
error flag
position bit

1. Read DTC
with diagnostic
scanner

2. Check LIN
line
connection(J3-
32)

### (9-11 V)


### U100901

IBS system fault

1. Battery voltage
is

### 8-18 V,


2. The BCM is
awake,

3. Lin wakeup
delay
1s starts, and
the number of
received signal
errors
reaches
5.
Frame.

### IBS_LIN_1_ERR

OR_Calib =
IBS sensor
fault.

1. Read DTC
with diagnostic
scanner

2. Replace IBS

3. Check LIN
line
connection(J3-
32)

### (9-11 V)

Body door lock and anti-theft system973
Body electrical appliance
0x01IBS_LIN_1_

### ERROR_IDENT =

0x014.1s after
power supply
status is IGN

### ON


### U102F81

IBS feedback
error

1. Battery voltage

### 8-18 V,


2. The BCM is
awake,

3. Lin wakeup
delay
1s start,
continuous
collection
The number of
consecutive
errors returned
exceeds
the
defined
maximum
number
of
times

1. Read DTC
with diagnostic
scanner

2. Check
whether the
BCM and IBS
module
connectors are
connected and
the terminals
are pinned.
Body electrical appliance
Body door lock and anti-theft system974

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

To Resp_Error
=0x1 5 times

3. Check harness

### (J3-32)


### (9-11 V)


### U103881

Rain closing
sunroof fa