import matplotlib, random

data = []
distance = 10


for angle in range(0,360):
    distance += random.randint(-1,1)
    data.append((angle,distance))

print(data)
