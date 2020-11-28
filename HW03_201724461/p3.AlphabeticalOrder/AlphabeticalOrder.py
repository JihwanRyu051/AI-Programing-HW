def main():
    word = input("Enter a word: ")
    if TripleConsecutive(word):
        print("{} contains three successive letters in consecutive alphabetical order.".format(word))
    else:
        print("{} doesn't contain three successive letters.".format(word))


def TripleConsecutive(word):
    pre = 0
    index = 0
    cntlist = [0]
    for ch in word.lower():
        if abs(pre - ord(ch)) == 1:
            cntlist[index] += 1
        else:
            index += 1
            cntlist.append(0)
        pre = ord(ch)
    for cnt in cntlist:
        if cnt >= 2:
            return True
    return False


main()
