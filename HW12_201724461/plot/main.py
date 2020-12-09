import matplotlib.pyplot as plt

def main():
    x = []
    y_lin = []
    y_nonlin = []
    infile01 = open("k.txt", 'r')
    infile02 = open("rmse_lin.txt", 'r')
    infile03 = open("rmse_nonlin.txt", 'r')
    for line in infile01:
        x.append(float(line))
    for line in infile02:
        y_lin.append(float(line))
    for line in infile03:
        y_nonlin.append(float(line))
    plt.plot(x, y_nonlin)
    plt.xlabel('Number of K')
    plt.ylabel('rmse')
    plt.legend(['case: nonlin'])
    plt.show()
    infile01.close()
    infile02.close()
    infile03.close()


main()