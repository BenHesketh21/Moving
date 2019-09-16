while True:
    field = input("Which field would you like to change?")
    field = field.upper()
    users = open("users.txt", "r")
    outfile = ""
    if field == "NAME":  # changing first name
        name = input("First or Second Name?")
        name = name.upper()
        if name == "FIRST":
            name = input("Enter Old First Name: ")
            name = name.upper()
            for line in users:
                line = line.upper()
                if name in line:
                    name = input("New First Name:")
                    name = name.upper()
                    outfile += name + "\n"
                else:
                    outfile += line
            users.close()
            break
        elif name == "SECOND":  # changing second name
            name = input("Enter Old Second Name: ")
            name = name.upper()
            for line in users:
                line = line.upper()
                if name in line:
                    name = input("New Second Name:")
                    name = name.upper()
                    outfile += name + "\n"
                else:
                    outfile += line
        else:
            print("Invalid Entry")
        users.close()
        break
    if field == "ADDRESS":  # changing address
        address1 = input("Enter First Line of Old Address: ")
        address2 = input("Enter Old City:")
        address3 = input("Enter Old Postcode:")
        address1 = address1.upper()
        address2 = address2.upper()
        address3 = address3.upper()
        for line in users:
            line = line.upper()
            if address1 in line:
                outfile += input("New First Line of Address:") + "\n"
            elif address2 in line:
                outfile += input("New City: ") + "\n"
            elif address3 in line:
                outfile += input("New Postcode: ") + "\n"
            else:
                outfile += line
        users.close()
        break
    if field == "PHONE NUMBER" or field == "NUMBER":  # changing phone number
        number = input("Old Number: ")
        number = number.upper()
        for line in users:
            line = line.upper()
            if number in line:
                number = input("New Number:")
                number = number.upper()
                outfile += number + "\n"
            else:
                outfile += line
        users.close()
        break
    else:
        print("Invalid Entry")
users = open("users.txt", "w")
users.write(outfile)
users.close()

