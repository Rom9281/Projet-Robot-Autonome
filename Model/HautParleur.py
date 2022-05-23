"""
CPE Lyon 

Projet Transversal

Groupe B1

Fares Zaghouane
"""
from Model.PeripheriqueCarte import PeripheriqueCarte
from Model.Carte import Carte

class HautParleur(PeripheriqueCarte):
    
    def __init__(self,carte: Carte)-> None:
        super().__init__(carte,"HAPRDR", 0 , 0 )
        
    
    def klaxon(self)-> bool:
        valideAction = False
        self._carte.ecrireCommand(self.creerCommande())
        valideAction = self.validationCommande()

        return valideAction


    

    
