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


rij_sq = np.zeros(len(pos))
angle = np.zeros(len(pos))
for i in range(0,len(pos)) :
    for j in range(1,n) :
        rij = pos[i][0] - pos[i][j]
        rij_sq[i]+=((rij[0]**2+rij[1]**2+rij[2]**2)/2)
    u = pos[i][0] - pos[i][1]
    v = pos[i][0] - pos[i][2]
    angle[i] = (np.arccos(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))))/(2*np.pi)*360


rij_tab = np.sqrt(rij_sq)

plt.title(" Évolution de la distance H-O en fonction du pas")
plt.xlabel("Pas")
plt.ylabel("Distance (Å)")
plt.plot(range(0,len(pos)),rij_tab)
plt.show()

plt.title("Evolution de l'angle H-O-H en fonction du pas")
plt.xlabel("Pas")
plt.ylabel("Angle (°)")
plt.plot(range(0,len(pos)),angle)
plt.show()

print(f"La distance moyenne est : {np.mean(rij_tab)} Å\nL'angle moyen est : {np.mean(angle)}°")

