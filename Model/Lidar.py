from rplidar import RPLidar
from Capteur import Capteur

class Lidar(Capteur):
    def __init__(self, pin, baude_rate):
        super().__init__(pin, baude_rate)
    
    def __connect(self):
        return super().__connect()