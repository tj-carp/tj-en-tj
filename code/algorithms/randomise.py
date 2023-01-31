from code.classes.railmap import RailMap
from code.visualisation.visualisation import run_visualise
import random
from tqdm import tqdm
from copy import deepcopy

class Randomise():
    """
    Randomise class in which constraints are determined depending on map size,
    one random railmap can be created with those parameters, or random railmaps
    with those parameters can be created tries amount of times
    """
    def __init__(self, connections, tries):
        self.connections = connections
        # create connections ids list
        self.connection_ids = [*range(1, len(self.connections) + 1)]
        # check whether holland or national map to determine maximum amount of routes in map
        self.max_routes = 7 if len(self.connections) == 28 else 20
        self.min_routes = 4 if len(self.connections) == 28 else 9
        self.min_length = 100 if len(self.connections) == 28 else 160
        # for best railmap
        self.scores = []
        self.sorted_scores = []
        self.railmaps = {}
        self.tries = tries

    def create_railmap(self):
        """
        create a random railmap
        """
        # create empty railmap
        railmap = RailMap(self.connections)
        # fill railmap with 4 or 9 to 7 or 20 routes
        while len(railmap.routes) < random.randint(self.min_routes, self.max_routes):
            #create empty route
            route = railmap.create_route()

            # create random route of anywhere between 100 or 160 and 120 or 180 minutes
            while route.length < random.randint(self.min_length, route.max_length):
                try:
                    random_connection = random.choice(self.connection_ids)            
                    route.add_connection(random_connection)
                    self.connection_ids.remove(route.ids)
                except:
                    random_connection = random.randint(1, len(self.connections))            
                    route.add_connection(random_connection)
    
            railmap.minutes += route.length
            railmap.visited += route.ids
            railmap.routes.append(route)
        
        return railmap

    def create_best_railmap(self):
        """
        run randomise tries amount of times, save all results and return best of random railmaps
        """
        # show progress bar and run randomise tries amount of times
        for item in tqdm(range(self.tries)):
            random_railmap = self.create_railmap()
            score = random_railmap.score()
            self.railmaps.update({score : random_railmap})
            self.scores.append(score)

        # sort scores to find highest score
        self.sorted_scores = deepcopy(self.scores)
        self.sorted_scores.sort()
        max_score = self.sorted_scores[(len(self.sorted_scores) - 1)]

        # use highest score to find best railmap
        best_random = deepcopy(self.railmaps[max_score])

        return best_random

    def run(self):
        """
        run random algorithm to get best random railmap and produce, save and show results
        """
        best_random = self.create_best_railmap()
        
        max_score = self.sorted_scores[(len(self.sorted_scores) - 1)]
        min_score = self.sorted_scores[0]

        result = f"\nAmount of runs: {self.tries} \n----------------------------------------------------------------\n"\
                f"lowest score: {min_score}, highest score: {max_score}, average score: {round(sum(self.scores)/self.tries)}\n"\
                f"----------------------------------------------------------------\n\n"\
                f"{best_random}"

        print(result)

        run_visualise(best_random, self.connections, "randomise", self.scores, self.tries, result)
