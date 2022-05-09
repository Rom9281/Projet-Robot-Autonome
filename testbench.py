import sys
from turtle import position
import serial
import matplotlib.pyplot as plt
import numpy as np
import random, math, time

# sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Model' )
# sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\Controller' )
# sys.path.append(r'C:\Users\romai\OneDrive\Documents\School\4A\ProjetTransversal\WorkspacePiGit\View' )

# from Controller.Robot import Robot
# from rplidar import RPLidar

"""
def polarToCartesian(data):
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

def cleanData(data,min_quality):
    clean_data = []

    for coord in data:

        if coord[0] > min_quality:
            clean_data.append((coord[1],coord[2]))
    
    return clean_data

def reax(ax):
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

#robot.moveForward(10)
# robot.turn(90,1)

lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

# Pyplot interactive mode : 
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)


for i, scan in enumerate(lidar.iter_scans()):
    #print('%d: Got %d measurments' % (i, len(scan)))

    if(len(scan)>200):
        data = cleanData(scan,13)
        X,Y,Theta,R = polarToCartesian(data)

        ax1.clear()
        ax2.clear()

        reax(ax1)

        ax1.plot(X, Y, 'b-')
        ax2.plot(Theta, R, 'r-')
        fig.canvas.draw()
        fig.canvas.flush_events()
        #time.sleep(0.4)

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

data = cleanData(data,13)

X,Y = polarToCartesian(data)

plt.plot(X, Y)
plt.show()

---------------------------------------------------------
ser = serial.Serial("/dev/ttyUSB0",19200)
angle = 120
distance = 11.832*angle + 140.41
#writ = "digo 1:%s:25 2:%s:\r" % (distance,-distance)
writ = "digo 1:%s:25 2:0:0\r" % (distance)
print("Distance = %s"%(distance))
print(ser.write(writ.encode()))
"""
# ser = serial.Serial("/dev/ttyUSB2",19200)

# writ = "PSTSRV : 1 : 90\n"

# while True:
#     print(writ)
#     print(ser.write(writ.encode()))
#     time.sleep(2)


#######################################################################


"""
* Programme de test de toutes les fonctions du robot
"""
import keyboard

def envoyerCommande(ser, commande, param1, param2):
    message = f"{commande} : {param1} : {param2}\r\n"
    # print(ser.write(message.encode()))
    print(message)
    time.sleep(0.2)
    return 0

  
def gestionUltrason(commande):
    envoyerCommande(ser, "USNDST", commande, 0)
    # print(ser.readline().decode())

positionH = 0
positionV = 0
ser = 10
# ser = serial.Serial("COM7",19200)
# ser.readline()
while 1:

    # #deplacement du robot
    if keyboard.is_pressed("z"):
        envoyerCommande(ser, "MVMTR", 0, 10)

    elif  keyboard.is_pressed("q"):
        envoyerCommande(ser, "MVMTR", 2, 10)

    elif  keyboard.is_pressed("s"):
        envoyerCommande(ser, "MVMTR", 3, 10)

    elif  keyboard.is_pressed("d"):
        envoyerCommande(ser, "MVMTR", 1, 10)

     # # visé plus tire
    elif  keyboard.is_pressed("o"):
        positionV = (positionV + 10) % 180
        envoyerCommande(ser, "PSTSRV", 1, positionV)
    
    elif  keyboard.is_pressed("k"):
        positionH = (positionH + 10) % 180
        envoyerCommande(ser, "PSTSRV", 0, positionH)
    
    elif  keyboard.is_pressed("l"):
        positionV = (positionV - 10) % 180
        envoyerCommande(ser, "PSTSRV", 1, positionV)

    elif  keyboard.is_pressed("m"):
        positionH = (positionH - 10) % 180
        envoyerCommande(ser, "PSTSRV", 0, positionH)
    
    elif  keyboard.is_pressed("t"):
        positionV = (positionV + 10) % 180
        envoyerCommande(ser, "TIRLMP", 0, 0)
        

     # # demande information ultrason

    elif  keyboard.is_pressed("a"):
        gestionUltrason(0)

    elif  keyboard.is_pressed("r"):
        gestionUltrason(1)
    

    # #deplacement du robot
    # keyboard.on_press_key("z", lambda ser: envoyerCommande(ser, "MVMTR", 0, 10))
    # keyboard.on_press_key("q", lambda ser: envoyerCommande(ser, "MVMTR", 2, 10))
    # keyboard.on_press_key("s", lambda ser: envoyerCommande(ser, "MVMTR", 3, 10))
    # keyboard.on_press_key("d", lambda ser: envoyerCommande(ser, "MVMTR", 1, 10))

    # # visé plus tire
    # keyboard.on_press_key("o", lambda positionV: envoyerCommande("PSTSRV", 1, positionV+10))
    # keyboard.on_press_key("k", lambda positionH: envoyerCommande("PSTSRV", 0, positionH+10))
    # keyboard.on_press_key("l", lambda positionV: envoyerCommande("PSTSRV", 1, positionV-10))
    # keyboard.on_press_key("m", lambda positionH: envoyerCommande("PSTSRV", 0, positionH-10))
    
    # keyboard.on_press_key("t", lambda : envoyerCommande("TIRLMP", 0, 0))

    # # demande information
    # keyboard.on_press_key("a", lambda : gestionUltrason(0))
    # keyboard.on_press_key("r", lambda : gestionUltrason(1))





