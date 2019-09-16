initial = int(input("Initial Value: "))
total = int(input("Desired Total: "))
interest = int(input("Interest Rate: "))
interest = interest / 100
count = 0
while initial < total:
    initial = initial + (initial * interest)
    count += 1
print(count, "years")

dic = {4:5,5:6}
print(list(dic.keys()))