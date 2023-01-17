from code.classes.graph import Graph
from code.classes.route import Route
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # test if stations read
    stations = Graph(stations_file, connections_file).stations

    df = []

    for id, station in enumerate(stations):
        y_coord = float(stations[station].coords[0])
        x_coord = float(stations[station].coords[1])
        # for k in stations[station].connections.keys():
        #     print(type(k))
        df.append([station, y_coord, x_coord, stations[station].connections.keys()])

    df = pd.DataFrame(df)
    df.columns = ['station', 'latitude', 'longitude', 'connections']
    print(df)

    plt.scatter(df['longitude'], df['latitude'], s=10, c='yellow', edgecolors='blue', linewidths=1)
    [plt.text( x=row['longitude'] + 0.005, y=row['latitude'], s=row['station'], fontsize=7) for k, row in df.iterrows()]
    plt.xticks(rotation=90)
    plt.show()





    









    
    