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

sem_start = mp.Semaphore(0)

corps = CorpsRobot(q_com,q_info,sem_start)
intel = IntelligenceRobot(q_com,q_info,sem_start)

corps.start()
intel.start()

print("[*] Corps PID %s"%(corps.pid))
print("[*] Intel PID %s"%(intel.pid))

sem_start.acquire()
sem_start.acquire()

while flag:

    commande = input("[?] Commande : ")

    if(commande == "off"):
        flag = False

        corps.terminate()
        corps.join()

        intel.terminate()
        intel.join()
    

    if(commande[0:2] == "C:"):
        commande = commande[3:]
        q_com.put(commande)


print("ENDED")
exit()

