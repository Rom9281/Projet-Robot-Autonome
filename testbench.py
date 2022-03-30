import sys

sys.path.append( '../Model' )

import Controller.Robot as Robot

robot = Robot()

robot.moveForward(10)