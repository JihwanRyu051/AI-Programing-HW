def main():
    m = int(input("Input Number m:"))
    n = int(input("Input Number n:"))
    displaySequenceOfNumbersRecursive(m, n)


def displaySequenceOfNumbersRecursive(m, n):
    if m > n:
        return m
    else:
        print(m)
        return displaySequenceOfNumbersRecursive(m+1, n)


main()
