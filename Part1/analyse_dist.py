import numpy as np
import matplotlib.pyplot as plt 


# On commence par lire la donnée

input = "./output/3au/TRAJEC.xyz"
input2 = "./output/4au/TRAJEC.xyz"
input3 = "./output/5au-correctif/TRAJEC.xyz"
ua_t = 0.024188

pos3au = []
pos4au = []
pos5au = []

with open(input,"r") as file :
    data = file.readlines()

with open(input2,"r") as file :
    data2 = file.readlines()

with open(input3,"r") as file :
    data3 = file.readlines()

i = -2
for lines in data :
    if i == -2 :
        n = int(lines.strip())
        pos_temp = np.zeros((n,3))
    if i >= 0 and len(lines.split()) == 4:
        line = lines.split() 
        elmt = line[0]
        pos_temp[i] = [float(line[1]),float(line[2]),float(line[3])]
    if i >= 0 and len(lines.split()) != 4:
        i = -2
        pos3au.append(np.copy(pos_temp))
    i += 1

i = -2
for lines in data2 :
    if i == -2 :
        n = int(lines.strip())
        pos_temp = np.zeros((n,3))
    if i >= 0 and len(lines.split()) == 4:
        line = lines.split() 
        elmt = line[0]
        pos_temp[i] = [float(line[1]),float(line[2]),float(line[3])]
    if i >= 0 and len(lines.split()) != 4:
        i = -2
        pos4au.append(np.copy(pos_temp))
    i += 1

i=-2
for lines in data3 :
    if i == -2 :
        n = int(lines.strip())
        pos_temp = np.zeros((n,3))
    if i >= 0 and len(lines.split()) == 4:
        line = lines.split() 
        elmt = line[0]
        pos_temp[i] = [float(line[1]),float(line[2]),float(line[3])]
    if i >= 0 and len(lines.split()) != 4:
        i = -2
        pos5au.append(np.copy(pos_temp))
    i += 1

print(f"n = {n}")

pos = pos3au
rij_sq = np.zeros(len(pos))
for i in range(0,len(pos)) :
    rij = pos[i][0] - pos[i][1]
    rij_sq[i]+=((rij[0]**2+rij[1]**2+rij[2]**2))

rij_tab3au = np.sqrt(rij_sq)
t3au = np.linspace(0,len(pos)*3*ua_t,len(pos))

pos = pos4au
rij_sq = np.zeros(len(pos))
for i in range(0,len(pos)) :
    rij = pos[i][0] - pos[i][1]
    rij_sq[i]+=((rij[0]**2+rij[1]**2+rij[2]**2))

rij_tab4au = np.sqrt(rij_sq)
t4au = np.linspace(0,len(pos)*4*ua_t,len(pos))

pos = pos5au
rij_sq = np.zeros(len(pos))
for i in range(0,len(pos)) :
    rij = pos[i][0] - pos[i][1]
    rij_sq[i]+=((rij[0]**2+rij[1]**2+rij[2]**2))

rij_tab5au = np.sqrt(rij_sq)
t5au = np.linspace(0,len(pos)*5*ua_t,len(pos))

print (f"mean 3au = {np.mean(rij_tab3au)}, mean 4au = {np.mean(rij_tab4au)}, mean 5au = {np.mean(rij_tab5au)}")

plt.title(" Évolution de la distance H-H en fonction du temps")
plt.xlabel("temps(fs)")
plt.ylabel("Distance (Å)")
plt.plot(t3au,rij_tab3au,label = "3au")
plt.plot(t4au,rij_tab4au,label = "4au")
plt.plot(t5au,rij_tab4au,label = "5au corrigé")
plt.legend()
plt.show()



