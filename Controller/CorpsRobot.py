"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import json, time,signal,os
from multiprocessing import Process
from Model.HautParleur import HautParleur

# from Model.Serializer import Serializer
from Model.STM import STM
from Model.ServoMoteur import ServoMoteur
from Model.Serializer import Serializer
from Model.LED import LED
from Model.Lidar import Lidar
from Model.Ultrason import Ultrason

class CorpsRobot(Process):
    
    def __init__(self,queue_com,queue_info,sem_start):
        super(CorpsRobot, self).__init__()

        # Multiprocessing
        self.__queue_com = queue_com
        self.__queue_info = queue_info
        self.__sem_start = sem_start
        self.__flag = True

        # Configuration des périphériques direct
        self.__config_periph_path = "./Controller/configPeriph.json"
        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des périphériques dans le json

        # Configuration des commandes
        self.__config_commandes_path = "./Controller/commandes.json"
        self.commandes = json.load(open(self.__config_commandes_path)) # récupère la config des périphériques dans le json

        # On configure la carte a laquelle va être connecte les périphériques
        self.__stm = STM()
        
        self.__camera = Camera
        self.__lidar = Lidar(self.__queue_info)

        # On ajoute les elements connectés au stm32
        # Initialisation des ServoMoteur
        self.__servo_horizontal = ServoMoteur(self.__stm,0)
        self.__servo_vertical = ServoMoteur(self.__stm,1)

        #Initialisation des Moteurs
        self.__serializer = Serializer(self.__stm)

        # Initialisation de la Led
        self.__led = LED(self.__stm)

        # Initialisation Haut Parleur
        self.__hautParleur = HautParleur(self.__stm)

        # Initialisation des Capteurs Ultrason
        self.__ultrasonAvant = Ultrason(self.__stm, position=0)
        self.__ultrasonArriere = Ultrason(self.__stm, position=1)


    
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler) # Definition du signal d'arret

        print("[$] %s:%s : Corps actif"%(os.getppid(),os.getpid())) 

        self.__sem_start.release() # Permet au processus père de commencer

        while self.__flag:

            # Lecture des commandes

            commande = self.__queue_com.get(block=True, timeout=None) # La commande n'a aucun timeout
            
            if  (commande == "STOP"):
                self.signal_handler()
                break

            self.gererCommande(commande)

            self.__sem_start.release()

            print(self.__lidar.envoyerMesures())

            # Lecture des données
            # print(self.__lidar.getMeasure())

            time.sleep(0.5)

        print("Je suis sorti de la boucle je me termine Corps")
    
    def gererCommande(self, commande):
        commande = commande.split(":")
        
        messageValidation = False
        # déplacements
        if(commande[0] == self.commandes["avancer"]):
            messageValidation = self.__serializer.avancer(commande[1])
            
        elif(commande[0] == self.commandes["tourner_droite"]):
            messageValidation = self.__serializer.tournerDroite(commande[1])

        elif(commande[0] == self.commandes["tourner_gauche"]):
            messageValidation = self.__serializer.tournerGauche(commande[1])
        
        elif(commande[0] == self.commandes["reculer"]):
            messageValidation = self.__serializer.reculer(commande[1])
        

        # rotation tourelle
        elif(commande[0] == self.commandes["rotation_horizontale"]):
            messageValidation = self.__servo_horizontal.rotation(commande[1])
        
        elif(commande[0] == self.commandes["rotation_verticale"]):
           messageValidation =  self.__servo_vertical.rotation(commande[1])
        
        elif(commande[0] == self.commandes["rot_hor_gauche"]):
            messageValidation = self.__servo_horizontal.petiteRotationAjout()
        
        elif(commande[0] == self.commandes["rot_hor_droite"]):
            messageValidation = self.__servo_horizontal.petiteRotationRetire()
        
        elif(commande[0] == self.commandes["rot_ver_droite"]):
            messageValidation = self.__servo_vertical.petiteRotationAjout()
        
        elif(commande[0] == self.commandes["rot_ver_gauche"]):
            messageValidation = self.__servo_vertical.petiteRotationRetire()
        

        # Commandes de la led
        elif(commande[0] == self.commandes["tirer"]):
            messageValidation = self.__led.tirer()
        
        elif(commande[0] == self.commandes["allumerLampe"]):
            messageValidation = self.__led.allumer()
        
        elif(commande[0] == self.commandes["eteindreLampe"]):
            messageValidation = self.__led.eteindre()
        

        # Commande haut parleur
        elif(commande[0] == self.commandes["klaxon"]):
            messageValidation = self.__hautParleur.klaxon()
        
        
        # Commandes ultrason
        elif(commande[0] == self.commandes["mesureUltrasonAv"]):
            messageValidation = self.__ultrasonAvant.recupererDistance()
            if messageValidation:
                distance = self.__ultrasonAvant.distance
        
        elif(commande[0] == self.commandes["mesureUltrasonAr"]):
            messageValidation = self.__ultrasonArriere.recupererDistance()
            if messageValidation:
                distance = self.__ultrasonArriere.distance

         
        else:
            print("Unerconised")

        self.__queue_info.put(messageValidation)

        if ( ( commande[0] == self.commandes["mesureUltrasonAv"] or  
            commande[0] == self.commandes["mesureUltrasonAr"] ) and 
            messageValidation ):
            self.__queue_info.put(distance)
    

    def signal_handler(self):
        print("[*] Process Corps est arrêté")
        self.__flag = False
        self.__sem_start.release()
    
