from rplidar import RPLidar
from Model.CapteurPeriph import CapteurPeriph
import matplotlib.pyplot as plt
import numpy as np,math
import time



class Lidar(CapteurPeriph):
    def __init__(self, pin, baude_rate):
        super().__init__(pin, baude_rate)

        self.__min_quailty = 8 # Qualité minimum de la mesure persue
        
        self.__coord_init=[0,0]
        self.__coord_actuelle=[0,0]
        self.__orientation_actuelle=0
        
        """
        if(self._serial):
            print(self._getInfo())
            flag =True
            while flag:
                try:
                    flag=False
                    self.displayIHM()
                except:
                    print("[$] Error, retrying")
        """
    
    def _connect(self):
        ret = None

        try:
            ret = RPLidar(self._pin)
        except:
            print("[$] Failed to connect to the Lidar")

        return ret
    
    def _getInfo(self):
        return self._serial.get_info()
    
    def _getHealth(self):
        return self._serial.get_health()
    
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

    def __cleanData(self,data):
        clean_data = []

        for coord in data:

            if coord[0] > self.__min_quality:
                clean_data.append((coord[1],coord[2]))

        return clean_data

    def __reax(self,ax):
        ax.grid(True)
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
    
    def getMeasure(self):
        return self.__polarToCartesian(self._serial.iter_scans(max_buf_meas=500, min_len=100))
        
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