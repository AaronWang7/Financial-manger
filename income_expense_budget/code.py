# Daniel Blanco, Income/Expense and Budgeting Tracker


import csv


def main(): 
    # This is the first thing the user sees, allows them to manage income expenses and budgeting.
    print("This is your income/expense and budgeting tracker.")
    while True:
        print("Choose an option: (1) Manage Income & Expenses, (2) Budgeting, (3) Exit")
        user_choice = input().strip()

        # Inputting 1 and 2 allow you to manage the stuff(income expenses and budgeting)
        if user_choice == "1":
            manage_income_expenses()
        elif user_choice == "2":
            manage_budgeting()
        # Inputting 3 exits the code
        elif user_choice == "3":
            print("Goodbye!")
            break
        else: # Error message, 1, 2, and 3 must be inputted
            print("Invalid choice. Please enter a number between 1 and 3.")



def manage_income_expenses():
    # When inputting 1, it takes you to this function, requesting inputs on income and expenses like date, amount, and source/categories.
    print("Input income and expense entries: date, amount, and source/categories.")
    with open("finance_data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        while True:
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter source or category: ")

            # These two lines of code confirm what you inputted was correct
            print(f"Confirm entry: {date}, {amount}, {category}")
            confirmation = input("Is this correct? (yes/no) or type 'exit' to cancel: ").strip().lower()

            # The response towards the confirmation
            if confirmation == "exit":
                return
            elif confirmation == "yes":
                writer.writerow([date, amount, category])
                print("Entry saved.")
                break
            else: 
                # Error message
                print("Incorrect input. Please re-enter the details.")



def display_total_income_expenses():
    # This function displays the total income expenses, requesting start and end dates
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    total_income = 0
    total_expenses = 0

    # Opens the csv file in read mode
    with open("finance_data.csv", "r") as file:
        reader = csv.reader(file)

        # Formatting
        for row in reader:
            date, amount, category = row
            amount = float(amount)

            if start_date <= date <= end_date:

                if amount > 0:
                    total_income += amount

                else:
                    total_expenses += amount

    # Displays the results
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")


def manage_budgeting():
    # When inputting 2, it takes you to this function, managing the budgets
    print("Input budget limits for expense categories.")

    # Opens budget csv file in append mode

    with open("budget_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        while True:
            category = input("Enter expense category: ")
            budget_limit = input("Enter budget limit amount: ")

            # These two lines of code confirm what you inputted was correct
            print(f"Confirm entry: {category} - Budget: ${budget_limit}")
            confirmation = input("Is this correct? (yes/no) or type 'exit' to cancel: ").strip().lower()

            # The response towards the confirmation
            if confirmation == "exit":
                return
            elif confirmation == "yes":
                writer.writerow([category, budget_limit])
                print("Budget saved.")
                compare_budget_to_expenses()
                break
            else:
                # Error message
                print("Incorrect input. Please re-enter the details.")


def compare_budget_to_expenses():
    # This function compares budget limits to the expenses
    print("Comparing actual expenses to budget limits...")
    budget_dict = {}

    # Opens the budget csv file in read mode
    with open("budget_data.csv", "r") as file:
        reader = csv.reader(file)
        # Formatting
        for row in reader:
            category, budget_limit = row
            budget_dict[category] = float(budget_limit)

    expense_totals = {}
    # Opens the finance csv file in read mode
    with open("finance_data.csv", "r") as file:
        reader = csv.reader(file)
        # Formatting
        for row in reader:
            date, amount, category = row
            amount = float(amount)

            if amount < 0:
                expense_totals[category] = expense_totals.get(category, 0) + abs(amount)

    # Prints results
    print("Budget vs Actual Expenses:")
    for category, budget_limit in budget_dict.items():
        spent = expense_totals.get(category, 0)
        
        print(f"{category}: Budget ${budget_limit} | Spent ${spent}")

if __name__ == "__main__":
    main()
