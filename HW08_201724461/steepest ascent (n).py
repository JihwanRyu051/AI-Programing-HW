from problem import *

def main():
    p = numeric()
    steepestAscent(p)
    p.describeProblem()
    p.displaySetting("Steepest-Ascent")
    p.displayResult()
##numeric 생성자로 변수 p 생성(p. _p = (expresion, domain), _NumEval = 0, _minimum = 0, _solution = [])
##이전 모듈 내 함수들을 클래스 p 내장 함수로 호출

def steepestAscent(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.setSolution(current)
    p.setMinimum(valueC)
##이전 모듈 내 동명의 함수와 기능적으로 동일
##변수 p에 최종 solution과 minmum을 저장

def mutants(current, p):
    neighbors = set()
    for index in range(len(current)):
        for d in [-1, 1]:
            neighbor = tuple(mutate(current, index, d*DELTA, p.getP()))
            ##p._p = (expresion, domain)이므로 p._p의 변수 값을 get 함수로 호출 후 mutate 함수로 전달.
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


def bestOf(neighbors, p):
    best = list(neighbors.pop())
    bestValue = p.evaluate(best)
    for tupNeighbor in neighbors:
        neighbor = list(tupNeighbor)
        candidate = p.evaluate(neighbor)
        if candidate < bestValue:
            best = neighbor
            bestValue = candidate
    return best, bestValue


main()
