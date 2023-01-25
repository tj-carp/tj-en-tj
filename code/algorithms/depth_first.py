# choose the first available connection (for previous connection if not first) to add, if it was not previously used
# if it was previously used, leave it for this trajectory
# maybe keep the last used id and keep it to avoid in the next iteration? and so on?

# or: given a starting point (first connection in collection connections):
# look through all connections and pick out the ones that have matching stations and from these choose the first
# save the last connection in the route in a list and remove it
# call the same function again but now the previous second connection will be the first
# repeat until having filled a railmap
# once the railmap is full, keep running the function. for every new route made, consider how
# for each of the current routes if replacing it with the new route would improve the score
# replace the route by which the score will be improved the most
# repeat until having iterated through all


# or: pick first connection from collection. then add the first one after that which is possible to add
# and so on until having a full route
# copy this route and try a different connection for the last part of the route
# repeat above until having tried all options ?


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