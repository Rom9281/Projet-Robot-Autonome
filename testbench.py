import sys
from turtle import position
import serial
import matplotlib.pyplot as plt
import numpy as np
import random, math, time


import keyboard

def envoyerCommande(ser, commande, param1, param2):
    message = f"{commande} : {param1} : {param2}\r\n"
    print(ser.write(message.encode()))
    print(message)
    time.sleep(0.2)
    return 0

  
def gestionUltrason(commande):
    envoyerCommande(ser, "USNDST", commande, 0)
    # print(ser.readline().decode())

positionH = 0
positionV = 0
ser = 10
ser = serial.Serial("/dev/ttyUSB0",19200)
print("Loaded")
# ser.readline()
while 1:

    # #deplacement du robot
    if keyboard.is_pressed("z"):
        print("Sent")
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





