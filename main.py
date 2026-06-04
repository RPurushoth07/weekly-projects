import math

history = []


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"


def power(a, b):
    return a ** b


def square_root(a):
    return math.sqrt(a)


while True:

    print("\n===== SMART CALCULATOR PRO =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Power")
    print("8. Square Root")
    print("9. View History")
    print("10. Save History")
    print("11. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = add(a, b)

        print("Result =", result)
        history.append(f"{a} + {b} = {result}")

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = subtract(a, b)

        print("Result =", result)
        history.append(f"{a} - {b} = {result}")

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = multiply(a, b)

        print("Result =", result)
        history.append(f"{a} * {b} = {result}")

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = divide(a, b)

        print("Result =", result)
        history.append(f"{a} / {b} = {result}")

    elif choice == 5:
        a = float(input("Enter a number: "))

        result = a ** 2

        print("Square =", result)
        history.append(f"Square of {a} = {result}")

    elif choice == 6:
        a = float(input("Enter a number: "))

        result = a ** 3

        print("Cube =", result)
        history.append(f"Cube of {a} = {result}")

    elif choice == 7:
        a = float(input("Enter base number: "))
        b = float(input("Enter power: "))

        result = power(a, b)

        print("Result =", result)
        history.append(f"{a}^{b} = {result}")

    elif choice == 8:
        a = float(input("Enter a number: "))

        if a < 0:
            print("Square root of negative number is not allowed")
        else:
            result = square_root(a)

            print("Square Root =", result)
            history.append(f"√{a} = {result}")

    elif choice == 9:

        print("\n===== CALCULATION HISTORY =====")

        if len(history) == 0:
            print("No calculations performed yet.")

        else:
            for item in history:
                print(item)

    elif choice == 10:

        with open("history.txt", "w", encoding="utf-8") as file:

            for item in history:
                file.write(item + "\n")

        print("History saved to history.txt")

    elif choice == 11:

        print("Thank you for using Smart Calculator Pro!")
        break

    else:
        print("Invalid Choice. Please try again.")