# Software

This directory contains the software developed for the hardware prototype.

## Structure

```text
software/
├── arduino/
│   ├── motor_control/
│   └── pump_control/
│
└── raspberry_pi/
    └── scan_controller/


## Arduino

The Arduino handles low-level hardware control including:

DC motor control through the L298N driver
Pump switching and spray-duration control
Raspberry Pi

The Raspberry Pi software handles:

Camera control
Image acquisition
Servo positioning
Scan-cycle control
Image processing integration

Only software developed or directly used for the documented prototype is included in this repository.
