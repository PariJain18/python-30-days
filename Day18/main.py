from expenses import load_expenses, add_expense, view_expenses, filter_by_month

expenses = load_expenses()

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses by Month")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        filter_by_month(expenses)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")