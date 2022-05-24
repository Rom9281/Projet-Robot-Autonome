from cmath import inf

from Model.PeripheriqueCarte import PeripheriqueCarte

class Ultrason(PeripheriqueCarte):
    def __init__(self,carte, position = 0 ) -> None:
        # position correspond a la position sur le robot 0 avant 1 arriere

        super().__init__(carte, codeCommande = "USNDST", arg1 = position)
        self.distance = inf
    
    def recupererDistance(self) -> bool:
        
        self._carte.ecrireCommand(self.creerCommande())
        valideAction = self.validationCommande()
        if (valideAction):
            mesureDistance = self._carte.lireCommande()
            if (mesureDistance != ""):
                self.distance = int(mesureDistance.split()[-1])

        return valideAction

