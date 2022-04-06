from Model.Actionneur import Actionneur
from Controller.Commande import Commande
from Controller.Vitesse import Vitesse

class Serializer(Actionneur):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    """
    A besoin de savoir:
    {
        commande: "nom commande"
        parametres: [
            liste param...
        ]
        
    }
    """
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
    
    def __tourner(self,param):
        angle = param["angle"]
        """
        str_command = "digo 1:%s:%s" %(distance,vitesse)
        str_command += " 2:%s:%s\r" %(distance,vitesse)
        self.__sendCommand(str_command)
        """
    
    """
    @PARAM : Vitesse sous forme d'enum dans controller
    @RET : vitesse sous forme de int
    """
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