
import login
import data_managment

def main():
    username = login.login_name()  # Get the username from the login process
    if username:  # If username is returned
        data_managment.main_menu(username)  # Pass the username to the main_menu function

main()