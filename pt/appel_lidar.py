import fonction_lidar as fl
import fonction_obstacles as fo

while (1):
    scan = fl.scan()
    print(fo.obstacle_avant(scan))
    print(fo.obstacle_droite(scan))
    print(fo.obstacle_gauche(scan))