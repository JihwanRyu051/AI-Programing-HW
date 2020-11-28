word = input("Enter word to translate: ")
vowels = "aeiou"
L = list(word)
vowel = True

while True:
    if L[0] in vowels:
        break
    else:
        L.append(L[0])
        L.remove(L[0])
        vowel = False

if vowel:
    pig = ''.join(L) + 'way'
else:
    pig = ''.join(L) + 'ay'

print("The word in Pig Latin is {}.".format(pig))





