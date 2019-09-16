id_number = str(input("Which ID do you wish to delete?"))
users = open("users.txt", "r")
outfile = ""
for line in users:  # goes through all the lines, as soon as it recognises the ID number it skips the whole entry
    if line == (id_number + "\n"):
        users.readline()
        users.readline()
        users.readline()
        users.readline()
        users.readline()
        users.readline()
    else:
        outfile += line
users.close()
users2 = open("users2.txt", "w")
users2.write(outfile)
users2.close()
