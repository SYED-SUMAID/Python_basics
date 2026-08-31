# ==============================
#        PYTHON CALCULATOR
# ==============================

history = []
last_result = 0


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot use zero."
    return a % b


def power(a, b):
    return a ** b


def show_history():
    if not history:
        print("\nNo calculations yet.")
        return

    print("\n===== CALCULATION HISTORY =====")

    for calculation in history:
        print(calculation)


def get_number(message):
    while True:
        value = input(message)

        if value.lower() == "ans":
            return last_result

        try:
            return float(value)

        except ValueError:
            print("Invalid input! Enter a number or 'Ans'.")


while True:

    print("\n==============================")
    print("       PYTHON CALCULATOR")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Show History")
    print("8. Clear History")
    print("9. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "9":
        print("\nCalculator closed.")
        break

    elif choice == "7":
        show_history()
        continue

    elif choice == "8":
        history.clear()
        print("\nHistory cleared.")
        continue

    elif choice not in ["1", "2", "3", "4", "5", "6"]:
        print("\nInvalid choice! Try again.")
        continue

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == "1":
        result = add(num1, num2)
        symbol = "+"

    elif choice == "2":
        result = subtract(num1, num2)
        symbol = "-"

    elif choice == "3":
        result = multiply(num1, num2)
        symbol = "*"

    elif choice == "4":
        result = divide(num1, num2)
        symbol = "/"

    elif choice == "5":
        result = modulus(num1, num2)
        symbol = "%"

    elif choice == "6":
        result = power(num1, num2)
        symbol = "**"

    if isinstance(result, str):
        print(result)

    else:
        last_result = result

        calculation = f"{num1} {symbol} {num2} = {result}"

        history.append(calculation)

        print("\nResult:", result)