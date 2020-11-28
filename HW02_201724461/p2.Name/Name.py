FullName = input("Enter a 3-part name: ")
begin = FullName.find(" ")
end = FullName[begin+1:].find(" ")
print("Middle name: {}".format(FullName[begin+1:begin+1+end]))
