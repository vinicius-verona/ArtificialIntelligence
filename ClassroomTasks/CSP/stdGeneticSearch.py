# Based on https://github.com/rcpsilva/BCC325_ArtificialIntelligence/blob/main/2022-1/Constraint%20Satisfaction%20Problems/nQueensEA.py

import copy
import math
import numpy as np
import random


def differentColumnViolations(sol):

    conflicts = 0

    for i in range(len(sol)):
        for j in range(len(sol)):
            if (i != j) and (sol[i] == sol[j]):
                conflicts += 1

    return conflicts


def differentDiagonalViolations(sol):

    conflicts = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            deltay = abs(sol[i]-sol[j])
            deltax = abs(i - j)
            if (deltay == deltax and i != j):
                conflicts += 1

    return conflicts


def evalSol(sol):

    return differentDiagonalViolations(sol) + differentColumnViolations(sol)


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


def checkConstraints(individual, constraints):
    """
        Verify if the current individual satisfies all constraints
    """
    for constraint in constraints:
        if (constraint(individual)):
            return False

    return True


def randSelect(population, iteration, evalSol):
    """
        Randomly select an individual within the population with a Boltzmann distribution probability
    """
    while True:

        for individual in population:
            randomNumber = abs(random.random())

            if (randomNumber < math.exp(-1 * evalSol(individual) / iteration)):
                return individual


def crossover(fstIndividual, sndIndividual):
    """
        Execute a crossover between two individuals
    """
    popSize = len(fstIndividual)
    mask = np.random.randint(2, size=popSize)  # Binary mask of size popSize

    child1 = copy.deepcopy(fstIndividual)
    child2 = copy.deepcopy(sndIndividual)

    for i in range(popSize):
        if not mask[i]:
            child1[i] = sndIndividual[i]
            child2[i] = fstIndividual[i]

    return child1, child2


def mutate(individual, domains, percentage):
    """
        Mutate an individual by changing the value of a percentage k of the variables
    """
    percentage = percentage / 100 if (percentage > 0) else percentage
    neighbor = copy.deepcopy(individual)

    for _ in range(math.ceil(percentage)):
        idx1 = np.random.randint(0, len(individual))
        idx2 = np.random.randint(0, len(individual))
        neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

    return neighbor


def findBestSolution(population, constraints):
    """
        Evaluate each solution within the population and return the best one
    """
    bestSol = copy.deepcopy(population[0])
    bestVal = evalSol(bestSol)

    for i in population:
        val = evalSol(i)

        if (val < bestVal and checkConstraints(i, constraints)):
            bestVal = val
            bestSol = i

    return bestSol, bestVal


def stdGeneticSearch(variables, domains, constraints, iterMax, popSize, evalSol):
    population = generatePopulation(variables, domains, popSize)

    for i in range(1, iterMax+1):

        # Check if a solution has been found
        for individual in population:
            if (checkConstraints(individual, constraints)):
                return findBestSolution(population, constraints)

        newPopulation = []
        for _ in range(math.floor(popSize / 2)):

            # Randomly select two individuals for crossovering
            fstInd = randSelect(population, i, evalSol)
            sndInd = randSelect(population, i, evalSol)

            newFstInd, newSndInd = crossover(fstInd, sndInd)
            newPopulation.append(mutate(newFstInd, domains, 40))
            newPopulation.append(mutate(newSndInd, domains, 40))

        population = newPopulation

    return findBestSolution(population, constraints)


if __name__ == "__main__":
    n = 4
    variables = [i for i in range(n)]
    domain = [[i for i in range(n)] for j in range(n)]
    constraints = [differentColumnViolations, differentDiagonalViolations]
    sol, val = stdGeneticSearch(variables, domain, constraints, 10000, 1000, evalSol)
    print(sol)
    print(val)
