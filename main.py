from code.classes.graph import Graph
from code.visualisation.visualisation import visualise, visualise_scores
from code.algorithms import randomise, greedy, hillclimber
from sys import argv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":

    # check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python3 main.py [area]")
        exit(1)
    # load the requested map or else holland
    if len(argv) == 2:
        map_name = argv[1]
    elif len(argv) == 1:
        map_name = "holland"

    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_{map_name}_text.csv"

    # read connections from given data
    connections = Graph(stations_file, connections_file).connections


    # --------------------------- Random ---------------------------------------

    randomise.run(connections)
    
    # --------------------------- Greedy ---------------------------------------

    # greedy_railmap = greedy.create_railmap(connections)
    # score = greedy_railmap.score()
    # visualise(greedy_railmap, connections)

   # --------------------------- Hillclimber ------------------------------------

    #hillclimber.create_railmap(connections)