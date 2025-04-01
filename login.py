import csv
import helper_funcs

def login_name():
    name = input("Please enter your username: ")
    log_slot = "Error: name not found:"
    with open("loginfo.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for index, row in enumerate(csv_reader):
            if row[0] == name.lower():
                log_slot = int(index) 
                return log_slot
        if type(log_slot) != int:
            print(log_slot)
            selection = helper_funcs.menu_select(log_slot,"New account","Try again")
            if selection == 1:
                print("WIP")
                #call account creation func here
            elif selection == 2:
                login_name()

print(login.login_name.log_slot)

