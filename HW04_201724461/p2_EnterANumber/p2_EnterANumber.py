def main():
    while True:
        try:
            num = int(input("Enter an integer from 1 to 100: "))
            if 1 <= num <= 100:
                print("Your number is {0}".format(num))
                break
            else:
                print("Your number was not between")
        except ValueError:
            print("You did not enter an integer.")


main()
