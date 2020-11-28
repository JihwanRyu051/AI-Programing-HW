from problem import *
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    p = tsp()
    firstChoice(p)
    p.describeProblem()
    p.displaySetting("First-Choice")
    p.displayResult()
##tsp 생성자로 변수 p 생성(p. _p = (numCities, locations, table), _minimum = 0.0, _NumEval = 0, _solution = [])
##이전 모듈 내 함수들을 클래스 p 내장 함수로 호출

def firstChoice(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    p.setSolution(current)
    p.setMinimum(valueC)
##이전 모듈 내 동명의 함수와 기능적으로 동일
##변수 p에 최종 solution과 minmum을 저장


def randomMutant(current, p):
    data = p.getP()
    while True:
        i, j = sorted([random.randrange(data[0]) for _ in range(2)])
        if i < j:
            curCopy = p.inversion(current, i, j)
            break
    return curCopy


main()
