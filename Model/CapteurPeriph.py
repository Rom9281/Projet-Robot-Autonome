from Model.Peripherique import Peripherique
from Model.Capteur import Capteur

class CapteurPeriph(Peripherique,Capteur):
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)