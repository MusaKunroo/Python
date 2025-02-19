guess_chance=1
guess_limit=3
winning_number=10
while guess_chance<=guess_limit:
    guess=int(input("Guess the winning number:"))
    guess_chance+=1
    if guess==winning_number:
        print("Congratulations! you guessed the correct number ")
        break
    else:
        print("Wrong guess try again:")
else:
    print("You failed the game")