from code.classes import graph

if __name__ == "__main__":

    map_name = "holland"
    stations_file = f"data/stations_{map_name}.csv"
    connections_file = f"data/connections_text.csv"

    # test if stations read
    test_stations = graph.Graph(stations_file, connections_file)

    for station in test_stations.stations:
        print (test_stations.stations[station])


# We kunnen beginnen met een algoritme waarbij we bij een van de eindstations beginnen
# en dan telkens een station met de meeste minuten eraan koppelen. Dit zelfde doe je bij het andere eindpunt.
# Vevolgens probeer je van de tussengelegen stations zo lang mogelijke trajecten te maken.
# 

# Bovenstaande kun je ook doen door tegen een bepaalde kans stations aan je trajecten toe te voegen
# zodat er voldoende randomisation plaatsvindt om tot verschillende oplossingen te komen