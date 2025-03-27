####
####
####
####
####
####
#Ethan Blanco, Main User-Interface
####
####
####
####
####
####

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

def main(): #Main user interface
    while True:
        print("----------Personal Financial Manager program----------")
        try:
            intro = inquirer.text(message="Welcome ot your personal financial manager! What's your name?").execute()
            pers_finan_opt = inquirer.select( #Main prompt
                message="What would you like to do?:", #Questions
                choices= ["Go to the Savings Goal Tracker", "Data Manager", "Convert Currency", "Check Budgetting", "Exit"],
                filter=lambda result: result.split()[0].lower() #Allows the user to be able to input their response correctly.
            ).execute()
            print(f"Welcome {intro}.") #Repeats the username with a welcome message.
            if pers_finan_opt == "go": #Different choices that go into the different functions.
                print("This is the '1' option, 'Savings Goal Tracker', if it is working, then great! Don't forget to callback the actual functions here later!")
                break
            elif pers_finan_opt == "data":
                print("This is the '2' option, 'Data Manager', if it is working, then great! Don't forget to callback the actual functions here later!")
                break
            elif pers_finan_opt == "convert":
                print("This is the '3' option, 'Convert Currency', if it is working, then great! Don't forget to callback the actual functions here later!")
                break
            elif pers_finan_opt == "check":
                print("This is the '4' option, 'Check Budgeting', if it is working, then great! Don't forget to callback the actual functions here later!")
                break
            elif pers_finan_opt == "exit":
                print("This is the '5' option, 'Exit', if it is working, then great! Don't forget to callback the actual functions here later!")
                break
        except:
            ValueError
            print("This doesn't work! Please input a correct input (1, 2, 3, 4, 5)")

main()

####
####
####
####
####
####
#Finished program, remember add in the actual function names.
####
####
####
####
####
####