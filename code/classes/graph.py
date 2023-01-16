import csv

from .station import Station


class Graph():
    def __init__(self, stations_file, connections_file):
        self.stations = self.load_stations(stations_file)
        self.load_connections(connections_file)

        
    def load_stations(self, stations_file):
        """
        load all the stations into the graph
        """
        stations = {}
        with open(stations_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(row['y'], row['x'])

        return stations


    def load_connections(self, connections_file):
        """
        load all the connections into the loaded stations
        """
        with open(connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                for station in self.stations:
                    if row['station1'] == station:
                        self.stations[station].add_connection(row['station2'], int(row['distance']))
                    if row['station2'] == station:
                        self.stations[station].add_connection(row['station1'], int(row['distance']))