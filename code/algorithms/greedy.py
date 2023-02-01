from code.classes.railmap import RailMap
from code.visualisation.visualisation import run_visualise
from collections import Counter
from itertools import combinations

def run(connections):
    """
    run a gready algorithm
    """
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


def extend_route(route, current_connection, railmap):
    """
    extend the given route with the given connection
    """
    railmap.visited.append(current_connection)
    # Note that the current_connection has been placed on the map 
    current_connection.set_visited()
    print(current_connection.distance)
    # Increase the length of the route with the distance of the appended
    route.length += current_connection.distance
    print(route.length)
    route.route.append(current_connection)
    print('run', route.route)
    
def next_connection(current_station, route, connections_per_station):
    """
    return the given station's connection with the highest distance which is not placed on the map yet
    """
    for connection in connections_per_station[current_station]:
        if connection.visited == False:
            return connection

def create_route(route, current_station, current_connection, railmap, connections_per_station):
    """
    create a route object filled with connections
    """
    # determine which station is the new tail of the route
    next_station = lambda station1, station2: station1 if station2 == current_station else station2
    
    # extend the route with connections untill the tail station of the route has no more connections to choose from
    while True:
        current_station = next_station(current_connection.station1, current_connection.station2)
        current_connection = next_connection(current_station, route.route, connections_per_station)  
        if current_connection == None:
            break
        elif route.length + current_connection.distance >= route.max_length:
            for j in reversed(connections_per_station[current_station][:-1]):
                if route.length + j.distance <= route.max_length and j.visited == False:
                    extend_route(route, j, railmap)
            break
        else:
            extend_route(route, current_connection, railmap)
    
    # increase the railmap time indicator with the length of the created route
    railmap.minutes += route.length         
    
    railmap.routes.append(route)

def create_railmap(connections):
    """
    create a railmap object filled with routes
    """
    connections = connections.values()

    # make a dictionary with all the stations as keys and its corresponding connections
    # for each station the connections are orderd by the value of the 'distance' attribute

    connections_per_station = dict(map(lambda station: (station, sorted(list(filter(lambda connection: connection.station1 == station or connection.station2 == station, connections)),\
                                key = lambda connection: connection.distance, reverse=False)),\
                                set(sum((list(map(lambda connection: connection.station1, connections)), list(map(lambda connection: connection.station2, connections))), []))))

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
    
        if current_connection != None:
            # extend the route of the railmap with the initial connection
            extend_route(route, current_connection, railmap)
            # initiate the algorithm that adds connections to a route untill the maximal length has been reached
            create_route(route, current_station, current_connection, railmap, connections_per_station)

    # returns the stations that have only one unplaced connection left
    def unsaturated_stations():
        return list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).keys())

    max_am_routes = (7 if len(connections) == 28 else 20)

    def route_max(routes, max = max_am_routes):
        # returns whether the maximum amount of routes has been reached
        return len(routes) < max 

    unsat_stats = unsaturated_stations()

    # Add routes to the railmap untill either the maximum amount of routes has been reached or when there are no more stations with one unplaced connection
    while unsat_stats and route_max(railmap.routes):

        # get the corresponding connections to the the stations that have only one unplaced connection left
        final_limbs = sum(list(map(lambda station: list(filter(lambda connection: connection.visited == False ,connections_per_station[station])), unsat_stats)),[])

        # stop temporarily adding routes when the current unsat_stats is depleaded
        while route_max(railmap.routes) and len(unsat_stats) != 0:
            current_station = unsat_stats.pop()
            route = railmap.create_route()
            route.route.append(final_limbs.pop())
            create_route(route, current_station, route.route[0], railmap, connections_per_station)

        # update unsat_stats
        unsat_stats = unsaturated_stations()

    for c in connections:
        c.visited = False

    return railmap