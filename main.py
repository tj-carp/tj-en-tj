from pandas import read_csv, unique
from code.classes import station

if __name__ == "__main__":

    map_name = "Holland"
    source_file = f"data/Stations{map_name}.csv"



# df = read_csv("ConnectiesHolland.csv")

# # print(df)

# def objective(connections, trajectories, timesum):
#     return connections / 28 * 10000 - (trajectories * 100 + Min)

# # Make a tuple of Connection instances containing the two stations and their distance
# connections = tuple(Connection(Station(x.station1), Station(x.station2), x.distance) for x in df.itertuples())

# # Get all station names from the 'station1' and 'station2' column 
# stations = sorted(df[['station1', 'station2']].values.ravel('K'))

# # Get the Stations which occur only once in stations, implying they don't have a multitude of  
# terminals = tuple(filter(lambda x: stations.count(x) == 1,stations))

# # Remove duplicates from stations
# stations = tuple(set(stations))

# # stations
# # print(terminals)

# # for i in terminals:
    
# #     while True:

# Station = node
# Trajectory = graph




# # We kunnen beginnen met een algoritme waarbij we bij een van de eindstations beginnen
# # en dan telkens een station met de meeste minuten eraan koppelen. Dit zelfde doe je bij het andere eindpunt.
# # Vevolgens probeer je van de tussengelegen stations zo lang mogelijke trajecten te maken.
# # 

# # Bovenstaande kun je ook doen door tegen een bepaalde kans stations aan je trajecten toe te voegen
# # zodat er voldoende randomisation plaatsvindt om tot verschillende oplossingen te komen.

# # Je kan ook een startoplossing nemen en kijken of 