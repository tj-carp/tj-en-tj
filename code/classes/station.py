class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coord_y = coord_y
        self.coord_x = coord_x
        self._connections = {}
        
    
    def add_connection(self, station, distance):
        self._connections.update({station : distance})

    #def get_station(self, )

