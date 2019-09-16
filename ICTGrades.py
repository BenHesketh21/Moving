name = input("Name: ")
hmk = int(input("Homework Mark: "))
ass = int(input("Assessment Mark: "))
fin = int(input("Final Exam Mark: "))


def per(home, assess, final):
    if home > 25:
        print("Invalid Homework Score")
        hmk = int(input("Try Again, Homework Mark: "))
        return per(hmk, assess, final)
    elif assess > 50:
        print("Invalid Assessment Score")
        ass = int(input("Try Again, Assessment Mark: "))
        return per(home, ass, final)
    elif final > 100:
        print("Invalid Final Exam Score")
        fin = int(input("Try Again, Final Exam Mark: "))
        return per(home, assess, fin)
    else:
        total = home + assess + final
        percent = (total / 175) * 100
        return percent


def grade(percent):
    if percent < 30:
        return "F"
    elif 30 <= percent < 40:
        return "E"
    elif 40 <= percent < 50:
        return "D"
    elif 50 <= percent < 60:
        return "C"
    elif 60 <= percent < 70:
        return "B"
    elif 70 <= percent:
        return "A"


answer1 = per(hmk, ass, fin)
answer2 = grade(answer1)
print(name)
print(round(answer1, 4), "%")
print("Grade: ", answer2)