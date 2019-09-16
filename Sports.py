sports = open("teams.txt", "w")
sportteams = "Man U\n" + "Man City\n" + "Arsenal\n" + "Bolton\n" + "Blackburn"
sports.write(sportteams)
sports.close()

sports = open("teams.txt", "r")
print("First Team: " + sports.readline())
print("Second Team: " + sports.readline())