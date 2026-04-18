import random

num = random.randint(1, 100)
guesses = 0

# print("Im thinking of a number between 1 and 100. Try to guess it un under 7 guesses!")
print(" ")
print("Jeg tenker på et tall mellom 1 og 100, og du skal prøve å gjette det på under 7 forsøk!")

while True:

    # guess = int(input("Guess a number between 1 and 100: "))
    print(" ")
    guess = int(input("Gjett tallet: "))

    if guess == 2304:
        print(num)
        # break

    guesses = guesses + 1

    if guesses >= 8:
        # print("Oops, used too long.")
        print(" ")
        print("Brukte for mye dessvere..")
        break

    if guess < num:
        # print("Nope, too low")
        print("Høyere!")
        print(f"Du har nå brukt {guesses} gjett")

    elif guess > num:
        # print("Oo, too high")
        print("For høyt!")
        print(f"Du har nå brukt {guesses} gjett")

    elif guess == num:
        print(" ")
        print(
            f"Wow! Bra jobba. Tallet var {num} og du klarte det på bare {guesses} gjett")

        if guesses < 6:
            # print("Wow, you really did it in under 5 guesses - impressive!")
            print(" ")
            print("Du er supergod! På under 6 gjett!")

        # answer = input("Play again? y/n: ")
        print(" ")
        answer = input("Har du lyst til å spille igjen? y/n: ")

        if answer == "n":
            break
        elif answer == "y":
            num = random.randint(1, 100)
            guesses = 0
            True
