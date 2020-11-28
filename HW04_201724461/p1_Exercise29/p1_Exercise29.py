def main():
    while True:
        try:
            n = int(input("Enter a nonzero integer: "))
            if n != 0:
                reciprocal = 1/n
                print("The reciprocal of {0} is {1:,.3f}".format(n, reciprocal))
                break
            else:
                print("You entered zero. Try again.")
        except ValueError:
            print("You did not enter a nonzero integer. Try again.")


main()
