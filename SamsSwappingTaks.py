import random
import string


def generated_answer():
    if length == 6:
        n = 0
        answer = "".join(random.choice(str(ascii_chrctr) + str(digits) + str(special_character)) for n in range(6))
        return answer
    elif length == 9:
        answer = "".join(random.choice(str(ascii_chrctr) + str(digits) + str(special_character)) for n in range(9))
        return answer
    else:
        answer = "".join(random.choice(str(ascii_chrctr) + str(digits) + str(special_character)) for n in range(15))
        return answer


while True:
    ascii_chrctr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_character = "!£$%&*@?"
    response = False
    if response is False:
        strength = input("Would you like a strong, medium, or weak password?: ")
        strength = strength.lower()
        if strength == "weak":
            length = 6
            response = True
        elif strength == "medium":
            length = 9
            response = True
        elif strength == "strong":
            length = 15
            response = True
        else:
            print("Please enter what strength password you require")
            response = False
    if response is True:
        print(generated_answer())
        again = input("Is this good enough?Y/N")
        again = again.upper()
        if again == "Y":
            print("Enjoy Safely")
            break
        elif again == "N":
            generated_answer()



