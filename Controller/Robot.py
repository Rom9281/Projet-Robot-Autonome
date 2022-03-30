"""
Projet Transversal

Groupe B1

Créateur: Romain GAUD
Contributeur : 

Description :  Modélisation du robot en entier
"""

import sys, json
from setuptools import Command

print(sys.path)

from Controller.Vitesse import Vitesse
from Controller.Commande import Commande

import Model.Serializer as Serializer

class Robot():
    def __init__(self):
        self.__config_periph_path = r"C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller\configPeriph.json"
        
        self.__vitesse = Vitesse.MOYENNE # Definit la vitesse initiale comme lente

        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des periphériques dans le json

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
                "commande":Commande.AVANCER,
                "param": {
                    "vitesse":self.__vitesse,
                    "distance":distance
                }
            }
        )
        
    