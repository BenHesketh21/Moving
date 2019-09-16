file = open("filename.txt", "r")

outfile = ""

for line in range(10):
    if line == 0:
        file.readline()
        outfile += "This is a new line\n"
    else:
        outfile += file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()