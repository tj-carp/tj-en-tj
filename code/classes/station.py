class Station:
    
    def __init__(self, name: str):
        self._name = name
        self._adjacents = {}#{i.station1 : i.distance for i in df.itertuples() if i.station2 == name}
        # for i in df.itertuples():
        #     if i.station1 == name:
        #         self._adjacents[i.station2] = i.distance
            