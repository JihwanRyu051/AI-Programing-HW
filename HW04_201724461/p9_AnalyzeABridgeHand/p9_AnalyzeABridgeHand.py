import random
import pickle


def main():
    infile = open("DeckOfCardsList.dat", 'rb')
    deck = pickle.load(infile)
    pack = random.sample(deck, 13)
    dic = countForSuits(pack)
    for k in dic.keys():
        if dic[k] != 0:
            print("Number of {} is {}".format(k, dic[k]))


def countForSuits(pack):
    dic = {"♠": 0, "♥": 0, "♣": 0, "♦": 0}
    for card in pack:
        for k in dic.keys():
            if k == card[-1]:
                dic[k] = dic[k]+1
    return dic


main()
