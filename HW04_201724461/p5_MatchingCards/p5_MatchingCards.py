import random
import pickle


def main():
    times = 10000
    infile = open("DeckOfCardsList.dat", 'rb')
    newOne = pickle.load(infile)
    infile.close()
    total = 0
    for time in range(times):
        deck1 = newOne.copy()
        deck2 = newOne.copy()
        random.shuffle(deck1)
        random.shuffle(deck2)
        total += matchTheCards(deck1, deck2)
    avg = total / times
    print("The average number of cards that matched was {:.3f}."
          .format(avg))


def drawAcard(deck):
    opencard = deck[-1]
    del deck[-1]
    return opencard


def matchTheCards(deck1, deck2):
    match = 0
    while True:
        if not deck1 or not deck2:
            break
        card1 = drawAcard(deck1)
        card2 = drawAcard(deck2)
        if card1 == card2:
            match += 1
    return match


main()