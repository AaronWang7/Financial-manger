# Daniel Blanco, Income/Expense and budgeting tracker.
# Over the weekend I will fix all the errors and add comments


import csv

budget_dict = {}


def main(): 
       print("This is your income/expense and budgeting tracker.") 
       while True: print("Choose an option: (1) Manage Income & Expenses, (2) Budgeting, (3) Exit") 
user_choice = input().strip()

        # Processes user choice
if user_choice == "1":
        manage_income_expenses()
elif user_choice == "2":
        manage_budgeting()
elif user_choice == "3":
        print("Goodbye!")
        break
else: #Error Mesage
    print("Invalid choice. Please enter a number between 1 and 3.")

def manage_income_expenses(): 
    print("Input income and expense entries: date, amount, and source/categories.") 
    with open("finance_data.csv", "a", newline = "") as file: writer = csv.writer(file) 
    while True: 
        date = input("Enter date (YYYY-MM-DD): ") 
        amount = input("Enter amount: ") 
        category = input("Enter source or category: ") 
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

def display_total_income_expenses(): 
    start_date = input("Enter start date (YYYY-MM-DD): ") 
    end_date = input("Enter end date (YYYY-MM-DD): ") 
    total_income = 0 
    total_expenses = 0

    with open("finance_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            date, amount, category = row
            amount = float(amount)
            if start_date <= date <= end_date:
                if amount > 0:
                    total_income += amount
                else:
                    total_expenses += amount

    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")

def manage_budgeting():
    print("Input budget limits for expense categories.") 
    with open("budget_data.csv", "a", newline="") as file: writer = csv.writer(file)
    while True: 
        category = input("Enter expense category: ")

        budget_limit = input("Enter budget limit amount: ") 
        print(f"Confirm entry: {category} - Budget: ${budget_limit}") 
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

def compare_budget_to_expenses(): 
    print("Comparing actual expenses to budget limits...") 
    

with open("budget_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        category, budget_limit = row
        budget_dict[category] = float(budget_limit)

expense_totals = {}
with open("finance_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        date, amount, category = row
        amount = float(amount)
        if amount < 0:
            expense_totals[category] = expense_totals.get(category, 0) + abs(amount)

print("Budget vs Actual Expenses:")
for category, budget_limit in budget_dict.items():
    spent = expense_totals.get(category, 0)
    print(f"{category}: Budget ${budget_limit} | Spent ${spent}")

if __name__ == "__main__":
    main()