file = open("filename.txt", "r")
print("First line: " + file.readline())
print("Rest of File" + file.read())
file.close()