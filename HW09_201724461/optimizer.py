from setup import *

LIMIT_STUCK = 100
EPSILON = 0.0001

class HillClimbing(Setup):
    def run(self, p):
        pass

    def displaySetting(self):
        pass


class firstChoice(HillClimbing):
    def __init__(self):
        super().__init__()
        self._limitStuck = LIMIT_STUCK

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0  # Reset stuck counter
            else:
                i += 1
        p.setSolution(current)
        p.setMinimum(valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: First-choice Hill Climbing")
        print()
        print("Mutation step size: ", self._delta)
        print("Max evalutations with no improvement: {0:,} iterations".format(self._limitStuck))


class steepestAscent(HillClimbing):
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = p.bestOf(neighbors)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.setSolution(current)
        p.setMinimum(valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        print()
        print("Mutation step size: ", self._delta)


class gradientDescent(HillClimbing):
    def __init__(self):
        super().__init__()
        self._epsilon = EPSILON

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            grd = p.gradientMutate(self._epsilon, current, valueC)
            successor = p.gradientMutant(grd, current)
            valueS = p.evaluate(successor)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS

        p.setSolution(current)
        p.setMinimum(valueC)


    def displaySetting(self):
        print()
        print("Search algorithm: Gradient decent")
        print()
        print("Update rate: ", self._delta)
        print("Increment for calculating derivatives: {}".format(self._epsilon))