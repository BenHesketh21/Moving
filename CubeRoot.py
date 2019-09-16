number = float(input("Number: "))


def midpoint(x):
    for i in range(1, int(x)):
        if i * i == x:
            print("Square Root of,", int(x),  "is", i)
        elif i * i > x:
            mid = ((i - 1) * i) / 2
            return midpoint(mid)
        elif i * i < x:
            mid = (())
        else:
            continue


midpoint(number)
