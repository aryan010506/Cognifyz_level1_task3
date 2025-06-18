import tkinter as tk
from tkinter import messagebox
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_email():
    email = entry.get().strip()
    if not email:
        messagebox.showwarning("Input Error", "Please enter an email address.")
        return

    if is_valid_email(email):
        messagebox.showinfo("Result", f"✅ '{email}' is a valid email address.")
    else:
        messagebox.showerror("Result", f"❌ '{email}' is not a valid email address.")

# GUI Setup
app = tk.Tk()
app.title("Email Validator")
app.geometry("350x200")
app.resizable(False, False)

tk.Label(app, text="Enter Email Address:", font=("Arial", 12)).pack(pady=15)
entry = tk.Entry(app, width=35, font=("Arial", 11))
entry.pack(pady=5)

tk.Button(app, text="Validate", command=validate_email, font=("Arial", 11)).pack(pady=15)

app.mainloop()
