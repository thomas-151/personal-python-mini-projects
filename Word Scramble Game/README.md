# 🔀 Word Scramble Game (Python)
Developed By Thomas Sasikanth Singadi  

This is a **command-line Word Scramble Game** written in Python.  
In this game, the computer randomly selects a word, **jumbles its letters**, and shows it to you.  
Your task is to guess the original word within **3 attempts**.  

It’s a fun little challenge to test your vocabulary, guessing skills, and Python basics.  

## ▶️ Demo

![word_scramble_game](https://github.com/user-attachments/assets/aed2ce6d-0c80-4f68-85f2-f0bcbf512043)

## ✨ Features
- 🎲 Randomly chooses a word from a predefined word list.  
- 🔀 Scrambles (shuffles) the letters before showing it to the player.  
- ⏳ Gives the player **3 attempts** to guess correctly.  
- ❌ Wrong guesses reduce the remaining attempts.  
- 👀 If out of attempts, the game **reveals the correct word**.  
- 🛑 Player can **exit anytime** by typing "exit".  
- 🔄 Option to **replay** after each round.  


## 📖 Rules of the Game
1. The computer picks a random word from the list.  
2. The letters of the chosen word are mixed up and shown scrambled.  
3. You have **3 chances** to guess the original word:  
   - ✅ If correct → You win instantly!  
   - ❌ If wrong → You lose 1 attempt.  
4. If you **use all 3 attempts**, the game reveals the original word.  
5. After finishing a round, you can **choose to play again**.  
6. If you type **exit**, the game ends immediately and the word is revealed.  


## ⚠️ Error Handling
- If you type **exit** → Game ends and reveals the correct word.  
- If you type a wrong guess → Attempts reduce by 1.  
- If all attempts are used → Game shows the correct word.  
- Inputs are handled in lowercase to avoid case issues.  


## 💡 Learning From This Project
This project helps beginners learn:
- How to use **lists** and **random module** (`random.choice`, `random.shuffle`).  
- How to implement **loops and attempts logic**.  
- Simple **input handling** in Python.  
- **Game flow control** (loops, break, continue).  
- Adding **play again features** for replayable games.  


## 👨‍💻 Author
Made with ❤️ in Python for beginners who want to practice coding.  
Enjoy unscrambling and keep improving your Python skills 🚀
