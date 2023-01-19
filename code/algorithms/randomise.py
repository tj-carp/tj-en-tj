from code.classes.railmap import RailMap
import random

def create_railmap(connections):
    # create empty railmap
    railmap = RailMap(connections)
    connection_ids = [*range(1, 29)]
    
    # fill railmap with 4 to 7 routes
    while len(railmap.routes) < random.randint(4,7):
        #create empty route
        route = railmap.create_route()

        # create random route of anywhere between 5 and 120 minutes
        while route.length < random.randint(5, 120):
            try:
                random_connection = random.choice(connection_ids)            
                route.add_connection(random_connection)
                connection_ids.remove(route.ids)
            except:
                random_connection = random.randint(1, 28)            
                route.add_connection(random_connection)
            
        railmap.minutes += route.length
        railmap.visited += route.ids
        railmap.routes.append(route)
    
    return railmap
