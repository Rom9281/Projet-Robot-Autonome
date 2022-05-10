from Model.PeripheriqueCarte import PeripheriqueCarte

class ServoMoteur(PeripheriqueCarte):
    
    def __init__(self,carte):
        super().__init__(carte,"PSTSRV","0","90")
        self.__angle_hor = 0
    
    def mouvementHorizontal(self,angle):
        self._arg1 = "0"
        self._arg2 = str(angle)
        self._carte.ecrireCommand(self._creerCommande())
        self.__angle_hor = angle
    
    def mouvementVertical(self,angle):
        self._arg1 = "1"
        self._arg2 = str(angle)
        self._carte.ecrireCommand(self._creerCommande())
        self.__angle_ver = angle
    
    def petitMouvVerDrt(self):
        self.mouvementVertical(self.__angle_ver+10)

    def petitMouvVerGch(self):
        self.mouvementVertical(self.__angle_ver-10)

    def petitMouvHorDrt(self):
        self.mouvementHorizontal(self.__angle_ver+10)

    def petitMouvHorGch(self):
        self.mouvementHorizontal(self.__angle_ver-10)

    
