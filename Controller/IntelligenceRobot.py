import os, time
from multiprocessing import Process

class IntelligenceRobot(Process):
    
    def __init__(self,q_com,q_info):

        super(IntelligenceRobot, self).__init__()

        self.__q_com = q_com
        self.__q_info = q_info
        self.__flag = True
    
    def run(self):
        while self.__flag:
            time.sleep(1)
            print("[$] %s:%s : Intelligence active"%(os.getppid(),os.getpid()))
        

