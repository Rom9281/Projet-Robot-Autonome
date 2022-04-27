"""_summary_

CPE Lyon - 2022

Projet Transversal

Groupe B1

Romain GAUD

Description: Classe modelisant l'ensemble du robot, possedant une intelligence et un corps

"""
import time,os
import multiprocessing as mp
from multiprocessing import Process

from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot

class Robot(Process):
    def __init__(self,corps,intel):

        super(Robot, self).__init__()

        # Process related
        self.__flag = True

        self.__corps = corps
        print("[$] Corps generé")
        self.__intel = intel
        print("[$] Intelligence generé")

        print("[$] Process prêt")

    def run(self):
        while self.__flag:
            time.sleep(1)
            print("[$] %s:%s Robot actif"%(os.getppid(),os.getpid()))

    
        


    
            
    
        
    
