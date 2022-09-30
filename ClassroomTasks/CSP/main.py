from stdGeneticSearch import differentColumnViolations, differentDiagonalViolations, stdGeneticSearch, evalSol


n = 4
variables = [i for i in range(n)]
domain = [[i for i in range(n)] for j in range(n)]
constraints = [differentColumnViolations, differentDiagonalViolations]
sol, val = stdGeneticSearch(variables, domain, constraints, 10000, 1000, evalSol)
print(sol)
print(val)
