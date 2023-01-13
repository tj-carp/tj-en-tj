class Connection:
    
    def __init__(self, station1: 'Station', station2: 'Station', distance: int):
        self._station1 = station1
        self._station2 = station2
        self._distance = distance