import matplotlib.pyplot as plt

def plot_routes(self):
        x_coords = []
        y_coords = []

        for route in self.routes:
            x_route = []
            y_route = []
            for connection in route.route:
                x_route.append(connection.station1.coords[1])
                y_route.append(connection.station1.coords[0])
                x_route.append(connection.station2.coords[1])
                y_route.append(connection.station2.coords[0])
                x_coords.append(connection.station1.coords[1])
                y_coords.append(connection.station1.coords[0])
                x_coords.append(connection.station2.coords[1])
                y_coords.append(connection.station2.coords[0])
            plt.plot(x_route, y_route, '-o')


        plt.scatter(x_coords, y_coords)
        plt.show()