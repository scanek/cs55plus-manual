# Тормозная система, суппорты и диски

> **Страницы в оригинале:** 786 – 815 | **Модель:** Changan CS55 Plus (2-е поколение / Plus)

## Схемы и иллюстрации раздела

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p786_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p786_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p786_2.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p786_2.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p799_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p799_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p799_2.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p799_2.jpeg" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p800_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p800_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p799_1.png" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p799_1.png" alt="Иллюстрация" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

## Содержание и процедуры

Removal and installation734
Interface definition:

### Hydraulic Control


### Mechanism Assembly

(HCU) System Schematic

### Connector Section

Terminal definition

### Pin


### Function Abbreviation


### Function Description


### KL30_P

EPBi Motor power supply

### MOT_R_A

Rear right caliper motor positive

### MOT_R_B

Rear right caliper motor negative

### FR_GND

Front right wheel speed sensor ground

### FR_SIG


### Right Front Wheel Speed Sensor Signal Input


### RL_GND

Left rear wheel speed sensor ground

### RL_SIG

Rear left wheel speed sensor signal input

### FL_GND

Front left wheel speed sensor ground
Removal and installation735

### FL_SIG

Front left wheel speed sensor signal input

### RR_GND

Rear right wheel speed sensor ground

### RR_SIG

Right rear wheel speed sensor signal input

### MOT_L_B

Left rear caliper motor negative

### MOT_L_A

Left rear caliper motor positive

### GND

EPBi Ground for motors, valves and ECUs

### EPB_SW1

EPB switch wire1

### EPB_SW2

EPB switch wire2

### EPB_SW3

EPB switch wire3

### EPB_SW4

EPB switch wire4

### VEHICLE_SPEED


### Hardwire Speed Output


### EPB_LED

EPB Switch LEDs

### FL_OUT


### Hard Wire Left Front Wheel Speed Output


### KL30_V

EPBi valve and ECU power supply

### IGN

Hardwire ignition

### CAN_H


### Can High


### CAN_L


### Can Low

Common methods
Hydraulic control mechanism assembly (HCU) exhaust
Use the scan tool Fill Exhaust operation to control the EPBi system pump valve action to purge air from the auxiliary oil circuit. These
lines are normally closed and only open during system initialization at vehicle start-up and during ESC operation. “The Refill Exhaust
procedure opens these auxiliary oil paths to allow air trapped in them to flow to the brake cylinder.

::: tip ПРИМЕЧАНИЕ
Note: Before performing the Refill Exhaust procedure, perform the
:::

Exhaust on the conventional brake system first. Note: When any of
the following conditions occur, it is recommended to perform the
"Filling and Exhausting" procedure:

1. Conventional brake system exhaust does not achieve the correct pedal height or pedal feel.

2. The auxiliary oil circuit of the EPBi
system is suspected to be airtight.

::: tip ПРИМЕЧАНИЕ
Note: Make sure the car is parked on
:::

a flat surface.

::: tip ПРИМЕЧАНИЕ
Note: When the ignition switch is in the "LOCK" position and the brake is cold, depress the brake pedal 3~5 times, or until the brake
:::

pedal force increases significantly. The purpose of this operation is to eliminate residual vacuum from the vacuum booster.

::: tip ПРИМЕЧАНИЕ
Note: When venting, the brake fluid reservoir must remain filled with new, clean brake fluid to ensure that the brake fluid level is close to the
:::

MAX-ray position.

1. With the engine off, place the ignition switch in the ON position.

2. Connect the scan tool to the vehicle diagnostic OBD port.

3. Establish communication with the EPBi system system via the scan tool. Select the Fill Exhaust procedure.

4. Lift the car.

5. Follow the scan tool instructions until the correct brake pedal height is reached.

6. If the exhaust procedure aborts abnormally, there is a fault. Read out the DTC and repair it if there is a DTC.

7. If the brake pedal reaches the correct height, depress the pedal and feel the appropriate pedal force. If the brake pedal feels soft, repeat
the exhaust procedure.

8. Lower the vehicle.

9. Remove the scan tool.

10. Road test vehicle. Also check whether the pedal maintains the correct height and proper pedal feel.
Removal and installation736
Fault symptom diagnosis
Inspection and confirmation

