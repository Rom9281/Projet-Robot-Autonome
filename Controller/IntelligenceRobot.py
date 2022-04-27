import os, time, signal
from multiprocessing import Process

class IntelligenceRobot(Process):
    
    def __init__(self,q_com,q_info):

        super(IntelligenceRobot, self).__init__()

        self.__q_com = q_com
        self.__q_info = q_info
        self.__flag = True

        signal.signal(signal.SIGTERM, self.__signal_handler)
    
    def run(self):
        print("[$] %s:%s : Intelligence active"%(os.getppid(),os.getpid()))
        while self.__flag:
            time.sleep(1)
    
    def __signal_handler(self,signum,frame):
        print("[*] Process Intelligence est arrêté")
        self.__flag = False
        

