class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coords = (coord_y, coord_x)
        self.connections = {}
        
    
    def add_connection(self, station, distance):
        self.connections.update({station : distance})


    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.name, self.coords, self.connections}"
