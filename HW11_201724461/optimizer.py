from setup import *

class Optimizer(Setup):
    def __init__(self, parameters):
        super().__init__(parameters)
        self._pType = parameters['pType']
        self._numExp = parameters['numExp']

    def getNumExp(self):
        return self._numExp
    
    def run(self, p):
        p.setNumEval(0)

    def displaySetting(self):
        pass

    def displayNumExp(self):
        print()
        print("Number of experiments: {}".format(self._numExp))


class HillClimbing(Optimizer):
    def __init__(self, parameters):
        super().__init__(parameters)
        self._numRestart = parameters['numRestart']
        self._limitStuck = parameters['limitStuck']

    def displaySetting(self):
        print("Number of random restarts: {}".format(self._numRestart))
        print()

    def randomRestart(self, p):
        self.run(p)
        bestValue = p.getValue()
        bestSolution = p.getSolution()
        for n in range(1, self._numRestart):
            self.run(p)
            newValue = p.getValue()
            if newValue < bestValue:
                bestSolution = p.getSolution()
                bestValue = newValue
        p.setValue(bestValue)
        p.setSolution(bestSolution)


class firstChoice(HillClimbing):
    ## 삼중주석() 처리된 코드들은 tsp100을 First Choice alg의 매회 결과값을 plot_tsp100/tsp100_firstChoice.txt에 저장하기 위한 코드임
    def run(self, p):
        ###outFirstChoice = open("plot_tsp100/tsp100_firstChoice.txt", 'w')
        Optimizer.run(self, p)
        current = p.randomInit()
        valueC = p.evaluate(current)
        ###outFirstChoice.writelines(str(valueC)+"\n")
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
            ###outFirstChoice.writelines(str(valueC)+"\n")
        p.setSolution(current)
        p.setValue(valueC)
        ###outFirstChoice.close()

    def displaySetting(self):
        print()
        print("Search algorithm: First-choice Hill Climbing")
        print()
        HillClimbing.displaySetting(self)
        print("Mutation step size: ", self._delta)
        print("Max evalutations with no improvement: {0:,} iterations".format(self._limitStuck))


