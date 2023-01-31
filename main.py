from code.classes.graph import Graph
from code.visualisation.visualisation import visualise
from code.algorithms import randomise, greedy, hillclimber
from sys import argv

if __name__ == "__main__":

    # check command line arguments
    if len(argv) not in [1]:
        print("Usage: python3 main.py")
        exit(1)
    # request input to determine map name
    print("1 Holland \n2 The Netherlands")
    map_choice = input("Type here: ")
    while map_choice not in ['1', '2']:
            print("You have given invalid input. Please choose either '1' or '2'")
            map_choice = input("Type here: ")

    # choose input map name and if valid use to load data
    if map_choice == '1':
        map_name = "holland"
    elif map_choice == '2':
        map_name = "national"

    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_{map_name}_text.csv"

    # read connections from given data
    connections = Graph(stations_file, connections_file).connections

    # request input to determine which algorithm to run
    print("\nWhich algorithm do you want to run?\n1 Randomise\n2 Greedy\n3 Hillclimber\n4 Run all algorithms \n"\
        "Please note that if you chose The Netherlands, options 3 and 4 will take at least 3 hours to run ")
    alg_choice = input("Type here: ")
    while alg_choice not in ['1', '2', '3', '4']:
        print("You have given invalid input. Please choose either '1' or '2' or '3' or '4'")
        alg_choice = input("Type here: ")

    # --------------------------- Randomise ------------------------------------
    if alg_choice == '1' or alg_choice == '4':
        print("\nHow many times iterations do you want randomise to run?\nPlease note that fewer than 1000 tries may give subpar results "\
        "and more than 100.000 tries may take a while or forever")
        tries = input("Type here: ")

        while not tries.isdigit():
            print("You have given invalid input. Please choose a positive integer")
            tries = input("Type here: ")
        tries = int(tries)
        randomise = randomise.Randomise(connections, tries)

        print(f"Running randomise {tries} times...")
        
        randomise.run()
        
    # --------------------------- Greedy ---------------------------------------
    if alg_choice == '2' or alg_choice == '4':
        print("Running greedy ...")
        greedy_railmap = greedy.create_railmap(connections)
        score = greedy_railmap.score()
        visualise(greedy_railmap, connections, "greedy")
    # --------------------------- Hill Climber ---------------------------------
    if alg_choice == '3' or alg_choice == '4':
        print("Type 1 to start hillclimber off with a random railmap, or type 2 to run randomise first and start off with the best random railmap")
        start_choice = input("Type here: ")

        while start_choice not in ['1', '2']:
            print("You have given invalid input. Please choose either '1' or '2'")
            start_choice = input("Type here: ")

        print("\nHow many times iterations do you want hillclimber to run?\nPlease note that fewer than 10 tries may give subpar results "\
        "and more than 10.000 tries may take a while or forever")
        tries = input("Type here: ")

        while not tries.isdigit():
            print("You have given invalid input. Please choose a positive integer")
            tries = input("Type here: ")
        tries = int(tries)

        hillclimber = hillclimber.HillClimber(connections, start_choice, tries)
        print(f"Running hillclimber {tries} times...")
        hillclimber.run()
    