from code.classes.railmap import RailMap

def extend_route(route, current_connection):
    route.route.append(current_connection)
    route.length += current_connection.distance

def create_railmap(connections):

    connections = connections.values()

    # uniques = set(sum((list(map(lambda connection: connection.station1, connections)),
    #                list(map(lambda connection: connection.station2, connections))), []))

    connections_per_station = dict(map(lambda station: (station, sorted(list(filter(lambda connection: connection.station1 == station or connection.station2 == station, connections)),key = lambda connection: connection.distance)),set(sum((list(map(lambda connection: connection.station1, connections)), list(map(lambda connection: connection.station2, connections))), []))))

    # for i in connections_per_station.keys():
    #    print(i)

    # stations= sum((list(map(lambda connection: connection.station1, connections)),
    #               list(map(lambda connection: connection.station2, connections))), [])

    # single_stations = list(filter(lambda station: stations.count(station) == 1,stations))

    single_stations = list(dict(filter(lambda item: len(item[1]) == 1, connections_per_station.items())).keys())

    railmap = RailMap(connections)

    next_station = lambda station1, station2: station1 if station1 == current_station else station2

    # next_connection = lambda current_station: connections_per_station[current_station][-1]

    for i in range(2):
        route = railmap.create_route()
        current_station = single_stations.pop()
        current_connection = connections_per_station[current_station][-1]
        extend_route(route, current_connection)
        
        while True:
            current_station = next_station(current_connection.station1, current_connection.station2)
            current_connection = connections_per_station[current_station][-1]
            if route.length + current_connection.distance >= 120:
                break
            extend_route(route, current_connection)   
        for i in route.route:
            print(i)         
        railmap.routes.append(route)

        #connectables = list(filter(lambda connection: connection.station1 == single or connection.station2 == single, connections))


         
    return railmap