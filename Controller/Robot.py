"""_summary_

CPE Lyon - 2022

Projet Transversal

Groupe B1

Romain GAUD

Description: Classe modelisant l'ensemble du robot, possedant une intelligence et un corps

"""
from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot

class Robot():
    def __init__(self):
        self.__corps = CorpsRobot()
        self.__intelligence = IntelligenceRobot()
        