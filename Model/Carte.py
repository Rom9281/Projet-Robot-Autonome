from Model.Peripherique import Peripherique

class Carte(Peripherique):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    
    def ecrireCommand(self,command):
        ret = False

        print("[$] Sending command")

        if(self._serial.write(command.encode(encoding='UTF-8',errors='strict'))):
            ret=True
        else:
            print("[$] Error")

        return ret

    def lireCommande(self):
        # TODO : permettre de parser les valeur lues pour les transmettres
        ret = self._serial.read()
        return ret