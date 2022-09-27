from time import sleep
from mazeEnv import Maze
from mazeAgent import MazeAgent

env = Maze(10, 10)

algs = ["DFS", "BFS", "A-Star", "Greedy", "Lowest-Cost-First", "B&B"]
alg = algs[2]
ag = MazeAgent(env)
ag.act(alg)
