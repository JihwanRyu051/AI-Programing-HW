s = input("Enter a sentence: ")
L = s.split()
punc = L[-1].find(".")

print("First word: {}".format(L[0]))
print("Last word: {}".format(L[-1][:punc]))
