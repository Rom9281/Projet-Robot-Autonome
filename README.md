# ProjetTransversal


## Rappel sur les commandes : 
Les différentes commandes sont les suivantes:
```
digo id:distance:vel [id:distance:vel] 
```
Pour avancer d'une certaine distance à une certaine allure
```
mogo motorId:vel [motorId:vel]
```


# Format envoi de commande 

``INSTRUCTION : ARG1 : ARG2``

!!! ATENTION les espaces sont necessaires entre les ":"
## Jeu d'instruction 

- MVMTR: mouvement Moteur 
- - Arg1: selection deplacement 
    *  mouvement = 0 => avancer
    * mouvement = 1 => tourner a droite
    * mouvement = 2 => tourner a gauche
    * mouvement = 3 => reculer

- - Arg2: parametre action
    * si mouvement = avancer || reculer : value  => distance en (cm)
    * si mouvement = rotation : value => angle de rotation (°)

- USNDST: acquisition distance capteur ultrason

- PSTSRV: mouvement des servos moteur:
- - Arg1: selection servo moteur
    *  0 => Horizontal
    *  1 => Vertical

- - Arg2: angle, valeure comprise entre 0° et 180°

- TIRLMP: actionner le tir de la Lampe LED
  