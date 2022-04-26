import matplotlib.pyplot as plt
import numpy as np
import random, math


data = []
distance = 10

def polarToCartesian(data):
    X = []
    Y = []

    for coord in data:
        X.append(coord[1]*math.cos(np.radians(coord[0])))
        Y.append( coord[1]*math.sin(np.radians(coord[0])))
    
    return X,Y



for angle in range(0,360):
    distance += random.randint(-1,1)
    data.append((angle,distance))

print(data)

X,Y = polarToCartesian(data)

plt.plot(X, Y)
plt.show()




