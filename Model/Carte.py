from calendar import c
from Model.Peripherique import Peripherique


## Peut etre ajouter une fonction de check initialisation du port serial dans le init afin d'
## d'eviter les tests a chaque fois et de dire que l'on ne peut pas initialiser une carte si le port serie ne l'est pas 
class Carte(Peripherique):
    
    def __init__(self):
        super().__init__()


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
            print("\n[$] %s : Peripherique n'est pas connecté" %(self.__class__.__name__))

        return ret

    """
    Permet de lire la commande envoyé par le peripherique
    Retourne True si jamais c'est ok
    """
    def lireCommande(self):
        ret = False

        if(self._serial):
            ret = self._serial.readline()

        else:
            print("\n[$] %s : Peripherique n'est pas connecté" %(self.__class__.__name__))

        return ret 
    
    """
    Permet de valider le faite que la commande ait bien été envoyé et effectuée
    """
    def valider(self,commande):
        read = self.lireCommande() # On lit la commande
        liste = read.split() # on parse la liste 

        return (liste[0]==commande) & (liste[-1]=="ok")

