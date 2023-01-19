import matplotlib.pyplot as plt

def visualise(railmap):
        x_coords = []
        y_coords = []

        for route in railmap.routes:
            x_route = []
            y_route = []
            for connection in route.route:
                x_route.append(connection.station1.coords[1])
                y_route.append(connection.station1.coords[0])
                x_route.append(connection.station2.coords[1])
                y_route.append(connection.station2.coords[0])
            plt.plot(x_route, y_route, '-o')


        plt.scatter(x_coords, y_coords)
        plt.show()