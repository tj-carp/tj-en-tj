import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("StationsHolland.csv")

print(df.head())



plt.scatter(x=df['x'], y=df['y'], s=10, c='yellow', edgecolors='blue', linewidths=1)
[plt.text( x=row['x'] + 0.005, y=row['y'], s=row['station'], fontsize=7) for k, row in df.iterrows()]
plt.ylim(51.75, 53)
plt.title('Visualisation of train stations')
plt.xlabel('latitude')
plt.ylabel('longitude')

# plt.text(x=df['x'], y=df['y'], )
plt.show()