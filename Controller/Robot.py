"""_summary_

CPE Lyon - 2022

Projet Transversal

Groupe B1

Romain GAUD

Description: Classe modelisant l'ensemble du robot, possedant une intelligence et un corps

"""
import time,os, signal
import multiprocessing as mp
from multiprocessing import Process

from Controller.CorpsRobot import CorpsRobot
from Controller.IntelligenceRobot import IntelligenceRobot

class Robot(Process):
    def __init__(self,corps_pid,intel_pid):

        super(Robot, self).__init__()

        # Process related

        self.__flag = True
        self.__pid_corps = corps_pid
        self.__pid_intel = intel_pid

        print("[$] Process prêt")

    def run(self):
        while self.__flag:
            #print("[$] %s:%s Robot actif"%(os.getppid(),os.getpid()))
            pass
            """
            try:
                commande = input("[?] Commande : ")

                if(commande == "off"):
                    os.kill(self.__pid_corps, signal.SIGTERM)
                    os.kill(self.__pid_intel, signal.SIGTERM)
                    self.terminate()
            
            except:
                print("Error")
            """
        

    
        


    
            
    
        
    
