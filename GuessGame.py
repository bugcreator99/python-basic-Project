setNumber = 5
guessCount = 1
guessLimit = 3

while guessCount < guessLimit:
    userGuessNum = int(input("Guess>>"))
    guessCount += 1
    if setNumber == userGuessNum:
        print("Winner :)")
        break
else:
    print("Loser :(")
