from pandas import read_csv, unique
from .station import Station

df = read_csv("ConnectiesHolland.csv")

class Trajectory:
    
    def __init__(self, course: list):
        self.course = course
        self.length = len(course)
        
class Connection:
    
    def __init__(self, station1: 'Station', station2: 'Station', distance: int):
        self._station1 = station1
        self._station2 = station2
        self._distance = distance


# print(df)

connections = tuple(Connection(Station(x.station1), Station(x.station2), x.distance) for x in df.itertuples())

stations = sorted(df[['station1', 'station2']].values.ravel('K'))
terminals = tuple(filter(lambda x: stations.count(x) == 1,stations))

stations = tuple(set(stations))

# stations
# print(terminals)

#for i in 