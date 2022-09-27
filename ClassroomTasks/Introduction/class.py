import numpy as np


class ToiletEnviroment:
    def __init__(self):
        self.inventory = 100   # Number of paper rolls in the environment
        self.max = 1000        # Maximum number of paper rolls in the environment
        self.min = 0           # Minimum number of paper rolls in the environment
        self.clock = 0         # Each clock unit represents 24 hours in the environment
        self.price = 1         # Price for the paper roll

    def initialPercepts(self):
        return {
            "inventory": self.inventory,
            "max": self.max,
            "min": self.min,
            "price": self.price
        }

    def signal(self, action):
        """
            For a given action, return a percept
        """
        averageConsumption = [30, 80, 100, 80, 10, 2, 1]
        day = self.clock % 7

        self.inventory += action["to_buy"]
        self.inventory = min(self.inventory, self.max)
        self.inventory -= (averageConsumption[day] +
                           np.random.randn() * averageConsumption[day] / 10)

        if (self.inventory < self.min):
            self.inventory = self.min

        self.price = 1 + (0.0005 * self.clock + np.random.randn() / 10)
        self.price = abs(self.price)
        self.clock += 1

        return {
            "inventory": self.inventory,
            "max": self.max,
            "min": self.min,
            "price": self.price
        }


class ToiletAgent:
    def __init__(self, env) -> None:
        self.percepts = env.initialPercepts()
        self.env = env

        # Tarefa:
        # Criar uma maneira de prever quando o agente deve comprar mais papéis higiênicos
        # E também quanto deve comprar, baseado no histórico de preço do papel
        # E o histórico de demanda de papel

    def act(self):
        invetory = self.percepts["inventory"]
        critical = 50

        action = {
            "to_buy": 0
        }

        if (invetory < critical):
            action["to_buy"] = critical - invetory

        self.percepts = self.env.signal(action)
