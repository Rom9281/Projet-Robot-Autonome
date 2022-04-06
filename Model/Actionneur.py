from abc import ABC, abstractmethod
import serial

class Actionneur(ABC):
    
    def __init__(self,pin,baude_rate):
        self._pin = pin # Pin auquelle l'actionneur est connecté
        self._baude_rate = baude_rate # Fréquence de communication
        self._serial = self.__connect() # Créer l'objet serial si celui-ci est disponile, sinon est indisponible
        print(self._serial)
    
    @abstractmethod
    def actionner(self,commande):
        pass

    def __connect(self):
        ret = False

        try:
            ret = serial.Serial(self._pin, self._baude_rate)
        except:
            pass

        return ret