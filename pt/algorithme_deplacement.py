import fonction_lidar as fl
import fonction_obstacles as fo
import time


coord_init=[0,0]
coord_actuelle=[0,1]
orientation_actuelle=0
distance_decalage = 2
compteur_exploration = 1
taille_map=10
distance_min_mvmt=1




def virage_droite():
    orientation(1)
    print('virage droite')
    return "digo 1:550:70 2:-550:70\r"

def virage_gauche():
    orientation(-1)
    print('virage gauche')
    return "digo 1:-550:70 2:550:70\r"

def avancer():
    global orientation_actuelle
    if orientation_actuelle == 0:
        coord_actuelle[1]+=1
    elif orientation_actuelle == 1:
        coord_actuelle[0]+=1
    elif orientation_actuelle ==2 :
        coord_actuelle[1]-=1
    else :
        coord_actuelle[0]-=1
    print('avance')
    time.sleep(0.5)
    return "mogo 1:-30 2:-30\r"

def orientation(p):
    global orientation_actuelle
    if orientation_actuelle==3 and p==1:
       orientation_actuelle = 0
    elif orientation_actuelle==0 and p==-1:
        orientation_actuelle = 3
    else :
         orientation_actuelle += p

    # possibilite de remplacer tout les if par:
    # orientation_actuelle = (orientation_actuell + p) % 4
    return

def premier_tour():
    if fo.obstacle_gauche(scan):
        if fo.obstacle_avant(scan):
            virage_droite()
            avancer()
        else :
            avancer()
    else:
        virage_gauche()
        avancer()
    print(coord_actuelle)

while (coord_actuelle != coord_init):
    scan = fl.scan()
    scan=scan[0]
    print("avant :",fo.obstacle_avant(scan))
    print("droite :",fo.obstacle_droite(scan))
    print("gauche :",fo.obstacle_gauche(scan))
    premier_tour()

fl.stop()
