import random


def main():
    tosses = 100
    times = 0
    coin = ["Head", "Tail"]
    for toss in range(tosses):
        side = random.choice(coin)
        if side == "Head":
            times = times + 1

    print("The number of times that a \"Head\" occurs in {} tosses: {}".format(tosses,times))


main()
