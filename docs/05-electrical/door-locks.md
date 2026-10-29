# Центральный замок и противоугонная система

> **Страницы в оригинале:** 996 – 1020 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p996_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p996_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p996_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p996_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p997_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p997_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p998_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p998_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p998_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p998_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p999_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p999_1.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Body electrical appliance
Wiper washer system917

::: tip ПРИМЕЧАНИЕ
Note 1: Some astigmatism of low beam may be above the cut-off line;
:::


::: tip ПРИМЕЧАНИЕ
Note 2: It may be necessary to perform vertical
:::

adjustment again after horizontal adjustment.
Combination headlamp principle

1. Functional diagram:

2. Interface definition:

### Pin

Function abbreviation
Function description
High beam
High beam signal
Low beam
Far and low beam power supply
High/low beam GND
Far and low beam ground
/
/
/
/
/
/
Day running lamp
Daily running lamp power supply
Front position lamp/day running lamp/front
turn signal lamp GND
Day lamp/front position lamp/front steering
lamp ground
Front position lamp
Position lamp power supply
Body electrical appliance
Wiper washer system918
Front turn signal lamp
Front turn signal lamp power supply
Front turn signal
Front turn signal

### Motor

Motor power supply
Motor signal
Motor control signal
Motor GND
Motor ground
Functional definition of rear combination lamp (including reversing lamp and brake lamp)
Interface definition of combination rear lamp assembly I:

### Pin

Function abbreviation
Function description
/
/
Rear position lamp
Rear position lamp positive
Rear turn signal lamp
Rear turn signal lamp positive

### GND

Rear position lamp/rear turn signal lamp
negative
/
/
/
/
Interface definition of combined rear lamp assembly II:
Body electrical appliance
Wiper washer system919

### Pin

Function abbreviation
Function description
/
/
Brake lamp
Brake lamp positive

### GND

Rear position lamp/brake lamp/reverse
lamp negative
Reverse lamp
Reverse lamp positive
Rear fog lamp assembly and reflex reflector

### Pin

Function abbreviation
Function description
Rear fog lamp
Rear fog lamp power supply

### GND

Ground wire
The above is the definition of rear fog lamp interface. If the rear fog lamp cannot be lit, first consider replacing the rear fog lamp bulb. The
bulb model is W16W.
Body electrical appliance
Wiper washer system920
High-mounted brake lamp assembly

### Pin

Function abbreviation
Function description
High-mounted brake lamp
High-mounted brake lamp power supply

### GND

Ground wire
The high-mounted brake lamp is LED.During inspection, if the removed high-mounted brake lamp is connected to
the 13.5 V power supply according to the interface definition and cannot be lit, the whole assembly shall be
considered to be replaced. License plate lamp and switch assembly

### Pin

Function abbreviation
Function description
Trunk switch

### Trunk

switch
power
supply
License plate lamp
License plate lamp power supply

### GND

Ground wire
The license plate lamp power supply is LEDs. If there is a fault, connect the 13.5 V power supply according to the
interface definition after removal. If it cannot be lit, consider replacing the entire license plate lamp assembly. Trunk
lamp

### Pin

Function abbreviation
Function description
Trunk lamp
Trunk lamp power supply

### GND

