# choose the first available connection (for previous connection if not first) to add, if it was not previously used
# if it was previously used, leave it for this trajectory
# maybe keep the last used id and keep it to avoid in the next iteration? and so on?

from code.classes.railmap import RailMap

def create_railmap(connections):
    # create empty railmap
    railmap = RailMap(connections)
    connection_ids = [*range(1, len(connections) + 1)]
    # check whether holland or national map to determine maximum amount of routes in map
    max_routes = 7 if len(connections) == 28 else 20


    # fill railmap with 7 or 20 routes
    while len(railmap.routes) < max_routes #or?:
        #create empty route
        route = railmap.create_route()

        # create random route of anywhere between 5 and 120 or 180 minutes
        while route.length < route.max_length # or until the connection has no more unused connections?:
            try:
                # new_connection = 
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

        # #check if connection already used
        # if connection_id in route.ids:
        #     print("connection already used in this route")
        #     return