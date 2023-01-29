from code.classes.graph import Graph
from code.visualisation.visualisation import visualise, visualise_scores
from code.algorithms import randomise, greedy, hillclimber
from sys import argv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":

    # check command line arguments
    if len(argv) not in [1]:
        print("Usage: python3 main.py")
        exit(1)
    # request input to determine map name
    print("For Holland, type 1 \nFor The Netherlands, type 2")
    choice = input("Type here: ")

    # choose input map name and if valid use to load data
    if choice == '1':
        map_name = "holland"
    elif choice == '2':
        map_name = "national"
    else:
        print("you have bungled it")
        exit(1)

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