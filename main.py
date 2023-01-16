from code.classes.graph import Graph
from code.classes.route import Route

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # test if stations read
    stations = Graph(stations_file, connections_file)

    #test_route = Route(stations)
    #test_route.add_station(stations.stations[1])
    print(stations.stations['Alkmaar'])

    #for station in stations.stations:
        #print (stations.stations[station])
        #print (stations.stations[station].connections)


# We kunnen beginnen met een algoritme waarbij we bij een van de eindstations beginnen
# en dan telkens een station met de meeste minuten eraan koppelen. Dit zelfde doe je bij het andere eindpunt.
# Vevolgens probeer je van de tussengelegen stations zo lang mogelijke trajecten te maken.
# 

# Bovenstaande kun je ook doen door tegen een bepaalde kans stations aan je trajecten toe te voegen
# zodat er voldoende randomisation plaatsvindt om tot verschillende oplossingen te komen