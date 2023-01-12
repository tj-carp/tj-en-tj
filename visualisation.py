import matplotlib.pyplot as plt
import pandas as pd

# import csv data
df = pd.read_csv("StationsHolland.csv")
df_verbindingen = pd.read_csv("verbindingen_geo.csv")

# maak coordinaten voor alle verbindingen
x1 = df_verbindingen.iloc[:, 1]
y1 = df_verbindingen.iloc[:, 0]
x2 = df_verbindingen.iloc[:, 3]
y2 = df_verbindingen.iloc[:, 2]
xy1 = pd.concat([y1, x1], axis=1)
xy2 = pd.concat([y2, x2], axis=1)


# debugging 
# print("DF: ")
# print(df.head)

# print("x 1: ")
# print(x1)
# print("y 1: ")
# print(y1)
# print("x 2: ")
# print(x2)
# print("y 2: ")
# print(y2)
# print("xy 1: ")
# print(xy1)
# print("xy 2: ")
# print(xy2)


plt.scatter(x=df['x'], y=df['y'], s=10, c='yellow', edgecolors='blue', linewidths=1)
[plt.text( x=row['x'] + 0.005, y=row['y'], s=row['station'], fontsize=7) for k, row in df.iterrows()]
# plt.plot()
plt.ylim(51.75, 53)
plt.title('Visualisation of train stations')
plt.xlabel('latitude')
plt.ylabel('longitude')


plt.show()