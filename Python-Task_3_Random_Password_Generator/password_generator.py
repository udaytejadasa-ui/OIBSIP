import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        chars = ""
        if upper.get():
            chars += string.ascii_uppercase
        if lower.get():
            chars += string.ascii_lowercase
        if numbers.get():
            chars += string.digits
        if symbols.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showwarning("Warning", "Select at least one option!")
            return

        password = "".join(random.choice(chars) for _ in range(length))

        result.delete(0, tk.END)
        result.insert(0, password)

    except:
        messagebox.showerror("Error", "Enter a valid length!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x450")
root.config(bg="white")
root.resizable(False, False)

tk.Label(root, text="🔐 Password Generator",
         font=("Arial", 20, "bold"),
         bg="white", fg="#0078D7").pack(pady=15)

tk.Label(root, text="Password Length",
         font=("Arial", 13), bg="white").pack()

length_entry = tk.Entry(root, font=("Arial", 13), justify="center")
length_entry.pack(pady=10)

upper = tk.BooleanVar(value=True)
lower = tk.BooleanVar(value=True)
numbers = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=upper, bg="white").pack(anchor="w", padx=90)
tk.Checkbutton(root, text="Lowercase (a-z)", variable=lower, bg="white").pack(anchor="w", padx=90)
tk.Checkbutton(root, text="Numbers (0-9)", variable=numbers, bg="white").pack(anchor="w", padx=90)
tk.Checkbutton(root, text="Special (!@#$)", variable=symbols, bg="white").pack(anchor="w", padx=90)

tk.Button(root, text="Generate Password",
          command=generate_password,
          bg="#0078D7", fg="white",
          font=("Arial", 12, "bold")).pack(pady=20)

result = tk.Entry(root, width=30, font=("Arial", 13), justify="center")
result.pack(pady=10)

root.mainloop()