from Model.PeripheriqueCarte import PeripheriqueCarte

class LED(PeripheriqueCarte):
    
    def __init__(self,carte):
        super().__init__(carte,"TIRLMP","0","0")
    
    def tirer(self):
        self._carte.ecrireCommand(self._creerCommande())
    
