class Route:
    def __init__(self, connections):
        self.connections = connections
        self.route = []
        self.ids = []
        self.current_connection = 0
        self.length = 0
        # check whether holland or national map to determine maximum and minimum allowed route length in minutes
        self.max_length = 120 if len(connections) == 28 else 180

    def add_connection(self, connection_id):
        """
        add a connection to the route
        """
        connection = self.connections[connection_id]

        # check if connection is first in route
        if not self.route:
            self.route.append(connection)
            connection.visited = True
            self.length += connection.distance
            self.ids.append(connection_id)
            self.current_connection = connection
            return
        # check if connected
        if not connection.check_connection(self.current_connection):
            # print("no connection")
            return
        # check if connection will not make route exceed length
        if self.length + connection.distance > self.max_length:
            return

        # add station and make it the current station in the route
        self.route.append(connection)
        connection.visited = True
        self.length += connection.distance
        self.ids.append(connection_id)
        self.current_connection = connection

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        rep = ''
        for i, connection in enumerate(self.route):
            if i == (len(self.route) - 1):
                rep += f"{connection}"
            else:
                rep += f"{connection}, "

        return rep
