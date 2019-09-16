import WrittenNumbersFuncs
number = list(str(input("Number: ")))
save = ""
save1 = ""
save2 = ""
save3 = ""
save4 = ""
save5 = ""
save6 = ""
save7 = ""
save8 = ""
save9 = ""
save10 = ""
save11 = ""
save12 = ""
save13 = ""
save14 = ""
while True:
    if WrittenNumbersFuncs.spec(number):
        print(WrittenNumbersFuncs.spec(number))
        break
    if len(number) == 1:
        if number[0] == "0":
            number.remove(number[0])
        else:
            save = WrittenNumbersFuncs.written(number[0])
            number.remove(number[0])
    elif len(number) == 2:
        save1 = WrittenNumbersFuncs.doubles(number)
    elif len(number) == 3:
        save2 = WrittenNumbersFuncs.hundreds(number)
    elif len(number) == 4:
        save3 = WrittenNumbersFuncs.add(number, "Thousand")
    elif len(number) == 5:
        save4 = WrittenNumbersFuncs.doubles(number)
    elif len(number) == 6:
        save6 = WrittenNumbersFuncs.hundreds(number)
    elif len(number) == 7:
        save7 = WrittenNumbersFuncs.add(number, "Million")
    elif len(number) == 8:
        save8 = WrittenNumbersFuncs.doubles(number)
    elif len(number) == 9:
        save9 = WrittenNumbersFuncs.hundreds(number)
    elif len(number) == 10:
        save10 = WrittenNumbersFuncs.add(number, "Billion")
    elif len(number) == 11:
        save11 = WrittenNumbersFuncs.doubles(number)
    elif len(number) == 12:
        save12 = WrittenNumbersFuncs.hundreds(number)
    elif len(number) == 13:
        save13 = WrittenNumbersFuncs.add(number, "Trillion")
    elif len(number) == 0:
        print(save13, save12, save11, save10, save9, save8, save7, save6, save5, save4, save3, save2, save1, save,
              save14)
        break