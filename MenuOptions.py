print("Menu")
print("1 - Add")
print("2 - Amend")
print("3 - delete")
print("4 - Display")

menu_option = int(input("Enter Option:"))

if menu_option == 1:
    print("Option 1 - Add Selected")
elif menu_option == 2:
    print("Option 2 - Amend Selected")
elif menu_option == 3:
    print("Option 3 - Delete Selected")
elif menu_option == 4:
    print("Displaying Menu")
else:
    print("Please choose a appropriate number")