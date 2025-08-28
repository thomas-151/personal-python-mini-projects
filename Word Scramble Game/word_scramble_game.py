# 🔀 Word Scramble Game (Python)
import random

# List of words that can be chosen for the scramble
word_list = [
    "python", "developer", "programming", "algorithm", "function",
    "variable", "debugging", "compiler", "codechef",
    "machine", "bitcoin", "operation"
]


# Function to shuffle/scramble the letters of the word
def scramble_word(word):
    """Scramble the letters of a word randomly"""
    word_list_chars = list(word)      # convert word into a list of characters
    random.shuffle(word_list_chars)   # shuffle the characters randomly
    return ''.join(word_list_chars)   # join back into a string


# Function for the guessing part of the game
def guess_word(original_word):
    attempts = 3   # player has 3 tries to guess the word

    while attempts > 0:
        # Take player input
        guess = input("\n🤔 Guess the word (or type 'exit' to quit): ").lower()

        # If player chooses to exit
        if guess == "exit":
            print(f"❌ You gave up! The correct word was: {original_word}\n")
            print("\n👋 Thanks for playing!\n")
            return "exit"

        # If guessed correctly
        if guess == original_word:
            print("🎉 Correct! You guessed it! ✅\n")
            return
        else:
            # Wrong guess reduces the attempts
            attempts -= 1
            print(f"😢 Wrong guess. Attempts left: {attempts}")

    # If all attempts are used up
    print(f"❌ Out of attempts! The correct word was: {original_word}\n")


# Main game loop
def play_game():
    while True:  # Keep playing until player decides to stop
        # Pick a random word and scramble it
        original_word = random.choice(word_list)
        scrambled = scramble_word(original_word)

        print("✨ Welcome to the Word Scramble Game! 📝✨")
        print(f"\n🔀 Scrambled word: {scrambled}")

        # Ask the player to guess the scrambled word
        if guess_word(original_word) == "exit":
            break

        # Prompt with validation loop
        while True:
            play_again = input("🔄 Do you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\n🎮 Starting a new round... All the Best! 🍀\n")
                break
            elif play_again in ['n', 'no']:
                print("\n👋 Thanks for playing! Goodbye!\n")
                return
            else:
                print("⚠️ Invalid input. Please enter 'y' or 'n'.")


# Program starts here
if __name__ == "__main__":
    play_game()
