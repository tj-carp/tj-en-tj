from code.classes.route import Route

class RailMap:
    
    def __init__(self, connections):
        self.connections = connections
        self.routes = []
        # cumulative minutes
        self.minutes = 0
        # connections used in railmap overall
        self.visited = []

    def create_route(self):
        """
        create an empty route object
        """
        route = Route(self.connections)
        return route

    def score(self):
        """
        calculate the quality score of railmap
        """
        fraction = len(self.connections)

        # calculate fraction of connections used
        p = 1/fraction * len(set(self.visited))

        T = len(self.routes)
        Min = self.minutes
        K = p * 10000 - (T * 100 + Min)
        
        return int(K)


    def __repr__(self):
        """
        make sure that the object is printed properly
        """
        rep = "Railmap: "
        
        for id, route in enumerate(self.routes, 1):
            rep += f"\n{id} {route}"
            
        rep += f"\nIts total length is {self.minutes} minutes"
        rep += f"\nIts score is {self.score()}"

        return rep
