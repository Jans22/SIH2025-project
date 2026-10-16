# Smart Pesticide Sprayer — PCB Design

## Overview
This folder contains the PCB design developed for our Smart Pesticide Sprayer project as part of Smart India Hackathon (SIH) 2025 by Team TheVisioneers.

The PCB was designed in EasyEDA to organize the power connections and embedded control interfaces for the sprayer system.

## Design Features
- Raspberry Pi GPIO interface
- L298N motor-driver control interface for carriage movement
- MOSFET-based switching circuits for the pump and solenoid valve
- 12V power input and external buck-converter interfaces
- Dedicated connectors for the carriage motor, pump, solenoid valve, and servo
- Schematic capture, component placement, and PCB routing in EasyEDA

## PCB Preview
![PCB 3D View](3D_Views/pcb_3d_view.png)

## Schematic
![Circuit Schematic](Schematic/schematic.png)

## PCB Layout
![Routed PCB Layout](PCB_Layout/pcb_top_layout.png)

## Tools Used
- EasyEDA
- PCB design and routing

## Project Status
**Educational design — not fabricated or electrically tested.**

The design is shared for documentation and learning purposes. Design-rule checks do not establish electrical validation.

## Folder Contents
- `Schematic/` — schematic files and images
- `PCB_Layout/` — PCB layout files and images
- `3D_Views/` — 3D board previews
- `Reports/` — DRC results and design notes
