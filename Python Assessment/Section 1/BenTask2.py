FirstName = str(input("First Name:"))
FirstName = FirstName.upper()
SecondName = str(input("Second Name:"))
SecondName = SecondName.upper()
Address1 = str(input("House Number and Street Name:"))
Address1 = Address1.upper()
Address2 = str(input("City:"))
Address2 = Address2.upper()
PostCode = str(input("Postcode:"))
PostCode = PostCode.upper()
Number = str(int(input("Phone Number:")))
users = open("users.txt", "r")
list0 = []
for line in users:
    list0.append(line)  # getting the lines in a list to use the size later
id0 = len(list0) / 8
id1 = id0 + 1
id1 = int(id1)  # using number of lines and dividing by 8 to split the people up
users.close()
# only works up to 6 people :(
users = open("users.txt", "a")
users.write("\n" + str(id1) + "\n")
users.write(FirstName + "\n")
users.write((SecondName + "\n"))
users.write(Address1 + "\n")
users.write(Address2 + "\n")
users.write(PostCode + "\n")
users.write(Number + "\n")
