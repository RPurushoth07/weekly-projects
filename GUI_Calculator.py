import tkinter as tk


def get_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except ValueError:
        result_label.config(text="Enter valid numbers")
        return None


def add():
    values = get_numbers()
    if values:
        result_label.config(text=f"Result: {values[0] + values[1]}")


def subtract():
    values = get_numbers()
    if values:
        result_label.config(text=f"Result: {values[0] - values[1]}")


def multiply():
    values = get_numbers()
    if values:
        result_label.config(text=f"Result: {values[0] * values[1]}")


def divide():
    values = get_numbers()
    if values:
        if values[1] == 0:
            result_label.config(text="Cannot divide by zero")
        else:
            result_label.config(text=f"Result: {values[0] / values[1]}")


def square():
    try:
        num = float(entry1.get())
        result_label.config(text=f"Square: {num ** 2}")
    except ValueError:
        result_label.config(text="Enter valid number")


def cube():
    try:
        num = float(entry1.get())
        result_label.config(text=f"Cube: {num ** 3}")
    except ValueError:
        result_label.config(text="Enter valid number")


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")


root = tk.Tk()
root.title("Smart Calculator Pro")
root.geometry("500x400")

title = tk.Label(root, text="Smart Calculator Pro", font=("Arial", 18))
title.grid(row=0, column=0, columnspan=3, pady=15)

tk.Label(root, text="First Number").grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, pady=5)

tk.Label(root, text="Second Number").grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, pady=5)

tk.Button(root, text="Add", width=15, command=add).grid(row=3, column=0, pady=5)
tk.Button(root, text="Subtract", width=15, command=subtract).grid(row=3, column=1, pady=5)

tk.Button(root, text="Multiply", width=15, command=multiply).grid(row=4, column=0, pady=5)
tk.Button(root, text="Divide", width=15, command=divide).grid(row=4, column=1, pady=5)

tk.Button(root, text="Square", width=15, command=square).grid(row=5, column=0, pady=5)
tk.Button(root, text="Cube", width=15, command=cube).grid(row=5, column=1, pady=5)

tk.Button(root, text="Clear", width=15, command=clear).grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result:", font=("Arial", 14))
result_label.grid(row=7, column=0, columnspan=2, pady=20)

root.mainloop()