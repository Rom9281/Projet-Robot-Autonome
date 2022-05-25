# ProjetTransversal

## Lien git

https://github.com/Rom9281/ProjetTransversal.git

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

!!! ATTENTION les espaces sont nécessaires entre les ":"
## Jeu d'instruction 

- MVMTR: mouvement Moteur 
- - Arg1: selection déplacement 
    *  mouvement = 0 => avancer
    * mouvement = 1 => tourner a droite
    * mouvement = 2 => tourner a gauche
    * mouvement = 3 => reculer

- - Arg2: parametre action
    * si mouvement = avancer || reculer : value  => distance en (cm)
    * si mouvement = rotation : value => angle de rotation (°)

- USNDST: acquisition distance capteur ultrason
- - Arg1: selection capteur avant ou arrière
	 * 0 => capteur avant
	 * 1 => capteur arrière

- PSTSRV: mouvement des servos moteur:
- - Arg1: selection servo moteur
    *  0 => Horizontal
    *  1 => Vertical

- - Arg2: angle, valeur comprise entre 0° et 180°

- TIRLMP: actionner le tir de la Lampe LED
- - Arg1: selection de l'action a réaliser:
    * 0 => Éteindre lampe
    * 1 => Allumer lampe
    * 2 => tire lampe

- HAPRDR: actionner le Haut-parleur
    


# Guide d'utilisation 

Le projet tourne sur un server Flask 

## Prérequis

 version de python 3
### installation

- flask : module de gestion du server web
- rpLidar : module de gestion du Lidar
- openCv : module de graphique processing
- multiprocessing : gestion de Thread 

### materiel
Dans ce projet nous somme partie dans l'utilisation d'un camera, si vous decide de ne pas en utiliser des erreurs vont apparaître dans le fichier ``index.py``

## Démarrage

Pour démarrer le projet vous devez démarrer le serveur Web qui se trouve dans le fichier `` index.py``

Une fois le serveur demarrer ouvrez un moteur de recherche et aller a l’adresse ``localhost:5000``

Vous arrivez sur la page d'acceuille du site internet et vous n'avez plus qu'a suivre les intructions 

