"""
Programme de lancement principal du robot,
Agis pour le moment également comme l'interface graphique avec l'utilisateur
"""
from ast import Import
import multiprocessing as mp, keyboard,sys, json

#sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
#sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
#sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

sys.path.append(r'~/.local/lib/python3.7/site-packages' )

# Bibliothèques personelles
from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot

# Recuperation des commandes dans le path
config_commandes_path = "/home/pi/Documents/Controller/commandes.json"
commandes = json.load(open(config_commandes_path)) # récupère la config des periphériques dans le json

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

try:
    while flag: # Tant qu'aucun signal d'arret n'est actif
    

        if keyboard.is_pressed("i"):
            print("[$] INTERRUPTION : ending all processes")
            q_com.put("STOP")
            flag = False
            break
        
        if keyboard.is_pressed("z"):
            q_com.put(f"{commandes['avancer']}:2")
            sem_start.acquire()
            
        elif  keyboard.is_pressed("q"):
            q_com.put(f"{commandes['tourner_gauche']}:2")
            sem_start.acquire()

        elif  keyboard.is_pressed("s"):
            q_com.put(f"{commandes['reculer']}:2")
            sem_start.acquire()

        elif  keyboard.is_pressed("d"):
            q_com.put(f"{commandes['tourner_droite']}:2")
            sem_start.acquire()

        # # visé plus tire
        elif  keyboard.is_pressed("k"):
            q_com.put(commandes["tourner_gauche"])
            sem_start.acquire()

        elif  keyboard.is_pressed("m"):
            q_com.put(commandes["rot_hor_droite"])
            sem_start.acquire()

        elif  keyboard.is_pressed("o"):
            q_com.put(commandes["rot_ver_droite"])
            sem_start.acquire()
        
        elif  keyboard.is_pressed("l"):
            q_com.put(commandes["rot_ver_gauche"])
            sem_start.acquire()
        
        elif  keyboard.is_pressed("k"):
            q_com.put(commandes["rot_hor_gauche"])
            sem_start.acquire()
        
        elif  keyboard.is_pressed("t"):
            q_com.put(commandes["tirer"])
            sem_start.acquire()
        
        


except ImportError as e:
    print(f"[$] {e} : veuillez être root pour lancer le programme")

# corps.terminate()
intel.terminate()

corps.join()
intel.join()
print("ENDED")


