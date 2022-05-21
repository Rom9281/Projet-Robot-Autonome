from ast import pattern
import time
from tkinter import N
import numpy as np
import cv2


coord_init = [11,14]
coord_actuelle = [9,10]
orientation_actuelle = 0
taille_map=10000
distance_min_mvmt_g=6
distance_min_mvmt_d=12
compteur_exploration=1
distance_decalage=12


#
M=np.zeros((taille_map,taille_map)) 
M[0,]=1
M[: 1]=1




#          Creation de 3 fonctions obstacles
def obstacle_avant (message) : 
    qualite_min = 8
    distance_min=450
    ret = False
    for tuple in message:
        if tuple[0]>=qualite_min:
            if tuple[1] < 168 and tuple[1]>=146: 
                if tuple[2]<= distance_min:
                    ret = True
                    maj_avant_g()
            if  tuple[1] >= 168 and tuple[1]<192:
                if tuple[2]<= distance_min:
                    ret = True
                    maj_avant_c()
            if  tuple[1] >= 192 and tuple[1]<214:
                if tuple[2]<= distance_min:
                    ret = True
                    maj_avant_d() 
    return ret


def obstacle_droite (message) :
    qualite_min = 8
    distance_min=450
    ret = False
    for tuple in message:
        if tuple[0]>=qualite_min:
            if tuple[1] >= 214 and tuple[1]<236: 
                if tuple[2]<= distance_min:
                    ret = True
                    maj_droite_g()
            if  tuple[1] >= 236 and tuple[1]<258:
                if tuple[2]<= distance_min:
                    ret = True
                    maj_droite_c()
            if  tuple[1] >= 258 and tuple[1]<280:
                if tuple[2]<= distance_min:
                    ret = True
                    maj_droite_d() 
    return ret


def obstacle_gauche (message) : 
    qualite_min = 8
    distance_min=450
    ret = False
    for tuple in message:
        if tuple[0]>=qualite_min:
            if tuple[1] >= 80 and tuple[1]<102: 
                if tuple[2]<= distance_min:
                    ret = True
                    maj_gauche_g()
            if  tuple[1] >= 102 and tuple[1]<124:
                if tuple[2]<= distance_min:
                    ret = True
                    maj_gauche_c()
            if  tuple[1] >= 124 and tuple[1]<146:
                if tuple[2]<= distance_min:
                    ret = True
                    maj_gauche_d() 
    return ret



def virage_droite():
    orientation(1)
    global orientation_actuelle
    if orientation_actuelle == 0:
        coord_actuelle[0]+=5
        coord_actuelle[1]+=1
    elif orientation_actuelle == 1:
        coord_actuelle[0]+=1
        coord_actuelle[1]-=5
    elif orientation_actuelle ==2 :
        coord_actuelle[0]-=5
        coord_actuelle[1]-=1
    else :
        coord_actuelle[0]-=1
        coord_actuelle[1]+=5
    print(coord_actuelle)
    print('virage droite')


def virage_gauche():
    orientation(-1)
    global orientation_actuelle
    if orientation_actuelle == 0:
        coord_actuelle[0]-=1
        coord_actuelle[1]-=5
    elif orientation_actuelle == 1:
        coord_actuelle[0]-=5
        coord_actuelle[1]-=1
    elif orientation_actuelle ==2 :
        coord_actuelle[0]-=1
        coord_actuelle[1]+=5
    else :
        coord_actuelle[0]-=5
        coord_actuelle[1]+=1
    print(coord_actuelle)
    print('virage gauche')


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
    print(coord_actuelle)



#           fonction de base

def orientation(p):
    global orientation_actuelle
    if orientation_actuelle==3 and p==1:
       orientation_actuelle = 0
    elif orientation_actuelle==0 and p==-1:
        orientation_actuelle = 3
    else :
         orientation_actuelle += p
    return

def premier_tour():
    avancer()
    while coord_actuelle != coord_init :
        if obstacle_gauche():
            maj_obstacle_gauche()
            if obstacle_avant():
                maj_obstacle_avant()
                virage_droite()
                avancer()
            else :
                avancer()
        else:
            virage_gauche()
            avancer()
    return 


def mise_en_position():
    global compteur_exploration
    if compteur_exploration == 1:
        virage_droite()
        virage_droite()
    else :
        virage_gauche()
    while coord_actuelle[0]!=coord_init[0]+compteur_exploration*distance_decalage:
        if obstacle_droite():
            maj_obstacle_droite()
            if obstacle_avant():
                maj_obstacle_avant()
                virage_gauche()
                avancer()
            else: 
                avancer()
        else:
            virage_droite()
            avancer()
    virage_gauche()
    return np.copy(coord_actuelle)
    
