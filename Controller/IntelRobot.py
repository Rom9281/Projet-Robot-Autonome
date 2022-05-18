import os, time, signal
from multiprocessing import Process
import numpy as np

class IntelligenceRobot(Process):
    
    def __init__(self,q_com,q_lidar,sem_start):
        super(IntelligenceRobot, self).__init__()

        self.__q_com = q_com
        self.__q_lidar = q_lidar
        self.__sem_start = sem_start
        self.__flag = True
        
        # Variable de localisation
        self.coord_init = [1,1]
        self.coord_actuelle = [1,1]
        self.orientation_actuelle = 0
        self.distance_decalage = 2
        self.compteur_exploration = 1
        self.taille_map=1000
        self.distance_min_mvmt=1
        self.qualite_min = 8
        self.distance_min=450

        self.M=np.zeros((self.taille_map,self.taille_map)) 
        self.M[0][1]=1
        self.M[1][0]=1
        
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler)

        print("[$] %s:%s : Process Intelligence actif"%(os.getppid(),os.getpid()))

        self.__sem_start.release()

        while self.__flag:
            time.sleep(2)

        self.premier_tour()

        self.deuxième_tour()

            
    
    def signal_handler(self,signum,frame):
        print("[*] Process Intelligence est arrêté")
        self.__flag = False
    

    def obstacle_avant (self,message) : 
        ret = False
        for tuple in message:
            if tuple[0]>=self.qualite_min:
                if tuple[1] < 168 and tuple[1]>=146: 
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_avant_g()
                if  tuple[1] >= 168 and tuple[1]<192:
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_avant_c()
                if  tuple[1] >= 192 and tuple[1]<214:
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_avant_d() 
        return ret


    def obstacle_droite (self,message) :
        ret = False
        for tuple in message:
            if tuple[0]>= self.qualite_min:
                if tuple[1] >= 214 and tuple[1]<236: 
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_droite_g()
                if  tuple[1] >= 236 and tuple[1]<258:
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_droite_c()
                if  tuple[1] >= 258 and tuple[1]<280:
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_droite_d() 
        return ret


    def obstacle_gauche (self,message) : 
        ret = False
        for tuple in message:
            if tuple[0]>= self.qualite_min:
                if tuple[1] >= 80 and tuple[1]<102: 
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_gauche_g()
                if  tuple[1] >= 102 and tuple[1]<124:
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_gauche_c()
                if  tuple[1] >= 124 and tuple[1]<146:
                    if tuple[2]<= self.distance_min:
                        ret = True
                        #maj_gauche_d() 
        return ret



    #      Recuperation des fonctions de base (avancer,tourner,...)

    def virage_droite():
        self.orientation(1)
        #print('virage droite')


    def virage_gauche():
        self.orientation(-1)
        # print('virage gauche')


    def avancer(self):
        if self.orientation_actuelle == 0:
            self.coord_actuelle[1]+=1
        elif self.orientation_actuelle == 1:
            self.coord_actuelle[0]+=1
        elif self.orientation_actuelle ==2 :
            self.coord_actuelle[1]-=1
        else :
            self.coord_actuelle[0]-=1
        #   print('avance')
        #  print(coord_actuelle)



    #           fonction de base

    def orientation(self,p):
        if self.orientation_actuelle==3 and p==1:
            self.orientation_actuelle = 0
        elif self.orientation_actuelle==0 and p==-1:
            self.orientation_actuelle = 3
        else :
            self.orientation_actuelle += p
        return

    def premier_tour(self):
        self.avancer()
        while self.coord_actuelle != self.coord_init :
            if self.obstacle_gauche():
                self.maj_obstacle_gauche()
                if self.obstacle_avant():
                    self.maj_obstacle_avant()
                    self.virage_droite()
                    self.avancer()
                else :
                    self.avancer()
            else:
                self.virage_gauche()
                self.avancer()
        self.taille_map=self.fond()
        return 


    def mise_en_position(self):
        if self.compteur_exploration == 1:
            self.virage_droite()
            self.virage_droite()
        else :
            self.virage_gauche()
        while self.coord_actuelle[0]!=self.coord_init[0]+self.compteur_exploration*self.distance_decalage:
            if self.obstacle_droite():
                self.maj_obstacle_droite()
                if self.obstacle_avant():
                    self.maj_obstacle_avant()
                    self.virage_gauche()
                    self.avancer()
                else: 
                    self.avancer()
            else:
                self.virage_droite()
                self.avancer()
        self.virage_gauche()
        return np.copy(self.coord_actuelle)

    def obstacle_fond(self):
        for i in range(self.coord_actuelle[0]-1+self.distance_min_mvmt,self.coord_actuelle[0]+self.distance_min_mvmt):
            ymin=np.copy(taille_map)
            for j in range(ymin//2,ymin):
                if self.M[i][j]==1:
                    if ymin>j:
                        ymin=j
        return ymin

    def fond(self):
        kmin=0
        for i,val in enumerate(self.M):
                    k=max(val)
                    if k>kmin:
                                kmin=k
        return(kmin)
                                    


    def maj_obstacle_gauche(self):
        if self.orientation_actuelle == 0:
            self.M[self.coord_actuelle[0]-1][self.coord_actuelle[1]]=1
        elif self.orientation_actuelle == 1:
                self.M[self.coord_actuelle[0]][self.coord_actuelle[1]+1]=1
        elif self.orientation_actuelle == 2:
            self.M[self.coord_actuelle[0]+1][self.coord_actuelle[1]]=1
        else :
                self.M[self.coord_actuelle[0]][self.coord_actuelle[1]-1]=1
        return

    def maj_obstacle_droite(self):
        if self.orientation_actuelle == 0:
            self.M[self.coord_actuelle[0]+1][self.coord_actuelle[1]]=1
        elif self.orientation_actuelle == 1:
                self.M[self.coord_actuelle[0]][self.coord_actuelle[1]-1]=1
        elif self.orientation_actuelle == 2:
            self.M[self.coord_actuelle[0]-1][self.coord_actuelle[1]]=1
        else :
                self.M[self.coord_actuelle[0]][self.coord_actuelle[1]+1]=1
        return

    def maj_obstacle_avant(self):
        if self.orientation_actuelle == 0:
            self.M[self.coord_actuelle[0]][self.coord_actuelle[1]+1]=1
        elif self.orientation_actuelle == 1:
                self.M[self.coord_actuelle[0]+1][self.coord_actuelle[1]]=1
        elif self.orientation_actuelle == 2:
            self.M[self.coord_actuelle[0]][self.coord_actuelle[1]-1]=1
        else :
                self.M[self.coord_actuelle[0]-1][self.coord_actuelle[1]]=1
        return


    def contournement(self,x):
        self.virage_gauche()
        self.avancer()
        while self.obstacle_droite():
            self.maj_obstacle_droite()
            self.avancer()

        self.virage_droite()
        self.avancer()

        while self.obstacle_droite():
            self.maj_obstacle_droite()
            self.avancer()
        self.virage_droite()
        self.avancer()
        while self.coord_actuelle[0]!=x:
            self.avancer()
        self.virage_gauche()
        return

    def exploration_allez(self,coord):
        self.avancer()
        while self.coord_actuelle[1]<self.obstacle_fond()-1:
            if self.obstacle_avant():
                self.maj_obstacle_avant()
                self.contournement(coord[0])
            else:
                self.avancer()
        self.virage_droite()
        self.virage_droite()
        return

    def exploration_retour(self,coord):
        while self.coord_actuelle[1]>coord[1]:
            if self.obstacle_avant()==True:
                self.maj_obstacle_avant()
                self.contournement(coord[0])
            else:
                self.avancer()
        while self.obstacle_avant()==False:
            self.avancer()
        return

    def deuxieme_tour(self):
        coord_utile=[0,0]
        for i in range((self.taille_map-2)//self.distance_decalage-1):
            coord_utile=self.mise_en_position()
            self.exploration_allez(coord_utile)
            self.exploration_retour(coord_utile)
            self.compteur_exploration+=1
        return
