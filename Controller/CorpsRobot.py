"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import json, time,signal,os
from multiprocessing import Process

# from Model.Serializer import Serializer
from Model.STM import STM
from Model.ServoMoteur import ServoMoteur
from Model.Serializer import Serializer
from Model.LED import LED
from Model.Lidar import Lidar

class CorpsRobot(Process):
    
    def __init__(self,q_com,q_lidar,sem_start):
        super(CorpsRobot, self).__init__()

        # Multiprocessing
        self.__q_com = q_com
        self.__q_lidar = q_lidar
        self.__sem_start = sem_start
        self.__flag = True

        # Configuration des peripheriques direct
        self.__config_periph_path = "/home/pi/Documents/Controller/configPeriph.json"
        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des periphériques dans le json

        # Configuration des commandes
        self.__config_commandes_path = "/home/pi/Documents/Controller/commandes.json"
        self.__com = json.load(open(self.__config_commandes_path)) # récupère la config des periphériques dans le json

        # On configure la carte a laquelle va etre connecte les peripheriques
        self.__stm = STM()
        self.__lidar = Lidar(self.__q_lidar)

        # On ajoute les elements connectés au stm32
        self.__servo_moteur = ServoMoteur(self.__stm)
        self.__serializer = Serializer(self.__stm)
        self.__led = LED(self.__stm)
    
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler) # Definition du signal d'arret

        print("[$] %s:%s : Corps actif"%(os.getppid(),os.getpid())) 

        self.__sem_start.release() # Permet au processus père de commencer

        while self.__flag:

            # Lecture des commandes

            commande = self.__q_com.get(block=True, timeout=None) # La commande n'a aucun timeout
            
            if  (commande == "STOP"):
                self.signal_handler()
                break

            self.gererCommande(commande)

            self.__sem_start.release()

            print(self.__lidar.envoyerMesures())

            # Lecture des données
            # print(self.__lidar.getMeasure())

            time.sleep(0.5)
    
    def gererCommande(self,commande):
        commande = commande.split(":")

        if(commande[0] == self.__com["avancer"]):
            self.__serializer.avancer(commande[1])
            
        elif(commande[0] == self.__com["tourner_droite"]):
            self.__serializer.tournerDroite(commande[1])

        elif(commande[0] == self.__com["tourner_gauche"]):
            self.__serializer.tournerGauche(commande[1])
        
        elif(commande[0] == self.__com["reculer"]):
            self.__serializer.reculer(commande[1])
        
        elif(commande[0] == self.__com["rotation_horizontale"]):
            self.__servo_moteur.mouvementHorizontal(commande[1])
        
        elif(commande[0] == self.__com["rotation_verticale"]):
            self.__servo_moteur.mouvementVertical(commande[1])
        
        elif(commande[0] == self.__com["rot_hor_gauche"]):
            self.__servo_moteur.petitMouvHorGch()
        
        elif(commande[0] == self.__com["rot_hor_droite"]):
            self.__servo_moteur.petitMouvHorDrt()
        
        elif(commande[0] == self.__com["rot_ver_droite"]):
            self.__servo_moteur.petitMouvVerHaut()
        
        elif(commande[0] == self.__com["rot_ver_gauche"]):
            self.__servo_moteur.petitMouvVerBas()
        
        elif(commande[0] == self.__com["tirer"]):
            self.__led.tirer()
        
        else:
            print("Unerconised")
    
    def signal_handler(self):
        print("[*] Process Corps est arrêté")
        self.__flag = False
        self.__sem_start.release()
    
