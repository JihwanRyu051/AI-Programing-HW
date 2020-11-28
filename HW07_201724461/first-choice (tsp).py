import random
import TSP

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    # Create an instance of TSP
    p = TSP.createProblem()    # 'p': (numCities, locations, distanceTable)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    TSP.describeProblem(p)
    TSP.displaySetting("First-Choice")
    # Report results
    TSP.displayResult(solution, minimum)


def firstChoice(p):
    current = TSP.randomInit(p)   # 'current' is a list of city ids
    valueC = TSP.evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = TSP.evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC


def randomMutant(current, p): # Apply inversion
    while True:
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            curCopy = TSP.inversion(current, i, j)
            break
    return curCopy


main()
