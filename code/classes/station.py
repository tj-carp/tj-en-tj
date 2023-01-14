class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coord_y = coord_y
        self.coord_x = coord_x
        self.connections = {}
        
    
    def add_connection(self, station, distance):
        self.connections.update({station : distance})


    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.name, self.coord_y, self.coord_x, self.connections}"
