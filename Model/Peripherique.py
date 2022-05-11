from abc import ABC, abstractmethod
import serial

class Peripherique(ABC):

    def __init__(self,pin,baude_rate):
            self._pin = pin # Pin auquelle l'actionneur est connecté
            self._baude_rate = baude_rate # Fréquence de communication
            self._serial = self._connect() # Créer l'objet serial si celui-ci est disponile, sinon est indisponible


    def _connect(self):
            ret = False

            try:
                ret = serial.Serial(self._pin, self._baude_rate)
            except:
               print("[$] Failed to connect to the serial")


            return ret