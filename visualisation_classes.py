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
        y_coord = stations[station].coords[0]
        x_coord = stations[station].coords[1]
        df.append([station, y_coord, x_coord, stations[station].connections.keys()])

    df = pd.DataFrame(df)
    df.columns = ['station', 'latitude', 'longitude', 'connections']
    print(df)

    plt.scatter(df['latitude'], df['longitude'])
    plt.xticks(rotation=90)
    # plt.ylim(51.75, 53)
    # plt.xlim(4.2, 5.1)
    plt.show()

    









    
    