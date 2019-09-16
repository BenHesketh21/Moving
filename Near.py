word1 = input("First Word: ")
word2 = input("Second Word: ")


def near(string0, string1):
    for j in string0:
        if string0.count(j) == 1:
            new = string0.replace(j, "")
            print(new)
            if new == string1:
                return True
            else:
                continue
        else:



if near(word1, word2):
    print("True")
else:
    print("False")

'''CORRECT
word1 = input("Please enter a word: ")
word2 = input("Please enter another word: ")
def near(word1, word2):
   i = 0
   status = False
   while i < len(word1):
       new_word = word1[:i] + word1[i+1:]
       if new_word == word2:
           status = True
           return(status)
       else:
           i+=1
   return(status)
print(near("reset","rest"))'''
