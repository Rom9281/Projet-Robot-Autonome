from abc import ABC, abstractmethod
import serial, json

class Peripherique(ABC):

    def __init__(self,pin,baude_rate):
        self.__name = self.__class__.__name__

        # Configuration des peripheriques direct
        self.__config_periph_path = "/home/pi/Documents/Controller/configPeriph.json"
        self.__config_periph = json.load(open(self.__config_periph_path)) # récupère la config des periphériques dans le json
        
        # Configuration des pins
        self._pin = self.__config_periph[self.__name]["Pin"] # Pin auquelle l'actionneur est connecté
        self._baude_rate = self.__config_periph[self.__name]["Baud"] # Fréquence de communication
        
        # Connection au dispositif
        self._serial = self._connect() # Créer l'objet serial si celui-ci est disponile, sinon est indisponible

    """
    Methode general de connection au dispositif
    Peut etre modifiée par les enfants
    """    
    def _connect(self):
            ret = False

            try:
                ret = serial.Serial(self._pin, self._baude_rate)
            except:
               print("[$] Failed to connect to the serial")


            return ret