from enum import Enum

class Sens(Enum):
    DROITE = 1
    GAUCHE = 2

class Vitesse(Enum):
    LENTE = 1
    MOYENNE = 2
    RAPIDE = 3

class Commande(Enum):
    AVANCER = 1
    TOURNER = 2 