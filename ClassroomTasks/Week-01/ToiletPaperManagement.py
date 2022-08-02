import numpy as np


class ToiletEnviroment:
    def __init__(self):
        self.number = 100   # Number of paper rolls in the environment
        self.max = 1000     # Maximum number of paper rolls in the environment
        self.min = 0        # Minimum number of paper rolls in the environment
        self.critical = 50  # Number of paper rolls considered as critical (need to buy more)
        self.clock = 0      # Each clock unit represents 24 hours in the environment
        self.price = 1      # Price for the paper roll

    def initialPercepts(self):
        return {
            "number": self.number,
            "max": self.max,
            "min": self.min,
            "critical": self.critical,
            "price": self.price
        }

    def signal(self, action):
        """
            For a given action, return a percept
        """
        averageConsumption = [30, 80, 100, 80, 10, 2, 1]
        day = self.clock % 7

        self.number += action["to-buy"]
        self.number = min(self.number, self.max)
        self.number -= (averageConsumption[day] +
                        np.random.randn() * averageConsumption[day] / 10)

        if (self.number < self.min):
            self.number = self.min

        self.price += (0.01 * self.clock + np.random.randn())
        self.price = abs(self.price)
        self.clock += 1

        return {
            "number": self.number,
            "number": self.number,
            "max": self.max,
            "min": self.min,
            "critical": self.critical,
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
        number = self.percepts["number"]
        critical = self.percepts["critical"]

        action = {
            "to_buy": 0
        }
        if (number < critical):
            action["to_buy"] = critical - number

        self.percepts = self.env.signal(action)
