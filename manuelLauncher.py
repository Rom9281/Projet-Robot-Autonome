import json
from os import kill

import serial
import matplotlib.pyplot as plt
import numpy as np
import random, math, time

from flask import Blueprint

manuelLauncher = Blueprint("manuelLauncher", __name__ )

@manuelLauncher.route("/man/<action>/<param>")
def robotController( action, param):
    message = CommandesManuellesRobot(action, param)
    
    return json.dumps(message)


def envoyerCommande(ser, commande, param1, param2):
    message = f"{commande} : {param1} : {param2}\r\n"
    # print(ser.write(message.encode()))
    print(message)
    time.sleep(0.5)
    return message


def gestionUltrason(ser, commande):
    message = envoyerCommande(ser, "USNDST", commande, 0)
    # print(ser.readline().decode())

    return message


start = False
positionH = 0
positionV = 0
ser = 0

def CommandesManuellesRobot(commande, param):
    global start, positionH, positionV, ser
    message = ""
    if commande == "start":
        start = True
        
        # ser = serial.Serial("/dev/ttyUSB0",19200)
        print("Loaded")

    if start:
        if (commande == "stop"):
                print("[$] INTERRUPTION : ending all processes")
                start = False
                
        
        elif (commande == "USNDST"):
            message = gestionUltrason(ser, param)
        
        elif (commande == "TIRLMP"):
            message = envoyerCommande(ser, commande=commande, param1=param, param2 = 0)

        elif (commande == "MVMTR"):
            message = envoyerCommande(ser, commande=commande, param1=param, param2 = 10)
            
        elif (commande == "PSTSRV"):
            if  param == "0":
                positionV = (positionV + 10) % 180
                message = envoyerCommande(ser, "PSTSRV", 1, positionV)
        
            elif  param == "1":
                positionH = (positionH + 10) % 180
                message = envoyerCommande(ser, "PSTSRV", 0, positionH)
            
            elif  param == "3":
                positionV = (positionV - 10) % 180
                message = envoyerCommande(ser, "PSTSRV", 1, positionV)

            elif  param == "2":
                positionH = (positionH - 10) % 180
                message = envoyerCommande(ser, "PSTSRV", 0, positionH)

    return message
