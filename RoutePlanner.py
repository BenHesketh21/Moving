#peaks = list(input("Enter List Of Peaks: "))
#peaksint = []
#for i in range(len(peaks)):
  #  peaksint.append(int(peaks[i]))
#print(peaksint)
peaksint = [0, 8, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


def path(list0):
    ideal = []
    for j in range(len(list0)):
        if j == 0:
            ideal.append(list0[j])
        elif ideal[j - 1] < list0[j]:
            ideal.append(list0[j])
        elif ideal[j - 1] > list0[j]:
            ideal.append(ideal[j - 1])
            continue
    return ideal


def noreps(list0):
    ideal = []
    for number in list0:
        if list0.index(number) == (len(list0) - 1):
            ideal.append(number)
            break
        elif len(ideal) == 0:
            ideal.append(number)
        elif number in ideal:
            continue
        else:
            ideal.append(number)
    return ideal


answer = path(peaksint)
answer2 = noreps(answer)
print(answer2)

