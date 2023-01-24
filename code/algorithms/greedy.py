from code.classes.railmap import RailMap

def extend_route(route, current_connection, railmap):
    current_connection.set_visited()
    railmap.visited.append(current_connection)
    print(current_connection.distance)
    route.length += current_connection.distance
    print(route.length)
    route.route.append(current_connection)
    
def next_connection(current_station, route, connections_per_station):
    for connection in connections_per_station[current_station]:
        if connection not in route:
            return connection
    # return connections_per_station[current_station][-1]

def create_route(route, current_station, current_connection, railmap, connections_per_station):
    next_station = lambda station1, station2: station1 if station2 == current_station else station2
    try:
        while True:
            current_station = next_station(current_connection.station1, current_connection.station2)
            print(current_station)
            current_connection = next_connection(current_station, route.route, connections_per_station) # connections_per_station[current_station][-1]
            print(current_connection)
            print(current_station)  
            if route.length + current_connection.distance >= route.max_length:
                print(connections_per_station[current_station][:-1])
                for j in reversed(connections_per_station[current_station][:-1]):
                    if route.length + j.distance and j not in route.route:
                        extend_route(route, j, railmap)
                break
            else:
                extend_route(route, current_connection, railmap)
    except:
        return
    
    # for i in route.route:
    #     print(i)
    railmap.minutes += route.length         
    print(railmap.minutes)
    railmap.routes.append(route)

def create_railmap(connections):

    connections = connections.values()

    # uniques = set(sum((list(map(lambda connection: connection.station1, connections)),
    #               list(map(lambda connection: connection.station2, connections))), []))

    connections_per_station = dict(map(lambda station: (station, sorted(list(filter(lambda connection: connection.station1 == station or connection.station2 == station, connections)),key = lambda connection: connection.distance)),set(sum((list(map(lambda connection: connection.station1, connections)), list(map(lambda connection: connection.station2, connections))), []))))

    # for i in connections_per_station.keys():
    #    print(i)

    # stations= sum((list(map(lambda connection: connection.station1, connections)),
    #               list(map(lambda connection: connection.station2, connections))), [])

    # single_stations = list(filter(lambda station: stations.count(station) == 1,stations))

    single_stations = list(dict(filter(lambda item: len(item[1]) == 1, connections_per_station.items())).keys())

    railmap = RailMap(connections)

    #next_connection = lambda current_station: connections_per_station[current_station][-1] if connections_per_station[current_station][-1] not in route.route else connections_per_station[current_station][-1]

    for i in range(len(single_stations)):
        route = railmap.create_route()
        current_station = single_stations.pop()
        current_connection = next_connection(current_station, route.route, connections_per_station) # connections_per_station[current_station][-1]
        extend_route(route, current_connection, railmap)

        create_route(route, current_station, current_connection, railmap, connections_per_station)


        #connectables = list(filter(lambda connection: connection.station1 == single or connection.station2 == single, connections))
    placed = sum(tuple(map(lambda route: route.route, railmap.routes)),[])
    remnants = set(filter(lambda connection: connection not in placed, connections))
    overlap = set(filter(lambda connection: placed.count(connection) == 2, placed))
    #overlap = set(filter(lambda connection: connection[1] > 1, Counter(placed).items()))
    solutions = [railmap]
     
    # print(remnants)
    # print(overlap)
    #print(i for i in list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values()))
    #final_limbs = list(reduce(lambda a, b: a if a.visited == False else b, list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values())))
    #final_limbs = list(reduce(lambda a, b: a if a.visited == False else b, i) for i in list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values()))
    
    #find the within the stations which have only one unvisited connection left the last unvisited connection. 
    # final_limbs = set(map(lambda limb: reduce(lambda a, b: a if a.visited == False else b, limb), list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values())))

    unsaturated_stations = list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).keys())
    final_limbs = sum(list(map(lambda station: list(filter(lambda connection: connection.visited == False ,connections_per_station[station])), unsaturated_stations)),[])

    while final_limbs:
        current_station = unsaturated_stations.pop()
        route = railmap.create_route()
        #print(final_limbs)
        route.route.append(final_limbs.pop())
        create_route(route, current_station, route.route[0], railmap, connections_per_station)

    placed = sum(tuple(map(lambda route: route.route, railmap.routes)),[])
    #remnants = set(filter(lambda connection: connection not in placed, connections))
    overlap = set(filter(lambda connection: placed.count(connection) == 2, placed))


    return railmap