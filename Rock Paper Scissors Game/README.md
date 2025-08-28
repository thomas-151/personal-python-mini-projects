# ✊✋✌️ Rock-Paper-Scissors (Python - Best of 5)
Developed By Thomas Sasikanth Singadi  

This is a **terminal-based Rock, Paper, Scissors game** written in Python.  
You play against the computer in a **best-of-five format**. The first to win **3 rounds** wins the match 🏆.  

It’s a quick, fun game that combines simple Python logic, randomness, and user input validation.  

## ▶️ Demo

![rock_paper_scissors](https://github.com/user-attachments/assets/e2193b45-9b09-40ba-acdc-cd3ac15884da)

## ✨ Features
- ➡️ Accepts **rock, paper, scissors** as input.  
- ⌨️ Allows **shortcut inputs**: `r`, `p`, `s`.  
- 🎲 Computer picks a random move every round.  
- 📊 **Scoreboard updates** after each round.  
- 🏆 Declares a winner once someone reaches 3 rounds, or after 5 rounds if tied.  
- 🔁 Gives option to **play again or quit** after a match.  
- 🔒 Strong **input validation**:  
  - Invalid round inputs → asks again.  
  - Invalid replay inputs → asks again.  


## 📖 Rules of the Game
1. Both player and computer choose from **rock, paper, scissors**.  
2. The choices are compared:
   - **Rock** crushes **Scissors**.  
   - **Scissors** cut **Paper**.  
   - **Paper** covers **Rock**.  
3. If both pick the same → The round is a **tie**.  
4. Match continues until:  
   - One player reaches **3 round wins**.  
   - Or all **5 rounds** finish.  
5. Final outcome:
   - More wins → Winner 🎉  
   - Equal wins → Match declared a draw ⚖️  


## ⚠️ Error Handling
- If you type `xyz` instead of rock/paper/scissors → Shows “Invalid choice!” and asks again.  
- If you mistype on replay prompt → Asks again until you enter `y` or `n`.  
- Inputs are **case-insensitive** and accept **shortcuts** (`r`, `p`, `s`).  


## 💡 Learning From This Project
- **Randomization** in Python (`random.choice`).  
- **Functions** with clear roles (`get_user_choice()`, `get_computer_choice()`, etc.).  
- **Control flow** with loops (`while`) and conditions.  
- **Game round system** (best-of-five with early win).  
- **Input validation** and re-prompting for correct entries.  
- **Scoreboard tracking** and match results.  


## 👨‍💻 Author
Made with ❤️ in Python.  
A small but fun project that shows how classic games can be turned into interactive programs.  
Play and see if you can beat the **computer in best-of-five**!  
