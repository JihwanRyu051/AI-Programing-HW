from problem import *

EPSILON = 0.0001
##EPSILON 값을 10^(-4)으로 설정


def main():
    p = numeric()
    gradientDecent(p)
    p.describeProblem()
    p.displaySetting("Gradient-decent")
    p.displayResult()
##numeric 생성자로 변수 p 생성(p. _p = (expresion, domain), _NumEval = 0, _minimum = 0, _solution = [])
##이전 모듈 내 함수들을 클래스 p 내장 함수로 호출


def gradientDecent(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        grd = gradient(p, current, valueC)
        ##모든 원소의 미분 값들의 배열
        successor = gradientMutant(p, grd, current)
        ##모든 원소를 각자의 미분 값만큼 감소
        valueS = p.evaluate(successor)
        ##각각의 미분 값만큼 감소 시킨 원소들을 매개변수로 지정해 알고리즘 값을 계산
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
        ##계산 값이 기존 값 미만일 경우 기존 배열과 값을 gradient로 변형한 배열과 값으로 업데이트
        ##계산 값이 기존 값 이상일 때 반복문 탈출
    p.setSolution(current)
    p.setMinimum(valueC)
    ##최종 배열과 값을 p에 저장


def gradient(p, current, valueC):
    grd = []
    ##모든 원소의 미분값을 저장할 빈 배열을 선언
    domain = p.getP()[1]
    ##p._p[1][0] = lower-bound, p._p[1][0] = upper-bound
    for index in range(len(current)):
        l = domain[1][index]
        u = domain[2][index]
        x = current[index]
        ##현 배열 내 index번째 원소를 x에 저장
        c_prime = current[:index]
        ##현 배열 내 0부터 index-1까지의 원소를 c_prime에 우선적으로 저장
        if l <= (current[index] + EPSILON) <= u:
            x += EPSILON
        ##x+EPSILON이 범위 내에 존재할 경우 x을 EPSILON만큼 증가
        c_prime.append(x)
        c_prime.extend(current[index + 1:])
        ##c_prime 배열에 x를 추가
        ##x_index 이후의 모든 원소를 c_prime에 저장
        valueX = p.evaluate(c_prime)
        ##현 배열 기반으로 index번째 원소에 EPSILON을 더한 c_prime 배열의 알고리즘 값을 계산
        grd.append((valueX - valueC) / EPSILON)
        ##현 배열의 index번째 원소의 미분 값을 grd 배열에 저장
    return grd
    ##모든 원소의 미분 값을 저장한 grd배열을 return


def gradientMutant(p, grd, current):
    successor = []
    for index in range(len(current)):
        s = current[index] - DELTA * grd[index]
        successor.append(s)
    return successor
    ##모든 원소를 각자의 미분 값만큼 감소

main()

