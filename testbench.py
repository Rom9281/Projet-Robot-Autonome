import sys
import serial
import matplotlib.pyplot as plt
import numpy as np
import random, math, time

sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

from Controller.Robot import Robot
from rplidar import RPLidar

robot = Robot()

"""
def polarToCartesian(data):
    X = []
    Y = []
    Theta= []
    R = []


    for coord in data:
        X.append(coord[1]*math.cos(np.radians(coord[0])))
        Y.append( coord[1]*math.sin(np.radians(coord[0])))
        Theta.append(coord[0])
        R.append(coord[1])
    
    return X,Y,Theta,R

def cleanData(data,min_quality):
    clean_data = []

    for coord in data:

        if coord[0] > min_quality:
            clean_data.append((coord[1],coord[2]))
    
    return clean_data

def reax(ax):
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

#robot.moveForward(10)
# robot.turn(90,1)

lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

# Pyplot interactive mode : 
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)


for i, scan in enumerate(lidar.iter_scans()):
    #print('%d: Got %d measurments' % (i, len(scan)))

    if(len(scan)>200):
        data = cleanData(scan,13)
        X,Y,Theta,R = polarToCartesian(data)

        ax1.clear()
        ax2.clear()

        reax(ax1)

        ax1.plot(X, Y, 'b-')
        ax2.plot(Theta, R, 'r-')
        fig.canvas.draw()
        fig.canvas.flush_events()
        #time.sleep(0.4)

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

data = cleanData(data,13)

X,Y = polarToCartesian(data)

plt.plot(X, Y)
plt.show()

---------------------------------------------------------
ser = serial.Serial("/dev/ttyUSB0",19200)
angle = 120
distance = 11.832*angle + 140.41
#writ = "digo 1:%s:25 2:%s:\r" % (distance,-distance)
writ = "digo 1:%s:25 2:0:0\r" % (distance)
print("Distance = %s"%(distance))
print(ser.write(writ.encode()))
"""

