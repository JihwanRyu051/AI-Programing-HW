from setup import *

class problem(Setup):
    def __init__(self, parameters):
        super().__init__(parameters)
        self._p = ()
        self._minimum = 0.0
        self._NumEval = 0
        self._solution = []
        self._results = ()

    def setSolution(self, solution):
        self._solution = solution

    def setValue(self, minimum):
        self._minimum = minimum

    def setNumEval(self, numEval):
        self._NumEval = numEval

##hw10추가.begin
    def getSolution(self):
        return self._solution

    def getValue(self):
        return self._minimum

    def getNumEval(self):
        return self._NumEval

    def getResults(self):
        return self._results

    def report(self):
        print()
        if 5 <= self._aType <= 6:
            print("Average of evaluation when best found: {0:,}".format(self._results[5]))
        print("Total number of evaluations: {0:,}".format(self._results[4]))

    def storeExpResult(self, results):
        self._results = results
##hw10추가.end

    def evaluate(self, current):
        self._NumEval += 1





class tsp(problem):
    def __init__(self, parameters):
        super().__init__(parameters)
        fileName = parameters['pFileName']
        infile = open(fileName, 'r')
        numCities = int(infile.readline())
        locations = []
        line = infile.readline()
        while line != '':
            locations.append(eval(line))
            line = infile.readline()
        infile.close()
        table = self.calcDistanceTable(numCities, locations)
        self._p = numCities, locations, table

    def calcDistanceTable(self, numCities, locations):
        start = list(range(numCities))
        assignment = start[:]
        table = []
        for sp in start:
            row = []
            for ap in assignment:
                dis = 0
                for dim in range(2):
                    dis += (locations[sp][dim] - locations[ap][dim]) ** 2
                row.append(math.sqrt(dis))
            table.append(row)
        return table

    def randomInit(self):
        n = self._p[0]
        init = list(range(n))
        random.shuffle(init)
        return init

    def mutants(self, current):
        data = self._p
        n = data[0]
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors

    def bestOf(self, neighbors):
        best = neighbors.pop()
        bestValue = self.evaluate(best)
        for neighbor in neighbors:
            nValue = self.evaluate(neighbor)
            if nValue < bestValue:
                best = neighbor
                bestValue = nValue
        return best, bestValue

    def randomMutant(self, current):
        data = self._p
        while True:
            i, j = sorted([random.randrange(data[0]) for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def evaluate(self, current):
        super().evaluate(current)
        cost = 0
        for index in range(len(current)):
            if index == (len(current) - 1):
                break
            cost += self._p[2][current[index]][current[index + 1]]
        return cost

    def inversion(self, current, i, j):  # Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describe(self):
        print()
        n = self._p[0]
        print("Number of cities:", n)
        print("City locations:")
        locations = self._p[1]
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end='')
            if i % 5 == 4:
                print()

    def report(self):
        print()
        print("Average objective value: {0:,.3f}".format(self._results[2]))
        print()
        print("Average number of evalutations: {0:,}".format(self._results[3]))
        print()
        print("Best Solution Found:")
        print(self.tenPerRow())
        print("Best value: {0:,.3f}".format(self._results[1]))
        super().report()

    def tenPerRow(self):
        for i in range(len(self._results[0])):
            print("{0:>5}".format(self._results[0][i]), end='') ##self._solution -> self._results[0](bestSolution)
            if i % 10 == 9:
                print()


class numeric(problem):
    def __init__(self, parameters):
        super().__init__(parameters)
        fileName = parameters['pFileName']
        infile = open(fileName, 'r')
        expression = infile.readline()
        domain = [[], [], []]
        for line in infile:
            data = line.split(',')
            domain[0].append(data[0])
            domain[1].append(float(data[1]))
            domain[2].append(float(data[2]))
        infile.close()
        self._p = expression, domain

    def mutants(self, current):
        neighbors = []
        for index in range(len(current)):
            for d in [-1, 1]:
                neighbor = self.mutate(current, index, d * self._delta)
                neighbors.append(neighbor)
        return neighbors

    def bestOf(self, neighbors):
        best = list(neighbors.pop())
        bestValue = self.evaluate(best)
        for tupNeighbor in neighbors:
            neighbor = list(tupNeighbor)
            candidate = self.evaluate(neighbor)
            if candidate < bestValue:
                best = neighbor
                bestValue = candidate
        return best, bestValue

    def randomMutant(self, current):  ###
        data = self._p
        i = random.randrange(len(data[1][0]))
        d = random.choice([-1, 1])
        d *= self._delta
        return self.mutate(current, i, d)

    def mutate(self, current, i, d):
        curCopy = current[:]
        domain = self._p[1]  # [VarNames, low, up]
        lower = domain[1][i]  # Lower bound of i-th
        upper = domain[2][i]  # Upper bound of i-th
        if lower <= (curCopy[i] + d) <= upper:
            curCopy[i] += d
        return curCopy

    def gradientMutate(self, epsilon, current, valueC):
        grd = []
        domain = self._p[1]
        for index in range(len(current)):
            l = domain[1][index]
            u = domain[2][index]
            x = current[index]
            c_prime = current[:index]
            if l <= (current[index] + epsilon) <= u:
                x += epsilon
            c_prime.append(x)
            c_prime.extend(current[index + 1:])
            valueX = self.evaluate(c_prime)
            grd.append((valueX - valueC) / epsilon)
        return grd

    def gradientMutant(self, grd, current):
        successor = []
        for index in range(len(current)):
            s = current[index] - self._delta * grd[index]
            successor.append(s)
        return successor

    def randomInit(self):
        init = []
        for index in range(len(self._p[1][0])):
            init.append(random.uniform(self._p[1][1][index], self._p[1][2][index]))
        return init

    def evaluate(self, current):
        super().evaluate(current)
        expr = self._p[0]  # p[0] is function expression
        varNames = self._p[1][0]  # p[1] is domain
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)

    def describe(self):
        print()
        print("Objective function:")
        print(self._p[0])  # Expression
        print("Search space:")
        varNames = self._p[1][0]  # p[1] is domain: [VarNames, low, up]
        low = self._p[1][1]
        up = self._p[1][2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Average objective value: {0:,.3f}".format(self._results[2]))
        print()
        print("Average number of evalutations: {0:,}".format(self._results[3]))
        print()
        print("Best Solution Found:")
        print(self.coordinate())  # Convert list to tuple
        print("Best value: {0:,.3f}".format(self._results[1]))
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._results[0]]
        return tuple(c)


