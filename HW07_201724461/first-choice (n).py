import numeric as nmr
import random

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    # Create an instance of numerical optimization problem
    p = nmr.createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    nmr.describeProblem(p)
    nmr.displaySetting("First-Choice")
    # Report results
    nmr.displayResult(solution, minimum)


def firstChoice(p):
    current = nmr.randomInit(p)   # 'current' is a list of values
    valueC = nmr.evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = nmr.evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC


def randomMutant(current, p): ###
    i = random.randrange(len(p[1][0]))
    d = random.choice([-1, 1])
    d *= DELTA
    return mutate(current, i, d, p) # Return a random successor


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy



main()
