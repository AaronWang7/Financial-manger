import csv
import matplotlib.pyplot as plt
import helper_funcs

# CSV file where user data is stored
CSV_FILE = "accounts.csv"

def load_user_data(username):
    try:
        with open(CSV_FILE, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == username:
                    encrypted_balances = row[2]
                    decrypted_balances = helper_funcs.caesar_cipher_decrypt(encrypted_balances)
                    return eval(decrypted_balances)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while loading user data: {e}")
    
    return None

def save_user_data(username, balances):
    rows = []
    updated = False
    encrypted_balances = helper_funcs.caesar_cipher_encrypt(str(balances))
    
    try:
        with open(CSV_FILE, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == username:
                    row[2] = encrypted_balances
                    updated = True
                rows.append(row)
        
        if not updated:
            rows.append([username, "", encrypted_balances])
        
        with open(CSV_FILE, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)
    
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while saving user data: {e}")

def create_account(username):
    balances = load_user_data(username)
    if balances is None:
        balances = {}

    account_name = input("Enter new account name: ")
    amount = float(input("Enter initial amount: "))
    balances[account_name] = amount
    save_user_data(username, balances)
    print(f"Account '{account_name}' created successfully!")

def update_account(username):
    balances = load_user_data(username)
    if balances is None:
        balances = {}

    print("Your accounts:")
    for account, amount in balances.items():
        print(f"{account}: ${amount}")
    
    account_name = input("Enter account name to update: ")
    if account_name not in balances:
        print("Account not found!")
        return

    choice = helper_funcs.inq_select("use arrow keys for naviagtionSelect an option: \n(use arrow keys for naviagtion)", "Change name", "Change amount", "Delete account")
    if choice == 1:
        new_name = input("Enter new account name: ")
        balances[new_name] = balances.pop(account_name)
    elif choice == 2:
        new_amount = float(input("Enter new amount: "))
        balances[account_name] = new_amount
    elif choice == 3:
        del balances[account_name]
    
    save_user_data(username, balances)
    print("Account updated successfully!")

def display_pie_chart(username):
    balances = load_user_data(username)
    if not balances:
        print("No accounts to display!")
        return
    
    labels = balances.keys()
    sizes = balances.values()
    
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"{username}'s Account Balances")
    plt.show()

def main_menu(username):
    while True:
        choice = helper_funcs.inq_select("Select an option: \n(use arrow keys for naviagtion)", "Create new account", "Update existing account", "Display account balances (Pie Chart)", "Exit")
        if choice == 1:
            create_account(username)
        elif choice == 2:
            update_account(username)
        elif choice == 3:
            display_pie_chart(username)
        elif choice == 4:
            break
        else:
            print("Invalid choice, try again!")
