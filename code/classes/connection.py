class Connection:
    
    def __init__(self, station1, station2, distance):
        self.station1 = station1
        self.station2 = station2
        self.distance = int(distance)
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
        return f"{self.station1, self.station2, self.distance}"