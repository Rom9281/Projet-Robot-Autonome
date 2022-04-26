"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import sys, json
from setuptools import Command

from Controller.Vitesse import Vitesse
from Controller.Commande import Commande

import Model.Serializer as Serializer

class CorpsRobot():
    
    def __init__(self):
        
        self.__config_periph_path = "/home/pi/Documents/Controller/configPeriph.json" # Fichier permettant d'indiquer quelle peripheriques sont branches 
        self.__vitesse = Vitesse.RAPIDE # Definit la vitesse initiale comme lente
        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des periphériques dans le json
        
        # CONFIGURATION DES ELEMENTS DU CORPS
        # ___________________________________

        self.__serializer = Serializer.Serializer(
            self.__config_periph["Serializer"]["Pin"],
            self.__config_periph["Serializer"]["Baud"]
            ) # Configure le Serializer comme voulut
        
    """"
    Prend une distance en metre et envois la commande au Serializer
    NOTE : Distance en cm, vitesse comme décrite dans le enum vitesse
    """
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
        
    