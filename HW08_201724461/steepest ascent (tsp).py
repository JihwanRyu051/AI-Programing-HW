from problem import *


def main():
    p = tsp()
    steepestAscent(p)
    p.describeProblem()
    p.displaySetting("Steepst-Ascent")
    p.displayResult()
##tsp 생성자로 변수 p 생성(p. _p = (numCities, locations, table), _minimum = 0.0, _NumEval = 0, _solution = [])
##이전 모듈 내 함수들을 클래스 p 내장 함수로 호출

def steepestAscent(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
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
    data = p.getP()
    n = data[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = p.inversion(current, i, j)
            count += 1
            neighbors.append(curCopy)
    return neighbors
##이전 모듈 내 함수를 p의 멤버 함수로 호출


def bestOf(neighbors, p):
    best = neighbors.pop()
    bestValue = p.evaluate(best)
    for neighbor in neighbors:
        nValue = p.evaluate(neighbor)
        if nValue < bestValue:
            best = neighbor
            bestValue = nValue
    return best, bestValue
##이전 모듈 내 함수를 p의 멤버 함수로 호출


main()
