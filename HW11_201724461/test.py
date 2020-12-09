import math

def main():
    fileName = 'problem/Ackley.txt'
    infile = open(fileName, 'r')
    line = infile.readline()
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    evaluate = eval(line)
    print(evaluate)
    infile.close()

main()