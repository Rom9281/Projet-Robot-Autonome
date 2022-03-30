from abc import ABC, abstractmethod
import serial

class Actionneur(ABC):
    
    def __init__(self,pin,baude_rate):
        self.__pin = pin # Pin auquelle l'actionneur est connecté
        self.__baude_rate = baude_rate # Fréquence de communication
        self.__serial = self.__connect() # Créer l'objet serial si celui-ci est disponile, sinon est indisponible
    
    @abstractmethod
    def actionner(self,commande):
        pass

    def __connect(self):
        ret = False

        try:
            ret = serial.Serial (self.__pin, self.__baude_rate)
        except:
            pass

        return ret