def create_railmap(connections):

    stations = sum(set(map(lambda connection: (connection.station1, connection.station2), connections)),[])

    single_stations = tuple(filter(lambda station: stations.count(station) == 1,stations))

    return single_stations