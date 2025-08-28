# ✍️ Word Guessing Hangman (Python)
import time
import random

# Function to pick a random word with its hint
def choose_word():
    words_with_hints = {
        'python': "Hint: A popular programming language named after a comedy group, not the snake.",
        'programming': "Hint: The process of writing instructions that computers can execute.",
        'variable': "Hint: A container for storing data values (like x = 10).",
        'function': "Hint: A reusable block of code that performs a specific task.",
        'loop': "Hint: A programming construct to repeat actions (for, while).",
        'class': "Hint: A blueprint for creating objects in object-oriented programming.",
        'object': "Hint: An instance of a class containing data and behavior.",
        'module': "Hint: A file containing Python code that can be imported (e.g., math).",
        'package': "Hint: A collection of Python modules, often with __init__.py.",
        'dictionary': "Hint: A Python collection of key-value pairs (like a real-life glossary).",
        'list': "Hint: A mutable sequence in Python, written with square brackets.",
        'tuple': "Hint: An immutable sequence in Python, similar to a list but unchangeable.",
        'set': "Hint: An unordered Python collection of unique items (like {1, 2, 3}).",
        'exception': "Hint: An error that disrupts program flow, often handled with try/except.",
        'indentation': "Hint: Leading spaces in Python code that define block structure instead of braces.",
        'recursion': "Hint: A function that calls itself until a base condition is met.",
        'algorithm': "Hint: A step-by-step method of solving a problem (like a recipe).",
        'syntax': "Hint: The set of rules that define the structure of valid code.",
        'debugging': "Hint: The process of finding and fixing errors (or bugs) in code.",
        'string': "Hint: A sequence of characters in quotes, e.g., 'hello'.",
        'compiler': "Hint: Converts source code into machine code (Python uses an interpreter instead).",
        'interpreter': "Hint: Executes code line by line, like Python does.",
        'boolean': "Hint: A data type with only two values: True or False.",
        'iteration': "Hint: Repeated execution of statements, usually inside loops."
    }
    return random.choice(list(words_with_hints.items()))

# Function to show the word with blanks and revealed letters
def reveal_progress(word, revealed_indices):
    display = ""
    for i, ch in enumerate(word):
        if i in revealed_indices:
            display += ch + " "
        else:
            display += "_ "
    return display.strip()

def play_game(name):
    # Get word and hint
    word, hint = choose_word()
    turns = 5
    guesses = []
    revealed_indices = set()

    print("\nYour word has", len(word), "letters.")
    print(hint)
    print("Current word:", reveal_progress(word, revealed_indices))

    while turns > 0:
        print("\nYou have", turns, "guesses remaining")
        guess = input("\nGuess a letter or the full word: ").lower().strip()

        # Already guessed check (no decrement here)
        if guess in guesses:
            print("You already tried:", guess)
            continue
        guesses.append(guess)

        # Case 1: Full word guessed correctly
        if guess == word:
            print("\n🎉 You won! You guessed", word, "correctly!")
            return

        # Case 2: Single character guess
        elif len(guess) == 1:
            if guess in word:
                for i, ch in enumerate(word):
                    if ch == guess:
                        revealed_indices.add(i)
                print("\n✅ Correct! Letter", guess, "is in the word.")
            else:
                print("\n❌ Wrong guess! Letter", guess, "is NOT in the word.")

        # Case 3: Wrong full-word guess
        else:
            print("\n❌ Wrong guess! That word is not correct.")

        # Always decrement turns for any *new* guess
        turns -= 1

        # Show current progress
        print("Revealed word so far:", reveal_progress(word, revealed_indices))

        # Check win condition
        if all(i in revealed_indices for i in range(len(word))):
            print("\n🎉 You won! The word was:", word)
            return

    # If out of turns
    print("\n😢 You Lose! The word was:", word)

# Program starts here
if __name__ == '__main__':
    name = input("What is your name? ")
    print("Hello, " + name + ", time to play ✍️ word guessing hangman!")
    time.sleep(1)

    while True:
        play_game(name)

        # Play again loop with validation
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\nStarting a new match...\n")
                break  # restart the game loop
            elif play_again in ['n', 'no']:
                print("\n👋 Thanks for playing!", name + "!")
                exit(0)
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")
