from code.classes.graph import Graph
from code.visualisation.visualisation import visualise, visualise_scores
from code.algorithms import randomise, greedy, hillclimber
from sys import argv


if __name__ == "__main__":

    # check command line arguments
    if len(argv) not in [1]:
        print("Usage: python3 main.py")
        exit(1)
    # request input to determine map name
    print("For Holland, type 1 \nFor The Netherlands, type 2")
    map_choice = input("Type here: ")

    # choose input map name and if valid use to load data
    if map_choice == '1':
        map_name = "holland"
    elif map_choice == '2':
        map_name = "national"
    else:
        print("you have bungled it")
        exit(1)

    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_{map_name}_text.csv"

    # read connections from given data
    connections = Graph(stations_file, connections_file).connections

    # request input to determine which algorithm to run
    print("Which algorithm do you want to run?\nFor randomise, type 1\nFor greedy, type 2\nFor hillclimber, type 3\nTo run all algorithms, type 4 "\
        "[Please note that this option will take at least 3 hours to run] ")
    alg_choice = input("Type here: ")

    if alg_choice == '1' or alg_choice == '4':
        randomise = randomise.Randomise(connections)
        randomise.run()
    if alg_choice == '2' or alg_choice == '4':
        greedy_railmap = greedy.create_railmap(connections)
        score = greedy_railmap.score()
        visualise(greedy_railmap, connections)
    if alg_choice == '3' or alg_choice == '4':
        print("Type 1 to start hillclimber off with a random railmap, or type 2 to run randomise first and start off with the best random railmap")
        start_choice = input("Type here: ")
        hillclimber = hillclimber.HillClimber(connections, start_choice)
        hillclimber.run()
    elif alg_choice not in ['1', '2', '3', '4']:
        print("you have bungled it")
        exit(1)

    