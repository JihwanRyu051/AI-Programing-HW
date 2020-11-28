import random
import math

DELTA = 0.01
##DELTA 값을 전역변수로 선언 및 초기화

class problem:
    def __init__(self):
        self._p = ()
        self._minimum = 0.0
        self._NumEval = 0
        self._solution = []
        ##알고리즘의 주요 요소 _minimum, _NumEval, _solution을 멤버 변수로 포함
        ##문제에서 제공하는 정보를 저장할 멤버 변수 _p를 추가

    def setSolution(self, solution):
        self._solution = solution

    def setMinimum(self, minimum):
        self._minimum = minimum

    def getSolution(self):
        return self._solution

    def getP(self):
        return self._p

    def getMinimum(self):
        return self._minimum

    def getNumEval(self):
        return self._NumEval
    ##멤버 변수들의 get, set 함수

    def displaySetting(self, msg):
        print()
        print("Search algorithm: {} Hill Climbing".format(msg))
    ##모든 problem에서 Report 시 중복적으로 사용하는 알고리즘 표기문을 함수로 구현
    ##msg(ex: Steepst-Ascent)를 매개변수로 받아 표기문에 추가하여 출력

    def displayResult(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._NumEval))
    ##모든 problem에서 Report 시 중복적으로 사용하는 평가횟수 출력문을 함수로 구현

    def evaluate(self):
        self._NumEval += 1
    ##evaluate 시 평가횟수 1증가

class tsp(problem):
    def __init__(self):
        super().__init__()
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')
        numCities = int(infile.readline())
        locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            locations.append(eval(line))  # Make a tuple and append
            line = infile.readline()
        infile.close()
        table = self.calcDistanceTable(numCities, locations)
        self._p = numCities, locations, table
        ##생성자가 이전 모듈에서 creatproblem()과 동일한 역할을 수행하도록 구현

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
    ##이전 모듈 내 동명의 함수와 내용 동일

    def randomInit(self):  # Return a random initial tour
        n = self._p[0]
        init = list(range(n))
        random.shuffle(init)
        return init
    ##이전 모듈 내 동명의 함수와 내용 동일

    def evaluate(self, current):
        super().evaluate()
        cost = 0
        for index in range(len(current)):
            if index == (len(current) - 1):
                break
            cost += self._p[2][current[index]][current[index + 1]]
        return cost
    ##evaluate() 실행 시 NumEval(평가횟수)를 1증가시키는 기능을 부모 클래스의 evaluate() 함수로 대체
    ##이전 모듈 내 동명의 함수와 내용 동일


    def inversion(self, current, i, j):  # Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy
    ##이전 모듈 내 동명의 함수와 내용 동일
    def describeProblem(self):
        print()
        n = self._p[0]
        print("Number of cities:", n)
        print("City locations:")
        locations = self._p[1]
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end='')
            if i % 5 == 4:
                print()
    ##이전 모듈 내 동명의 함수와 내용 동일

    def displayResult(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()  # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._minimum)))
        super().displayResult()
    ##하단의 평가횟수 출력문을 부모 클래스의 displayResult()문으로 대체
    ##이전 모듈 내 동명의 함수와 내용 동일

    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()
    ##이전 모듈 내 동명의 함수와 내용 동일


class numeric(problem):
    def __init__(self):
        super().__init__()
        fileName = input("Enter the file name of a function: ")
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
    ##이전 모듈의 createProblem()의 기능을 생성자로 구현

    def randomInit(self):  ###
        init = []
        for index in range(len(self._p[1][0])):
            init.append(random.uniform(self._p[1][1][index], self._p[1][2][index]))
        return init
    ##이전 모듈내  동명의 함수와 내용 동일

    def evaluate(self, current):
        super().evaluate()
        expr = self._p[0]  # p[0] is function expression
        varNames = self._p[1][0]  # p[1] is domain
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)
    ##evaluate() 실행 시 NumEval(평가횟수)를 1증가시키는 기능을 부모 클래스의 evaluate() 함수로 대체
    ##이외 이전 모듈 내 동명의 함수와 내용 동일

    def describeProblem(self):
        print()
        print("Objective function:")
        print(self._p[0])  # Expression
        print("Search space:")
        varNames = self._p[1][0]  # p[1] is domain: [VarNames, low, up]
        low = self._p[1][1]
        up = self._p[1][2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))
    ##이전 모듈 내 동명의 함수와 내용 동일


    def displaySetting(self, msg):
        super().displaySetting(msg)
        print()
        print("Mutation step size:", DELTA)
    ##사용한 알고리즘명을 msg로 받아 부모 클래스의 displaySetting(msg)로 전달.
    ##이외 이전 모듈 내 동명의 함수와 내용 동일

    def displayResult(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.2f}".format(self.getMinimum()))
        super().displayResult()
    ##evaluate() 실행 시 NumEval(평가횟수)를 1증가시키는 기능을 부모 클래스의 evaluate() 함수로 대체
    ##이전 모듈 내 동명의 함수와 내용 동일

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)
    #이전 모듈 내 동명의 함수와 내용 동일


