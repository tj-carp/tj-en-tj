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

    railmap.plot_routes()

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
