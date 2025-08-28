# ✊✋✌️ Rock, Paper, Scissors (Python - Best of 5)
import random


# Mapping of game choices to emojis for better UX
choice_emojis = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}


# Function to get player's choice (supports both full words & shortcuts)
def get_user_choice():
    """
    Get user's choice: rock, paper, or scissors.
    Accepts both full words and shortcuts: r / p / s.
    Keeps asking until valid input is entered.
    """
    valid_choices = {
        'r': 'rock', 'p': 'paper', 's': 'scissors',
        'rock': 'rock', 'paper': 'paper', 'scissors': 'scissors'
    }

    while True:
        user_input = input("\nEnter rock ✊ (r), paper ✋ (p), or scissors ✌️ (s): ").strip().lower()

        if user_input in valid_choices:   # Valid input
            return valid_choices[user_input]
        else:
            print("❌ Invalid choice! Please enter rock, paper, or scissors (or r, p, s).")


# Function for computer to randomly choose rock, paper, or scissors
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# Function to determine round winner
def determine_winner(user_choice, computer_choice):
    """
    Compares user and computer choices to decide:
    - 'user'     => if player wins
    - 'computer' => if computer wins
    - 'tie'      => if both same
    """
    if user_choice == computer_choice:
        return 'tie'

    # Rules: rock > scissors, scissors > paper, paper > rock
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if wins[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'


# Function to play a match (Best of 5 system)
def play_best_of_five():
    print("🎮 Welcome to Rock, Paper, Scissors! Best of 5 rounds wins the match. 🏆\n")

    # Initialize match variables
    user_score = 0
    computer_score = 0
    round_num = 1

    # Loop for rounds until max 5 or someone wins early
    while round_num <= 5:
        print(f"\n📢 ----- Round {round_num} -----")

        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Show each player's choice
        print(f"👉 You chose: {user_choice} {choice_emojis[user_choice]}")
        print(f"🤖 Computer chose: {computer_choice} {choice_emojis[computer_choice]}")

        # Decide who won
        winner = determine_winner(user_choice, computer_choice)

        # Update scores accordingly
        if winner == 'user':
            user_score += 1
            print("\n🎉 You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("\n🤖 Computer wins this round!")
        else:
            print("\n😐 This round is a tie!")

        # Show scoreboard
        print(f"\n📊 Score => You: {user_score} | Computer: {computer_score}\n")

        # Early winning condition (first to 3 out of 5)
        if user_score == 3:
            print("🏆 Congratulations! You won the match! 🎊")
            break
        elif computer_score == 3:
            print("💻 Computer won the match! Better luck next time! 😅")
            break

        round_num += 1
    else:
        # Match ended after 5 rounds without early winner
        if user_score > computer_score:
            print("🏆 Congratulations! You won the match! 🎊")
        elif computer_score > user_score:
            print("💻 Computer won the match! Better luck next time! 😅")
        else:
            print("🤝 The match is a tie! Well played!")


# Main driver function
def main():
    while True:
        play_best_of_five()

        # Ask if user wants to replay
        while True:
            play_again = input("🔄 Do you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\n✨ Starting a new match... ✨\n")
                break
            elif play_again in ['n', 'no']:
                print("\n👋 Thanks for playing! Goodbye!")
                return
            else:
                print("⚠️ Invalid input. Please enter 'y' or 'n'.")


# Program starts here
if __name__ == '__main__':
    main()
