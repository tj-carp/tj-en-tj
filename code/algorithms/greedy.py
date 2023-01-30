from code.classes.railmap import RailMap
from code.visualisation.visualisation import visualise, visualise_scores
from collections import Counter
from itertools import combinations

def run(connections):
    scores = []
    railmaps = {}
    tries = 1

    for i in range(tries):
        greedy_railmap = create_railmap(connections)
        score = greedy_railmap.score()
        railmaps.update({score : greedy_railmap})
        print(score)
        scores.append(score)

    # visualise_scores(scores)

    max_score = max(scores)
    min_score = min(scores)

    result = f"\nAmount of runs: {tries} \n----------------------------------------------------------------\n"\
             f"lowest score: {min_score}, highest score: {max_score}, average score: {round(sum(scores)/tries)}\n"\
             f"----------------------------------------------------------------\n\n"\
             f"{railmaps[max_score]}"
    print(result)
    
    #print(Counter(sum(tuple(map(lambda route: route.route,railmaps[max_score].routes)),[])))
    
    return railmaps[max_score]


def extend_route(route, current_connection, railmap):
    
    current_connection.set_visited()
    railmap.visited.append(current_connection)
    # print(current_connection.distance)
    route.length += current_connection.distance
    # print(route.length)
    route.route.append(current_connection)
    # print('run', route.route)
    
def next_connection(current_station, route, connections_per_station):
    for connection in connections_per_station[current_station]:
        if connection not in route:
            return connection
    # return connections_per_station[current_station][-1]

def create_route(route, current_station, current_connection, railmap, connections_per_station):
    next_station = lambda station1, station2: station1 if station2 == current_station else station2
    
    #try:
    while True:
        current_station = next_station(current_connection.station1, current_connection.station2)
        # print(current_station)
        current_connection = next_connection(current_station, route.route, connections_per_station) # connections_per_station[current_station][-1]
        #print(current_connection)
        #print(current_station)  
        if current_connection == None:
            break
        elif route.length + current_connection.distance >= route.max_length and current_connection.visited == False:
            # print(connections_per_station[current_station][:-1])
            for j in reversed(connections_per_station[current_station][:-1]):
                if route.length + j.distance >= route.max_length and j.visited == False:
                    extend_route(route, j, railmap)
            break
        else:
            extend_route(route, current_connection, railmap)
    #except:
    #    return
    
    # for i in route.route:
    #     print(i)
    railmap.minutes += route.length         
    # print(railmap.minutes)
    railmap.routes.append(route)
    #print('railmap.routes', len(railmap.routes))

