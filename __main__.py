actualNumber = 45
attempts = 1
guessNumber = int(input("I am thinking of a number between 1 and 50. What is the number i AM THINKING OF?\n"))

while guessNumber != actualNumber:
    attempts += 1

    if guessNumber < actualNumber:
        print(f"Your number, {guessNumber} is too low")
        guessNumber = int(input("Try again!\n"))
    elif guessNumber > actualNumber:
        print(f"Your number, {guessNumber} is too high")
        guessNumber = int(input("Try again!\n"))
else:
    print(f"Congratulations!, {guessNumber} is the number and you guess it from {attempts} attempts")