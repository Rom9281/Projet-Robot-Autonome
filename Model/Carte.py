from Model.Peripherique import Peripherique

class Carte(Peripherique):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    
    def ecrireCommand(self,command):
        ret = False
        if(self._serial):
            print(command)
            print(self._serial.write(command.encode()))
            
            """
            if():
                ret=True
            else:
                print("[$] %s : Commande non envoyé"%(self.__class__.__name__))
            """

        else:
            print("[$] %s : Peripherique n'est pas connecté" %(self.__class__.__name__))

        return ret

    def lireCommande(self):
        # TODO : permettre de parser les valeur lues pour les transmettres
        ret = self._serial.read()
        return ret