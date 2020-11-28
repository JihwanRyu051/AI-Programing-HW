def main():
    names = Infile()
    wordset = Input()
    diff = diffset(wordset, names)
    nlist = Update(names, diff)
    Output(nlist)


def Infile():
    infile = open("Names.txt", 'r')
    names = set([line.rstrip() for line in infile])
    infile.close()
    return names


def Input():
    words = input("Enter the three first names: ")
    wordset = set(word.lstrip() for word in words.split(","))
    return wordset


def diffset(wordset, names):
    diff = wordset - names          ##set operation(-)
    for word in wordset - diff:
        print("{} already exists in the the file.".format(word))
    return diff


def Update(names, diff):
    names.update(diff)              ##set operation(update)
    nlist = list(names)
    nlist.sort()
    for word in diff:
        index = nlist.index(word)
        print("{} adds between {} and {}"
              .format(word, nlist[index - 1], nlist[index + 1]))
    return nlist


def Output(nlist):
    outfile = open("NamesOutput.txt", 'w')
    for name in nlist:
        outfile.write("{}\n".format(name))
    print("Number of Lines: {0:}".format(len(nlist)))
    outfile.close()


main()

