from code.classes.graph import Graph
from code.classes.route import Route

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # test if stations read
    stations = Graph(stations_file, connections_file).stations

    print(stations)

    #start_station = stations['Alkmaar']
    #test_route = Route(stations, start_station)
    #test_route.add_station(stations['Alkmaar'])
    #print(test_route)
    #test_route.add_station(stations['Castricum'])

    #for station in stations:
        #print (station)
        #print (stations[station].connections)


# We kunnen beginnen met een algoritme waarbij we bij een van de eindstations beginnen
# en dan telkens een station met de meeste minuten eraan koppelen. Dit zelfde doe je bij het andere eindpunt.
# Vevolgens probeer je van de tussengelegen stations zo lang mogelijke trajecten te maken.
# 

# Bovenstaande kun je ook doen door tegen een bepaalde kans stations aan je trajecten toe te voegen
# zodat er voldoende randomisation plaatsvindt om tot verschillende oplossingen te komen