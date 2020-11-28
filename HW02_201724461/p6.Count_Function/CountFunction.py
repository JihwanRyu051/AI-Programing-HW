def cnt(s, ch):
    c = 0
    while s.find(ch) != -1:
        s = s[s.find(ch) + 1:]
        c += 1

    return c


def main():
    s = "electromagnetics"
    ch = "e"
    print("count '{char}' from '{string}' is {count}".format(char=ch, string=s, count=cnt(s, ch)))

    return 0


main()
