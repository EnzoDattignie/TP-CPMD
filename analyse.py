import numpy as np
import matplotlib.pyplot as plt 


# On commence par lire la donnée

input = "./output/h2o_dyna/TRAJEC.xyz"

nstep = 10

n_H = 0
n_O = 0
pos = []

with open(input,"r") as file :
    data = file.readlines()

i = -2
for lines in data :
    if i == -2 :
        n = int(lines.strip())
        pos_temp = np.zeros((n,3))
    if i >= 0 and len(lines.split()) == 4:
        line = lines.split() 
        elmt = line[0]
        pos_temp[i] = [float(line[1]),float(line[2]),float(line[3])]
        if elmt == "H" :
            n_H += 1
        if elmt == "O" :
            n_O += 1
    if i >= 0 and len(lines.split()) != 4:
        n_H = 0
        n_O = 0
        i = -2
        pos.append(np.copy(pos_temp))
    i += 1

print(f"n = {n}, n_O = {n_O}, n_H = {n_H}")

rij_mean = np.zeros(len(pos))
for i in range(0,len(pos)) :
    for j in range(1,n) :
        rij = pos[0][0] - pos[0][j]
        rij_mean[i]+=((rij[0]**2+rij[1]**2+rij[2]**2)/2)
    
plt.plot(range(0,len(pos)),rij_mean)
plt.show()
print(len(rij_mean))

