from operator import le
from Model.PeripheriqueCarte import PeripheriqueCarte
from Model.Carte import Carte

class LED(PeripheriqueCarte):
    
    def __init__(self,carte: Carte):
        super().__init__(carte,"TIRLMP", 0 , 0 )
        self.etat = 0
    
    def tirer(self):
        self._carte.ecrireCommand(self._creerCommande())

    def allumer(self):
        self.etat = 1
        self.__carte.ecrireCommande(self._creerCommande())

    def allumer(self):
        self.etat = 1
        self.__carte.ecrireCommande(self._creerCommande())


if __name__ == "__main__":

    testLed = LED(carte = Carte())
    

    
