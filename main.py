from code.classes.graph import Graph
from code.classes.route import Route
import random

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # # read stations
    # stations = Graph(stations_file, connections_file).stations

    # read connections
    test_connections = Graph(stations_file, connections_file).connections

    print(test_connections)

    # # check if stations loaded correctly
    # for station in stations:
    #     print (stations[station])

    # # create empty route
    # test_route = Route(stations)

    # # create random route of at least 20 minutes
    # random_station = random.choice(list(stations.keys()))
    
    # while test_route.length < 20:            
    #     test_route.add_station(stations[random_station])
    #     random_station = random.choice(list(stations.keys()))

    # print(f"Here's a random route of at least 20 minutes: {test_route.get_route()}")

    # # create random route
    # 
    # random_station = random.choice(list(stations.keys()))
    
    # while len(test_route.route) < 5:            
    #     test_route.add_station(stations[random_station])
    #     random_station = random.choice(list(stations.keys()))
    
    # print(f"Here's a random route of 5 stations: {test_route.get_route()}")
