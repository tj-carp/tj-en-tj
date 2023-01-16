class Route:
    
    def __init__(self, stations):
        self.route = []
        self.stations = stations
        self.length = 0


    def add_station(self, station):
        """
        add a station to the route
        """
        
        self.route.append(station)

    




# route: lijst met nodes - waarbij tot 120 minuten stations die een verbinding met elkaar hebben in kunnen. uit de verbindingen geen station die al in de lijst staat. voor functie?
# met een variabele om de hoeveelheid (cumulatieve) minuten in bij te houden 
# in route functie om stations toe te voegen/te kiezen ?
# self.connection: dict of connections (class) object?