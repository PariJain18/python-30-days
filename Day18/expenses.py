import json
from datetime import date

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    expense_date = input("Enter date (YYYY-MM-DD): ")

    if expense_date == "":
        expense_date = str(date.today())

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": expense_date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense saved successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(expense)

def filter_by_month(expenses):
    month = input("Enter month (YYYY-MM): ")

    for expense in expenses:
        if expense["date"].startswith(month):
            print(expense)








            










            