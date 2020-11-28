import random
import math
import TSP


def main():
    # Create an instance of TSP
    p = TSP.createProblem()    # 'p': (numCities, locations, table)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    TSP.describeProblem(p)
    TSP.displaySetting("Steepst-Ascent")
    # Report results
    TSP.displayResult(solution, minimum)


def steepestAscent(p):
    current = TSP.randomInit(p)   # 'current' is a list of city ids
    valueC = TSP.evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC


def mutants(current, p): # Apply inversion
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = TSP.inversion(current, i, j)
            count += 1
            neighbors.append(curCopy)
    return neighbors


def bestOf(neighbors, p): ###
    best = neighbors.pop()
    bestValue = TSP.evaluate(best, p)
    for neighbor in neighbors:
        nValue = TSP.evaluate(neighbor, p)
        if nValue < bestValue:
            best = neighbor
            bestValue = nValue
    return best, bestValue


main()
