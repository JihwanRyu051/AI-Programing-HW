def main():
    inputStr = "."
    while True:
        state = input("Enter a state: ")
        if state == "End":
            break
        for alpha in reversed(state):
            inputStr += alpha
        inputStr += ","
    outputStr(inputStr[:-1])


def outputStr(inputStr):
    if inputStr == ".":
        return inputStr
    elif inputStr[-1] == ",":
        print()
        return outputStr(inputStr[:-1])
    else:
        print(inputStr[-1], end='')
        return outputStr(inputStr[:-1])


main()
