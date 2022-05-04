import os, time, signal
from multiprocessing import Process

class IntelligenceRobot(Process):
    
    def __init__(self,q_com,q_info,sem_start):
        super(IntelligenceRobot, self).__init__()

        self.__q_com = q_com
        self.__q_info = q_info
        self.__sem_start = sem_start
        self.__flag = True

        
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler)

        print("[$] %s:%s : Process Intelligence actif"%(os.getppid(),os.getpid()))

        self.__sem_start.release()
        
        while self.__flag:
            time.sleep(1)
    
    def signal_handler(self,signum,frame):
        print("[*] Process Intelligence est arrêté")
        self.__flag = False
        

