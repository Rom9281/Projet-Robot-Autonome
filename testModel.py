
import time

from Controller.Camera import Camera
from Controller.CorpsRobot import CorpsRobot
from Controller.IntelRobot import IntelligenceRobot
from Model.Lidar import Lidar
import rplidar
import multiprocessing as mp

if __name__ == "__main__":

    queue_commande = mp.Queue() # queue contenant les commandes
    queue_info = mp.Queue() # queue contenant les informations retournées

    sem_start = mp.Semaphore(0)

    testCamera = CorpsRobot(queue_commande, queue_info, sem_start)
    testCamera.run()