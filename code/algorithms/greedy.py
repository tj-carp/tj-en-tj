from code.classes.railmap import RailMap
from code.visualisation.visualisation import run_visualise
from collections import Counter
from itertools import combinations

def run(connections):
    tries = 1

    greedy_railmap = create_railmap(connections)
    score = greedy_railmap.score()
    scores = [score]

    result = f"\nAmount of runs: {tries} \n----------------------------------------------------------------\n"\
             f"score: {score}\n"\
             f"----------------------------------------------------------------\n\n"\
             f"{greedy_railmap}"
    print(result)

    run_visualise(greedy_railmap, connections, "greedy", scores, tries, result)
    
    return greedy_railmap


def extend_route(route, current_connection, railmap):
    
    current_connection.set_visited()
    railmap.visited.append(current_connection)
    print(current_connection.distance)
    route.length += current_connection.distance
    print(route.length)
    route.route.append(current_connection)
    print('run', route.route)
    
def next_connection(current_station, route, connections_per_station):
    for connection in connections_per_station[current_station]:
        if connection not in route:
            return connection

def create_route(route, current_station, current_connection, railmap, connections_per_station):
    next_station = lambda station1, station2: station1 if station2 == current_station else station2
    
    while True:
        current_station = next_station(current_connection.station1, current_connection.station2)
        current_connection = next_connection(current_station, route.route, connections_per_station)  
        if current_connection == None:
            break
        elif route.length + current_connection.distance >= route.max_length: # or current_connection.visited == True:
            for j in reversed(connections_per_station[current_station][:-1]):
                if route.length + j.distance <= route.max_length:# or j.visited == True:
                    extend_route(route, j, railmap)
            break
        else:
            extend_route(route, current_connection, railmap)
    
    railmap.minutes += route.length         
    
    railmap.routes.append(route)

def create_railmap(connections):
    
    connections = connections.values()

    # make a dictionary with all the stations as keys and its corresponding connections
    # for each station the connections are orderd by the value of the 'distance' attribute

    connections_per_station = dict(map(lambda station: (station, sorted(list(filter(lambda connection: connection.station1 == station or connection.station2 == station, connections)),key = lambda connection: connection.distance)),set(sum((list(map(lambda connection: connection.station1, connections)), list(map(lambda connection: connection.station2, connections))), []))))

    # find the stations that have only one connection.
    single_stations = list(dict(filter(lambda item: len(item[1]) == 1, connections_per_station.items())).keys())

    railmap = RailMap(connections)

    # for each single station ... 
    for i in range(len(single_stations)):
        # initiate a route
        route = railmap.create_route()
        # get a station that has only one connection
        current_station = single_stations.pop()
        # find the connection belonging to the single station 
        current_connection = next_connection(current_station, route.route, connections_per_station)
        # extend the route of the railmap with the initial connection
        extend_route(route, current_connection, railmap)
        # initiate the algorithm that adds connections to a route untill the maximal length has been reached
        create_route(route, current_station, current_connection, railmap, connections_per_station)

    # get the stations that have only one unplaced connection left
    unsaturated_stations = list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).keys())
    # get the corresponding connections to the 
    final_limbs = sum(list(map(lambda station: list(filter(lambda connection: connection.visited == False ,connections_per_station[station])), unsaturated_stations)),[])

    print()

    while len(railmap.routes) < (7 if len(connections) == 28 else 20) and len(Counter(tuple(map(lambda connection: connection.visited, connections))).keys()) > 1:
        current_station = unsaturated_stations.pop()
        route = railmap.create_route()
        #print(final_limbs)
        route.route.append(final_limbs.pop())
        create_route(route, current_station, route.route[0], railmap, connections_per_station)

    route_combinations = list(combinations(railmap.routes, 2))

    print("route_combinations", len(route_combinations))

    # for i in range(len(route_combinations)):
    #     chain = route_combinations[i]
    #     for k in range(min(len(chain[0].route, chain[1].route))):
    #         if chain[0].route[k] == chain[1].route[k]:
    #             chain[0].route.remove(chain[1].route[k])

    #         if chain[0].route[k] == chain[1].route[k]:
    #             chain[0].route.remove(chain[1].route[k])

    # for i,j in route_combinations:
    #     for connect in i.route.copy():
    #         if connect in j.route:
    #             i.route.remove(connect)

    get_stations = lambda route: tuple(dict(filter(lambda attr: attr == 'station1' or attr == 'station2', route.__dict__)).values())

    if len(connections) == 28:
        for i,j in route_combinations:
            print(i.length + j.length)
            if i.length + j.length <= i.max_length:
                for k in range(4):
                    x = i.route[-(k % 2)]   # 0, -1, 0, -1
                    y = j.route[-(k//2)]    # 0, 0, -1, -1
                    print(x, x.__dict__)
                    print(y, y.__dict__)
                    x_stations = get_stations(x)
                    y_stations = get_stations(x)
                    for l in x_stations:
                        for m in y_stations:
                            if l == m:
                                x.extend(y)        
           
    for c in connections:
        c.visited = False

    return railmap