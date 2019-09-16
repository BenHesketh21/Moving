count = 0
for num in range(2, 3000000):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1

print(count)
