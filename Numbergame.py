import random

num = random.randint(1, 100)
guesses = 0

print("Im thinking of a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    guesses = guesses + 1

    if guesses >= 8:
        print("Oops, used too long.")
        break

    if guess < num:
        print("Nope, too low")

    elif guess > num:
        print("Oo, too high")

    else:
        print(
            f"Wow! Great job. The number was {num} and you did it in only {guesses} guesses")

        if guesses < 6:
            print("Wow, you really did it in under 5 guesses - impressive!")

        answer = input("Play again? y/n: ")

        if answer == "n":
            break
        elif answer == "y":
            True
