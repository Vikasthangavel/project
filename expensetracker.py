import time
addexpense = []
addincome = []
def save_data():
    with open('expense_data.txt', 'w') as f:
        f.write("Expenses:\n")
        for expense in addexpense:
            f.write(f"{expense}\n")
        f.write("Income:\n")
        for income in addincome:
            f.write(f"{income}\n")
    print("Data saved successfully!")
# Function to load data from a text file
def load_data():
    try:
        with open('expense_data.txt', 'r') as f:
            lines = f.readlines()
            global addexpense, addincome
            addexpense, addincome = [], []
            section = None
            for line in lines:
                line = line.strip()
                if line == "Expenses:":
                    section = "expenses"
                elif line == "Income:":
                    section = "income"
                elif line.isdigit():
                    if section == "expenses":
                        addexpense.append(int(line))
                    elif section == "income":
                        addincome.append(int(line))
    except FileNotFoundError:
        print("No saved data found, starting fresh.")

class ExpenseTracker:
    def add_expense():
        expense = int(input("Enter your Expense: "))
        if(sum(addincome )>= sum(addexpense)):
            addexpense.append(expense)
            print("Expense Added successfully!")
            save_data()
        else:
            print("your expense is higher than income")
            

    def add_income():
        income = int(input("Enter your Income: "))
        addincome.append(income)
        print("Income Added successfully!")
        save_data()

    def view_balance():
        balance = sum(addincome) - sum(addexpense)
        print("The remaining amount: ", balance)

    def view_expense():
        for i, expense in enumerate(addexpense, start=1):
            print(i, ".", expense)
        print("Total: ", sum(addexpense))

    def view_income():
        for i, income in enumerate(addincome, start=1):
            print(i, ".", income)
        print("Total: ", sum(addincome))

    def edit_expense():
        print("1. Edit\n2. Delete")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            edit = int(input("Enter the value to Edit: "))
            if edit in addexpense:
                edit1 = int(input("Enter the new value: "))
                addexpense[addexpense.index(edit)] = edit1
                print("Expense updated!")
            else:
                print("Value not found.")
        elif choice == 2:
            edit = int(input("Enter the value to Delete: "))
            if edit in addexpense:
                addexpense.remove(edit)
                print("Expense deleted!")
            else:
                print("Value not found.")
        save_data()

    def edit_income():
        print("1. Edit\n2. Delete")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            edit = int(input("Enter the value to Edit: "))
            if edit in addincome:
                edit1 = int(input("Enter the new value: "))
                addincome[addincome.index(edit)] = edit1
                print("Income updated!")
            else:
                print("Value not found.")
        elif choice == 2:
            edit = int(input("Enter the value to Delete: "))
            if edit in addincome:
                addincome.remove(edit)
                print("Income deleted!")
            else:
                print("Value not found.")
        save_data()

# Load saved data at the start
load_data()

# Menu to handle user input
while True:
    print("-----------------------------------------------------------")
    print("Menu\n1. Add Expense\n2. Add Income\n3. View Balance\n4. View Expense\n5. Edit/Delete Expense\n6. Edit/Delete Income\n7. Exit")
    print("-----------------------------------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ExpenseTracker.add_expense()
    elif choice == 2:
        ExpenseTracker.add_income()
    elif choice == 3:
        ExpenseTracker.view_balance()
    elif choice == 4:
        ExpenseTracker.view_expense()
    elif choice == 5:
        ExpenseTracker.view_expense()
        ExpenseTracker.edit_expense()
    elif choice == 6:
        ExpenseTracker.view_income()
        ExpenseTracker.edit_income()
    elif choice == 7:
        break
    else:
        print("Invalid input")
    print("Please wait for 2 seconds...")
    time.sleep(2)
