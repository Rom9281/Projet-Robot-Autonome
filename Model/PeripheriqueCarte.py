"""
Objet etant en peripherie d'une carte connectée à la Pi
Connection au deuxième degré
Possède une carte a qui passer des instructions pour se faire activer
"""
class PeripheriqueCarte():
    
    def __init__(self,carte,commande='',arg1=0,arg2=0):
        self._carte = carte
        self._commande = commande
        self._arg1 = arg1
        self._arg2= arg2

        
    def _creerCommande(self):
        ret = self._commande+" : "
        ret += self._arg1+" : "
        ret += self._arg2+"\n"
        return ret
    
    