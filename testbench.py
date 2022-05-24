

import serial
import matplotlib.pyplot as plt
import numpy as np
import random, math, time

import keyboard

<<<<<<< HEAD



=======
>>>>>>> 4eb1db6971bc719d3a169f00b172bcab55abf882
def envoyerCommande(ser, commande, param1, param2):
    message = f"{commande} : {param1} : {param2}\r\n"
    print(ser.write(message.encode()))
    print(message)
    print(ser.readline().decode())
    time.sleep(0.5)
    return 0

  
def gestionUltrason(commande):
    envoyerCommande(ser, "USNDST", commande, 0)
    print(ser.readline().decode())







positionH = 0
positionV = 0
ser = 10
ser = serial.Serial("COM7",19200)
print("Loaded")
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

        envoyerCommande(ser, "TIRLMP", 2, 0)

    elif keyboard.is_pressed("c"):
        envoyerCommande(ser, "HAPRDR", 0, 0)    
        

    # # demande information ultrason

    elif  keyboard.is_pressed("a"):
        gestionUltrason(0)

    elif  keyboard.is_pressed("r"):
        gestionUltrason(1)

    elif keyboard.is_pressed("n"):
        break


gestionRobot()