class Station:
    
    def __init__(self, name: str, uid: int):
        self._name = name
        self._id = uid
        self._adjacents = {}#{i.station1 : i.distance for i in df.itertuples() if i.station2 == name}
        
        # for i in df.itertuples():
        #     if i.station1 == name:
        #         self._adjacents[i.station2] = i.distance
    
    def is_neighbor(self, other: Station) -> bool:
        return self._id in other._adjacents and other._id in self._adjacents

    def __repr__(self) -> str:
        pass
