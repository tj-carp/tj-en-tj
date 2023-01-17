class Route:
    
    def __init__(self, connections):
        self.connections = connections
        self.route = []
        self.current_connection = 0
        self.length = 0
        

    def add_connection(self, connection_id):
        """
        add a connection to the route
        """
        connection = self.connections[connection_id]

        # check if connection is first in route
        if not self.route:
            self.route.append(connection)
            connection.set_visited()
            self.current_connection = connection
            return

        # check if connected
        if not connection.check_connection(self.current_connection):
            print("not allowed")
            return
        # #check if station already in route
        # if station in self.route:
        #     return
        # # check if station will not make route exceed length
        # if self.length + self.current_station.connections[station.name] > 120:
        #     return

        # add station and make it the current station in the route
        self.route.append(station)
        self.length += self.current_station.connections[station.name]
        station.set_visited()
        self.current_station = station

    
    # def get_route(self):
    #     route_names = ''
    #     for station in self.route:
    #         if station == self.route[0]:
    #             route_names += f"{station.name}"
    #         else:
    #             route_names += f" - {station.name}"
        
    #     return f"{route_names}"
        

    def __repr__(self):
        """
        make sure that the object is printed properly if it is in a list/dict
        """
        return f"{self.route}" 
