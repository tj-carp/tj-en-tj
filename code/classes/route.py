class Route:
    
    def __init__(self, stations):
        self.stations = stations
        self.route = []
        self.current_station = 0
        self.length = 0
        

    def add_station(self, station):
        """
        add a station to the route
        """
        # check if station is first in route
        if not self.route:
            self.route.append(station)
            self.current_station = station
            return

        # check if station in connections
        if station.name not in self.current_station.connections.keys():
            # print("no that doesnt go there :(")
            return

        if station in self.route:
            # print("you were just there!")
            return

        # add station and make it the current station in the route
        # print("congration you did it :)")
        self.route.append(station)
        self.length += self.current_station.connections[station.name]
        # print(self.length)
        self.current_station = station
        

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.route}" 
