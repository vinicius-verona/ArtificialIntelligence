from ToiletPaper_Environment import ToiletEnviroment
import matplotlib.pyplot as plt


class ToiletAgent:
    def __init__(self, env) -> None:
        self.percepts = env.initialPercepts()
        self.env = env
        self.clock = 0
        self.expectedDemand = 0
        self.expectedPrice = self.percepts['price']
        self.purchases = []  # Used to plot

    def act(self):
        """
            For a given state of the environment, decide how much paper rolls should be bought
        """
        inventory = self.percepts["inventory"]
        critical = max(0, self.expectedDemand - inventory)
        toBuy = critical

        if (self.percepts["price"] < self.expectedPrice / 2):
            toBuy *= 4
        elif (self.percepts["price"] < self.expectedPrice):
            toBuy *= 2

        # Keep the total amount of paper rolls to the maximum allowed
        toBuy = min(toBuy, self.percepts["max"] - self.percepts["inventory"])

        self.purchases.append(toBuy)  # Just used on the plot

        self.percepts = self.env.signal({"to_buy": toBuy})
        self.clock += 1

        newInventory = self.percepts["inventory"]

        # Update the expected price for the paper roll
        self.expectedPrice *= (self.clock - 1)
        self.expectedPrice += self.percepts["price"]
        self.expectedPrice /= self.clock

        if (self.clock - 1 > 0):
            self.expectedDemand *= (self.clock - 1)

            # If the current amount of paper is the minimmum, there is a great chance that the demand is greater than the amount we had
            # Therefore, we sum the lack of paper rolls to the demand
            if (inventory == 0):
                inventory = self.percepts["shortage"]

            self.expectedDemand += (inventory - newInventory + toBuy)
            self.expectedDemand /= self.clock


# Simple test to plot both demands and price
if (__name__ == "__main__"):
    env = ToiletEnviroment()
    ag = ToiletAgent(env)

    prices = []
    demands = []

    for _ in range(1000):
        ag.act()
        prices.append(ag.expectedPrice)
        demands.append(ag.expectedDemand)

    plt.plot(prices)
    plt.title("Expected Prices")
    plt.show()

    plt.plot(ag.purchases)
    plt.title("Purchases")
    plt.show()

    plt.plot(demands)
    plt.title("Expected Demands")
    plt.show()
