import sys
import serial

sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

from Controller.Robot import Robot

robot = Robot()

"""
robot.moveForward(10)

robot.turn(90,1)
"""




ser = serial.Serial("/dev/ttyACM0",19200)
print(ser.read())

"""
angle = 120
distance = 11.832*angle + 140.41
#writ = "digo 1:%s:25 2:%s:\r" % (distance,-distance)
writ = "digo 1:%s:25 2:0:0\r" % (distance)
print("Distance = %s"%(distance))
print(ser.write(writ.encode()))
"""

