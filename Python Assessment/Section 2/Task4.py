while True:
    field = input("Which field would you like to search?")
    field = field.upper()
    users = open("users.txt", "r")
# got it working for the first entry on all fields and tried using a counter to get the other entries as well by using
# users.seek(count)
# using a list worked better so going with that
    if field == "ID":  # searching by ID
        id1 = input("Enter ID:")
        id1 = id1.upper()
        for line in users:
            line = line.upper()
            if line == (id1 + "\n"):
                print(users.readline(),
                      users.readline(),
                      users.readline(),
                      users.readline(),
                      users.readline(),
                      users.readline())
            else:
                continue
        users.close()
        break
    elif field == "NAME":  # searching by name
        name = input("First Name or Second Name?")
        name = name.upper()
        if name == "FIRST NAME":  # searching by first name
            name = input("Enter First Name: ")
            name = name.upper()
            for line in users:
                line = line.upper()
                if name in line:
                    line = line.title()
                    print(line,
                          users.readline(),
                          users.readline(),
                          users.readline(),
                          users.readline(),
                          users.readline())
            users.close()
            break
        elif name == "SECOND NAME":  # searching by second name
            name = input("Enter Second Name: ")
            list0 = []  # adding all lines to a list to use later
            name = name.upper()
            for line in users:
                line = line.upper()
                list0.append(line)
                if name in line:
                    print(list0[list0.index(line) - 1],  # using list entries saved above
                          line,
                          users.readline(),
                          users.readline(),
                          users.readline(),
                          users.readline())
            users.close()
            break
        else:
            print("Invalid Entry")

    elif field == "ADDRESS":  # searching by address
        address1 = input("Address Line 1, City or Postcode?")
        address1 = address1.upper()
        if address1 == "ADDRESS LINE 1":  # searching by address line 1
            address1 = input("Enter First Line of the Address:")
            list0 = []  # adding each line to a list so I can refer to it later
            address1 = address1.upper()
            for line in users:
                line = line.upper()
                list0.append(line)
                if address1 in line:
                    print(list0[list0.index(line) - 2],
                          list0[list0.index(line) - 1],  # referring to list0 mentioned above
                          line,
                          users.readline(),
                          users.readline(),
                          users.readline())
                    break
                elif address1 not in line:
                    continue
            users.close()
            break
        elif address1 == "CITY":  # searching by city
            address1 = input("Enter City:")
            list0 = []  # adding each line to a list so I can refer to it later
            address1 = address1.upper()
            for line in users:
                line = line.upper()
                list0.append(line)
                if address1 in line:
                    print(list0[list0.index(line) - 3],
                          list0[list0.index(line) - 2],  # referring to list0 mentioned above
                          list0[list0.index(line) - 1],
                          line,
                          users.readline(),
                          users.readline())
                    break
                elif address1 not in line:
                    continue
            users.close()
            break
        elif address1 == "POSTCODE":  # searching by postcode
            address1 = input("Enter Postcode:")
            list0 = []  # adding each line to a list so I can refer to it later
            address1 = address1.upper()
            for line in users:
                line = line.upper()
                list0.append(line)
                if address1 in line:
                    print(list0[list0.index(line) - 4],
                          list0[list0.index(line) - 3],
                          list0[list0.index(line) - 2], # referring to list0 mentioned above
                          list0[list0.index(line) - 1],
                          line,
                          users.readline())
                    break
                elif address1 not in line:
                    continue
            users.close()
            break
        else:
            print("Invalid Entry")
    elif field == "PHONE NUMBER" or field == "NUMBER":  # searching by phone number
        number1 = input("Enter Number:")
        list0 = []  # adding each line to a list so I can refer to it later
        for line in users:
            line = line.upper()
            list0.append(line)
            if number1 in line:
                print(list0[list0.index(line) - 5],
                      list0[list0.index(line) - 4],
                      list0[list0.index(line) - 3],  # referring to list0 mentioned above
                      list0[list0.index(line) - 2],
                      list0[list0.index(line) - 1],
                      line)
            elif number1 not in line:
                continue
        users.close()
        break
    else:
        print("Invalid Field")
        users.close()


