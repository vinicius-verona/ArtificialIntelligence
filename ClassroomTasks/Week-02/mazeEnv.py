# Reused from: "https://github.com/rcpsilva/BCC325_2022_01/blob/624f785049c1c73099fa88afd82aad315147de16/ED%202/maze.py"

from pyamaze import maze, agent


class Maze:

    def __init__(self, n, m) -> None:
        self.start = (n, m)
        self.maze = maze(n, m)
        self.maze.CreateMaze(loopPercent=10)
        self.goal = self.maze._goal

    def initial_percepts(self) -> dict:

        return {
            'position': self.start,
            'available_neighbors': self.get_available_neighboors(self.start),
            'goal': False,
            'goal_position': self.maze._goal
        }

    def get_available_neighboors(self, pos):

        neighbors = self.maze.maze_map[pos]
        available = [coordinate for coordinate in neighbors if neighbors[coordinate] == 1]

        available_neighbors = []
        new_pos = list(pos)

        for a in available:
            aux = new_pos.copy()
            if a == 'N':
                aux[0] -= 1
            elif a == 'S':
                aux[0] += 1
            elif a == 'W':
                aux[1] -= 1
            elif a == 'E':
                aux[1] += 1
            available_neighbors.append(tuple(aux))

        return available_neighbors

    def change_state(self, action):

        goal = True if action['path'][-1] == self.maze._goal else False
        position = action['path'][-1]

        self.maze.tracePath({
            agent(self.maze, shape='arrow', footprints=True): action['path']
        }, kill=True, delay=5)

        return {
            'position': position,
            'available_neighbors': self.get_available_neighboors(position),
            'goal': goal,
            'goal_position': self.maze._goal
        }

    def run(self):
        self.maze.run()

    def draw(self, path):
        self.maze.tracePath({
            agent(self.maze, shape='arrow', footprints=True): path
        }, kill=False, delay=5)
        self.maze.run()


if __name__ == "__main__":
    env = Maze(10, 10)
    print(env.initial_percepts())
