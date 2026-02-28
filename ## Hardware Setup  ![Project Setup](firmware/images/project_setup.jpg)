# Advanced Ultrasonic Sonar using ESP32

ESP32-based rotating ultrasonic sonar system with real-time radar visualization using Python.

---

## 📌 Project Overview

This project implements a radar-like scanning system using an ESP32 microcontroller, an HC-SR04 ultrasonic sensor, and servo motors.  
The sensor rotates across angles while measuring distance and sends real-time data to a Python application that visualizes detected objects.

The system demonstrates embedded systems programming, sensor interfacing, serial communication, and real-time visualization.

---

## 🧠 Features

- 180° ultrasonic scanning
- Servo motor controlled radar sweep
- Distance measurement using HC-SR04
- Real-time serial data transmission
- Python radar visualization
- ESP32 embedded firmware

---

## 🛠 Hardware Used

- ESP32 Development Board
- HC-SR04 Ultrasonic Sensor
- SG90 Servo Motor (2-axis mount)
- Breadboard & jumper wires
- USB power supply

---

## 📷 Hardware Setup

### Front View
![Front Setup](images/setup_front.jpg)

### Side View
![Side Setup](images/setup_side.jpg)

### ESP32 Wiring
![ESP32 Wiring](images/esp32_wiring.jpg)

---

## ⚙️ Firmware

Location:

Responsibilities:
- Controls servo sweep
- Triggers ultrasonic sensor
- Calculates distance
- Sends angle & distance via Serial

---

## 🖥 Python Visualization

Location:

Responsibilities:
- Reads serial data from ESP32
- Converts angle data to polar coordinates
- Displays live radar visualization

---

## ▶️ How to Run

### 1️⃣ Upload Firmware
- Open Arduino IDE
- Select **ESP32 Dev Module**
- Upload `firmware/sonar_scan.ino`

### 2️⃣ Install Python Libraries

### 3️⃣ Run Radar Visualization

---

## 📡 Working Principle

1. Servo rotates ultrasonic sensor from 0° to 180°.
2. Sensor measures distance using time-of-flight calculation.
3. ESP32 sends `(angle, distance)` via serial communication.
4. Python script plots data as radar visualization.

Distance formula:

---

## 🚀 Future Improvements

- WiFi-based data transmission
- Object tracking algorithm
- STM32 implementation
- ROS integration for robotics

---

## 📄 License

This project is licensed under the MIT License.

