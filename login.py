import csv
import helper_funcs
import data_managment

CSV_FILE = "loginfo.csv"

def login_name():
    #Prompts user for username and verifies it from the CSV file.
    name = input("Please enter your username: ").strip().lower()  # 'name' is the user input

    # Now using data_managment to load user data
    # Check if the username exists
    with open(CSV_FILE, "r") as file:
        existing_users = {row[0] for row in csv.reader(file)}  # Set for faster lookup

    if name in existing_users:  # Check if 'name' is in the existing users
        return name  # Return the username if found
    else:
        print("Error: Username not found.")
        selection = helper_funcs.menu_select("Would you like to:", "Create New Account", "Try Again")
    
        if selection == 1:
            return create_account()
        elif selection == 2:
            return login_name()


def login_password(username, stored_password):
    #Verifies user password against stored encrypted password.
    password = input("Enter your password: ").strip()
    encrypted_password = helper_funcs.caesar_cipher_encrypt(password)

    if encrypted_password == stored_password:
        print(f"Welcome {username}, you have successfully logged in!")
        return username  # Return username on successful login
    else:
        print("Incorrect password. Please try again.")
        return login_name()

def create_account():
    #Handles new account creation.
    username = input("Enter a new username: ").strip().lower()

    # Check if the username exists
    with open(CSV_FILE, "r") as file:
        existing_users = {row[0] for row in csv.reader(file)}  # Set for faster lookup

    if username in existing_users:
        print("That username already exists. Please try again.")
        return create_account()

    password = input("Enter your password: ").strip()
    confirm_password = input("Confirm your password: ").strip()

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return create_account()

    encrypted_password = helper_funcs.caesar_cipher_encrypt(password)

    # Now save user info with empty balances in accounts.csv
    with open(CSV_FILE, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([username, encrypted_password, "{}"])  # Empty dictionary for balances

    print(f"Account created successfully! You can now log in.")
    return username  # Return the username for further use
