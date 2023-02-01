import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np 
from datetime import datetime
import os
from copy import deepcopy

def visualise(railmap, connections, output_folder):

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
    plt.savefig(f"{output_folder}/railmap.png")
    plt.show()
    plt.close()

    
def visualise_scores(scores, output_folder):
    """
    creates a histogram of distribution of scores
    """

    # make histogram
    plt.hist(scores, bins=50)
    plt.xlabel("Score on objective function")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of scores")

    # save output
    plt.savefig(f"{output_folder}/histogram.png")
    print(f"saved file as histogram")
    plt.show()
    plt.close()

def vis_progress(scores, tries, output_folder):
    x = [i for i in range(tries)]
    sorted_scores = deepcopy(scores)
    sorted_scores.sort()
    y = [scores[i] for i in range(tries)]
    plt.plot(x, y)
    plt.xlabel("Number of tries")
    plt.ylabel("Best score")
    plt.ylim(2000, 10000)
    plt.title(f"Progress of scores")
    plt.savefig(f"{output_folder}/progress.png")
    print(f"output saved as progress")
    plt.show()
    plt.close()

def run_visualise(railmap, connections, algorithm, scores, tries, result):
    """
    calls all visualisation functions
    """

    now = str(datetime.now())
    output_folder = f"output/{algorithm}/folder {now}"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    visualise(railmap, connections, output_folder)
    visualise_scores(scores, output_folder)
    vis_progress(scores, tries, output_folder)
    save_output(result, output_folder)

def save_output(result, output_folder):
    f = open(f"{output_folder}/output.txt", 'w+')
    f.write(result)
    f.close()
