# ❌⭕ Tic-Tac-Toe with AI (Python)
Developed By Thomas Sasikanth Singadi  

This is a **command-line Tic Tac Toe game** built in Python.  
You will play against the computer 🤖, which uses the **Minimax Algorithm** (AI) to make intelligent moves.  
The game is played on a **3x3 board**, with:

- **🙂 You → O**  
- **🤖 Computer → X**

## ▶️ Demo

![tic_tac_toe_with_AI](https://github.com/user-attachments/assets/14a88069-56cf-4c96-823d-43300d0a1dde)

## ✨ Features
- Play Tic Tac Toe directly in the terminal.  
- Choose from **3 difficulty levels**:  
  - Easy 🙂 (random moves)  
  - Medium 😎 (mix of random + smart moves)  
  - Hard 🤖 (**Minimax AI for unbeatable gameplay**)  
- Option to **start first** or let the computer start.  
- Handles **invalid inputs** (wrong number, letters, already filled spots).  
- Ends with **winner announcement** or **draw** if the board is full.  
- Friendly design with **emoji-based feedback** 🎉⚔️.  


## 📖 Rules of the Game
1. The board has **9 positions**, numbered left to right, top to bottom
2. You (O) and the computer (X) take turns placing marks.  
3. First to form **3 in a row** (horizontally, vertically, or diagonally) wins.  
4. If all spots are filled and no one wins → it’s a **draw** 🤝.  


## 🧠 AI & Difficulty Levels
- **Easy Mode 🙂** → Random computer moves.  
- **Medium Mode 😎** → 60% smart moves (Minimax), 40% random.  
- **Hard Mode 🤖** → Full **Minimax algorithm** for unbeatable moves.  

The **Minimax algorithm** makes the computer play **optimally**:  
- Maximizes its own winning chances.  
- Minimizes your chances of winning.  
👉 At best, you can **draw** if you play perfectly.  


## ⚠️ Error Handling
- Entering letters or invalid numbers →  
  `❌ Invalid input, enter a number between 1-9.`  
- Choosing an already filled cell →  
  `❌ Invalid or occupied position, try again.`  
- Wrong choice at start (difficulty or first turn) →  
  Asks again until valid answer.  


## 💡 Learning from this Game
Playing and building this game helps you understand:
- How to represent a **game board** and control game flow in Python.  
- Handling **user inputs**, validating choices, and managing errors gracefully.  
- Implementing and checking **winning conditions** (rows, columns, diagonals).  
- Designing **difficulty levels** that change how the AI plays.  
- Applying the **Minimax algorithm** to make smart, optimal decisions.  
- The importance of **turn-based logic** in two-player games.  
- How small tweaks (like randomization in Medium mode) affect **game balance and fun**.  


## 👨‍💻 Author
Made with ❤️ in Python for beginners who want to practice coding.  
Enjoy playing Tic Tac Toe and leveling up your Python skills 🚀
