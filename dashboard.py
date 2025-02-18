import tkinter
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
#import calender
#from tkCalender import calender

transactions = [] ##list that will hold a dictionary of the type of transaction and the amount
def add_item():
    description = description_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()
    trans_type = transaction_type.get()
    

    if description and amount and date and trans_type:
        #insert the data into the treeview from index 0 to the end
        expenseTreeView.insert("", "end", values=(description, amount, date, trans_type))

        #add data to the transactions list
        transactions.append({trans_type: amount})
        print(transactions)

        #clear the input fields
        description_entry.delete(0, "end")
        amount_entry.delete(0, "end")
        date_entry.delete(0, "end")
    else: 
        messagebox.showerror("Error", "Please fill in all fields")


def get_balance():
    income_list = []
    expense_list = []
    sum_income = 0
    sum_expense = 0
    for i in transactions: 
       for key, value in i.items():
           if key == "income":
               print(value)
               income_amount = int(value)
               income_list.append(income_amount)
               sum_income = sum(income_list)
               print(sum_income)
           elif key == "expense":
               expense_amount = int(value)
               expense_list.append(expense_amount)
               sum_expense = sum(expense_list)
           else:
                messagebox.showerror("Error", "Please select a transaction type") 
    sum_balance = sum_income - sum_expense
    print(sum_balance)
    messagebox.showinfo("balance", f"your balance is {sum_balance}")          
        
       

window = tkinter.Tk() #creates the main window
window.title("Expense Tracker")

label = tkinter.Label(window, text = "Expense Tracker")
label.grid(row = 0, column = 0, padx=10, pady=10)

#select between income and expense
selectLabel = tkinter.Label(window, text = "Select Type")
selectLabel.grid(row=1, column = 0, pady=5, padx=10)
transaction_type = tkinter.StringVar( value="income") #ensures only one is active at a time, sets income as default choice
tkinter.Radiobutton(window, text="Income", value="income", variable=transaction_type).grid(row=2, column = 0 , pady=0)
tkinter.Radiobutton(window, text="Expense", value="expense", variable=transaction_type).grid(row=3, column = 0 , pady=0)

tkinter.Label(window, text="Amount: ").grid(row = 4, column = 0, pady=10 , padx=10)
amount_entry = tkinter.Entry(window)
amount_entry.grid(row = 4, column = 1, pady=10, padx=10)

tkinter.Label(window, text="Description: ").grid(row=5, column=0, pady=10, padx=10)
description_entry = tkinter.Entry(window)
description_entry.grid(row=5, column=1, pady=10, padx=10)

tkinter.Label(window, text="Date: ").grid(row=6, column=0, pady=10, padx=10)
date_entry = tkinter.Entry(window)
date_entry.grid(row=6, column=1, pady=10, padx=10)

button = tkinter.Button(window, text = "Add", command=add_item)
button.grid(row = 7, column = 0, sticky="ew", pady=10, padx=10)

getButton  = tkinter.Button(window, text = "Get Balance", command=get_balance)
getButton.grid(row = 7, column = 1, sticky="ew", pady=10, padx=10)

frame = tkinter.Frame(window)
frame.grid(row=1, column=3,rowspan=8, pady=10, padx=10)

##treeview to show expenses and income
expenseTreeView = ttk.Treeview(frame, columns=("Description", "Amount", "Date", "type"), show="headings")
expenseTreeView.grid(row=0, column=0, pady=10, padx=10)
expenseTreeView.heading("Description", text="Description")
expenseTreeView.heading("Amount", text="Amount")
expenseTreeView.heading("Date", text="Date")
expenseTreeView.heading("type", text="Type")



window.geometry("1100x450")
window.mainloop()
