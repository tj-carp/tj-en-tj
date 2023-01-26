from code.classes.railmap import RailMap
from copy import deepcopy
from code.algorithms import randomise
import random
import time

def create_railmap(connections):
    st = time.time()
    # create random railmap
    random_railmap = randomise.create_railmap(connections)
    connection_ids = [*range(1, len(connections) + 1)]
    unused_ids = list(set(connection_ids) - set(random_railmap.visited))
    # check whether holland or national map to determine minimum length of route
    min_length = 100 if len(connections) == 28 else 160

    best_score = random_railmap.score()
    first_score = random_railmap.score()
    print(best_score)
    better_railmap = deepcopy(random_railmap)
    best_railmap = deepcopy(random_railmap)
    new_railmap = deepcopy(random_railmap)

    for i in range(1000):
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

        # check against existing routes and swap with existing route that gives biggest score gain
        for j, route in enumerate(new_railmap.routes):
            new_railmap.minutes -= route.length
            new_railmap.visited = list(set(new_railmap.visited) - set(route.ids))
            new_railmap.routes[j] = new_route
            new_railmap.minutes += new_route.length
            new_railmap.visited += new_route.ids
            new_score = new_railmap.score()
            if new_score > best_score:
                best_score = new_score
                best_railmap = deepcopy(new_railmap)

            if i > 0:
                new_railmap = deepcopy(better_railmap)
            else:
                new_railmap = deepcopy(random_railmap)
        
        better_railmap = deepcopy(best_railmap)
        print(i, best_score)
    print(first_score)
    print(best_score)
    et = time.time()
    print (et-st)