# 🧮 Python Calculator (Menu-Driven)
def calculator_display():
    """Show the calculator menu with operation options (with emojis)."""
    menu = """
🧮 Welcome to Calculator 🧮

Choose one operation:
1. ➕ Add
2. ➖ Subtract
3. ✖️  Multiply
4. ➗ Divide
5. 🚪 Exit
"""
    return menu


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("❌ Cannot divide by zero.")
    return a / b


def get_number_input(prompt):
    """Prompt user for a number until valid input is entered."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")


def get_user_input():
    """Get two validated float numbers."""
    a = get_number_input("\n🔢 Enter the first number: ")
    b = get_number_input("🔢 Enter the second number: ")
    return a, b


def format_result(value):
    """Format result: remove .0 if integer."""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def calculator_function(choice):
    """
    Perform operation and return result string formatted as:
    Result of a [operator] b = result
    """
    operations = {
        1: ("➕", add),
        2: ("➖", subtract),
        3: ("✖️", multiply),
        4: ("➗", divide),
    }

    if choice in operations:
        symbol, func = operations[choice]
        a, b = get_user_input()
        try:
            result = func(a, b)
            result = format_result(result)
            return f"\n✅ Result of {a} {symbol} {b} = {result}"
        except ValueError as e:
            return f"❌ Error: {e}"
    elif choice == 5:
        return "\n👋 Exiting the calculator, goodbye!"
    else:
        return "\n⚠️  Invalid input. Please enter a number between 1 and 5."

# Program starts here
if __name__ == '__main__':
    """Main program loop"""
    while True:
        print(calculator_display())
        try:
            user_choice = int(input("👉 Select an operation (1-5): "))
        except ValueError:
            print("\n⚠️ Invalid input. Please enter a number between 1 and 5.")
            continue

        message = calculator_function(user_choice)
        print(message)
        if user_choice == 5:
            break
