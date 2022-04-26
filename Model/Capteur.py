from abc import ABC, abstractmethod

class Capteur():
    
    @abstractmethod
    def recupererMesure(self):
        pass

