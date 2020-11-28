import fraction

def main():
    n = int(input("Enter numerator of fraction: "))
    d = int(input("Enter denominator of fraction: "))
    frac = fraction.Fraction(n, d)
    print("Reduction to lowest terms: " + str(frac))
    return


main()
