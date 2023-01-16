class Route:
    
    def __init__(self, stations, start_station):
        self.stations = stations
        self.route = [start_station]
        self.current_station = start_station
        self.length = 0
        

    def add_station(self, station):
        """
        add a station to the route
        """
        #check if station in connections
        if station.name not in self.current_station.connections.keys():
            print("no that doesnt go there :(")
            return

        #add station and make it the current station in the route
        print("congration you did :)")
        self.route.append(station)
        self.length += self.current_station.connections[station.name]
        print(self.length)
        self.current_station = station
        

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.route}" 

    




# route: lijst met nodes - waarbij tot 120 minuten stations die een verbinding met elkaar hebben in kunnen. uit de verbindingen geen station die al in de lijst staat. voor functie?
# met een variabele om de hoeveelheid (cumulatieve) minuten in bij te houden 
# in route functie om stations toe te voegen/te kiezen ?
# self.connection: dict of connections (class) object?