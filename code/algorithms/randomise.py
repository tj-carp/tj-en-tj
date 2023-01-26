from code.classes.railmap import RailMap
from code.visualisation.visualisation import visualise, visualise_scores
import random

def create_railmap(connections):
    # create empty railmap
    railmap = RailMap(connections)
    connection_ids = [*range(1, len(connections) + 1)]
    # check whether holland or national map to determine maximum amount of routes in map
    max_routes = 7 if len(connections) == 28 else 20
    min_routes = 4 if len(connections) == 28 else 9
    min_length = 100 if len(connections) == 28 else 160


    # fill railmap with 4 or 9 to 7 or 20 routes
    while len(railmap.routes) < random.randint(min_routes, max_routes):
        #create empty route
        route = railmap.create_route()

        # create random route of anywhere between 100 or 160 and 120 or 180 minutes
        while route.length < random.randint(min_length, route.max_length):
            try:
                random_connection = random.choice(connection_ids)            
                route.add_connection(random_connection)
                connection_ids.remove(route.ids)
            except:
                random_connection = random.randint(1, len(connections))            
                route.add_connection(random_connection)
            
        railmap.minutes += route.length
        railmap.visited += route.ids
        railmap.routes.append(route)
    
    return railmap


def run(connections):
    scores = []
    railmaps = {}
    tries = 10000

    for i in range(tries):
        random_railmap = create_railmap(connections)
        score = random_railmap.score()
        railmaps.update({score : random_railmap})
        scores.append(score)

    visualise_scores(scores)
    scores.sort()

    max_score = scores[(len(scores) - 1)]
    min_score = scores[0]

    result = f"\nAmount of runs: {tries} \n----------------------------------------------------------------\n"\
             f"lowest score: {min_score}, highest score: {max_score}, average score: {round(sum(scores)/tries)}\n"\
             f"----------------------------------------------------------------\n\n"\
             f"{railmaps[max_score]}"
    print(result)
    visualise(railmaps[max_score], connections)
