from Model.PeripheriqueCarte import PeripheriqueCarte
from Model.Carte import Carte


class ServoMoteur(PeripheriqueCarte):
    
    def __init__(self,carte, Orientation : int):
        super().__init__(carte,"PSTSRV",Orientation ,0)  
        self.__angle = 0
        
    def getAngle(self)-> int:
        return self.__angle
    
    def getOrientation(self)-> int:
        return self._arg1

    
    def mouvement(self, angle : int):
        self.__angle += angle
        self.arg2 = self.__angle
        self.__carte.ecrireCommand(self._creerCommande())
        return self.carte.valider(self.__commande)
    

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
        return self.mouvement(self.__angle_ver + 10)

    def petitMouvVerBas(self):
        return  self.mouvement(self.__angle_ver - 10)

    def petitMouvHorDrt(self):
        return self.mouvement(self.__angle_hor + 10)

    def petitMouvHorGch(self):
        return self.mouvement(self.__angle_hor - 10)

    

if __name__ == "__main__":
    carte = Carte()
    testServoMoteur = ServoMoteur(carte, 1)

    print(testServoMoteur.getAngle())
    print(testServoMoteur.getOrientation())
    print(testServoMoteur.mouvement(20))
    print(testServoMoteur.getAngle())
