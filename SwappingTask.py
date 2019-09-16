import random


def selection():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    player_word = ""
    while len(player_word) < 5:
        player_word += random.choice(letters)
    while 5 <= len(player_word) < 7:
        player_word += random.choice(vowels)
    player_word = player_word.upper()
    print("These are your letters: ", player_word)
    player_word = list(player_word)
    return player_word


def score(word2):
    word = input("Enter a word: ")
    word1 = word.upper()
    list0 = list(word1)
    singles = ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"]
    doubles = ["D", "G"]
    triples = ["B", "C", "M", "P"]
    quadruple = ["F", "H", "V", "W", "Y"]
    five = ["K"]
    eights = ["J", "X"]
    tens = ["Q", "Z"]
    points = 0
    for i in range(len(list0)):
        if list0[i] not in list(word2):
            print("Invalid Word")
            score(word2)
            break
        if list0[i] in singles:
            points += 1
        elif list0[i] in doubles:
            points += 2
        elif list0[i] in triples:
            points += 3
        elif list0[i] in quadruple:
            points += 4
        elif list0[i] in five:
            points += 5
        elif list0[i] in eights:
            points += 8
        elif list0[i] in tens:
            points += 10
    return points


final_scores = []
high_scores = {0: "No one"}
winner = "NO ONE WINS"
while True:
    new_player = input("New Player? Y/N: ")
    new_player = new_player.upper()
    if new_player == "Y":
        name = input("Player Name: ")
        random_letters = selection()
        z = score(random_letters)
        x = name + "'s" + " " + "Score:" + " " + str(z)
        x = x.upper()
        final_scores.append(x)
        highest_points = list(high_scores.keys())[0]
        if z > highest_points:
            high_scores = {z: name}
    elif new_player == "N":
        print(10 * "-", "WELL PLAYED!", 10 * "-")
        for j in range(len(final_scores)):
            print(final_scores[j])
            winner = list(high_scores.values())[0].upper()
        print(10 * "-", winner, "WINS", 10 * "-")
        break
    else:
        print("Invalid Entry")




