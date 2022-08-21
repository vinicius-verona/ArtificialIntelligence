from mazeEnv import Maze
from mazeAgent import MazeAgent

env = Maze(10, 10)

algs = ["DFS", "BFS", "A-Star", "Greedy", "Lowest-Cost-First", "B&B"]
alg = algs[-1]

ag = MazeAgent(env)
ag.act(alg, float('inf'))
