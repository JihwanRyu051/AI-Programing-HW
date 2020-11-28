import fraction


def main():
    for index in range(3):
        denom = 1
        decimal = inputDecimal()
        frac = makeFrac(decimal, denom)
        outputFrac(frac)
    return


def inputDecimal():
    while True:
        try:
            decimal = float(input("Enter a positive decimal number less than 1: "))
            if decimal < 1:
                break
            else:
                print("Decimal number less than 1, only.")
        except ValueError:
            print("Decimal number less than 1, only.")
    return decimal


def makeFrac(decimal, denom):
    while decimal != int(decimal):
        denom *= 10
        decimal *= 10
    frac = fraction.Fraction(decimal, denom)
    return frac


def outputFrac(frac):
    print("Converted to fraction: ", end='')
    print(frac,end="\n\n")


main()