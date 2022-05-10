"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import json, time,signal,os
from multiprocessing import Process

from Controller.Enums import Vitesse, Commande

# from Model.Serializer import Serializer
from Model.STM import STM
from Model.Lidar import Lidar
from Model.ServoMoteur import ServoMoteur
from Model.Serializer import Serializer
from Model.LED import LED

class CorpsRobot(Process):
    
    def __init__(self,q_com,q_info,sem_start):
        super(CorpsRobot, self).__init__()

        # Multiprocessing
        self.__q_com = q_com
        self.__q_info = q_info
        self.__sem_start = sem_start
        self.__flag = True

        # Configuration des peripheriques direct
        self.__config_periph_path = "/home/pi/Documents/Controller/configPeriph.json"
        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des periphériques dans le json

        # On configure la carte a laquelle va etre connecte les peripheriques
        self.__stm = STM(
            self.__config_periph["STM32"]["Pin"],
            self.__config_periph["STM32"]["Baud"]
            )
        

        # On ajoute un lidar directement connecté au raspberry
        self.__lidar = Lidar(
            self.__config_periph["Lidar"]["Pin"],
            self.__config_periph["Lidar"]["Baud"]
        )
        
        # On ajoute les elements connectés au stm32
        self.__servo_moteur = ServoMoteur(self.__stm)
        self.__serializer = Serializer(self.__stm)
        self.__led = LED(self.__stm)


        """
        self.__serializer = Serializer(
            self.__config_periph["Serializer"]["Pin"],
            self.__config_periph["Serializer"]["Baud"]) # Configure le Serializer comme voulut
        """
    
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler) # Definition du signal d'arret

        print("[$] %s:%s : Corps actif"%(os.getppid(),os.getpid())) 

        self.__sem_start.release() # Permet au processus père de commencer

        while self.__flag:
            commande = self.__q_com.get(block=True, timeout=None)
            # La commande n'a aucun timeout

            #print("Commande = %s"%(commande,))

            self.gererCommande(commande)

            self.__sem_start.release()
    
    def gererCommande(self,commande):
        commande = commande.split(":")

        if(commande[0] == Commande.AVANCER):
            self.__serializer.avancer(commande[1])
            
        elif(commande[0] == Commande.TOURDROIT):
            self.__serializer.tournerDroite(commande[1])

        elif(commande[0] == Commande.TOURGAUCHE):
            self.__serializer.tournerGauche(commande[1])
        
        elif(commande[0] == Commande.RECULER):
            self.__serializer.reculer(commande[1])
        
        elif(commande[0] == Commande.ROTHORIZON):
            self.__servo_moteur.mouvementHorizontal(commande[1])
        
        elif(commande[0] == Commande.ROTVERTICAL):
            self.__servo_moteur.mouvementVertical(commande[1])
        
        elif(commande[0] == Commande.ROTHORGCH):
            self.__servo_moteur.petitMouvHorGch()
        
        elif(commande[0] == Commande.ROTHORDRT):
            self.__servo_moteur.petitMouvHorDrt()
        
        elif(commande[0] == Commande.ROTVERDRT):
            self.__servo_moteur.petitMouvVerDrt()
        
        elif(commande[0] == Commande.ROTVERGCH):
            self.__servo_moteur.petitMouvVerGch()
        
        elif(commande[0] == Commande.TIRER):
            self.__led.tirer()
        
        else:
            print("Unerconised")

            
    
    def signal_handler(self,signum,frame):
        print("[*] Process Corps est arrêté")
        self.__flag = False
    


    """"
    Prend une distance en metre et envois la commande au Serializer
    NOTE : Distance en cm, vitesse comme décrite dans le enum vitesse
    
    def moveForward(self,distance):
        self.__serializer.actionner(
            {
                "commande":Commande.AVANCER,
                "param": {
                    "vitesse":self.__vitesse,
                    "distance":distance
                }
            }
        )
    
    @PARAM:
     - coté : enum Sens
     - Angle en degré
    
    def turn(self,sens,angle):
        self.__serializer.actionner(
            {
                "commande":Commande.TOURNER,
                "param": {
                    "vitesse":self.__vitesse,
                    "angle":angle,
                    "sens":sens,
                }
            }
        )
    """
        

