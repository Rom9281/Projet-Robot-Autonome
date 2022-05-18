import fonction_lidar as fl
import fonction_obstacles as fo
import time

while (1):
    scan = fl.scan()
    scan=scan[0]
    print("avant :",fo.obstacle_avant(scan))
    print("droite :",fo.obstacle_droite(scan))
    print("gauche :",fo.obstacle_gauche(scan))
