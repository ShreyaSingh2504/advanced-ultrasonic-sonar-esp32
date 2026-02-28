# Advanced Ultrasonic Sonar using ESP32

ESP32-based rotating ultrasonic sonar system with real-time radar visualization using Python.

---

## Project Overview

This project implements a radar-like scanning system using an ESP32 microcontroller, an HC-SR04 ultrasonic sensor, and servo motors.

The sensor rotates across angles while measuring distance and sends real-time data to a Python application that visualizes detected objects.

---

## Features

- 180° ultrasonic scanning
- Servo motor controlled radar sweep
- Distance measurement using HC-SR04
- Real-time serial communication
- Python radar visualization

---

## Hardware Setup

firmware/images/4F6E02C3-C62B-4C0A-8007-4D2F450DE14C.JPG

---

## Firmware

Location:

Controls servo motion, reads ultrasonic sensor, and sends angle-distance data via serial.

---

## Python Visualization

Location:

Displays live radar visualization using matplotlib.

---

## How to Run

1. Upload firmware using Arduino IDE (ESP32 Dev Module).
2. Install Python libraries:

3. Run visualization:

---

## License

MIT License
