def main():
    infile = open("SomeMonths.txt", 'r')
    listOfMonths = set([line.rstrip() for line in infile])
    infile.close()
    contain = containRinMonths(listOfMonths)
    remain = listOfMonths - contain
    print("Months Contain 'r':")
    for month in contain:
        print(month)
    print("\nRemain Months:")
    for month in remain:
        print(month)


def containRinMonths(listOfMonths):
    contain = set([])
    for month in listOfMonths:
        if "r" in month:
            contain.add(month)
    return contain


main()
