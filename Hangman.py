# Can add "Choose category"

import random

word_database = [
    "variable", "function", "array", "string", "boolean", "integer",
    "float", "loop", "recursion", "syntax", "parameter", "argument",
    "scope", "constant", "operator", "expression", "statement",
    "class", "object", "inheritance", "polymorphism", "encapsulation",
    "abstraction", "instantiation", "constructor", "method", "interface",
    "linked_list", "stack", "queue", "hash_map", "binary_tree", "graph",
    "heap", "sorting", "searching", "big_o_notation", "pointer", "node",
    "compiler", "interpreter", "debugger", "repository", "version_control",
    "git", "ide", "api", "framework", "library", "documentation", "refactoring",
    "frontend", "backend", "fullstack", "http", "protocol", "server",
    "client", "database", "query", "json", "xml", "rest", "websocket",
    "operating_system", "kernel", "multithreading", "concurrency",
    "memory_management", "garbage_collection", "binary", "hexadecimal",
    "compilation", "runtime", "virtual_machine", "containerization"
]  # A small database of code and cs related words :)

# Chooses a word at random from the database
word = random.choice(word_database)
# Creates a list of guessed words (currently empty)
guessed = []
lives = 6                           # Starts at 6 lives (left)

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
]  # Creates 6 different stages, each for one of the six lives. Sorted from latest to earliest (will be explained in detail later)


def clear_ansi():
    print("\033[H\033[J", end="")       # Clears the terminal screen


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
        if len(guess) != 1:
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
            # If the guess is not in the word or you are dead: print that the guess was wrong
            print("Wrong!")
    else:
        # If not not in word, meaning in word, print correct
        print("Correct!")
