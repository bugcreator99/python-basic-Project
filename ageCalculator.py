print("What is your Name: ")
name = input()
print(name, "How old are you?")
age = int(input())

days = age * 365
minutes = age * 525948
seconds = age * 31556926

print(name, 'You has lived for',days,'days',minutes,'minutes',seconds,'seconds')