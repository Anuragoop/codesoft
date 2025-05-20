import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result_label.config(text="Select a valid operation.")
            return

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Widgets
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Select operation:").pack()
operation = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]

for op in operations:
    tk.Radiobutton(root, text=op, variable=operation, value=op).pack(anchor="w")

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run app
root.mainloop()
