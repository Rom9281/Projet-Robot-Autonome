from Model.ActionneurCarte import ActionneurCarte

class ServoMoteur(ActionneurCarte):
    
    def __init__(self,carte):
        super().__init__(carte,"PSTSRV","0","90")
        self.mouvementHorizontal(90)
    
    def mouvementHorizontal(self,angle):
        self._arg1 = "0"
        self._arg2 = str(angle)
        self._carte.ecrireCommand(self._creerCommande())
    
    def mouvementVertical(self,angle):
        self._arg1 = "1"
        self._arg2 = str(angle)
        self._carte.ecrireCommand(self._creerCommande())
    
