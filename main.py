from code.classes.graph import Graph
from code.classes.railmap import RailMap
from code.algorithms import randomise


if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # read connections
    connections = Graph(stations_file, connections_file).connections

    railmap = RailMap(connections)

    railmap.create_railmap()

    railmap.plot_routes()


    # route.add_connection(2)
    # route.add_connection(1)

    # print(route)

    # # check if connections loaded correctly
    # for connection in connections:
    #     print (connections[connection])

    # # create random route of at least 20 minutes
    # random_connection = random.randint(1, 28)
    
    # while route.length < 40:            
    #     route.add_connection(random_connection)
    #     random_connection = random.randint(1, 28)

    # print(f"Here's a random route of at least 20 minutes: {route}")

    # # create random route
    # 
    # random_station = random.choice(list(stations.keys()))
    
    # while len(test_route.route) < 5:            
    #     test_route.add_station(stations[random_station])
    #     random_station = random.choice(list(stations.keys()))
    
    # print(f"Here's a random route of 5 stations: {test_route.get_route()}")
    # use connections read to create random railmap
    random_railmap = randomise.create_railmap(connections)
    print(random_railmap)

    # implement quality formula
    # calculate fraction of connections used
    p = 1/28 * len(set(random_railmap.visited))
    T = len(random_railmap.routes)
    Min = random_railmap.minutes
    K = p * 10000 - (T * 100 + Min)
    print(f"Its score is {int(K)}")
