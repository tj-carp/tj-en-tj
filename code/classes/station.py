class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coords = (coord_y, coord_x)
        self.connections = {}
        self.visited = False
        
    # add a connection to station
    def add_connection(self, station, distance):
        self.connections.update({station : distance})

    # change if station has been used in route
    def set_visited(self):
        self.visited = True

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.name, self.coords, self.connections}"
