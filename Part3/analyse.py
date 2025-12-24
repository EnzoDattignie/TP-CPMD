import numpy as np
import matplotlib.pyplot as plt 


# On commence par lire la donnée

input = "./output/nh3_dm/TRAJEC.xyz"

nstep = 10

n_H = 0
n_N = 0
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
        if elmt == "N" :
            n_N += 1
    if i >= 0 and len(lines.split()) != 4:
        n_H = 0
        n_N = 0
        i = -2
        pos.append(np.copy(pos_temp))
    i += 1

print(f"n = {n}, n_N = {n_N}, n_H = {n_H}")


rij_sq = np.zeros(len(pos))
angle = np.zeros(3)
angle_tab = np.zeros(len(pos))
for i in range(0,len(pos)) :
    for j in range(1,n) :
        rij = pos[i][0] - pos[i][j]
        rij_sq[i]+=((rij[0]**2+rij[1]**2+rij[2]**2)/(n-1))
    Liste_H = np.copy(pos[i][1:])
    for j in range(len(Liste_H)) :
        u = pos[i][0] - Liste_H[j-1]
        v = pos[i][0] - Liste_H[j]
        angle[j] = (np.arccos(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))))/(2*np.pi)*360
    # print(angle)
    angle_tab[i] = np.mean(angle)

rij_tab = np.sqrt(rij_sq)

plt.title(" Évolution de la distance N-H en fonction du pas")
plt.xlabel("Pas")
plt.ylabel("Distance (Å)")
plt.plot(range(0,len(pos)),rij_tab)
plt.show()

plt.title("Evolution de l'angle H-N-H en fonction du pas")
plt.xlabel("Pas")
plt.ylabel("Angle (°)")
plt.plot(range(0,len(pos)),angle_tab)
plt.show()

print(f"La distance moyenne est : {np.mean(rij_tab)} Å\nL'angle moyen est : {np.mean(angle)}°")

