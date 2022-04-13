
from Peripherique import Peripherique
from abc import ABC, abstractmethod

class Actionneur(Peripherique):
    
    def __init__(self,pin,baude_rate):
        super.__init__(pin,baude_rate)
    
    @abstractmethod
    def actionner(self,commande):
        pass

    