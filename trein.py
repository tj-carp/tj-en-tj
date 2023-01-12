from pandas import read_csv, unique

df = read_csv("ConnectiesHolland.csv")

class Traject:
    
    def __init__(self, course: list):
        self.course = course
        self.length = len(course)
        
class Connection:
    
    def __init__(self, station1: 'Station', station2: 'Station', distance: int):
        self._station1 = station1
        self._station2 = station2
        self._distance = distance

class Station:
    
    def __init__(self, name: str):
        self._name = name
        self._adjacents = {i.station1 : i.distance for i in df.itertuples() if i.station2 == name}
        for i in df.itertuples():
            if i.station1 == name:
                self._adjacents[i.station2] = i.distance
            
# print(df)

connections = tuple(Connection(Station(x.station1), Station(x.station2), x.distance) for x in df.itertuples())

stations = sorted(df[['station1', 'station2']].values.ravel('K'))
terminals = tuple(filter(lambda x: stations.count(x) == 1,stations))

stations = tuple(set(stations))

# stations
# print(terminals)

#for i in 