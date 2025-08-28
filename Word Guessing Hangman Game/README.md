# ✍️ Word Guessing Hangman (Python)  
Developed By Thomas Sasikanth Singadi  

This is a **command-line word guessing game** (similar to Hangman) made in Python.  
The computer randomly selects a **programming-related word** and gives you a **hint** to help.  
You get **5 attempts** to guess the word correctly.  
Correct guesses reveal the matching letters in the word, but wrong guesses only reduce your turns.  


## ▶️ Demo

<video src="https://github.com/thomas-151/personal-python-mini-projects/blob/main/Word%20Guessing%20Hangman%20Game/Demo.mp4" autoplay muted loop playsinline width="600"></video>


## ✨ Features
- Randomly selects a programming/CS-related word.  
- Each word comes with a **helpful hint**.  
- Shows **progress with blanks `_` for hidden letters**.  
- **Correct guesses** reveal the letter in all its positions.  
- **Wrong guesses** only reduce your remaining attempts.  
- Limited **5 chances** to get the word correct.  
- Prevents repeated guesses (warns if you try the same guess again).  


## 📖 Rules of the Game
1. The program picks a random word and shows its **hint**.  
2. You have **5 chances** to guess the correct word.  
3. You can try to guess either **a single letter** or the **whole word** each time.  
4. If your guess is WRONG →  
   - Lose **1 chance**.  
   - No letters are revealed.  
5. If your guess is CORRECT (letter or full word) → 🎉 **You Win!**  
6. If you fail all 5 chances → 😢 The game reveals the word and ends.  




## ⚠️ Error Handling
- If you enter the **same guess twice**, the game reminds you (but does not reduce turns).  
- Any new wrong input (incorrect word or wrong letter) counts as an attempt.  



## 💡 Learning from This Game
- Working with **random choices** in Python.  
- Using **lists, sets, and strings**.  
- Building a simple **game loop with limited attempts**.  
- Handling **inputs and repeated guesses**.  
- Displaying **progressive reveals** of the word.  



## 👨‍💻 Author
Made with ❤️ in Python to make learning fun.  
Try it out and see if you can beat the **hint-powered Hangman!**  
