import random
import string
import pyperclip


import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window = ctk.CTk()
window.title("Password Generator")
window.geometry("500x600")
window.resizable(False, False)
window.configure(fg_color="#ACACEC")




def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if score <= 2:
        return "Weak🔴"
    elif score <= 4:
        return "Moderate🟡"
    else:
        return "Strong🟢"


def generate_password():
    length = int(length_Entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Your generated password is: " + password)
    password_label.configure(text=f"password={password}")
    strength = check_strength(password)
    if strength == "Weak🔴":
     strength_label.configure(text=f"Strength={strength}",fg="red")
    elif strength == "Moderate🟡":
        strength_label.configure(text=f"Strength={strength}",fg="yellow")
    else:
        strength_label.configure(text=f"Strength={strength}",fg="green")
    print("Password Strength: " + strength)
 
def copy_password():
    pyperclip.copy(password_label["text"])
    messagebox.showinfo("Copied", "Password copied to clipboard!")
title_label = ctk.CTkLabel(window, text="🔑 Password Generator", font=("segoe ui", 24, "bold"),fg_color="transparent",text_color="black")
title_label.pack(pady=25)
length_label = ctk.CTkLabel(window, text="Enter the length of the password:", font=("segoe ui", 14, "bold"),text_color="black")
length_label.pack(pady=10, padx=5)
length_Entry = ctk.CTkEntry(window,width=250, font=("segoe ui", 12),justify="center")
length_Entry.pack()
generate_Button = ctk.CTkButton(window, text="Generate Password",width=250,height=45,corner_radius=15,font=("segoe ui", 15, "bold"), command=generate_password)
generate_Button.pack(pady=10)
copy_Button = ctk.CTkButton(window, text="Copy Password",width=120,height=40, command=copy_password)
copy_Button.pack(pady=10)
password_label = ctk.CTkLabel(window, text="Your generated password is: ", font=("segoe ui", 12,"bold"),text_color="black")
password_label.pack(pady=10, padx=5)
strength_label = ctk.CTkLabel(window, text="Strength", font=("segoe ui", 12, "bold"),text_color="black")
strength_label.pack(pady=10, padx=5)


window.mainloop()

