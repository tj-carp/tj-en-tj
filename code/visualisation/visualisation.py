import matplotlib.pyplot as plt
import pandas as pd

# import csv data
df = pd.read_csv("StationsHolland.csv")

# hardcode alle verbindingen
alkmaar_x = [52.64472198, 52.63777924, 52.95527649]
alkmaar_y = [5.055555344, 4.739722252, 4.761111259]
ams_amstel_x = [52.338889, 52.34666824, 52.37888718]
ams_amstel_y = [4.872356, 4.917778015, 4.900277615]
ams_cs_x = [52.37888718, 52.38888931]
ams_cs_y = [4.900277615, 4.837777615]
ams_sloterdijk_x = [52.38777924, 52.38888931, 52.43888855]
ams_sloterdijk_y = [4.638333321, 4.837777615, 4.813611031]
ams_zuid_x = [52.38888931, 52.338889, 52.30944443]
ams_zuid_y = [4.837777615, 4.872356, 4.761944294]
beverwijk_x = [52.47833252, 52.54583359]
beverwijk_y = [4.656666756, 4.658611298]
castricum_x = [52.54583359, 52.63777924]
castricum_y = [4.658611298, 4.739722252]
dh_cs_x = [52.00666809, 52.08027649, 52.01750183]
dh_cs_y = [4.356389046, 4.324999809, 4.704444408]
dh_2_x = [52.16611099, 52.08027649]
dh_2_y = [4.481666565, 4.324999809]
roffa_cs_x = [51.80722046, 51.92499924, 51.92124381]
roffa_cs_y = [4.66833353, 4.46888876, 4.408993721]
roffa_2_x = [51.95194626, 51.92499924]
roffa_2_y = [4.553611279, 4.46888876]
zaandam_x = [52.54583359, 52.43888855, 52.47833252]
zaandam_y = [4.658611298, 4.813611031, 4.656666756]
zaandam_2_x = [52.64472198, 52.43888855]
zaandam_2_y = [5.055555344, 4.813611031]
leiden_x = [52.35916519, 52.16611099, 52.12444305]
leiden_y = [4.606666565, 4.481666565, 4.657777786]
leiden_2_x = [52.30944443, 52.16611099]
leiden_2_y = [4.761944294, 4.481666565]
gouda_x = [52.01750183, 52.12444305]
gouda_y = [4.704444408, 4.657777786]
heemsae_x = [52.35916519, 52.38777924]
heemsae_y = [4.606666565, 4.638333321]
roffa_a_x = [51.95194626, 52.01750183]
roffa_a_y = [4.553611279, 4.704444408]
schiedam_x = [51.92124381, 52.00666809]
schiedam_y = [4.408993721, 4.356389046]


plt.scatter(x=df['x'], y=df['y'], s=10, c='yellow', edgecolors='blue', linewidths=1)
[plt.text( x=row['x'] + 0.005, y=row['y'], s=row['station'], fontsize=7) for k, row in df.iterrows()]
plt.plot(alkmaar_y, alkmaar_x, color='blue', linestyle='dashed')
plt.plot(ams_amstel_y, ams_amstel_x, color='blue', linestyle='dashed')
plt.plot(ams_cs_y, ams_cs_x, color='blue', linestyle='dashed')
plt.plot(ams_sloterdijk_y, ams_sloterdijk_x, color='blue', linestyle='dashed')
plt.plot(ams_zuid_y, ams_zuid_x, color='blue', linestyle='dashed')
plt.plot(beverwijk_y, beverwijk_x, color='blue', linestyle='dashed')
plt.plot(castricum_y, castricum_x, color='blue', linestyle='dashed')
plt.plot(dh_cs_y, dh_cs_x, color='blue', linestyle='dashed')
plt.plot(dh_2_y, dh_2_x, color='blue', linestyle='dashed')
plt.plot(roffa_cs_y, roffa_cs_x, color='blue', linestyle='dashed')
plt.plot(roffa_2_y, roffa_2_x, color='blue', linestyle='dashed')
plt.plot(zaandam_y, zaandam_x, color='blue', linestyle='dashed')
plt.plot(zaandam_2_y, zaandam_2_x, color='blue', linestyle='dashed')
plt.plot(leiden_y, leiden_x, color='blue', linestyle='dashed')
plt.plot(leiden_2_y, leiden_2_x, color='blue', linestyle='dashed')
plt.plot(gouda_y, gouda_x, color='blue', linestyle='dashed')
plt.plot(heemsae_y, heemsae_x, color='blue', linestyle='dashed')
plt.plot(roffa_a_y, roffa_a_x, color='blue', linestyle='dashed')
plt.plot(schiedam_y, schiedam_x, color='blue', linestyle='dashed')

# plt.ylim(51.75, 53)
# plt.xlim(4.2, 5.1)
plt.title('Visualisation of train stations')
plt.xlabel('latitude')
plt.ylabel('longitude')


plt.show()
