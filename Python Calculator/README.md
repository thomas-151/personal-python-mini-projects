# 🧮 Python Calculator (Menu-Driven)
Developed By Thomas Sasikanth Singadi  

This is a **command-line calculator** that performs the four basic arithmetic operations: **Addition, Subtraction, Multiplication, and Division**.  
The user interacts with a **menu-driven interface** and can perform calculations until they choose to exit.

## ▶️ Demo

![python_calculator](https://github.com/user-attachments/assets/41138448-7ed2-4dc9-a797-f09a5f9c5c60)

## ✨ Features
- 📝 User-friendly **menu interface**.
- ➕ Perform **addition** of two numbers.  
- ➖ Perform **subtraction** of two numbers.  
- ✖️ Perform **multiplication** of two numbers.  
- ➗ Perform **division** (with special handling to prevent division by zero).  
- 🔁 Loops until the user chooses to exit.  
- ✅ Gracefully validates all inputs, ensures only valid numbers are used.  

## 📖 Rules of the Calculator
1. You can choose from **5 options** in the menu:  
   - `1` ➕ Add  
   - `2` ➖ Subtract  
   - `3` ✖️ Multiply  
   - `4` ➗ Divide  
   - `5` 🚪 Exit  

2. The program will keep running in a **loop** until you select **Exit (5)**.  

3. You must enter **numeric inputs** for calculations — decimals are also supported.  

4. If you select an **invalid option (not 1–5)**, the program will remind you and ask again.  

5. Division by **zero (0)** is not allowed. Trying it will show an error.  

6. Results are always shown in a clean format:  
   - Whole numbers are displayed without decimals.  


## ⚠️ Error Handling
- **Invalid menu choice** → Shows `Invalid choice. Please select a valid option.`  
- **Non-numeric input for numbers** → Shows `Invalid input. Please enter a number.`  
- **Divide by zero** → Shows `Error: Cannot divide by zero.`  
- **Invalid inputs for menu selection (letters instead of 1–5)** → Reprompts until valid.  
- **Output cleanup** → Converts `-0.0` into `0` for neat display.  



## 💡 Learning From This Project
By studying and using this project, you can learn:
- How to organize Python programs using **functions**.
- How to create a **menu-driven interface**.
- Handling **user input validation** and error messages.
- Preventing runtime errors (like divide-by-zero).
- Using **loops** to keep the program running until user quits.
- Returning proper messages and maintaining **clean output format**.


## 👨‍💻 Author
Made with ❤️ in Python as a simple but practical project.  
Use it as a stepping stone toward more advanced Python projects 🚀. 
