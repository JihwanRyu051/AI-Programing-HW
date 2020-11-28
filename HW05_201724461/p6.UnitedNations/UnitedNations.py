import pickle
from nation import Nation

def main():
    nationsDic = {}
    binaryDic = {}
    practice = input("Choose a practice(a or c)")
    if practice.lower() == 'a':
        practiceA(nationsDic)
    else:
        practiceC("nationsDict.dat", binaryDic)


def practiceA(nationsDic):
    print("p6(a)")
    nationsDic = getDicFromText("UN.txt")
    for index in range(3):
        country = input("Enter the name of country: ")
        print(nationsDic[country])

    saveDicToBinary(nationsDic)
    return


def getDicFromText(fileName):
    nationsDic = {}
    infile = open(fileName, 'r')
    for line in infile:
        data = line.split(',')
        country = Nation(data[0], data[1], data[2], data[3])
        nationsDic[country.getName()] = country
    infile.close()
    return nationsDic


def saveDicToBinary(dic):
    outfile = open("nationsDict.dat", "wb")
    pickle.dump(dic, outfile)
    outfile.close()


def practiceC(fileName, binaryDic):
    print("p6(c)")

    binaryDic = getDicFromBinary(fileName)

    for index in range(3):
        count = 0
        cont = input("\nEnter a continent: ")
        contDic = getContDic(binaryDic, cont)
        for country in contDic:
            print("\t" + country)
            count = count+1
            if count == 5:
                break



def getContDic(binaryDic, continent):
    contDic = {}
    for name in binaryDic.keys():
        if binaryDic[name].getContinent() == continent:
            contDic[name] = binaryDic[name]

    contDic = sorted(contDic, key=lambda k: contDic[k].popDensity(), reverse = True)
    return contDic



def getDicFromBinary(fileName):
    infile = open(fileName, 'rb')
    binaryDic = pickle.load(infile)
    infile.close()
    return binaryDic


main()