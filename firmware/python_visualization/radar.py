import serial
import matplotlib.pyplot as plt
import numpy as np

# 🔹 Change COM port if needed
ser = serial.Serial('COM7', 115200, timeout=1)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Radar settings
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_ylim(0, 100)   # Max distance (cm)

while True:
    try:
        line = ser.readline().decode('utf-8').strip()

        if line:
            angle_str, distance_str = line.split(',')

            angle = np.deg2rad(float(angle_str))
            distance = float(distance_str)

            ax.clear()
            ax.set_theta_zero_location("N")
            ax.set_theta_direction(-1)
            ax.set_ylim(0, 100)

            ax.scatter(angle, distance, c='green')

            plt.pause(0.01)

    except:
        pass
