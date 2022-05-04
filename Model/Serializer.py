#from Model.Actionneur import Actionneur
#from Controller.Enums import Vitesse, Commande,Sens

from Model.PeripheriqueCarte import PeripheriqueCarte

class Serializer(PeripheriqueCarte):
    
    def __init__(self,carte):
        # super().__init__(pin,baude_rate)
        super().__init__(carte,"MVTMTR","0","0")

    
    def avancer(self,distance):

        self._commande = "MVTMTR"
        self._arg1 = "1"
        self._arg2 = str(distance)

        self._carte.ecrireCommand(self._creerCommande())
    
    def reculer(self,distance):

        self._commande = "MVTMTR"
        self._arg1 = "3"
        self._arg2 = str(distance)

        self._carte.ecrireCommand(self._creerCommande())
    
    def tournerDroite(self,angle):

        self._commande = "MVTMTR"
        self._arg1 = "2"
        self._arg2 = str(angle)

        self._carte.ecrireCommand(self._creerCommande())
    
    def tournerGauche(self,angle):
    
        self._commande = "MVTMTR"
        self._arg1 = "4"
        self._arg2 = str(angle)

        self._carte.ecrireCommand(self._creerCommande())

    """
    CODE SI LE SERIALISER EST BRANCHE DIRECTEMENT AU RASPBERRY
    
    A besoin de savoir:
    {
        commande: "nom commande"
        parametres: [
            liste param...
        ]
        
    }
    
    def actionner(self,commande):
        if self._serial:
            print("[$] Commande : %s" % (commande["commande"]))
            if(commande["commande"] == Commande.AVANCER):
                self.__avancer(commande["param"])
            elif(commande["commande"]==Commande.TOURNER):
                self.__avancer(commande["param"])
    

    def __avancer(self, param):
        vitesse = self.__getSpeed(param["vitesse"])
        distance = 31,243*param["distance"] - 3,766 # Passage de la mesure en inch

        str_command = "digo 1:%s:%s" %(distance,vitesse)
        str_command += " 2:%s:%s\r" %(distance,vitesse)

        self.__sendCommand(str_command)
    
    
    Faire tourner les roues du robot
    
    def __tourner(self,param):

        vitesse = self.__getSpeed(param["vitesse"])
        angle = 11,832*param["angle"] + 140,41

        if(param["sens"]==Sens.GAUCHE):
            str_command = "digo 1:%s:%s 2:0:0\r" %(angle,vitesse)
        else:
            str_command = "digo 1:0:0 2:%s:%s\r" %(angle,vitesse)

        self.__sendCommand(str_command)
    
    
    @PARAM : Vitesse sous forme d'enum dans controller
    @RET : vitesse sous forme de int
    
    def __getSpeed(self,vitesse):
        ret = 0

        if(vitesse==Vitesse.LENTE):
            ret=5

        elif(vitesse==Vitesse.MOYENNE):
            ret=15

        elif(vitesse==Vitesse.RAPIDE):
            ret=25
        
        return ret

    def __sendCommand(self,str_command):
        print("[$] Sending command")
        res = self._serial.write(str_command.encode(encoding='UTF-8',errors='strict'))
        print("[$] Result : %s"%(res))
    """