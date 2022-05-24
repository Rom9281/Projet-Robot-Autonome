"""
CPE Lyon 

Projet Transversal

Groupe B1

Fares Zaghouane
"""

import json,serial, matplotlib.pyplot as plt, numpy as np,random, math, time
from os import kill
from flask import Blueprint

manuelLauncher = Blueprint("manuelLauncher", __name__ )

@manuelLauncher.route("/man/<action>/<param>")
def robotController( action, param):
    message = CommandesManuellesRobot(action, param)
    
    return json.dumps(message)


def envoyerCommande(ser, commande, param1, param2):
    message = f"{commande} : {param1} : {param2}\r\n"
    print(ser.write(message.encode()))
    print(message)
    validation = ser.readline().decode()
    validation = f"{commande} : ok"
    time.sleep(0.5)
    return validation


def gestionUltrason(ser, commande):
    validation = envoyerCommande(ser, "USNDST", commande, 0)
    print(ser.readline().decode())
    if (validation.split()[-1] == "ok"):
        distance = ser.redline().decode()
        distance = "AR : 20"
        distance = distance.split()[-1] # on ne garde que la valeur
    return validation , distance


start = False
positionH = 0
positionV = 0
ser = 0

def CommandesManuellesRobot(commande, param):
    global start, positionH, positionV, ser
    validation = {"validation": ""}
    if commande == "start":
        start = True
        
        ser = serial.Serial("/dev/ttyUSB0",19200)
        print("Loaded")

    if start:
        if (commande == "stop"):
                print("[$] INTERRUPTION : ending all processes")
                start = False
                
        
        elif (commande == "USNDST"):
            validation["validation"] , validation["distance"] = gestionUltrason(ser, param)

        elif (commande == "TIRLMP"):
            validation["validation"] = envoyerCommande(ser, commande=commande, param1=param, param2 = 0)

        elif (commande == "MVMTR"):
            validation["validation"] = envoyerCommande(ser, commande=commande, param1=param, param2 = 10)
            
        elif (commande == "PSTSRV"):
            if  param == "0":
                positionV = (positionV + 5) % 180
                validation["validation"]= envoyerCommande(ser, "PSTSRV", 1, positionV)
        
            elif  param == "1":
                positionH = (positionH + 5) % 180
                validation["validation"]= envoyerCommande(ser, "PSTSRV", 0, positionH)
            
            elif  param == "3":
                positionV = (positionV - 5) % 180
                validation["validation"] = envoyerCommande(ser, "PSTSRV", 1, positionV)

            elif  param == "2":
                positionH = (positionH - 5) % 180
                validation["validation"] = envoyerCommande(ser, "PSTSRV", 0, positionH)

    return validation

