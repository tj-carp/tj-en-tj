import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np 
from datetime import datetime

def visualise(railmap, connections):

    map = Basemap(projection='merc',
                    llcrnrlat=50.5,
                    urcrnrlat=53.5,
                    llcrnrlon=3.2,
                    urcrnrlon=7.2,
                    resolution='i')
    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color='lightgrey', lake_color='aqua')
    map.drawmapboundary(fill_color='aqua')
    map.drawmeridians(np.arange(0, 360, 30))
    map.drawparallels(np.arange(-90, 90, 30))
    map.plot([53, 54, 55, 56], [3,4,5,6], color="r")

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

        x, y = map(x_route_map, y_route_map)

        map.plot(x, y, color='grey', linestyle='dashed', linewidth=1)
        map.scatter(x, y)

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
        x, y = map(x_route, y_route)
        map.plot(x, y, '-o')

    now = str(datetime.now())
    print(f"saved file as railmap-{now}")
    map.scatter(x_coords, y_coords)
    # m.savefig(f"output/randomise/railmap-{str(now)}.jpg")
    # m.show()


    
def visualise_scores(scores):

    now = str(datetime.now())

    plt.hist(scores, bins=50)
    plt.xlabel("Score on objective function")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of scores with random for {len(scores)} tries")
    plt.savefig(f"output/randomise/histogram-{str(now)}.jpg")
    print(f"saved file as histogram-{now}")
    plt.show()