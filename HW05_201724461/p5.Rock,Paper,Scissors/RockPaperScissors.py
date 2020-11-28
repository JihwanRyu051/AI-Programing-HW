import random

class Contestant:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def getScore(self):
        return self._score

    def getName(self):
        return self._name

    def win(self):
        self._score += 1

    def __str__(self):
        return "{name}: {score} ".format(name=self._name, score=self._score)


class Computer(Contestant):
    def getSign(self):
        sign = random.choice(["rock", "scissors", "paper"])
        print("{name} chooses {hand}".format(name=self._name, hand=sign))
        return sign.lower()


class Human(Contestant):
    def getSign(self, truth):
        while True:
            try:
                sign = input("\n{name}, enter your choice: "
                             .format(name=self._name))
                if sign.lower() in truth.keys():
                    break
                else:
                    warning(truth)
            except ValueError:
                warning(truth)

        return sign.lower()


def warning(truth):
    print("YOU CAN CHOOSE TRUTH ONLY.")
    print("TRUTH: ", end="")
    for sign in truth.keys():
        print(sign, end="  ")



def battle(com, human, dic):
    humansign = human.getSign(dic)
    comsign = com.getSign()
    if dic[comsign] == humansign:
            com.win()
    elif dic[humansign] == comsign:
            human.win()
    print(human, end="  ")
    print(com)


def whoIsWinner(com, human):
    comscore = com.getScore()
    humanscore = human.getScore()
    if comscore > humanscore:
        print("\n{com} WINS".format(com=com.getName().upper()))
    elif comscore < humanscore:
        print("\n{human} WINS".format(human=human.getName().upper()))
    else:
        print("\nTIE")


def main():
    truth = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    for index in range(3):
        print("\ncase {}\n".format(index+1))
        hName = input("Enter name of human: ")
        cName = input("Enter name of computer: ")
        com = Computer(cName, 0)
        human = Human(hName, 0)

        for round in range(3):
            battle(com, human, truth)

        whoIsWinner(com, human)


main()

