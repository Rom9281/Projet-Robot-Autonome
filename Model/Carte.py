from calendar import c
from Model.Peripherique import Peripherique

class Carte(Peripherique):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    
    def ecrireCommand(self,command):
        ret = False
        if(self._serial):
            print(command)
            print(self._serial.write(command.encode()))

        else:
            pass
            print("[$] %s : Peripherique n'est pas connecté" %(self.__class__.__name__))

        return ret

    def lireCommande(self):
        ret = False
        # TODO : permettre de parser les valeur lues pour les transmettres
        ret = self._serial.read()
        return ret
    
    def recupererInfo(self,commande):
        self.ecrireCommand(commande)
        return self.lireCommande()