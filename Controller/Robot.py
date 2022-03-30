"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import sys, json
from setuptools import Command
import Vitesse, Commande

sys.path.append( '../Model' )

import Model.Serializer as Serializer

class Robot():
    def __init__(self):
        self.__vitesse = Vitesse['moyenne'] # Definit la vitesse initiale comme lente

        self.__config_periph = json.load(open("configPeriph.json")) # récupère la config des periphériques dans le json

        self.__serializer = Serializer(
            self.__config_periph["Pin"],
            self.__config_periph["Baud"]) # Configure le Serializer comme voulut
        
    """"
    Prend une distance en metre et envois la commande au Serializer
    NOTE : Distance en cm, vitesse comme décrite dans le enum vitesse
    """
    def moveForward(self,distance):
        self.__serializer.actionner(
            {
                "commande":Commande['avancer'],
                "param": {
                    "vitesse":self.__vitesse,
                    "distance":distance
                }
            }
        )
        
    