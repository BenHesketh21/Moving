sports = ["football", "rugby", "cricket", "darts"]
sports.append("basketball")
sports.append("baseball")
sports.insert(0, "softball")
del sports[4]
print(sports[0:5])

string = "We will be the best Python Developers the world has ever seen!"
new_string = string.replace("Python Developers", "Cloud Engineers")
ce = new_string[20:35]
shout = ce.upper()
final_string = "".join(reversed(shout))
print(final_string)