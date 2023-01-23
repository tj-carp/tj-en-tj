from code.classes.railmap import RailMap
import random

def create_railmap(connections):
    # create empty railmap
    railmap = RailMap(connections)
    connection_ids = [*range(1, len(connections) + 1)]
    # check whether holland or national map to determine maximum amount of routes in map
    max_routes = 7 if len(connections) == 28 else 20


    # fill railmap with 4 to 7 or 20 routes
    while len(railmap.routes) < random.randint(4, max_routes):
        #create empty route
        route = railmap.create_route()

        # create random route of anywhere between 5 and 120 or 180 minutes
        while route.length < random.randint(5, route.max_length):
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
