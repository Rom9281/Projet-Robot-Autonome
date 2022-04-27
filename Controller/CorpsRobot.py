"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import json, time,signal,os
from multiprocessing import Process

from Controller.Enums import Vitesse, Commande,Sens

# from Model.Serializer import Serializer
from Model.STM import STM
from Model.Lidar import Lidar
from Model.ServoMoteur import ServoMoteur
from Model.Serializer import Serializer

class CorpsRobot(Process):
    
    def __init__(self,q_com,q_info):

        super(CorpsRobot, self).__init__()

        # Multiprocessing
        self.__q_com = q_com
        self.__q_info = q_info
        self.__flag = True
        signal.signal(signal.SIGTERM, self.__signal_handler)

        # Configuration des peripheriques direct
        self.__config_periph_path = "/home/pi/Documents/Controller/configPeriph.json"
        self.__vitesse = Vitesse.RAPIDE # Definit la vitesse initiale comme lente
        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des periphériques dans le json

        self.__stm = STM(
            self.__config_periph["STM32"]["Pin"],
            self.__config_periph["STM32"]["Baud"])

        self.__lidar = Lidar(
            self.__config_periph["Lidar"]["Pin"],
            self.__config_periph["Lidar"]["Baud"]
        )

        self.__servo_moteur = ServoMoteur(self.__stm)
        self.__serializer = Serializer(self.__stm)

        """
        self.__serializer = Serializer(
            self.__config_periph["Serializer"]["Pin"],
            self.__config_periph["Serializer"]["Baud"]) # Configure le Serializer comme voulut
        """
    
    def run(self):
        print("[$] %s:%s : Corps actif"%(os.getppid(),os.getpid()))
        while self.__flag:
            self.__serializer.avancer(10)
            self.__servo_moteur.mouvementHorizontal(90)
            time.sleep(2)
            
    
    def __signal_handler(self,signum, frame):
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
        

