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
    def __init__(self):

        super(Robot, self).__init__()

        # Process related
        self.q_com = mp.Queue() # queue contenant les commandes
        self.q_info = mp.Queue() # queue contenant les informations
        self.__flag = True



        self.__corps = CorpsRobot(self.q_com,self.q_info)
        print("[$] Corps generé")
        self.__intel = IntelligenceRobot(self.q_com,self.q_info)
        print("[$] Intelligence generé")

        print("[$] Process prêt")

    def run(self):
        self.__corps.start()
        self.__intel.start()

        self.__task()

        self.__intel.join()
        self.__corps.join()
    
    def __task(self):
        while self.__flag:
            time.sleep(1)
            print("[$] %s:%s Robot actif"%(os.getppid(),os.getpid()))

    
        


    
            
    
        
    