1. Confirm the customer's problem.

2. Visually inspect for obvious
mechanical or electrical faults.

### Visual Checklist


### Machinery


### Electrical

Wheel speed sensor, wheel speed sensor ring gear
Fuse, connector, harness

3. Resolve the found issue before proceeding to the next check.

4. If the apparent cause of the observed or raised problem has been found, the cause must be corrected before proceeding to the next step.

5. If the visual inspection passes, confirm the fault and
refer to the fault symptom table. General equipment
Digital multimeter
Diagnostic scanner
Fault phenomenon
diagnosis and test
intermittent fault
diagnosis process
•

::: tip ПРИМЕЧАНИЕ
Note:
:::


1. Clear DTC.

2. Perform simulation tests.

3. Check and swing harness, connectors and terminals
When the fault cannot be confirmed by DTC check, the fault phenomenon only occurs occasionally in use. All circuits and
components that may cause malfunction should be identified at this time. In many cases, by performing the basic checks shown in
the flow chart below, the location of the fault can be quickly and effectively identified, particularly for malfunctioning harness
connectors, etc.
Fault Definition: This fault does not currently occur, but a history DTC record indicates that the fault has occurred. Or the customer
reported the fault, but because the fault is not related to the DTC, the fault symptom cannot be reproduced currently.
Test conditions
Details/Results/Actions

1. Vibration method
If a malfunction or more severe malfunction occurs while driving
on an uneven road, or if the engine is vibrating, go to step 2 or 3.

::: tip ПРИМЕЧАНИЕ
Note: There are several reasons that may cause electrical failure
:::

due to vibration of the car or engine. Check the following:
•
Connector is not fully in place.
•
The harness does not have sufficient clearance.
•
The harness is routed across the bracket or moving parts.
•
The harness is routed too close to the hot parts.

::: tip ПРИМЕЧАНИЕ
Note: Improper wiring, improper clamping, or loose harnesses
:::

can cause the wiring to squeeze between parts.

::: tip ПРИМЕЧАНИЕ
Note: The joints of the connectors, the vibrations, and the
:::

locations where the harnesses pass through are all areas to be
inspected, e.g. the harnesses pass through the firewall and body
panels.

2. Check method of switch connector or wire harness
A. Connect the diagnostic scanner to the diagnostic interface
(OBD).
B. Turn the ignition switch to the ON position (engine not starting).
C. Access the data flow of the switch you are checking.
D. Open the switch manually.
E. While monitoring the data flow, gently shake each connector or
harness vertically and horizontally. If the data flow value is
unstable, check for poor connectivity.
Removal and installation737

3. Check method of sensor connector or wire harness
A. Connect the diagnostic scanner to the diagnostic interface
(OBD).
B. Turn the ignition switch to the ON position (engine off).
C. Access the data flow of the switch you are checking.
D. While monitoring the data flow, gently shake each connector or
harness vertically and horizontally. If the data flow value is
unstable, check for poor connectivity.

4. Inspection Method of Actuator or Relay
A. Connect the diagnostic scanner to the diagnostic interface
(OBD).
B. Ignition switch to "ON" position (engine off).
C. Actively test the actuator or relay you inspected.

5. Test Drive Simulation Fault, Read Data Stream
A. Connect the diagnostic scanner to the diagnostic interface
(OBD).
B. Perform a test drive to simulate a fault while reading the data
stream. If the data flow value is erratic or malfunctioning, repair or
replace the part.
ABS Warning Lamp Keep On Diagnostic Flow
Test conditions
Details/Results/Actions

1. Access the EPBi control module with the diagnostic scanner
A. Check if DTC is output?
? Is repaired according to the output DTC.
? No to step 2.

2. Access the Gateway Control Module with the diagnostic
scanner
A. Check if DTC is output?
? Is repaired according to the output DTC.
? No to step 3.

3. Access the instrument cluster control unit with the diagnostic
scanner
A. Check if DTC is output?
? Is repaired according to the output DTC.
? No to step 4.

4. Replacing instrument cluster control unit
A. Turn the ignition switch to the "LOCK" position and disconn