from code.classes.route import Route
import random

class RailMap:
    
    def __init__(self, connections):
        self.connections = connections
        self.routes = []
        # cumulative minutes
        self.minutes = 0
        # 
        self.visited = []

    def create_railmap(self):
        while len(self.routes) < 7:
            #create empty route
            route = Route(self.connections)

            # create random route of at least 40 minutes
            while route.length < 40:
                random_connection = random.randint(1, 28)            
                route.add_connection(random_connection)

            self.routes.append(route)
        
        print(f"Here's a random railmap of 7 routes: ")
        for id, route in enumerate(self.routes, 1):
            print(id, route)