class steepestAscent(HillClimbing):
    def run(self, p):
        Optimizer.run(self, p)
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
        p.setValue(valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        print()
        HillClimbing.displaySetting(self)
        print("Mutation step size: ", self._delta)


class gradientDescent(HillClimbing):
    def run(self, p):
        Optimizer.run(self, p)
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            grd = p.gradientMutate(self._dx, current, valueC)
            successor = p.gradientMutant(grd, current)
            valueS = p.evaluate(successor)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.setSolution(current)
        p.setValue(valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: Gradient decent")
        print()
        HillClimbing.displaySetting(self)
        print("Update rate: ", self._delta)
        print("Increment for calculating derivatives: {}".format(self._dx))

##HW10 추가본.begin
class stochastic(HillClimbing):
    def run(self, p):
        Optimizer.run(self, p)                              ## numEval = 0으로 초기화
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:                         ## neighbors 중 무작위로 고른 값이 기존의 값보다 작을 경우 current <- next, limit Stuck을 초과할 때까지 current가 업데이트 되지 않았다면 loop 탈출
            neighbors = p.mutants(current)
            successor, valueS = self.stochasticBest(neighbors, p)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.setSolution(current)                              ## current를 best case로 저장
        p.setValue(valueC)

    def stochasticBest(self, neighbors, p):
        # Smaller valuse are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]

    def displaySetting(self):
        print()
        print("Search algorithm: Stochastic Hill Climbing")
        print()
        HillClimbing.displaySetting(self)
        print("Mutation step size: ", self._delta)
        print("Max evalutations with no improvement: {0:,} iterations".format(self._limitStuck))


class MetaHeuristics(Optimizer):
    def __init__(self, parameters):
        super().__init__(parameters)
        self._limitEval = parameters['limitEval']
        self._whenBestFound = 0

    def getWhenBestFound(self):
        return self._whenBestFound

    def displaySetting(self,):
        print("Number of evaluation when terminate: {0:,d}".format(self._limitEval))


class simulatedAnnealing(MetaHeuristics):
    def __init__(self, parameters):
        super().__init__(parameters)
        self._numSample = 1                             ## numSample = 1로 설정

    def run(self, p):
        ## 삼중주석() 처리된 코드들은 tsp100을 Simulated Aneealing alg의 매회 결과값을 plot_tsp100/tsp100_simulatedAnnealing.txt에 저장하기 위한 코드임
        ###outSimulatedAnnealing = open("plot_tsp100/tsp100_simulatedAnnealing.txt", 'w')
        Optimizer.run(self, p)
        current = p.randomInit()  # A random point
        valueC = p.evaluate(current)
        ###outSimulatedAnnealing.writelines(str(valueC) + "\n")
        temparature = self.initTemp(p)
        while True:
            temparature = self.tSchedule(temparature)   ## T <- schedule[t]
            if temparature == 0:
                break
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            dE = valueS - valueC                        ## dE = next.Value - current.Value
            prob = math.exp(-dE/temparature)
            if dE < 0 or random.random() < prob:        ## de<0 혹은 exp(-dE/temparature)의 확률로 current <- next
                current = successor
                valueC = valueS
                self._whenBestFound = p.getNumEval()    ## current값이 업데이트 되었으므로 whenBestFound 값 또한 업데이트
            ###outSimulatedAnnealing.writelines(str(valueC) + "\n")
            if p.getNumEval() == self._limitEval:
                break
        p.setSolution(current)
        p.setValue(valueC)
        ###outSimulatedAnnealing.close()

    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t
    def tSchedule(self, t):
        return t * (1 - (1 / 10 ** 4))

    def displaySetting(self):
        print()
        print("Search algorithm: Simulated Annealing")
        print()
        super().displaySetting()
        print("Temparature Schedule: t * (1 - (1 / 10 ** 4))")

class GA(MetaHeuristics):
    def __init__(self, parameters):
        MetaHeuristics.__init__(self, parameters)
        self._popSize = parameters['popSize']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        if self._pType == 1:
            self._pC = self._uXp
            self._pM = self._mrF
        if self._pType == 2:
            self._pC = self._XR
            self._pM = self._mR


    def run(self, p):
        Optimizer.run(self, p)
        currentPop = p.initializePop(self._popSize)
        p.evalInd(currentPop[0])
        best = currentPop[0]
        for i in range(1, self._popSize):
            p.evalInd(currentPop[i])
            if best[0] > currentPop[i][0]:
                best = currentPop[i]
                self._whenBestFound = p.getNumEval()
        ##초기 population 중 가장 작은 값을 가지는 원소를 best로 설정
        while p.getNumEval() < self._limitEval:
            newPop = []
            for i in range(self._popSize//2):
                parents = self.parentsSelection(p, currentPop)          ## parents 생성
                children = p.crossover(parents[0], parents[1], self._pC)## 두개의 child 생성
                for child in children:
                    if p.getNumEval() >= self._limitEval:
                        break
                    p.evalInd(child)
                    if best[0] > child[0]:
                        best = child
                        self._whenBestFound = p.getNumEval()            ## child의 값이 best의 값보다 작다면 best를 child로 업데이트
                newPop.extend(children)
            currentPop = newPop
        p.setSolution(p.indToSol(best))
        p.setValue(best[0])

    def parentsSelection(self, p, currentPop):
        parents = list(range(2))
        for i in range(2):
            candinates = random.choices(currentPop, k=2)
            for j in range(len(parents)):
                p.evalInd(candinates[j])
            if candinates[0][0] > candinates[1][0]:
                parents[i] = candinates[1]
            elif candinates[0][0] < candinates[1][0]:
                parents[i] = candinates[0]
            else:
                parents[i] = random.choice(candinates)
        return parents

    def displaySetting(self):
        print()
        print("Search Algorithm: Genetic Algorithm")
        print()
        MetaHeuristics.displaySetting(self)
        print()
        print("Population size:", self._popSize)
        if self._pType == 1:  # Numerical optimization
            print("Number of bits for binary encoding:", self._resolution)
            print("Swap probability for uniform crossover:", self._uXp)
            print("Multiplication factor to 1/L for bit-flip mutation:",
                  self._mrF)
        elif self._pType == 2:  # TSP
            print("Crossover rate:", self._XR)
            print("Mutation rate:", self._mR)






