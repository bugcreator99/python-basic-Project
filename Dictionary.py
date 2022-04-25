number = {
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six','7': 'Seven', '8': 'Eight', '9': 'Nine'
}

userNum = input("Enter your phone number: ")
for i in userNum:
    print(number.get(i,"(!)"),end=" ")
