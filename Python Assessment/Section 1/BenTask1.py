users = open("users.txt", "r")
list0 = []
for line in users:  # to give me the number of lines via the size of the list
    list0.append(line)
users.seek(0)

for i in range(int(len(list0) / 8)):  # using number of lines and dividing by 8 to split the people up
    users.readline()
    a = users.readline()
    b = users.readline()
    c = users.readline()
    d = users.readline()
    e = users.readline()
    f = users.readline()
    g = users.readline()
    print(str(a) + "First Name: " + str(b) + "Second Name: " + str(c) + "Phone Number: " + str(g) + "\nAddress: " +
          str(d) + "         " + str(e) + "         " + str(f))
