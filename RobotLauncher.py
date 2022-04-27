import multiprocessing as mp

import sys
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

from Controller.Robot import Robot
from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot


q_com = mp.Queue() # queue contenant les commandes
q_info = mp.Queue() # queue contenant les informations

corps = CorpsRobot(q_com,q_info)
intel = IntelligenceRobot(q_com,q_info)
robot = Robot(corps,intel)

print("PID CORPS : ")

robot.start()
corps.start()
intel.start()
print("PID")
intel.join()
corps.join()
robot.join()