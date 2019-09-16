users = open("users.txt", "r")
outfile = ""
for line in users:
    outfile += line
users.close()
users_copy = open("users_copy.txt", "w")  # reads the whole file and saves it in OUTFILE and then rewrites it with a
users_copy.write(outfile)                 # new name (copy)
users_copy.close()