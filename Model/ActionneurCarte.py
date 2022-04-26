from Model.Actionneur import Actionneur

class ActionneurCarte(Actionneur):
    
    def __init__(self,carte,commande,arg1,arg2):
        self._carte = carte
        self._commande = commande
        self._arg1 = arg1
        self._arg2= arg2
        self._len_chiffre = 10;

        

    def _creerCommande(self):
        ret = self._commande+":"
        ret += "0"*(self._len_chiffre-len(list(self._arg1)))
        ret += self._arg1+":"
        ret += "0"*(self._len_chiffre-len(list(self._arg2)))
        ret += self._arg2+";"

        return ret
    
    