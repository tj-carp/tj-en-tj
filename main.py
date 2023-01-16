from code.classes.graph import Graph
from code.classes.route import Route
import random

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # read stations
    stations = Graph(stations_file, connections_file).stations

    # check if stations loaded correctly
    for station in stations:
        print (stations[station])

    # create empty route
    test_route = Route(stations)


    # create random route of at least 20 minutes
    random_station = random.choice(list(stations.keys()))
    
    while test_route.length < 20:            
        test_route.add_station(stations[random_station])
        random_station = random.choice(list(stations.keys()))


    # create random route of at least 4 stations
    random_station = random.choice(list(stations.keys()))
    
    while len(test_route.route) < 4:            
        test_route.add_station(stations[random_station])
        random_station = random.choice(list(stations.keys()))
