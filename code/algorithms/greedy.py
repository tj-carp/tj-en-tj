from code.classes.graph import Graph
from code.classes.railmap import RailMap
from code.algorithms import randomise

# read connections
connections = Graph(stations_file, connections_file).connections

railmap = RailMap(connections)

stations = sum(set(map(lambda connection: (connection.station1, connection.station2), connections)),[])

single_stations = tuple(filter(lambda station: stations.count(station) == 1,stations))

print(single_stations)