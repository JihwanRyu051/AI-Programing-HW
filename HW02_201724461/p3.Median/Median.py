enter = int(input("How many numbers do you want to enter? "))

N = [0 for i in range(enter)]

for i in range(0, enter):
    N[i] = int(input("Enter a number: "))

N.sort()

if enter % 2 == 1:
    print("Median: {0:,.1f}".format(N[int(enter/2)]))
else:
    Median = (N[int(enter/2)] + N[int(enter/2)-1])/2
    print("Median: {0:,.1f}".format(Median))
