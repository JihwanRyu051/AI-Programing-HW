multi = 9
for number in range(1000, 10000):
    sp = str(number)
    spn = 0
    index = 0
    for s in sp:
        spn += int(s) * 10 ** index
        index += 1

    if number*multi == spn:
        print("Since {m} times {n} is {s},".format(m=multi, n=number, s=spn))
        print("the special number is {n}".format(n=number))
