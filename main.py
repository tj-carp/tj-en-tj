from code.classes.graph import Graph
from code.algorithms import randomise


if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # read connections
    connections = Graph(stations_file, connections_file).connections

    # use connections read to create random railmap
    random_railmap = randomise.create_railmap(connections)
    print(random_railmap)
