"""
CPE Lyon 

Projet Transversal

Groupe B1

Fares Zaghouane
"""
from Model.PeripheriqueCarte import PeripheriqueCarte
from Model.Carte import Carte

class LED(PeripheriqueCarte):
    
    def __init__(self,carte: Carte)-> None:
        super().__init__(carte,"TIRLMP", 0 , 0 )
        self.etat = 0
    
    def tirer(self)-> bool:
        valideAction = False
        self._arg1 = 2
        self._carte.ecrireCommand(self.creerCommande())
        valideAction = self.validationCommande()

        return valideAction

    def eteindre(self)-> bool:
        valideAction = False
        self._arg1 = 0        
        self.__carte.ecrireCommande(self.creerCommande())

        valideAction = self.validationCommande()
        if (valideAction):
            self.etat = 0

        return valideAction

    def allumer(self)-> bool:
        self._arg1 = 1
        self.__carte.ecrireCommande(self.creerCommande())

        valideAction = self.validationCommande()
        if (valideAction):
            self.etat = 1

        return valideAction



    

    
