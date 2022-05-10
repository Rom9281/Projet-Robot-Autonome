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

    TOURGAUCHE = 2 
    TOURDROIT = 3
    
    RECULER = 4

    TIRER = 5

    ROTHORIZON = 6 # Rotation de la tour à l'horizontal 
    ROTVERTICAL = 7 # Rotation de la tour à la verticale

    ROTVERDRT = 8 # Rotation de la tour à la veritcale droite
    ROTVERGCH = 9 # Rotation de la tour à la verticale gauche
    ROTHORDRT = 10 # Rotation de la tour à l'horizontal droite
    ROTHORGCH = 11 # Rotation de la tour à l'horizontal gauce

