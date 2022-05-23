import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar
import math, time

from sympy import li

def get_data():
    # lidar = RPLidar('COM8', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=1000):
        break
    lidar.stop()
    return scan

i = 0
lidar = RPLidar('COM8', baudrate=115200)


while True:

    if (i % 5 == 0):
        x = []
        y = []
    current_data=get_data()

    for point in current_data:
        if point[0]==15:
            x.append(point[2]*np.sin(np.radians(point[1])))
            y.append(point[2]*np.cos(np.radians(point[1])))
    plt.clf()
    plt.scatter(x, y, s=0.5, c="limegreen")
    plt.pause(.1)
    i += 1


line1.set_ydata(np.cos(2 * np.pi * (x1+i*3.14/2) ) * np.exp(-x1) )

