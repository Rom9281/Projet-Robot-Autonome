from rplidar import RPLidar
import time
coord_init=[0,0]
coord_actuelle=[0,0]
orientation_actuelle=0

def obstacle_avant (m) : 
    ret = False
    for t in m:
        if t[0]>=8:
            if t[1] <= 50 or t[1]>=310:
                if t[2]<= 150:
                    ret = True
    return ret

def obstacle_gauche (m) : 
    ret = False
    for t in m:
        if t[0]>=8:
            if t[1] <= 150 and t[1]>=100:
                if t[2]<= 550:
                    ret = True
            elif t[1] <= 100 and t[1]>= 50:
                if t[2]<= 300:
                    ret = True
    return ret


def obstacle_droite (m) : 
    ret = False
    for t in m:
        if t[0]>=8:
            if t[1] <= 310 and t[1]>=260:
                if t[2]<= 300:
                    ret = True
            elif t[1] <= 260 and t[1]>= 210:
                if t[2]<= 550:
                    ret = True
    return ret
    
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

def reculer():
    global orientation_actuelle
    if orientation_actuelle == 0:
        coord_actuelle[1]-=1
    elif orientation_actuelle == 1:
        coord_actuelle[0]-=1
    elif orientation_actuelle ==2 :
        coord_actuelle[1]+=1
    else :
        coord_actuelle[0]+=1
    print('recule')
    time.sleep(0.5)
    return "mogo 1:30 2:30\r"

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
    avancer()
    while coord_actuelle != coord_init :
        if obstacle_gauche(lidar.iter_scans()[-1]):
            if obstacle_avant(lidar.iter_scans()[-1]):
                virage_droite()
                avancer()
            else :
                avancer()
        else:
            virage_gauche()
            avancer()
        print(coord_actuelle)
    return 

lidar = RPLidar('/dev/ttyUSB0')
premier_tour()

