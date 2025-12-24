import numpy as np
import matplotlib.pyplot as plt 


# On commence par lire la donnée

input = "./output/3au/ENERGIES"
input2 = "./output/4au/ENERGIES"
input3 = "./output/5au-correctif/ENERGIES"
ua_t = 0.024188



with open(input,"r") as file :
    data = file.readlines()

with open(input2,"r") as file :
    data2 = file.readlines()

with open(input3,"r") as file :
    data3 = file.readlines()

En3au = np.zeros(len(data))
En4au = np.zeros(len(data))
En5au = np.zeros(len(data))
for i in range(0,len(data)) :
    En3au[i]=(float(data[i].split()[3].strip()))
    En4au[i]=(float(data2[i].split()[3].strip()))
    En5au[i]=(float(data3[i].split()[3].strip()))

t_3au = np.linspace(0,len(En3au)*3*ua_t,len(En3au))
t_4au = np.linspace(0,len(En3au)*4*ua_t,len(En3au))
t_5au = np.linspace(0,len(En3au)*5*ua_t,len(En3au))



plt.title(" Évolution de l'énergie électronique fonction du temps")
plt.xlabel("temps(fs)")
plt.ylabel("En(H)")
plt.plot(t_3au,En3au,label = "3au")
plt.plot(t_4au,En4au,label = "4au")
plt.plot(t_5au,En5au,label = "5au corrigé")
plt.legend()
plt.show()



