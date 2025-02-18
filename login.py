# -*- coding: utf-8 -*-
import tkinter
import os
from System.databaseLogic import insert_user


def login():
    window.destroy()
    os.system("python System/dashboard.py")

def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        insert_user(username, password)
        window.destroy()
        os.system("python System/signUp.py")
    else:
        tkinter.messagebox.showerror("Error", "Please fill in all fields")

window = tkinter.Tk()
window.title("Login")
tkinter.Label(window, text = "Login").grid(row = 0, column = 0, padx=10, pady=10)

tkinter.Label(window, text = "Username").grid(row = 1, column = 0, padx=10, pady=10)
username_entry = tkinter.Entry(window)
username_entry.grid(row = 1, column = 1, padx=10, pady=10)

tkinter.Label(window, text = "Password").grid(row = 2, column = 0, padx=10, pady=10)
password_entry = tkinter.Entry(window)
password_entry.grid(row = 2, column = 1, padx=10, pady=10)

tkinter.Label(window, text="don't have an account?").grid(row = 3, column = 0, padx=10, pady=10)
tkinter.Button(window, text = "Sign Up" ,command=sign_up).grid(row = 4, column = 0, padx=10, pady=10)
tkinter.Button(window, text = "Login", command=login).grid(row = 4, column = 1, padx=10, pady=10)

window.geometry("300x200")
window.mainloop()