import math
import random


def generatePopulation(variables, domains, popSize):
    """
        Generates a random population given a set of variables, domain for each variable and a population size.
    """
    pop = []
    domSize = len(domains)

    for _ in range(popSize):
        if (domSize > 1):
            pop.append([random.choice(domains[j]) for j in range(len(variables))])
        else:
            pop.append([random.choice(domains[0]) for _ in range(len(variables))])

    return pop


def checkConstraints(individual, domains, constraints):
    """
        Verify if the current individual satisfies all constraints
    """
    for constraint in constraints:
        if (not constraint(individual, domains)):
            return False

    return True


def randSelect(population, iteration, evalFunction):
    """
        Randomly select an individual within the population with a Boltzmann distribution probability
    """
    while True:

        for individual in population:
            randomNumber = abs(random.random())

            if (randomNumber < math.exp(-1 * evalFunction(individual) / iteration)):
                return individual


def crossover(fstIndividual, sndIndividual):
    """
        Execute a crossover between two individuals
    """
    popSize = len(fstIndividual)
    randomInt = random.randint(1, popSize)

    newFstIndividual = [fstIndividual[i] for i in range(randomInt)]
    newSndIndividual = [sndIndividual[i] for i in range(randomInt)]

    for i in range(randomInt, popSize):
        newFstIndividual.insert(-1, sndIndividual[i])
        newSndIndividual.insert(-1, fstIndividual[i])

    return newFstIndividual, newSndIndividual


def mutate(individual, domains, percentage):
    """
        Mutate an individual by changing the value of a percentage k of the variables
    """
    percentage = percentage / 100 if (percentage > 0) else percentage
    domLen = len(domains)

    for i in range(math.ceil(percentage)):
        randomVarPosition = random.randint(0, len(individual)-1)

        if (domLen > 1):
            individual[randomVarPosition] = random.choice(domains[randomVarPosition])
        else:
            individual[randomVarPosition] = random.choice(domains[0])

    return individual


def stdGeneticSearch(variables, domains, constraints, iterMax, popSize, evalFunction):
    population = generatePopulation(variables, domains, popSize)

    for i in range(1, iterMax+1):

        # Check if a solution has been found
        for individual in population:
            if (checkConstraints(individual, domains, constraints)):
                return individual

        newPopulation = []
        for _ in range(math.floor(popSize / 2)):

            # Randomly select two individuals for crossovering
            fstInd = randSelect(population, i, evalFunction)
            sndInd = randSelect(population, i, evalFunction)

            newFstInd, newSndInd = crossover(fstInd, sndInd)
            newPopulation.append(mutate(newFstInd, domains, 40))
            newPopulation.append(mutate(newSndInd, domains, 40))

        population = newPopulation

    return []
