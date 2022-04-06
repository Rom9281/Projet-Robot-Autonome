from Model.Actionneur import Actionneur
from Controller.Commande import Commande
from Controller.Vitesse import Vitesse

class STM(Actionneur):
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)
    

    