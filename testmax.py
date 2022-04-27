from rplidar import RPLidar

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


lidar = RPLidar('/dev/ttyUSB0')


for i, scan in enumerate(lidar.iter_scans()):
    print("AVANT",obstacle_avant(scan))
    print("DROITE",obstacle_droite(scan))
    print("GAUCHE",obstacle_gauche(scan))


