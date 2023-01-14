import csv

from .station import Station


class Graph():
    def __init__(self, stations_file, connections_file):
        self.stations = self.load_stations(stations_file)
        #self.load_connections(connections_file)

        
    def load_stations(self, stations_file):
        """
        load all the stations into the graph
        """
        stations = {}
        with open(stations_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(row['station'], row['y'], row['x'])

        return stations


    # def load_connections(self, connections_file):
    #     """
    #     load all the connections into the loaded stations
    #     """
    #     with open(connections_file, 'r') as in_file:
    #         reader = csv.DictReader(in_file)

    #         for row in reader:
    #             if row['station1'] = stations['station']


                # connections = {}

                # for connection in row['connections'].split(','):
                #     # only add if the result is not an empty string
                #     if connection.strip('[] ') != '':
                #         connections.append(connection.strip('[] '))

                # station_id = row['id']

                # # add the connection to the correct node
                # for connection in connections:
                #     connection = self.stations[connection]
                #     self.stations[station_id].add_connection(connection)