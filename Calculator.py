num1 = int(input("First Number: "))
op = str(input("Operator: "))
num2 = int(input("Second Number: "))


def calc(number0, operator, number1):
    if operator == "+":
        answer = number0 + number1
        print(answer)
    elif operator == "-":
        answer = number0 - number1
        print(answer)
    elif operator == "x" or operator == "*":
        answer = number0 * number1
        print(answer)
    elif operator == "/":
        answer = number0 / number1
        print(answer)
    else:
        print("Please enter a valid operator")
        op = input("Try Again: ")
        calc(num1, op, num2)


calc(num1, op, num2)

while True:

    another = input("Would you like to do another? Yes or No")
    if another == "Yes":
        num1 = int(input("First Number: "))
        op = str(input("Operator: "))
        num2 = int(input("Second Number: "))
        calc(num1, op, num2)
    elif another == "No":
        print("Okay Bye!")
        break
    else:
        print("Invalid")