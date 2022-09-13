from stdGeneticSearch import stdGeneticSearch
import numpy as np


def diffCol(variables, domains=[]):

    occurrences = np.bincount(variables)

    for i in occurrences:
        if (i > 1):
            return False
    return True


def diffDiagonal(variables, domains=[]):

    variables = variables.copy()

    for i in range(len(variables)):
        for j in range(1, len(variables)):

            deltay = abs(0 - j)
            deltax = abs(variables[0] - variables[j])

            if (deltax == deltay):
                return False

        variables.pop(0)

    return True


def evalFunction(individual):
    return 1


n = 4
variables = [i for i in range(n)]
domain = [[i for i in range(n)] for j in range(n)]
constraints = [diffCol, diffDiagonal]
sol = stdGeneticSearch(variables, domain, constraints, 10000, 100, evalFunction)
print(sol)
