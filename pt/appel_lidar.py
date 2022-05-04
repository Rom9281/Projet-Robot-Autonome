import fonction_lidar as fl
import fonction_obstacles as fo

#while (1):
scan = fl.scan()

print(fo.obstacle_avant(scan[0]))
print(fo.obstacle_droite(scan[0]))
print(fo.obstacle_gauche(scan[0]))