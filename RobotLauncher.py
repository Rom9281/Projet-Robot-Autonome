import multiprocessing as mp,signal,os, keyboard
from Controller.Enums import Commande

import sys,time
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )
sys.path.append(r'~/.local/lib/python3.7/site-packages' )

from Controller.Robot import Robot
from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot

flag = True
q_com = mp.Queue() # queue contenant les commandes
q_info = mp.Queue() # queue contenant les informations

sem_start = mp.Semaphore(0)

corps = CorpsRobot(q_com,q_info,sem_start)
intel = IntelligenceRobot(q_com,q_info,sem_start)

corps.start() # Commence le processus corps
intel.start() # idem intelligence

print("[*] Corps PID %s"%(corps.pid))
print("[*] Intel PID %s"%(intel.pid))

# Attend l'initialisation des deux autres processus avant de passer des commandes
sem_start.acquire()
sem_start.acquire()

while flag: # Tant qu'aucun signal d'arret n'est actif

    if keyboard.is_pressed(" "):
        print("letsgo")

    if keyboard.is_pressed("f"):
        print("ok")
        flag = False

        corps.terminate()
        corps.join()

        intel.terminate()
        intel.join()
    
    if keyboard.is_pressed("z"):
        q_com.put(str(Commande.AVANCER)+":"+str(2))
        sem_start.acquire()

    elif  keyboard.is_pressed("q"):
        q_com.put(Commande.TOURGAUCHE+":"+2)
        sem_start.acquire()

    elif  keyboard.is_pressed("s"):
        q_com.put(Commande.RECULER+":"+2)
        sem_start.acquire()

    elif  keyboard.is_pressed("d"):
        q_com.put(Commande.TOURDROIT+":"+2)
        sem_start.acquire()

     # # visé plus tire
    elif  keyboard.is_pressed("k"):
        q_com.put(Commande.ROTHORGCH)
        sem_start.acquire()
    
    elif  keyboard.is_pressed("m"):
        q_com.put(Commande.ROTHORDRT)
        sem_start.acquire()

    elif  keyboard.is_pressed("o"):
        q_com.put(Commande.ROTVERDRT)
        sem_start.acquire()
    
    elif  keyboard.is_pressed("l"):
        q_com.put(Commande.ROTVERGCH)
        sem_start.acquire()
    
    elif  keyboard.is_pressed("t"):
        q_com.put(Commande.TIRER+":0")
        sem_start.acquire()

print("ENDED")
exit()

