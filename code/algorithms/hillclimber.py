from copy import deepcopy
from code.algorithms import randomise
from code.visualisation.visualisation import run_visualise
import random
from tqdm import tqdm


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

    def create_railmap(self):
        """
        instantiates a random railmap according to input to begin with and 
        creates new random routes for possible improvement for i tries
        """
        # create random or best random railmap according to start choice
        random_railmap = randomise.Randomise(self.connections, 100000)

        if self.start == '1':
            random_railmap = random_railmap.create_railmap()
        else:
            random_railmap = random_railmap.create_best_railmap()

        # if there are any unused connections collect them in a list
        unused_ids = list(set(self.connection_ids) -
                          set(random_railmap.visited))

        # begin all values with (the score of) the railmap just created
        self.first_score = random_railmap.score()
        self.best_score = random_railmap.score()
        better_railmap = deepcopy(random_railmap)
        best_railmap = deepcopy(random_railmap)
        new_railmap = deepcopy(random_railmap)

        # show progress bar and try to swap a new route with existing routes tries amount of times
        for i in tqdm(range(self.tries)):
            # create a new random route of anywhere between 100 to 120 or 160 to 180 minutes
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
                new_railmap.visited = list(
                    set(new_railmap.visited) - set(route.ids))
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

        return best_railmap

    def run(self):
        """
        run hillclimber algorithm to get railmap and produce, save and show results
        """
        railmap = self.create_railmap()
        result = f"\nAmount of runs: {self.tries} \n----------------------------------------------------------------\n"\
            f"initial score: {self.first_score}, end score: {self.best_score}\n"\
            f"----------------------------------------------------------------\n\n"\
            f"{railmap}"

        print(result)

        run_visualise(railmap, self.connections, "hillclimber",
                      self.scores, self.tries, result)
