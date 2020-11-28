from problem import *
from optimizer import *

problemMSG = ["\nSelect the problem type: ", ["Numerical Optimization", "TSP"]]
algorithmMSG = ["\nSelect the search algorithm: ",
                ["Steepest-Ascent", "First-Choice", "Gradient Descent"]]
optDic = {1: steepestAscent(),
          2: firstChoice(),
          3: gradientDescent()}


def setQuery(msgArr):
    while True:
        index = 1
        try:
            print(msgArr[0])
            for msg in msgArr[1]:
                print("\t{}. {}".format(index, msg))
                index = index+1
            select = int(input("Enter the number: "))
            if not 1 <= select <= len(msgArr[1]):
                raise ValueError
            break
        except ValueError:
            print()
            print("!!!Only integer 1 ~ {}!!!".format(len(msgArr[1])))
    return select


def start():
    pChoice = setQuery(problemMSG)
    if pChoice == 1:
        p = numeric()
        optChoice = setQuery(algorithmMSG)
    else:
        p = tsp()
        optChoice = setQuery([algorithmMSG[0], algorithmMSG[1][0:2]])
    return p, optDic[optChoice]


def main():
    p, opt = start()
    opt.run(p)
    p.describeProblem()
    opt.displaySetting()
    p.displayResult()


main()
