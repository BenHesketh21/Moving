file = open("filename.txt","w")
for n in range(1,11):
    newline = "This is line" + str(n) + "\n"
    file.write(newline)
file.close()