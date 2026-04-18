import random

print(" ")
print("Welcome to Hangman")
print(" ")
print("Im thinking of a word and you will try to guess it in 8 or under tries!")
print(" ")
category = input("Choose norwegian or english (n/e): ")


def clear_ansi():
    print("\033[H\033[J", end="")       # Clears the terminal screen


if category == "n":
    word_database = [
        # Norwegian words
        "hund", "katt", "bil", "hus", "bok", "sol", "regn", "snø", "vind", "fjell",
        "sjø", "skog", "blomst", "fugl", "fisk", "eple", "banan", "melk", "brød", "ost",
        "stol", "bord", "vindu", "dør", "lampe", "klokke", "skole", "lærer", "elev", "venn",
        "familie", "mor", "far", "bror", "søster", "bestemor", "bestefar", "baby", "gutt", "jente",
        "dag", "natt", "morgen", "kveld", "uke", "måned", "sommer", "vinter", "høst", "vår"
    ]
    clear_ansi()

elif category == "e":
    word_database = [
        "apple", "train", "beach", "cloud", "dream", "eagle", "flame", "grape", "happy", "island",
        "jungle", "kite", "lemon", "music", "night", "ocean", "piano", "queen", "river", "stone",
        "tiger", "umbrella", "valley", "wallet", "yellow", "zebra", "bridge", "candle", "dinner", "earth",
        "forest", "garden", "harbor", "igloo", "jacket", "kettle", "ladder", "mirror", "needle", "orange",
        "pencil", "rabbit", "shadow", "temple", "uncle", "violet", "window", "explore", "farmer", "golden",
    ]
    clear_ansi()

else:
    print("Choose a catergory between norwgegian (answer with a simple n) or english (answer with a simple e)")

# Chooses a word at random from the database
word = random.choice(word_database)
# Creates a list of guessed words (currently empty)
guessed = []
lives = 7                           # Starts at 6 lives (left)

STAGES = [
    """
    Hangman by Jakob
    _________
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    """,
    """
    Hangman by Jakob
    _________
    |       |
    |       O
    |      /|\\
    |      /
    |
    """,
    """
    Hangman by Jakob
    _________
    |       |
    |       O
    |      /|\\
    |
    |
    """,
    """
    Hangman by Jakob
    _________
    |       |
    |       O
    |      /|
    |
    |
    """,
    """
    Hangman by Jakob
    _________
    |       |
    |       O
    |       |
    |
    |
    """,
    """
    Hangman by Jakob
    _________
    |       |
    |       O
    |
    |
    |
    """,
    """
    Hangman by Jakob
    _________
    |       |
    |
    |
    |
    |
    """,
    """
    Hangman by Jakob
    _________
    |       
    |
    |
    |
    |
    """
]  # Creates 6 different stages, each for one of the six lives. Sorted from latest to earliest (will be explained in detail later)

# Creates the letter-line, customized after the randomized word.


def show_word(word, guessed):
    display = ""                        # Sets the line as empty
    for letter in word:                 # This basically checks a letter, then moves to the right. This leads to the "perfect placement"
        if letter in guessed:
            # Adds the letter if the letter is in the list guessed, ergo your guessed letters
            display += letter + " "
        else:
            display += "_ "             # If not in guessed, placeholder
    return display

# Creates the main display.


# Sets parameters that is updated throughout the code
def full_display(lives, word, guessed):
    # First clears the terminal
    clear_ansi()
    # Prints the display from stage_list number equal to lives left.
    print(STAGES[lives])
    print("-------------------------------------------")
    # Prints out the updated letter_line
    print("\n" + show_word(word, guessed))
    print(" ")
    # Prints out amount of lives left
    print("Lives:", lives)
    print(" ")
    # Prints the letters that is guessed and if no guessed, prints "none"
    print("Letters guessed:", ", ".join(guessed) if guessed else "none")
    print(" ")
    print("-------------------------------------------\n")


# Function for retreaving the guess from user
def get_guess(guessed):
    while True:
        # Takes a letter from user and turns it into lowercase
        guess = input("Guess a letter: ").lower()
        if guess == "secret1":
            print(word)
        elif len(guess) != 1:
            # If user input is above or below 1, prints out one letter at a time
            print("One letter at a time.")
        elif guess in guessed:
            # If user guesses guess word that is already guessed
            print("Already guessed that.")
        else:
            return guess


while lives > 0:                                            # The general game order
    # Displays the display with updated arguments
    full_display(lives, word, guessed)
    if all(letter in guessed for letter in word):           # If all letters guessed print you win
        print("You win! The word was:", word)
        break
    # Runs the guess_getting code
    guess = get_guess(guessed)
    # Adds the newest guess to the "guessed" list
    guessed.append(guess)
    if guess not in word:
        # If you guess wrong, removes 1 life.
        lives -= 1
        if lives == 0:
            # If you die, prints out new screen
            full_display(lives, word, guessed)
            # Prints game over screen
            print("Game over! The word was:", word)
        else:
            # If the guess is not in the word or you are not dead: print that the guess was wrong
            print("Wrong!")
    else:
        # If not not in word, meaning in word, print correct
        print("Correct!")
