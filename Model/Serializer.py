from unittest import case
from Model.Actionneur import Actionneur

class Serializer(Actionneur):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    """
    A besoin de savoir:
    {
        commande: "nom commande"
        parametres: [
            liste param...
        ]
        
    }
    """
    def actionner(self,commande):
        if self.__serial:
            if(commande["commande"]==1):
                self.__avancer(commande["param"])
            elif(commande["commande"]==2):
                pass
    
    def __avancer(self, param):
        vitesse = param["vitesse"]
        distance = param["distance"]*0.393701 # Passage de la mesure en inch

        str_command = "digo 1:%s:%s" %(distance,vitesse)
        str_command += " 2:%s:%s" %(distance,vitesse)
        self.__sendCommand(self,str_command)


    def __sendCommand(self,str_command):
        self.__serial.write(str_command) 