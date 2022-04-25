firstName = input("enter your first name: ")
lastName = input("enter your last name: ")
fullName = f"{firstName} {lastName}"

print("Full Name: ",fullName)
print("Title is: ",fullName.title())
print("Upper case: ",fullName.upper())

changeSecondName = input("replace your second name: ")
newFullName = fullName.replace(lastName,changeSecondName)

print("New Full Name: ",newFullName)