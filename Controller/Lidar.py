"""
Code pour le lidar:
Maxime - Romain
"""

# Imports
from multiprocessing.dummy import Process
import matplotlib.pyplot as plt, json, signal
from rplidar import RPLidar

# 
from Model.Peripherique import Peripherique


class Lidar(Peripherique,Process):
    def __init__(self,q_comm,sem_start):
        super().__init__(pin, baude_rate)

        self.__q_comm = q_comm # Queue de commande
        self.__sem_start = sem_start # 

        # Configuration des commandes:
        self.__config_commandes_path = "/home/pi/Documents/Controller/commandes.json"
        self.__com = json.load(open(self.__config_commandes_path)) # récupère la config des periphériques dans le json

        self.__min_quality = 8 # Qualité minimum de la mesure persue

        

        self.__iter = 0
        self.__flag = True
        
    """
    Permet la connection au lidar en utilisant la bibliotheque
    Retourne un objet RPLidar ou None
    """
    def _connect(self) -> RPLidar:
        ret = None

        try:
            ret = RPLidar(self._pin)
            print(f"[$] Info Lidar : {self._getInfo}")
            print(f"[$] Santé Lidar : {self._getHealth}")
        except :
            print("[$] Failed to connect to the Lidar")

        return ret
    
    def _getInfo(self):
        return self._serial.get_info()

    def _getHealth(self):
        return self._serial.get_health()
    
    """
    Methode principale pour le fonctionnement du LIDAR
    """
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler)

        print("[$] %s:%s : Process Intelligence actif"%(os.getppid(),os.getpid()))

        self.__sem_start.release()

        while self.__flag:
            # Mettre ici les taches effectués par le lidar

            self.__q_comm.put(item, block=True, timeout=None) 
            # exemple pour mettre une commande dans la queue:
            # q_com.put(commandes["rot_ver_gauche"])
            # Voir le fichier commandes.json

            pass

    """
    Permet de virer les données en dessous d'un seuil de qualité
    """
    def __cleanData(self,data):
        clean_data = []

        for coord in data:

            if coord[0] > self.__min_quality:
                clean_data.append((coord[1],coord[2]))

        return clean_data
    
    """
    Permet de gerer l'interruption du programme LidarIntel
    """
    def signal_handler(self,signum,frame):
        print("[*] Process LidarIntel est arrêté")
        self.__flag = False

    

"""
    def __reax(self,ax):
        ax.grid(True)
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')

    def displayIHM(self):
        plt.ion()

        fig = plt.figure()
        ax1 = fig.add_subplot(211)

        ax2 = fig.add_subplot(212)


        for i, scan in enumerate(self._serial.iter_scans()):
        #print('%d: Got %d measurments' % (i, len(scan)))

            if(len(scan)>200):
                data = self.__cleanData(scan,13)
                X,Y,Theta,R = self.__polarToCartesian(data)

                ax1.clear()
                ax2.clear()

                self.__reax(ax1)

                ax1.plot(X, Y, 'b-')
                ax2.plot(Theta, R, 'r-')
                fig.canvas.draw()
                fig.canvas.flush_events()
                #time.sleep(0.4)

    def __polarToCartesian(self,data):
        data = self.__cleanData(data)
        X = []
        Y = []
        Theta= []
        R = []

        for coord in data:
            X.append(coord[1]*math.cos(np.radians(coord[0])))
            Y.append( coord[1]*math.sin(np.radians(coord[0])))
            Theta.append(coord[0])
            R.append(coord[1])

        return X,Y,Theta,R
"""