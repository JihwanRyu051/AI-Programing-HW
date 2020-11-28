starting = input("Starting word: ")
nine = "NINELETTERS"
single = "ASINGLEWORD"

crossed = []
remain = []

for alpha in starting:
    if alpha in nine:
        index = nine.find(alpha)
        nine = nine[:index]+nine[index+1:]
        crossed.append(alpha)
    else:
        remain.append(alpha)


print(" ".join(crossed))
print(" ".join(remain))

