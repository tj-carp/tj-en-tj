class Route:
    
    def __init__(self, stations):
        self.route = []
        self.stations = stations
        self.length = 0


    def add_station(self, station):
        """
        add a station to the route
        """
        if not self.route:
            self.route.append(station)
            self.current_station = station
        
        elif station in self.stations:
            print(f"{self.current_station}")
        

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.route}" 

    




# route: lijst met nodes - waarbij tot 120 minuten stations die een verbinding met elkaar hebben in kunnen. uit de verbindingen geen station die al in de lijst staat. voor functie?
# met een variabele om de hoeveelheid (cumulatieve) minuten in bij te houden 
# in route functie om stations toe te voegen/te kiezen ?
# self.connection: dict of connections (class) object?