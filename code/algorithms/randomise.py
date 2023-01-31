from code.classes.railmap import RailMap
from code.visualisation.visualisation import visualise, visualise_scores
import random
from tqdm import tqdm
from matplotlib import pyplot as plt
from datetime import datetime
from copy import deepcopy

class Randomise():
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
        self.railmaps = {}
        self.tries = tries

    def create_railmap(self):
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
        for x, i in enumerate(range(self.tries)):
            # tdqm(x, desc="Progress")
            random_railmap = self.create_railmap()
            score = random_railmap.score()
            self.railmaps.update({score : random_railmap})
            self.scores.append(score)

        scores_copy = deepcopy(self.scores)
        scores_copy.sort()
        max_score = scores_copy[(len(self.scores) - 1)]

        best_random = deepcopy(self.railmaps[max_score])

        return best_random

    def run(self):
        self.create_best_railmap()
        
        visualise_scores(self.scores, "randomise")
        self.scores.sort()

        max_score = self.scores[(len(self.scores) - 1)]
        min_score = self.scores[0]

        result = f"\nAmount of runs: {self.tries} \n----------------------------------------------------------------\n"\
                f"lowest score: {min_score}, highest score: {max_score}, average score: {round(sum(self.scores)/self.tries)}\n"\
                f"----------------------------------------------------------------\n\n"\
                f"{self.railmaps[max_score]}"
        
        print(result)
        visualise(self.railmaps[max_score], self.connections, "randomise")
        self.visualise_Random()

    
    def visualise_Random(self):
        x = [i for i in range(self.tries)]
        y = [max(self.scores[:i+1]) for i in range(self.tries)]
        now = str(datetime.now())
        plt.plot(x, y)
        plt.xlabel("Number of tries")
        plt.ylabel("Best score")
        plt.ylim(2000, 10000)
        plt.title("Progress of Randomise")
        plt.savefig(f"output/randomise/progress of randomise-{now}.jpg")
        print(f"output saved as progress of randomise-{now}.jpg")
        plt.show()
