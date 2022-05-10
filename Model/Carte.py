from calendar import c
from Model.Peripherique import Peripherique

class Carte(Peripherique):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    """
    Permet d'ecrire une commande pour le peripherique
    Retourne 
    """
    def ecrireCommand(self,command):
        ret = False

        if(self._serial):
            self._serial.write(command.encode())
            ret = True

        else:
            print("[$] %s : Peripherique n'est pas connecté" %(self.__class__.__name__))

        return ret

    """
    Permet de lire la commande envoyé par le peripherique
    Retourne True si jamais c'est ok
    """
    def lireCommande(self):
        ret = False

        if(self._serial):
            ret = self._serial.read()

        else:
            print("[$] %s : Peripherique n'est pas connecté" %(self.__class__.__name__))

        return ret 
    
    """
    Permet de valider le faite que la commande ait bien été envoyé et effectuée
    """
    def valider(self,commande):
        read = self.lireCommande() # On lit la commande
        read = read[:-2] # On enleve la fin
        liste = read.split(":") # on parse la liste 

        return (liste[0]==commande)&(liste[1]=="OK")

