from code.classes.route import Route
from code.visualisation.visualise_railmap import plot_routes
import matplotlib.pyplot as plt
import random



class RailMap:
    
    def __init__(self, connections):
        self.connections = connections
        self.routes = []
        # cumulative minutes
        self.minutes = 0
        # connections used in railmap overall
        self.visited = []

    def create_route(self):
        route = Route(self.connections)
        return route

    def __repr__(self):
        """
        Make sure that the object is printed properly
        """
        rep = "Here's a railmap: "
        
        for id, route in enumerate(self.routes, 1):
            rep += f"\n{id} {route}"
            
        rep += f"\nIts total length is {self.minutes} minutes"
        return rep

    def plot_routes(self):
        plot_routes(self)
    