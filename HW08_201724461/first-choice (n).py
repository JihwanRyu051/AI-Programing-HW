from problem import *

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    p = numeric()
    firstChoice(p)
    p.describeProblem()
    p.displaySetting("First-Choice")
    p.displayResult()
##numeric 생성자로 변수 p 생성(p. _p = (expresion, domain), _NumEval = 0, _minimum = 0, _solution = [])
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
##이전 모듈 내 함수들을 클래스 p 내장 함수로 호출

def randomMutant(current, p): ###
    data = p.getP()
    ##p._p = (expression, domain)인 멤버 변수의 값을 get 함수로 호출 후 data 변수에 저장
    i = random.randrange(len(data[1][0]))
    d = random.choice([-1, 1])
    d *= DELTA
    return mutate(current, i, d, data)


def mutate(current, i, d, data): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = data[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy



main()
