import multiprocessing as mp,signal,os

import sys,time
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

from Controller.Robot import Robot
from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot

flag = True
q_com = mp.Queue() # queue contenant les commandes
q_info = mp.Queue() # queue contenant les informations

corps = CorpsRobot(q_com,q_info)
intel = IntelligenceRobot(q_com,q_info)

corps.start()
intel.start()

print("[*] Corps PID %s"%(corps.pid))
print("[*] Intel PID %s"%(intel.pid))

#robot = Robot(corps.pid,intel.pid)
#robot.start()

time.sleep(1)

while flag:

    commande = input("[?] Commande : ")

    if(commande == "off"):
        flag = False
        os.kill(corps.pid, signal.SIGTERM)
        os.kill(intel.pid, signal.SIGTERM)
        


# robot.join()
intel.join()
corps.join()
print("ENDED")
os.exit()

