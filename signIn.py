import tkinter

window = tkinter.Tk()
window.title("Sign Up")
tkinter.Label(window, text = "Login").grid(row = 0, column = 0, padx=10, pady=10)

tkinter.Label(window, text = "Username").grid(row = 1, column = 0, padx=10, pady=10)
tkinter.Entry(window).grid(row = 1, column = 1, padx=10, pady=10)

tkinter.Label(window, text = "Password").grid(row = 2, column = 0, padx=10, pady=10)
tkinter.Entry(window).grid(row = 2, column = 1, padx=10, pady=10)

tkinter.Button(window, text = "Login").grid(row = 3, column = 0, padx=10, pady=10)

window.geometry("300x200")
window.mainloop()
