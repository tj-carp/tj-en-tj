import csv

from .station import Station
from .connection import Connection


class Graph():
    def __init__(self, stations_file, connections_file):
        self.stations = self.load_stations(stations_file)
        self.connections = self.load_connections(connections_file)

    def load_stations(self, stations_file):
        """
        load all the stations
        """
        stations = {}
        with open(stations_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(
                    row['station'], row['y'], row['x'])

        return stations

    def load_connections(self, connections_file):
        """
        load all the connections and load stations into them

        """
        connections = {}

        with open(connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for connection_id, row in enumerate(reader, 1):
                connections[connection_id] = Connection(
                    self.stations[row['station1']], self.stations[row['station2']], int(float(row['distance'])))

        return connections
