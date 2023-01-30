from copy import deepcopy
from code.algorithms import randomise
from code.visualisation.visualisation import visualise, visualise_scores
from matplotlib import pyplot as plt
import random
from datetime import datetime
import time


class HillClimber:
    """
    HillClimber class in which a new random route is created for i iterations and
    checked against existing routes in a random railmap - the best swap will be chosen 
    and the next iteration will be executed according to the improved railmap or remain
    the same if no improvements on score are made
    """
    def __init__(self, connections, start_choice, tries):
        self.connections = connections
        self.connection_ids = [*range(1, len(self.connections) + 1)]
        # check whether holland or national map to determine minimum length of route
        self.min_length = 100 if len(self.connections) == 28 else 160
        self.start = start_choice
        # track the scores for visualisation
        self.scores = []
        self.initial_score = 0
        self.best_score = 0
        self.tries = tries
        #10000 if len(self.connections) == 28 else 1000

    def create_railmap(self):
        """
        Instantiates a random railmap to begin with and creates new random routes for 
        possible improvement for i tries
        """
        st = time.time()

        # create random railmap according to start choice
        random_railmap = randomise.Randomise(self.connections, 1000)

        if self.start == 1:
            random_railmap = random_railmap.create_railmap()
        else:
            random_railmap = random_railmap.create_best_railmap()       

        # if there are any unused connections collect them in a list
        unused_ids = list(set(self.connection_ids) - set(random_railmap.visited))

        # begin all values with (the score of) the railmap just created
        self.first_score = random_railmap.score()
        self.best_score = random_railmap.score()
        better_railmap = deepcopy(random_railmap)
        best_railmap = deepcopy(random_railmap)
        new_railmap = deepcopy(random_railmap)


        for i in range(self.tries):
            # create a new random route of anywhere between 100 or 160 and 120 or 180 minutes
            new_route = random_railmap.create_route()

            while new_route.length < random.randint(self.min_length, new_route.max_length):
                try:
                    random_connection = random.choice(unused_ids)            
                    new_route.add_connection(random_connection)
                    unused_ids.remove(random_connection)
                except:
                    random_connection = random.choice(self.connection_ids)            
                    new_route.add_connection(random_connection)

            # check each existing route to see if swapping for new route gives score gain
            for j, route in enumerate(new_railmap.routes):
                new_railmap.minutes -= route.length
                new_railmap.visited = list(set(new_railmap.visited) - set(route.ids))
                new_railmap.routes[j] = new_route
                new_railmap.minutes += new_route.length
                new_railmap.visited += new_route.ids
                new_score = new_railmap.score()
                self.scores.append(new_score)
                # save the swap with best score gain
                if new_score > self.best_score:
                    self.best_score = new_score
                    best_railmap = deepcopy(new_railmap)
                # after the first iteration, check against previous iteration's railmap
                if i > 0:
                    new_railmap = deepcopy(better_railmap)
                else:
                    new_railmap = deepcopy(random_railmap)
            
            # save previous iteration's result in case improved
            better_railmap = deepcopy(best_railmap)
            print(i, self.best_score)

        et = time.time()
        print (et-st)
        return best_railmap

    def run(self):
        railmap = self.create_railmap()
        result = f"\nAmount of runs: {self.tries} \n----------------------------------------------------------------\n"\
        f"initial score: {self.first_score}, end score: {self.best_score}\n"\
        f"----------------------------------------------------------------\n\n"\
        f"{railmap}"
        
        print(result)
        self.visualise_HC()
        visualise(railmap, self.connections, "hillclimber")
    

    def visualise_HC(self):
        x = [i for i in range(self.tries)]
        y = [max(self.scores[:i+1]) for i in range(self.tries)]
        now = str(datetime.now())
        plt.plot(x, y)
        plt.xlabel("Number of tries")
        plt.ylabel("Best score")
        plt.ylim(2000, 10000)
        plt.title("Progress of Hill Climber")
        plt.savefig(f"output/hillclimber/progress of hillclimber-{now}.jpg")
        print(f"output saved as progress of hillclimber-{now}.jpg")
        plt.show()

        

