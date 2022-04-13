import sys
import serial
import matplotlib.pyplot as plt
import numpy as np
import random, math

sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

from Controller.Robot import Robot
from rplidar import RPLidar

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
    
    return X,Y

def cleanData(data,min_quality):
    clean_data = []

    for coord in data:

        if coord[0] > min_quality:
            clean_data.append((coord[1],coord[2]))
    
    return clean_data

"""
robot = Robot()

robot.moveForward(10)

robot.turn(90,1)
"""

# ser = serial.Serial("/dev/ttyUSB0",19200)

lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

data = []

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    data.extend(scan)
    if i > 100:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

data = cleanData(data,8)

print(data)

X,Y = polarToCartesian(data)

plt.plot(X, Y)
plt.show()



"""
angle = 120
distance = 11.832*angle + 140.41
#writ = "digo 1:%s:25 2:%s:\r" % (distance,-distance)
writ = "digo 1:%s:25 2:0:0\r" % (distance)
print("Distance = %s"%(distance))
print(ser.write(writ.encode()))
"""

