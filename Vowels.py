word = input("Word:")
word1 = word
vowels = []
vowels1 = ["a", "e", "i", "o", "u"]
word = word.lower()
for char in word:
    if char in vowels1:
        vowels.append(char)
    else:
        continue

print(word1, "contains", len(vowels), "vowels")