def obstacle_fond():
    for i in range(coord_actuelle[0]-1+distance_min_mvmt_g,coord_actuelle[0]+distance_min_mvmt_d):
        ymin=np.copy(taille_map)
        for j in range(taille_map//2,taille_map):
           if M[i][j]==1:
               if ymin>j:
                   ymin=j
    return taille_map-ymin




def maj_avant_g():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]-i][coord_actuelle[1]+10]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+10][coord_actuelle[1]+i]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]+i][coord_actuelle[1]-10]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-10][coord_actuelle[1]-i]=1

def maj_avant_c():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]+i][coord_actuelle[1]+10]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+10][coord_actuelle[1]-i]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]-i][coord_actuelle[1]-10]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-10][coord_actuelle[1]+i]=1

def maj_avant_d():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]+i+6][coord_actuelle[1]+10]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+10][coord_actuelle[1]-i-6]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]-i-6][coord_actuelle[1]-10]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-10][coord_actuelle[1]+i]=1




def maj_gauche_g():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]-10][coord_actuelle[1]-i]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]-i][coord_actuelle[1]+10]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]+10][coord_actuelle[1]+i]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]+i][coord_actuelle[1]-10]=1

def maj_gauche_c():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]-10][coord_actuelle[1]+i]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+i][coord_actuelle[1]+10]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]+10][coord_actuelle[1]-i]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-i][coord_actuelle[1]-10]=1

def maj_gauche_d():
   if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]-10][coord_actuelle[1]+i+6]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+i+6][coord_actuelle[1]+10]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]+10][coord_actuelle[1]-i-6]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-i-6][coord_actuelle[1]-10]=1



def maj_droite_g():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]+16][coord_actuelle[1]-i]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]-i][coord_actuelle[1]-16]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]-16][coord_actuelle[1]+i]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]+i][coord_actuelle[1]+16]=1

def maj_droite_c():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]+16][coord_actuelle[1]+i]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+i][coord_actuelle[1]-16]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]-16][coord_actuelle[1]-i]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-i][coord_actuelle[1]+16]=1

def maj_droite_d():
    if orientation_actuelle == 0:
        for i in range(6):
          M[coord_actuelle[0]+16][coord_actuelle[1]+i+6]=1
    elif orientation_actuelle == 1:
        for i in range(6):
          M[coord_actuelle[0]+i+6][coord_actuelle[1]-16]=1
    elif orientation_actuelle == 2:
        for i in range(6):
          M[coord_actuelle[0]-16][coord_actuelle[1]-i-6]=1
    else :
        for i in range(6):
          M[coord_actuelle[0]-i-6][coord_actuelle[1]+16]=1



def contournement(x):
    if obstacle_gauche():
        maj_obstacle_gauche()
        virage_gauche()
        virage_gauche()
        avancer()
        while obstacle_droite():
            maj_obstacle_droite()
            avancer()
        virage_droite()
        avancer()
    else :
        virage_gauche()
        avancer()
    while coord_actuelle[0]!=x:
        if obstacle_avant() and obstacle_droite():
            maj_obstacle_avant()
            virage_gauche() 
            avancer()
            while obstacle_droite():
                maj_obstacle_droite()
                avancer()
            virage_droite()
            avancer()
        elif obstacle_droite():
            maj_obstacle_droite()
            avancer()
        else : 
            virage_droite()
            avancer()
    virage_gauche()
    return

def exploration_allez(coord):
    avancer()
    while coord_actuelle[1]<taille_map-1-obstacle_fond():
        if obstacle_avant():
            maj_obstacle_avant()
            contournement(coord[0])
        else:
            avancer()
    virage_droite()
    virage_droite()
    return

def exploration_retour(coord):
    while coord_actuelle[1]>coord[1]:
        if obstacle_avant()==True:
            maj_obstacle_avant()
            contournement(coord[0])
        else:
            avancer()
    while obstacle_avant()==False:
        avancer()
    return

def deuxieme_tour():
    global compteur_exploration
    coord_utile=[0,0]
    for i in range((taille_map-2)//distance_decalage-1):
        coord_utile=mise_en_position()
        exploration_allez(coord_utile)
        exploration_retour(coord_utile)
        compteur_exploration+=1
    return



# test global

premier_tour()
deuxieme_tour()

M=M*255
print(M)
N=N*255



cv2.imwrite('carto.png',M)
#cv2.imwrite('carto2.png',N)
