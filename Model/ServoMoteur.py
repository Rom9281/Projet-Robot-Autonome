from Model.PeripheriqueCarte import PeripheriqueCarte

class ServoMoteur(PeripheriqueCarte):
    
    def __init__(self,carte):
        super().__init__(carte,"PSTSRV","0","90")   ## probleme de type de valeur pour l'initilisation arg1 et arg2
        self.__angle_hor = 0
        self.__angle_ver = 0

    def mouvementHorizontal(self,angle):
        self._arg1 = "0"
        self._arg2 = str(angle)
        self._carte.ecrireCommand(self._creerCommande())
        self.__angle_hor = angle
        return self._carte.valider(self._commande)
    
    def mouvementVertical(self,angle):
        self._arg1 = "1"
        self._arg2 = str(angle)
        self._carte.ecrireCommand(self._creerCommande())
        self.__angle_ver = angle
        return self._carte.valider(self._commande)
    
    def petitMouvVerHaut(self):
        return self.mouvementVertical(self.__angle_ver+10)

    def petitMouvVerBas(self):
        return  self.mouvementVertical(self.__angle_ver-10)

    def petitMouvHorDrt(self):
        return self.mouvementHorizontal(self.__angle_hor+10)

    def petitMouvHorGch(self):
        return self.mouvementHorizontal(self.__angle_hor-10)

    
