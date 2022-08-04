import numpy as np
import matplotlib.pyplot as plt

# Used to test
TEST = {
    "demand": 0
}


class ToiletEnviroment:
    def __init__(self):
        self.inventory = 100    # Number of paper rolls in the environment
        self.max = 1000     # Maximum stock of paper rolls in the environment
        self.min = 0        # Minimum stock of paper rolls in the environment
        self.clock = 0      # Each clock unit represents 24 hours in the environment
        self.price = 1      # Price for the paper roll

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
        demand = (averageConsumption[day] +
                  np.random.randn() * averageConsumption[day] / 10)

        TEST["demand"] = demand  # used to plot demands

        self.inventory -= demand
        shortage = min(0, self.inventory)
        shortage = abs(shortage)

        if (self.inventory < self.min):
            self.inventory = self.min

        self.price = 1 + (0.0005 * self.clock + np.random.randn() / 10)
        self.price = abs(self.price)
        self.clock += 1

        return {
            "inventory": self.inventory,
            "max": self.max,
            "min": self.min,
            "price": self.price,
            "shortage": shortage
        }


# Simple test
if (__name__ == "__main__"):
    env = ToiletEnviroment()
    prices = []
    demands = []

    for _ in range(1000):
        env.signal({"to_buy": 50})
        prices.append(env.price)
        demands.append(TEST["demand"])

    plt.plot(prices)
    plt.title("Prices")
    plt.show()

    plt.plot(demands)
    plt.title("Demands")
    plt.show()
