# Wiring and Electrical Connections

## 1. DC Motor and L298N
The carriage movement is controlled using a 12 V DC motor and an L298N motor driver.

### L298N to Arduino

| L298N Pin | Arduino Connection |

| IN1 | D8 |
| IN2 | D9 |
| ENA | D10 |
| GND | Arduino GND |

### Motor Connections

| L298N | Motor |

| OUT1 | Motor Terminal A |
| OUT2 | Motor Terminal B |

### Power Connections

| Component | Connection |
|---|---|
| L298N 12 V | +12 V power supply |
| L298N GND | Power supply negative |
| Arduino GND | Common ground |
| Motor | L298N OUT1 / OUT2 |

The Arduino, L298N and external power supply share a common ground.

## 2. Pump Driver Circuit

The 12 V diaphragm pump is controlled using a 2N2222A transistor.


Pump (+)
   |
 +12 V