Ground wire
Body electrical appliance
Wiper washer system921
The bulb model of trunk lamp is W5W. If it is damaged, it is
recommended to replace the bulb first. Interior front dome
lamp
Functional structure
Dome lamp fades on
If the dome lamp is in gear DOOR, it will be illuminated linearly within 1s under any of the following conditions:
Any door is opened (including trunk door);
The ignition switch is in the off state, and press the "unlock" button on the remote controller to unlock the door or use the mechanical
key or central control lock switch or receive the PEPS on the bus.
The "unlock" signal is sent to unlock the door;
The power supply gear changes from
START/ON/ACC to OFF. Dome lamp fade out
If the dome lamp is in gear DOOR, it will extinguish linearly within one under any of the following conditions:
Without central locking, all doors (including trunk door) are closed for 25 seconds. If the DOOR gear switch is turned off within this
time, the dome lamp immediately goes out and then is turned on.
DOOR gear switch, dome lamp is on immediately;
Power supply gear is OFF, all doors (including trunk door) are closed and the door is locked with central locking switch;
When the ignition switch is in the OFF position, all doors (including trunk door) are closed, and then press the "lock" button on the
remote control to lock the door;
The power supply position is in the off position, and the door is locked by receiving the "lock" signal from PEPS on the bus;
All doors are closed and the power supply position is in ON position/START.
Power saving function
The power supply gear is in the OFF state, and the dome lamp switch is in the non-OFF position. If the door is not related, the dome
lamp will go out immediately after 10 minutes delay;
If the ignition key is removed (or the key is not detected), the dome lamp switch is in the ON position, and all
doors are closed, the dome lamp goes out immediately after 10 minutes delay. Non-panoramic roof configuration
Front dome lamps for non-panoramic sunroof configuration include: Sunroof switch, illumination lamp and illumination lamp switch, dual
microphone, USB connector.
If you want to open the sunroof slightly, press the second end of the switch for a short time to stop the sunroof movement after a
short distance.
If you want to close the sunroof slightly, press the switch end I briefly to stop the sunroof movement after a short distance.
Press switch end I and hold it for more than 0.4 seconds. The sunroof will move to full open state. In this case, only part of sunroof
will be opened. Press switch end I or II.
When the sunroof is in a fully closed state, press end I of the switch, and the sunroof will tilt outwards. To
close the sunroof tilt, just press end II of the switch. Panoramic roof configuration
Body electrical appliance
Wiper washer system922
The front dome lamps for the panoramic roof include: Sunroof/sunshade switch, illumination lamp and illumination lamp switch, dual
microphone.
If you want the sunroof to open slightly, press the rear end II of the switch briefly, and the sunroof will stop moving after it starts to
move for a short distance.
If you want to close the sunroof slightly, press the front end II of the switch for a short time to stop the sunroof movement after a
short distance.
Press the rear end II of the switch and keep it for more than 0.4 s, and the sunroof moves to full open state.
When the sunroof is completely closed, press the sunroof switch, and the sunroof will tilt outwards. To close the sunroof tilt, just
press the sunroof switch.
If you want the sunroof sunshade to open slightly, press the rear end I of the switch for a short time to stop the sunroof sunshade
after it starts to move for a short distance.
If you want to close the sunroof slightly, press the front end I of the switch briefly to stop the sunroof movement after a short distance.
Press the rear end I of the sunroof switch and keep it for more than 0.4
s, and the sunroof sunshade will move to full open state. Schematic diagram
and pin definition of PIN
Non-panoramic roof configuration
Pin pin
Function abbreviation
Input/output
Function description
Signal type
Energy-saving power
supply

### Input

Reading lamp power
supply

### Level

\
\
\
\
Button backlight power
supply

### Input

Button backlight power
supply

### Level

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
OPEN(Sunroof open)

### Output

Sunroof opening signal
output(Low efficiency)

### Pulse

Body electrical appliance
Wiper washer system923
CLOSE(Sunroof closed)

### Output

Sunroof close signal
output(Low efficiency)

### Pulse

\
\
\
\

### GND

\
Power ground

### Level


### USB-


### Input

USB ground

### Level


### USB+


### Input

USB electric

### Level

\
\
\
\
\
\
\
\
\
\
\
\

### SKYLIGHT_GND

Sunroof key signal
ground

### Level

\
\
\
\
\
\
\
\
\
\
\
\

### LIGHTING


### Input

To BCM dome lamp
output
\
\
\
\
\
\
\
\
\
\
\
\
\

### B1

Microphone 1
(Passenger) -

### Output

Microphone 1 negative
\

### B2

Microphone 2 (driver) 