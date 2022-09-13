import heapq as hp
import numpy as np


def heuristic(currentNode, goalNode):
    """
        Return the manhattan distance between the current node and the goal node
    """
    try:
        return max(np.sum(abs(np.array(currentNode) - np.array(goalNode)), axis=0))
    except:
        return np.sum(abs(np.array(currentNode) - np.array(goalNode)), axis=0)


def cost(path):
    """
        Return the total cost of a path 
    """
    cost = 0

    for i in range(len(path) - 1):
        try:
            cost += max(np.sum(abs(np.array(path[i]) - np.array(path[i+1])), axis=0))
        except:
            cost += np.sum(abs(np.array(path[i]) - np.array(path[i+1])), axis=0)

    return cost


class MazeAgent:

    def __init__(self, env) -> None:
        self.env = env
        self.percepts = env.initial_percepts()
        self.frontier = None
        self.path = []

    def act(self, alg="DFS", bound=None, no_draw=False):
        if (alg == "DFS"):
            self.dfs(no_draw)
        elif(alg == "BFS"):
            self.bfs(no_draw)
        elif(alg == "A-Star"):
            self.aStar(no_draw)
        elif(alg == "Greedy"):
            self.greedy(no_draw)
        elif(alg == "Lowest-Cost-First"):
            self.lowestCostFirst(no_draw)
        elif(alg == "B&B"):
            self.branchAndBound(bound, no_draw)

    def dfs(self, no_draw=False):
        self.frontier = [[self.percepts['position']]]

        while (self.frontier):
            path = self.frontier.pop(-1)
            self.percepts = self.env.change_state({"path": path.copy()})

            if (self.percepts["goal"]):
                break
            else:
                for neighbor in self.percepts["available_neighbors"]:
                    if (neighbor not in path):
                        self.frontier.insert(-1, path + [neighbor])

        self.path = path

        if (not no_draw):
            self.env.draw(path)

    def bfs(self, no_draw=False):
        self.frontier = [[self.percepts['position']]]

        while (self.frontier):
            path = self.frontier.pop(0)
            self.percepts = self.env.change_state({"path": path.copy()})

            if (self.percepts["goal"]):
                break
            else:
                for neighbor in self.percepts["available_neighbors"]:
                    if (neighbor not in path):
                        self.frontier.insert(-1, path + [neighbor])

        self.path = path

        if (not no_draw):
            self.env.draw(path)

    def aStar(self, no_draw=False):
        self.frontier = []

        # To build the heap, we will use the cost as key and the path as the item
        # Heap format: (key, item) -> the key is the returned value from the heuristic + the cost of the path
        hp.heappush(self.frontier, (heuristic(self.percepts["position"], self.percepts["goal_position"]),
                                    [self.percepts["position"]]))

        while (self.frontier):
            path = hp.heappop(self.frontier)[1]
            self.percepts = self.env.change_state({"path": path.copy()})

            if (self.percepts["goal"]):
                break
            else:
                for neighbor in self.percepts["available_neighbors"]:
                    if (neighbor not in path):
                        hp.heappush(self.frontier, (cost(path + [neighbor]) + heuristic(neighbor, self.percepts["goal_position"]),
                                                    path + [neighbor]))

        self.path = path

        if (not no_draw):
            self.env.draw(path)

    def greedy(self, no_draw=False):
        self.frontier = []

        # To build the heap, we will use the cost as key and the path as the item
        # Heap format: (key, item) -> the key is the returned value from the heuristic
        hp.heappush(self.frontier, (heuristic(self.percepts["position"], self.percepts["goal_position"]),
                                    [self.percepts["position"]]))

        while (self.frontier):
            path = hp.heappop(self.frontier)[1]
            self.percepts = self.env.change_state({"path": path.copy()})

            if (self.percepts["goal"]):
                break
            else:
                for neighbor in self.percepts["available_neighbors"]:
                    if (neighbor not in path):
                        hp.heappush(self.frontier, (heuristic(neighbor, self.percepts["goal_position"]),
                                                    path + [neighbor]))

        self.path = path

        if (not no_draw):
            self.env.draw(path)

    def lowestCostFirst(self, no_draw=False):
        self.frontier = []

        # To build the heap, we will use the cost as key and the path as the item
        # Heap format: (key, item) -> the key is the returned value from the cost of the path
        hp.heappush(self.frontier, (cost([self.percepts["position"]]), [self.percepts["position"]]))

        while (self.frontier):
            path = hp.heappop(self.frontier)[1]
            self.percepts = self.env.change_state({"path": path.copy()})

            if (self.percepts["goal"]):
                break
            else:
                for neighbor in self.percepts["available_neighbors"]:
                    if (neighbor not in path):
                        hp.heappush(self.frontier, (cost(path + [neighbor]), path + [neighbor]))

        self.path = path

        if (not no_draw):
            self.env.draw(path)

    def branchAndBound(self, bound=None, no_draw=False):

        # Use a initial solution as bound in case a bound has not been passed as parameter
        if (not bound):
            self.greedy(no_draw=True)
            bound = cost(self.path)

        self.path = []
        self.percepts = self.env.change_state({"path": [self.env.initial_percepts()["position"]].copy()})
        self.percepts = self.env.initial_percepts()
        self.frontier = [[self.percepts['position']]]

        def costBoundSearch(args):
            path = self.frontier.pop(-1)
            bound = args["bound"]

            if (cost(path) + heuristic(path[-1], self.percepts["goal_position"]) < bound):
                self.percepts = self.env.change_state({"path": path.copy()})

                if (self.percepts["goal"]):
                    bound = cost(path)
                    self.path = path
                    return
                else:
                    for neighbor in self.percepts["available_neighbors"]:
                        if (neighbor not in path):
                            args["frontier"].insert(-1, path + [neighbor])
                            args["bound"] = bound
                            costBoundSearch(args)

        costBoundSearch({"bound": bound, "frontier": self.frontier})
        if (not no_draw):
            self.env.draw(self.path)


if __name__ == "__main__":
    print(cost([(0, 0), (1, 1), (2, 2), (3, 3)]))
