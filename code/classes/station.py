class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coord_y = coord_y
        self.coord_x = coord_x
        self._connections = {}
        
    
    def add_connection(self, station, distance):
        self._connections.update({station : distance})

    def get_connection(self):
        return self._connections    

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return f"{self.name, self.coord_y, self.coord_x, self._connections}"
