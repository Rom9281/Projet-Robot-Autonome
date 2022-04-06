import sys
import serial

sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

from Controller.Robot import Robot

robot = Robot()



robot.moveForward(10)


"""
distance = 15000

ser = serial.Serial("/dev/ttyUSB0",19200)

writ = "digo 1:%s:25 2:%s:25\r" % (distance,distance)

print("Distance = %s"%(distance))
print(ser.write(writ.encode()))
"""

