class Station:
    
    def __init__(self, name, coord_y, coord_x):
        self.name = name
        self.coord_y = coord_y
        self.coord_x = coord_x
        self.connections = {}
        
    
    def is_neighbor(self, other: Station) -> bool:
        return self._id in other._connections and other._id in self._connections

    def __repr__(self) -> str:
        pass
