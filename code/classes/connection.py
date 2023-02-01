class Connection:
    def __init__(self, station1, station2, distance):
        self.station1 = station1
        self.station2 = station2
        self.distance = int(distance)
        self.visited = False

    def check_connection(self, connection):
        """
        check if either of the stations in this connection are connected to stations in another connection
        """
        if connection.station1.name == self.station1.name:
            return True
        if connection.station1.name == self.station2.name:
            return True
        if connection.station2.name == self.station1.name:
            return True
        if connection.station2.name == self.station2.name:
            return True

        return False

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.station1} - {self.station2}"
