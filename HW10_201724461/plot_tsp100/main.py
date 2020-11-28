import numpy as np
import matplotlib.pyplot as plt


def main():
    y_firstChoice = []
    y_simulatedAnnealing = []
    infile01 = open("tsp100_firstChoice.txt", 'r')
    infile02 = open("tsp100_simulatedAnnealing.txt", 'r')
    i = 0
    for line01 in infile01:
        y_firstChoice.append(float(line01))
        i = i+1
    x_firstChoice = np.arange(i) ## tsp100_firstChoice.txt의 line의 수를 x축의 차원으로 설정
    i = 0
    for line02 in infile02:
        y_simulatedAnnealing.append(float(line02))
        i = i+1
    x_simulatedAnnealing = np.arange(i) ## tsp100_simulatedAnnealing.txt의 line의 수를 x축의 차원으로 설정

    plt.plot(x_firstChoice, y_firstChoice)
    plt.plot(x_simulatedAnnealing, y_simulatedAnnealing)
    plt.xlabel('Number of Evaluations')
    plt.ylabel('Tour Cost')
    plt.title('Search Performance (TSP-100)')
    plt.legend(['First-Choice HC', 'Simulated Annealing'])
    plt.show()
    infile01.close()
    infile02.close()


main()
