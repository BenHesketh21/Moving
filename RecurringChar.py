string0 = input("Letters: ")
string0 = list(string0)
answer = False
list1 = []
list1.append(string0[0])
string0.remove(string0[0])
for char in string0:
    if char in list1:
        CHAR = char.upper()
        answer = True
        break
    else:
        list1.append(char)

if answer is True:
    print("Yes", CHAR)
else:
    print("Nope")




