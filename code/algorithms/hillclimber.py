from code.classes.railmap import RailMap
from copy import deepcopy
from code.algorithms import randomise
import random

def create_railmap(connections):
    # create random railmap
    random_railmap = randomise.create_railmap(connections)
    connection_ids = [*range(1, len(connections) + 1)]
    unused_ids = list(set(connection_ids) - set(random_railmap.visited))
    # check whether holland or national map to determine minimum length of route
    min_length = 100 if len(connections) == 28 else 160

    best_score = random_railmap.score()

    print(best_score)

    better_railmap = deepcopy(random_railmap)
    new_railmap = deepcopy(random_railmap)

    for i in range(40):
        # create a new random route of anywhere between 100 or 160 and 120 or 180 minutes
        new_route = random_railmap.create_route()

        while new_route.length < random.randint(min_length, new_route.max_length):
            try:
                random_connection = random.choice(unused_ids)            
                new_route.add_connection(random_connection)
                unused_ids.remove(random_connection)
            except:
                random_connection = random.choice(connection_ids)            
                new_route.add_connection(random_connection)

        # check against existing routes and if swapping improves score, swap

        for route in new_railmap.routes:
            new_railmap.minutes -= route.length
            new_railmap.visited = list(set(new_railmap.visited) - set(route.ids))
            route = new_route
            new_railmap.minutes = new_route.length
            new_railmap.visited += new_route.ids
            new_score = new_railmap.score()
            if new_score > best_score:
                best_score = new_score
                better_railmap = new_railmap
            new_railmap = deepcopy(random_railmap)
        
        print(best_score)
        new_railmap = deepcopy(better_railmap)    

    print(better_railmap)


    # repeat a couple times ?