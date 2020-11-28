def main():
    inputWord = input("Enter the word: ")
    word = inputWord.lower()
    if isRecursiveAlpha(word):
        print("{} is in alphabetical order.".format(inputWord))
    else:
        print("{} is not in alphabetical order.".format(inputWord))


def isRecursiveAlpha(L):
    if len(L) == 1:
        return True
    elif L[0] <= L[1]:
        return isRecursiveAlpha(L[1:])
    else:
        return False


main()