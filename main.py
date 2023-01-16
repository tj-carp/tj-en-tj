from code.classes.graph import Graph
from code.classes.route import Route
import random

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # test if stations read
    stations = Graph(stations_file, connections_file).stations

    #print(stations)

    start_station = stations['Alkmaar']
    test_route = Route(stations)

    random_station = random.choice(list(stations.keys()))

    while test_route.length < 120:            
        test_route.add_station(stations[random_station])
        random_station = random.choice(list(stations.keys()))
    
    
    #for station in stations:
        #print (station)
        #print (stations[station].connections)
