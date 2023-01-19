import matplotlib.pyplot as plt

def visualise_graph(connections):
    x_coords = []
    y_coords = []

    for connection in connections:
        connection = connections[connection]
        x_route = []
        y_route = []
        x_route.append(connection.station1.coords[1])
        y_route.append(connection.station1.coords[0])
        x_route.append(connection.station2.coords[1])
        y_route.append(connection.station2.coords[0])
        plt.plot(x_route, y_route, '-o')


    plt.scatter(x_coords, y_coords)
    plt.show()