def create_railmap(connections):
    
    connections = connections.values()

    # uniques = set(sum((list(map(lambda connection: connection.station1, connections)),
    #               list(map(lambda connection: connection.station2, connections))), []))

    connections_per_station = dict(map(lambda station: (station, sorted(list(filter(lambda connection: connection.station1 == station or connection.station2 == station, connections)),key = lambda connection: connection.distance)),set(sum((list(map(lambda connection: connection.station1, connections)), list(map(lambda connection: connection.station2, connections))), []))))

    # for i in connections_per_station.keys():
    #    print(i)

    # stations= sum((list(map(lambda connection: connection.station1, connections)),
    #               list(map(lambda connection: connection.station2, connections))), [])

    # single_stations = list(filter(lambda station: stations.count(station) == 1,stations))

    single_stations = list(dict(filter(lambda item: len(item[1]) == 1, connections_per_station.items())).keys())

    railmap = RailMap(connections)

    #next_connection = lambda current_station: connections_per_station[current_station][-1] if connections_per_station[current_station][-1] not in route.route else connections_per_station[current_station][-1]

    for i in range(len(single_stations)):
        route = railmap.create_route()
        current_station = single_stations.pop()
        current_connection = next_connection(current_station, route.route, connections_per_station) # connections_per_station[current_station][-1]
        extend_route(route, current_connection, railmap)

        create_route(route, current_station, current_connection, railmap, connections_per_station)


        #connectables = list(filter(lambda connection: connection.station1 == single or connection.station2 == single, connections))
    
    #overlap = set(filter(lambda connection: connection[1] > 1, Counter(placed).items()))
     
    # print(remnants)
    # print(overlap)
    #print(i for i in list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values()))
    #final_limbs = list(reduce(lambda a, b: a if a.visited == False else b, list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values())))
    #final_limbs = list(reduce(lambda a, b: a if a.visited == False else b, i) for i in list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values()))
    
    #find the within the stations which have only one unvisited connection left the last unvisited connection. 
    # final_limbs = set(map(lambda limb: reduce(lambda a, b: a if a.visited == False else b, limb), list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).values())))

    unsaturated_stations = list(dict(filter(lambda item: tuple(map(lambda connection: connection.visited, item[1])).count(False) == 1, connections_per_station.items())).keys())
    final_limbs = sum(list(map(lambda station: list(filter(lambda connection: connection.visited == False ,connections_per_station[station])), unsaturated_stations)),[])

    while len(railmap.routes) < 7 and len(Counter(tuple(map(lambda connection: connection.visited, connections))).keys()) > 1:
        current_station = unsaturated_stations.pop()
        route = railmap.create_route()
        #print(final_limbs)
        route.route.append(final_limbs.pop())
        create_route(route, current_station, route.route[0], railmap, connections_per_station)

    

    # placed = sum(tuple(map(lambda route: route.route, railmap.routes)),[])
    #remnants = set(filter(lambda connection: connection not in placed, connections))
    # overlap = dict(sorted(Counter(set(filter(lambda connection: placed.count(connection) == 2, placed))).items(), lambda x: (x[1], x[0])))

    route_combinations = list(combinations(railmap.routes, 2))

    #print("route_combinations", len(route_combinations))

    # chains = list()

    # for i, j in route_combinations:
    #     chain = list()
    #     for connect in i.route.copy():
    #         if connect in j.route:
    #             i.route
    #             chain.append(connect)
    #         elif chain:
    #             chains.append(chain)


    # removable_overlaps = dict(map(lambda chain: (tuple(chain),chains.count(chain)), chains))

    # #print(f'removable_overlaps {i for i in removable_overlaps}')
    
    # # removers = list()
    # for route in railmap.routes:
    #     print('route.route',route.route)
    #     for headtail in removable_overlaps:
    #         index1 = 0
    #         remover = list()
    #         len_headtail = len(headtail)
    #         for index1 in range(len(route.route)):
    #             print(index1)
    #             if route.route[index1] == headtail[0]:
                    
    #                 index2 = 0
    #                 #remover.append(route.route[index1])
    #                 print(len(route.route), len(headtail))
    #                 while route.route[index1] == headtail[min(index2, len_headtail)]:
    #                     print(index1, index2)
    #                     remover.append(headtail[index2])
    #                     index1 += 1
    #                     index2 += 1
    #                 #removers.append(remover)
    #                 break
    #             elif route.route[index1] == headtail[-1]:
    #                 index2 = 0
    #                 #remover.append(route.route[index1])
    #                 while route.route[index1] == headtail[min(index2, len_headtail)]:
    #                     remover.append(headtail[index2])
    #                     index1 -= 1
    #                     index2 += 1
    #                 #removers.append(remover)
    #                 break
    #             #index1 += 1
    #     route.route = list(filter(lambda connection: connection not in remover, route.route))
    #     remover.clear()
        
        # for remover in removers:
        #     route.remove()
            
            



    # splitter = lambda slice: sum(tuple(map(lambda connection: connection.distance, slice)))

    # for connection in overlap:
    #     i = 0
    #     for r in route:
    #         cutoff = min(route[i + 1:], route[:i], key = splitter)
    #         i += 1
    #         placed_copy = deepcopy(placed)
    #         if len(set(map(lambda connection: placed_copy.remove(connection), cutoff))) == len(connections):
    #             railmap_copy = deepcopy(railmap)
    #             for j in railmap_copy.routes:-

    for c in connections:
        c.visited = False




        

    return railmap