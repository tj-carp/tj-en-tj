import csv

from .station import Station


class Graph():
    def __init__(self, source_file):
        self.stations = self.load_stations(source_file)
        self.load_adjacents(source_file)

        
    def load_stations(self, source_file):
        """
        load all the stations into the graph
        """
        stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(row['station'], row['y'], row['x'])

        return stations


    # def load_adjacents(self, source_file):
    #     """
    #     load all the adjacents into the loaded stations
    #     """
    #     with open(source_file, 'r') as in_file:
    #         reader = csv.DictReader(in_file)

    #         for row in reader:
    #             adjacents = []

    #             for adjacent in row['adjacents'].split(','):
    #                 # only add if the result is not an empty string
    #                 if adjacent.strip('[] ') != '':
    #                     adjacents.append(adjacent.strip('[] '))

    #             station_id = row['id']

    #             # add the adjacent to the correct node
    #             for adjacent in adjacents:
    #                 adjacent = self.stations[adjacent]
    #                 self.stations[station_id].add_adjacent(adjacent)