#Daniel Blanco, Income/Expense and budgeting tracker.

#Over the weekend I will fix all the errors and add comments

import csv from datetime import datetime

budget_dict = {}

def main(): print("This is your income/expense and budgeting tracker.") while True: print("Choose an option: (1) Manage Income & Expenses, (2) Budgeting, (3) Exit") user_choice = input().strip()

if user_choice == "1":
        manage_income_expenses()
    elif user_choice == "2":
        manage_budgeting()
    elif user_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

def manage_income_expenses(): print("Input income and expense entries: date, amount, and source/categories.") with open("finance_data.csv", "a", newline="") as file: writer = csv.writer(file) while True: date = input("Enter date (YYYY-MM-DD): ") try: datetime.strptime(date, "%Y-%m-%d") except ValueError: print("Invalid date format. Please enter in YYYY-MM-DD format.") continue

amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        category = input("Enter source or category: ").strip().lower()
        print(f"Confirm entry: {date}, {amount}, {category}") 
        confirmation = input("Is this correct? (yes/no) or type 'exit' to cancel: ").strip().lower()
        if confirmation == "exit":
            return
        elif confirmation == "yes":
            writer.writerow([date, amount, category])
            print("Entry saved.")
            break
        else:
            print("Incorrect input. Please re-enter the details.")
display_total_income_expenses()

def display_total_income_expenses(): start_date_input = input("Enter start date (YYYY-MM-DD): ") end_date_input = input("Enter end date (YYYY-MM-DD): ") try: start_date = datetime.strptime(start_date_input, "%Y-%m-%d") end_date = datetime.strptime(end_date_input, "%Y-%m-%d") except ValueError: print("Invalid date format. Returning to menu.") return

total_income = 0
total_expenses = 0

with open("finance_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            amount = float(row[1])
            category = row[2].strip().lower()
        except (ValueError, IndexError):
            continue

        if start_date <= date <= end_date:
            if amount > 0:
                total_income += amount
            else:
                total_expenses += amount

print(f"Total Income: ${total_income:.2f}")
print(f"Total Expenses: ${abs(total_expenses):.2f}")

def manage_budgeting(): print("Input budget limits for expense categories.") with open("budget_data.csv", "a", newline="") as file: writer = csv.writer(file) while True: category = input("Enter expense category: ").strip().lower() budget_input = input("Enter budget limit amount: ") try: budget_limit = float(budget_input) except ValueError: print("Invalid budget amount. Please enter a numeric value.") continue

print(f"Confirm entry: {category} - Budget: ${budget_limit:.2f}")
        confirmation = input("Is this correct? (yes/no) or type 'exit' to cancel: ").strip().lower()

        if confirmation == "exit":
            return
        elif confirmation == "yes":
            writer.writerow([category, budget_limit])
            print("Budget saved.")
            compare_budget_to_expenses()
            break
        else:
            print("Incorrect input. Please re-enter the details.")

def compare_budget_to_expenses(): print("Comparing actual expenses to budget limits...") budget_dict.clear()

with open("budget_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            category = row[0].strip().lower()
            budget_limit = float(row[1])
            budget_dict[category] = budget_limit
        except (ValueError, IndexError):
            continue

expense_totals = {}
with open("finance_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            amount = float(row[1])
            category = row[2].strip().lower()
        except (ValueError, IndexError):
            continue

        if amount < 0:
            expense_totals[category] = expense_totals.get(category, 0) + abs(amount)

print("Budget vs Actual Expenses:")
for category, budget_limit in budget_dict.items():
    spent = expense_totals.get(category, 0)
    print(f"{category.capitalize()}: Budget ${budget_limit:.2f} | Spent ${spent:.2f}")

if name == "main": main()

