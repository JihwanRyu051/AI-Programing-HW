line = input("Enter a sentence: ")
wtr = input("Enter word to replace: ")
rw = input("Enter replacement word: ")
search = False

index = line.find(wtr)

while index >= 0:
    line = line[:index]+rw+line[index+len(wtr):]
    search = True
    index = line.find(wtr)

if search:
    print(line)
else:
    print("Can't find the word to replace in a sentence!")