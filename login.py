import csv
import helper_funcs
import data_managment

CSV_FILE = "loginfo.csv"

def login_name():
    name = input("Please enter your username: ").strip().lower()

    with open(CSV_FILE, "r") as file:
        existing_users = {row[0]: row[1] for row in csv.reader(file)}  # store usernames & passwords

    if name in existing_users:
        stored_password = existing_users[name]
        return login_password(name, stored_password)  # 🔐 Ask for password before returning
    else:
        print("Error: Username not found.")
        selection = helper_funcs.inq_select("Would you like to: \n(use arrow keys for naviagtion)", "Create New Account", "Try Again")

        if selection == 1:
            return create_account()
        elif selection == 2:
            return login_name()

def login_password(username, stored_password):
    password = input("Enter your password: ").strip()
    encrypted_password = helper_funcs.caesar_cipher_encrypt(password)

    if encrypted_password == stored_password:
        print(f"Welcome {username}, you have successfully logged in!")
        return username
    else:
        print("Incorrect password. Please try again.")
        return login_name()

def create_account():
    username = input("Enter a new username: ").strip().lower()

    with open(CSV_FILE, "r") as file:
        existing_users = {row[0] for row in csv.reader(file)}

    if username in existing_users:
        print("That username already exists. Please try again.")
        return create_account()

    password = input("Enter your password: ").strip()
    confirm_password = input("Confirm your password: ").strip()

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return create_account()

    encrypted_password = helper_funcs.caesar_cipher_encrypt(password)

    with open(CSV_FILE, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([username, encrypted_password, "{}"])

    print(f"Account created successfully! You can now log in.")
    return username
