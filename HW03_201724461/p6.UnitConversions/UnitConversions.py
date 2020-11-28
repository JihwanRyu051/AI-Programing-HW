def main():
    dic = dicOfCSV()
    data = Input(dic)
    print("Length in miles: {0:.4f}".
          format((data[2] * dic[data[0]]) / dic[data[1]]))


def dicOfCSV():
    infile = open("Units.txt", 'r')
    dic = {}
    for line in infile:
        data = line.split(',')
        dic.update({data[0]: float(data[1])})
    infile.close()
    return dic


def Input(dic):
    fromUnit = input("Unit to convert from: ")
    while not fromUnit in dic.keys():
        print("That Unit doesn't exist in the CSV")
        fromUnit = input("Unit to convert from: ")
    toUnit = input("Unit to convert to: ")
    while not toUnit in dic.keys():
        print("That Unit doesn't exist in the CSV")
        toUnit = input("Unit to convert from: ")
    length = float(input("Enter length in {}: ".format(fromUnit)))
    data = [fromUnit, toUnit, length]
    return data


main()







