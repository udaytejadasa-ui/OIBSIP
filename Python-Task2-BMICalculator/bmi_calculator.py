import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("💪 BMI Calculator")
root.geometry("600x700")
root.configure(bg="#0F172A")
root.resizable(False, False)

# -----------------------------
# Fonts
# -----------------------------
TITLE_FONT = ("Segoe UI", 24, "bold")
LABEL_FONT = ("Segoe UI", 12)
ENTRY_FONT = ("Segoe UI", 12)
BUTTON_FONT = ("Segoe UI", 12, "bold")

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="💪 BMI Calculator",
    font=TITLE_FONT,
    bg="#0F172A",
    fg="#38BDF8"
)
title.pack(pady=20)

# -----------------------------
# Main Card
# -----------------------------
card = tk.Frame(
    root,
    bg="white",
    bd=3,
    relief="ridge"
)
card.pack(padx=20, pady=10, fill="both", expand=True)

# -----------------------------
# Name
# -----------------------------
tk.Label(
    card,
    text="Name",
    bg="white",
    font=LABEL_FONT
).pack(pady=(20,5))

name_entry = tk.Entry(
    card,
    font=ENTRY_FONT,
    width=30,
    justify="center"
)
name_entry.pack()

# -----------------------------
# Age
# -----------------------------
tk.Label(
    card,
    text="Age",
    bg="white",
    font=LABEL_FONT
).pack(pady=(15,5))

age_entry = tk.Entry(
    card,
    font=ENTRY_FONT,
    width=15,
    justify="center"
)
age_entry.pack()

# -----------------------------
# Gender
# -----------------------------
tk.Label(
    card,
    text="Gender",
    bg="white",
    font=LABEL_FONT
).pack(pady=(15,5))

gender = tk.StringVar(value="Male")

gender_frame = tk.Frame(card,bg="white")
gender_frame.pack()

tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender,
    value="Male",
    bg="white"
).grid(row=0,column=0,padx=10)

tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender,
    value="Female",
    bg="white"
).grid(row=0,column=1,padx=10)

# -----------------------------
# Height
# -----------------------------
tk.Label(
    card,
    text="Height (cm)",
    bg="white",
    font=LABEL_FONT
).pack(pady=(15,5))

height_entry = tk.Entry(
    card,
    font=ENTRY_FONT,
    width=20,
    justify="center"
)
height_entry.pack()

# -----------------------------
# Weight
# -----------------------------
tk.Label(
    card,
    text="Weight (kg)",
    bg="white",
    font=LABEL_FONT
).pack(pady=(15,5))

weight_entry = tk.Entry(
    card,
    font=ENTRY_FONT,
    width=20,
    justify="center"
)
weight_entry.pack()

# -----------------------------
# Result
# -----------------------------

result_label = tk.Label(
    card,
    text="Your BMI will appear here",
    bg="white",
    fg="#0F172A",
    font=("Segoe UI",15,"bold")
)
result_label.pack(pady=20)

tip_label = tk.Label(
    card,
    text="",
    bg="white",
    justify="center",
    wraplength=450,
    font=("Segoe UI",11)
)
tip_label.pack()

# -----------------------------
# BMI Progress
# -----------------------------

progress = ttk.Progressbar(
    card,
    length=300,
    mode="determinate",
    maximum=40
)
progress.pack(pady=15)

# -----------------------------
# BMI Calculation
# -----------------------------

def calculate_bmi():

    try:

        name = name_entry.get().strip()

        if name == "":
            messagebox.showerror(
                "Error",
                "Please enter your name."
            )
            return

        height = float(height_entry.get()) / 100
        weight = float(weight_entry.get())

        bmi = weight / (height ** 2)

        progress["value"] = bmi

        if bmi < 18.5:

            category = "Underweight"
            color = "#2563EB"

            tip = (
                "Increase calorie intake.\n"
                "Eat nutritious food and exercise regularly."
            )

        elif bmi < 25:

            category = "Normal Weight"
            color = "#16A34A"

            tip = (
                "Excellent!\n"
                "Maintain a balanced diet and regular exercise."
            )

        elif bmi < 30:

            category = "Overweight"
            color = "#EA580C"

            tip = (
                "Exercise daily.\n"
                "Reduce junk food and sugary drinks."
            )

        else:

            category = "Obese"
            color = "#DC2626"

            tip = (
                "Consult a doctor.\n"
                "Follow a healthy diet and fitness plan."
            )

        result_label.config(

            text=(
                f"{name}\n\n"
                f"BMI : {bmi:.2f}\n"
                f"Category : {category}"
            ),

            fg=color
        )

        tip_label.config(text=tip)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid height and weight."
        )

# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(card, bg="white")
button_frame.pack(pady=20)

calculate_btn = tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#2563EB",
    fg="white",
    font=BUTTON_FONT,
    width=15,
    cursor="hand2"
)
calculate_btn.grid(row=0, column=0, padx=10)


def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

    gender.set("Male")

    result_label.config(
        text="Your BMI will appear here",
        fg="#0F172A"
    )

    tip_label.config(text="")
    progress["value"] = 0


clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#F59E0B",
    fg="white",
    font=BUTTON_FONT,
    width=10,
    cursor="hand2"
)
clear_btn.grid(row=0, column=1, padx=10)


exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    bg="#DC2626",
    fg="white",
    font=BUTTON_FONT,
    width=10,
    cursor="hand2"
)
exit_btn.grid(row=0, column=2, padx=10)

# -----------------------------
# Footer
# -----------------------------

footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    bg="#0F172A",
    fg="white",
    font=("Segoe UI", 10, "italic")
)
footer.pack(pady=10)

# -----------------------------
# Run Application
# -----------------------------

root.mainloop()