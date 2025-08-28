# 🎲 Number Guessing Game (Python)
import random

# Function to generate a random number between 1–100
def getRandomNumber():
    """Return a random number between 1 and 100."""
    return random.randint(1, 100)

# Function to give hints based on how close the guess is
def giveHint(number, guess):
    """Return only 3 categories of hints based on closeness."""
    if guess == number:
        return "Correct ✅"

    # Find the gap between the correct number and the guess
    difference = abs(number - guess)

    # Decide the type of hint based on difference
    if difference <= 5:
        return "Very Close 🔥"
    elif difference <= 15:
        return "Close 🌡️"
    else:
        return "Far ❄️"

# Main function to run the game
def runGuess():
    print("🎲 Welcome to the Number Guessing Game!")
    print("\nA secret number is chosen between 1 and 100.")
    print("\nYou have 12 attempts to guess it. After each guess, you'll be told:")
    print("- 'Far' ❄️, 'Close' 🌡️, or 'Very Close' 🔥\n")

    while True:
        # Generate a new random secret number each game
        secretNumber = getRandomNumber()
        MAX_ATTEMPTS = 12   # total chances allowed
        attempts = 0        # how many attempts used so far
        previous_guesses = []  # store past guesses to prevent repeats

        # Loop for player attempts
        while attempts < MAX_ATTEMPTS:
            try:
                # Ask user for input
                user_guess = int(input(f"Attempt {attempts+1}/{MAX_ATTEMPTS} - Enter your guess (1–100): "))

                # Check if guess is within valid range
                if 1 <= user_guess <= 100:

                    # If user already entered this guess earlier
                    if user_guess in previous_guesses:
                        print(f"⚠ You already guessed {user_guess}. Try another number.\n")
                        continue

                    # Save guess and count it as an attempt
                    previous_guesses.append(user_guess)
                    attempts += 1

                    # Get hint on closeness
                    hint = giveHint(secretNumber, user_guess)

                    # If guessed correctly, end the round
                    if "Correct" in hint:
                        print(f"\n🎉 You got it! The secret number was {secretNumber}. Guessed in {attempts} attempts.")
                        break
                    else:
                        # Otherwise, show hint and remaining attempts
                        print(hint)
                        print(f"Attempts left: {MAX_ATTEMPTS - attempts}\n")

                else:
                    print("⚠ Please enter a number between 1–100.\n")

            except ValueError:
                # Handles cases where input is not a number
                print("⚠ Invalid input! Please enter numbers only.\n")

        else:
            # This runs when user uses up all attempts without success
            print(f"\n😢 Out of attempts! The number was {secretNumber}.")

        # Prompt with validation loop
        while True:
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\nStarting a new match...\n")
                break
            elif play_again in ['n', 'no']:
                print("\n👋Thanks for playing! Goodbye!\n")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# Program starts here
if __name__ == '__main__':
    runGuess()
