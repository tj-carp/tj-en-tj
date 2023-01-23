import matplotlib.pyplot as plt

def visualise(railmap, connections):

    x_coords_map = []
    y_coords_map = []

    for connection in connections:
        connection = connections[connection]
        x_route_map = []
        y_route_map = []
        x_route_map.append(connection.station1.coords[1])
        y_route_map.append(connection.station1.coords[0])
        x_route_map.append(connection.station2.coords[1])
        y_route_map.append(connection.station2.coords[0])
        plt.plot(x_route_map, y_route_map, color='grey', linestyle='dashed', linewidth=1)
        plt.scatter(x_coords_map, y_coords_map)

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
    plt.savefig("output/randomise/ railmap1")
    plt.show()


def visualise_scores(scores):
    plt.plot(scores)
    plt.savefig("output/randomise/ scores")
    plt.show()
    