import tkinter
from tkinter import ttk
from datetime import datetime
#import calender
#from tkCalender import calender

window = tkinter.Tk() #creates the main window
window.title("Expense Tracker")

label = tkinter.Label(window, text = "Expense Tracker")
label.grid(row = 0, column = 0, padx=10, pady=10)

#select between income and expense
selectLabel = tkinter.Label(window, text = "Select Type")
selectLabel.grid(row=1, column = 0, pady=5)
tkinter.Radiobutton(window, text="Income", value="income").grid(row=2, column = 0 , pady=0)
tkinter.Radiobutton(window, text="Expense", value="expense").grid(row=3, column = 0 , pady=0)

tkinter.Label(window, text="Amount: ").grid(row = 4, column = 0 )
input = tkinter.Entry(window)
input.grid(row = 4, column = 1)

tkinter.Label(window, text="Description: ").grid(row=4, column=2)
tkinter.Entry(window).grid(row=4, column=3)

tkinter.Label(window, text="Date: ").grid(row=4, column=4)
tkinter.Entry(window).grid(row=4, column=5)

button = tkinter.Button(window, text = "Add")
button.grid(row = 5, column = 3, sticky="ew", pady=10)

frame = tkinter.Frame(window)
frame.grid(row=6, column=0, columnspan=3, pady=10)

##treeview to show expenses and income
expenseTreeView = ttk.Treeview(frame, columns=("Description", "Amount", "Date"))
expenseTreeView.grid(row=0, column=0, pady=10)
expenseTreeView.heading("#0", text="Expenses")

incomeTreeView = ttk.Treeview(frame, columns=("Description", "Amount", "Date"))
incomeTreeView.grid(row=7, column=0,columnspan=3 ,pady=10)
expenseTreeView.heading("#0", text="kjjkl")


window.geometry("500x350")
window.mainloop()
