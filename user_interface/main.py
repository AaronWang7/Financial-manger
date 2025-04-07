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

args = ["----------Personal Financial Manager program----------"] #Extra menu text to introduce the program.

def main(): #Main user interface
    while True: #While loop
        print(args[0]) #Fancy fancy stuff, allows for direct and specific things on the variable for what it displays.
        try:
            intro = inquirer.text(message="Welcome ot your personal financial manager! What's your name?").execute()
            print(f"Welcome {intro}.") #Repeats the username with a welcome message.
            pers_finan_opt = inquirer.select( #Main prompt
                message="What would you like to do?:", #Questions
                choices= ["Go to the Savings Goal Tracker", "Data Manager", "Convert Currency", "Check Budgetting", "Exit"],
                filter=lambda result: result.split()[0].lower() #Allows the user to be able to input their response correctly.
            ).execute()
            if pers_finan_opt == "go": #Different choices that go into the different functions, this one goes into the Savings/Goal Trackers.
                pass
                break
            elif pers_finan_opt == "data": #This one goes into the Data Manager.
                pass
                break
            elif pers_finan_opt == "convert": #This one goes into the Convert Currency.
                pass
                break
            elif pers_finan_opt == "check": #This one goes into the Check Budgetting.
                pass
                break
            elif pers_finan_opt == "exit": #As the name implies, exits and quits the program.
                print("Goodbye, thank you for using your personal financial manager!")
                break
        except:
            ValueError #Error management.
            print("This doesn't work! Please choose a correct input mainly using the arrow keys.")

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