from rplidar import RPLidar

def obstacle_avant (m) : 
    ret = False
    for t in m:
        if t[0]>=8:
            if t[1] <= 50 or t[1]>=310:
                if t[2]<= 15:
                    ret = True
    return ret

def obstacle_gauche (m) : 
    ret = False
    for t in m:
        if t[0]>=8:
            if t[1] <= 150 and t[1]>=100:
                if t[2]<= 55:
                    ret = True
            elif t[1] <= 100 and t[1]>= 50:
                if t[2]<= 30:
                    ret = True
    return ret


def obstacle_droite (m) : 
    ret = False
    for t in m:
        if t[0]>=8:
            if t[1] <= 310 and t[1]>=260:
                if t[2]<= 30:
                    ret = True
            elif t[1] <= 260 and t[1]>= 210:
                if t[2]<= 55:
                    ret = True
    return ret

lidar = RPLidar('/dev/ttyUSB0')
for i, scan in enumerate(lidar.iter_scans()):
    print(scan)


