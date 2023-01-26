from code.classes.railmap import RailMap
from copy import deepcopy
import randomise
import random

def create_railmap(connections):
    # create random railmap
    random_railmap = randomise.create_railmap(connections)
    connection_ids = [*range(1, len(connections) + 1)]
    unused_ids = list(set(connection_ids) - set(random_railmap.visited))
    # check whether holland or national map to determine minimum length of route
    min_length = 100 if len(connections) == 28 else 160

    best_score = random_railmap.score()

    # create a new random route of anywhere between 100 or 160 and 120 or 180 minutes
    new_route = random_railmap.create_route()

    while new_route.length < random.randint(min_length, new_route.max_length):
        try:
            random_connection = random.choice(unused_ids)            
            new_route.add_connection(random_connection)
            unused_ids.remove(random_connection)
        except:
            random_connection = random.randint(connection_ids)            
            new_route.add_connection(random_connection)

    # check against existing routes and if swapping improves score, swap
    better_railmap = deepcopy(random_railmap)
    
    for route in random_railmap.routes:
        new_railmap = deepcopy(random_railmap)
        new_railmap.minutes -= route.length
        new_railmap.visited -= route.ids
        new_railmap.routes[route] = new_route
        new_railmap.minutes += new_route.length
        new_railmap.visited += new_route.ids
        new_score = new_railmap.score()
        if new_score > best_score:
            best_score = new_score
            better_railmap = new_railmap
    
    return better_railmap


    # repeat a couple times ?