import random
import string


def main():
    random_three_alpha = random.sample(string.ascii_lowercase, 3)
    for alpha in random_three_alpha:
        print(alpha, end=" ")


main()
