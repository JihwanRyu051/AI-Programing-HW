import numeric as nmr
DELTA = 0.01

def main():
    # Create an instance of numerical optimization problem
    p = nmr.createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    nmr.describeProblem(p)
    nmr.displaySetting("Steepest-Ascent")
    # Report results
    nmr.displayResult(solution, minimum)


def steepestAscent(p):
    current = nmr.randomInit(p) # 'current' is a list of values
    valueC = nmr.evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC


def mutants(current, p): ###
    neighbors = set()
    for index in range(len(current)):
        for d in [-1, 1]:
            neighbor = tuple(mutate(current, index, d*DELTA, p))
            neighbors.add(neighbor)
    return neighbors     # Return a set of successors


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    lower = domain[1][i]     # Lower bound of i-th
    upper = domain[2][i]     # Upper bound of i-th
    if lower <= (curCopy[i]+d) <= upper:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): ###
    best = list(neighbors.pop())
    bestValue = nmr.evaluate(best, p)
    for neighbor in neighbors:
        candidate = nmr.evaluate(neighbor, p)
        if candidate < bestValue:
            best = list(neighbor)
            bestValue = candidate
    return best, bestValue




main()
