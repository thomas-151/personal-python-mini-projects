# 🎲 Number Guessing Game (Python)
Developed By Thomas Sasikanth Singadi  

This is a simple and fun **command-line game** written in Python.  
The computer secretly picks a number between **1 and 100**, and your goal is to guess it.  

You will get a total of **12 attempts** to guess the number correctly.  
After each guess, the game will tell you how close your guess was:

- **Very Close 🔥** → If your guess is within **5 numbers** of the secret number.  
- **Close 🌡️** → If your guess is within **15 numbers** of the secret number.  
- **Far ❄️** → If your guess is more than 15 away.  


## ▶️ Demo

![number_guessing_game](https://github.com/user-attachments/assets/7d523678-d2ec-4fd0-8d13-aa49473439f7)


## ✨ Features
✅ Computer randomly selects a number between **1 and 100**.  
✅ Player gets **12 chances** to guess the number.  
✅ After each wrong attempt, a **hint** is shown.  
✅ Prevents repeated guesses (no duplicate entries wasted).  
✅ Handles **errors** (like entering letters instead of numbers).  
✅ Offers **play again** option at the end of each round.  


## 🎮 Rules of the Game
1. The secret number is always between **1 and 100**.  
2. You will have **12 attempts** to guess it.  
3. Input must be a **number** (otherwise you’ll get a warning).  
4. If you repeat the same number, the game will remind you.  
5. After each guess:  
   - You get a hint — **Far ❄️**, **Close 🌡️**, or **Very Close 🔥**.  
6. If you guess it before attempts run out → **You Won 🎉**.  
7. If you run out of attempts → The game reveals the number.  


## ⚠️ Error Handling  
- If you enter a **non-numeric input** (like letters or symbols), you’ll get a warning without losing an attempt.  
- If you enter a number **outside 1–100**, the game will remind you to choose only within range.  
- If you **repeat the same number**, the game will warn you without deducting an attempt.  


## 💡 Learning from This Game
- **Looping** and controlling game flow.  
- **User Input Handling** (checking for errors in input).  
- **Logic building** (using hints based on the difference).  
- **Randomness in Python** (`random.randint`).  


## 👨‍💻 Author  
Made with ❤️ in Python to make learning fun.  
Try it out and see if you can beat the **hint-powered Number Guessing Game!**  

