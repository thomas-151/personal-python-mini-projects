# ❌⭕ Tic Tac Toe with AI (Python)
import random

# Constants
COMPUTER = 1
YOU = 2
SIDE = 3
COMPUTERMOVE = 'X'   # Computer is 'X'
YOUMOVE = 'O'        # You are 'O'

# Print the current board
def show_board(board):
    for i in range(SIDE):
        print("\t", end="")
        for j in range(SIDE):
            print(board[i][j], end=" ")
            if j < SIDE - 1:
                print("|", end=" ")
        print()
        if i < SIDE - 1:
            print("\t" + "-" * 9)

# Show instructions with updated marks
def show_instructions():
    print("\n📖 Choose a cell numbered from 1 to 9 as below and play:")
    print("\t 1 | 2 | 3 ")
    print("\t-----------")
    print("\t 4 | 5 | 6 ")
    print("\t-----------")
    print("\t 7 | 8 | 9 \n")

# Initialize empty board
def initialize():
    return [['*' for _ in range(SIDE)] for _ in range(SIDE)]

# Announce winner
def declare_winner(whose_turn):
    if whose_turn == COMPUTER:
        print("🎉 COMPUTER has won!")
    else:
        print("🎉 YOU have won!")

# Row check
def row_crossed(board):
    return any(board[i][0] == board[i][1] == board[i][2] != '*' for i in range(SIDE))

# Column check
def column_crossed(board):
    return any(board[0][i] == board[1][i] == board[2][i] != '*' for i in range(SIDE))

# Diagonal check
def diagonal_crossed(board):
    return (board[0][0] == board[1][1] == board[2][2] != '*') or \
           (board[0][2] == board[1][1] == board[2][0] != '*')

# Game over check
def game_over(board):
    return row_crossed(board) or column_crossed(board) or diagonal_crossed(board)

# Minimax algorithm
def minimax(board, depth, is_ai):
    if game_over(board):
        return -10 if is_ai else 10
    if depth == 9:
        return 0
    best_score = -9999 if is_ai else 9999
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == '*':
                board[i][j] = COMPUTERMOVE if is_ai else YOUMOVE
                score = minimax(board, depth + 1, not is_ai)
                board[i][j] = '*'
                best_score = max(best_score, score) if is_ai else min(best_score, score)
    return best_score

# Computer best move using minimax
def best_move(board, move_index):
    best_score = -9999
    moves = []
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == '*':
                board[i][j] = COMPUTERMOVE
                score = minimax(board, move_index + 1, False)
                board[i][j] = '*'
                if score > best_score:
                    best_score = score
                    moves = [(i, j)]
                elif score == best_score:
                    moves.append((i, j))
    return random.choice(moves)

# Computer move based on difficulty
def computer_move(board, move_index, difficulty):
    empty_cells = [(i, j) for i in range(SIDE) for j in range(SIDE) if board[i][j] == '*']
    if difficulty == "easy":
        return random.choice(empty_cells)
    elif difficulty == "medium":
        if random.random() < 0.6:  # 60% best, 40% random
            return best_move(board, move_index)
        else:
            return random.choice(empty_cells)
    else:  # hard mode
        return best_move(board, move_index)

# Main game
def play_tic_tac_toe(whose_turn, difficulty):
    board = initialize()
    move_index = 0
    show_instructions()

    while not game_over(board) and move_index < SIDE * SIDE:
        if whose_turn == COMPUTER:
            x, y = computer_move(board, move_index, difficulty)
            board[x][y] = COMPUTERMOVE
            print(f"🤖 COMPUTER has put an {COMPUTERMOVE} in cell {x * 3 + y + 1}\n")
            show_board(board)
            whose_turn = YOU
        else:
            while True:
                print("Available positions:", end=" ")
                for i in range(SIDE):
                    for j in range(SIDE):
                        if board[i][j] == '*':
                            print(i * 3 + j + 1, end=" ")
                print()
                try:
                    n = int(input("🙂 Enter the position (1-9): ")) - 1
                    x, y = divmod(n, SIDE)
                    if board[x][y] == '*' and 0 <= n < 9:
                        board[x][y] = YOUMOVE
                        print(f"\n🙂 YOU have put an {YOUMOVE} in cell {n + 1}\n")
                        show_board(board)
                        whose_turn = COMPUTER
                        break
                    else:
                        print("❌ Invalid or occupied position, try again.\n")
                except (ValueError, IndexError):
                    print("❌ Invalid input, enter a number between 1-9.\n")
        move_index += 1

    if not game_over(board) and move_index == SIDE * SIDE:
        print("🤝 It's a draw! Great fight ⚔️\n")
    else:
        declare_winner(COMPUTER if whose_turn == YOU else YOU)

# Main loop
def main():
    print("\n================== 🎮 Tic-Tac-Toe 🎮 ==================\n")
    print("✨ Welcome! Let's play Tic-Tac-Toe against the computer 🤖")
    print("\n🙂 You are 'O'  |  Computer is 'X'")
    while True:
        # Step 1: Ask difficulty until valid
        while True:
            print("\n🎚️ Choose Difficulty:")
            print("1. Easy 🙂")
            print("2. Medium 😎")
            print("3. Hard 🤖")
            diff_choice = input("Enter (1/2/3): ")
            if diff_choice == "1":
                difficulty = "easy"
                break
            elif diff_choice == "2":
                difficulty = "medium"
                break
            elif diff_choice == "3":
                difficulty = "hard"
                break
            else:
                print("\n❌ Invalid choice, please enter 1, 2, or 3.\n")

        # Step 2: Ask who starts (loop until valid input)
        while True:
            choice = input("Do you want to start first? (y/n): ").lower()
            if choice in ['y', 'yes']:
                play_tic_tac_toe(YOU, difficulty)
                break
            elif choice in ['n', 'no']:
                play_tic_tac_toe(COMPUTER, difficulty)
                break
            else:
                print("\n❌ Invalid input, please enter 'y' or 'n'.\n")

        # Step 3: Play again with validation loop
        while True:
            play_again = input("🔄 Do you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\n✨ Starting a new match... ✨\n")
                break
            elif play_again in ['n', 'no']:
                print("\n👋 Thanks for playing!")
                return
            else:
                print("⚠️ Invalid input. Please enter 'y' or 'n'.")

# Program starts here
if __name__ == "__main__":
    main()
