####
####
####
#Ethan Blanco, Main User-Interface
####
####
####

def main():
    while True:
        print("----------Personal Financial Manager program----------")
        try:
            main = int(input("""\n Welcome to your personal financial manager! What would you like to check and update?
                         1. Goal Savings Tracker
                         2. Data Manager
                         3. Convert Currency
                         4. Check Budget
                         5. Exit\n"""))
            if main == 1:
                print("This is the '1' option, if it is working, then great! Don't forget to callback the actual functions here later!")
                continue
            elif main == 2:
                print("This is the '2' option, if it is working, then great! Don't forget to callback the actual functions here later!")
                continue
            elif main == 3:
                print("This is the '3' option, if it is working, then great! Don't forget to callback the actual functions here later!")
                continue
            elif main == 4:
                print("This is the '4' option, if it is working, then great! Don't forget to callback the actual functions here later!")
                continue
            elif main == 5:
                print("Thank you for using your personal program, goodbye!")
                break
            
        except:
            ValueError
            print("This doesn't work!")

main()

####
####
####
#Finished program, remember add in the actual function names.
####
####
####