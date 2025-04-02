import base64
from InquirerPy import inquirer

#start of menu select function
def menu_select(*args):


    while True: #loop because having a recursive function wouldnt work

        print(f"\n{args[0]}") #prints the message

        items = [] #creates empty list, allowing appending later

        for i in range(len(args)-1): #loops for each item in paramater aside from message

            items.append(i+1) # adds a number to a list, this list is used for checking if the users input is inside of the paramaters

            print(f"({i+1}) {args[i+1]}") #prints each item in format (number it is in the list) paramater entered into the function

        try:    #stage 1 of checking user input, to make sure its an integer 

            menu_input = int(input("Please type the number corosponding to your selection: "))

            if menu_input not in items:     #essentially saying, if the users input, isnt in the list of numbers created earlier, then its not valid.

                print(f"\nPlease only type numbers 1 - {len(args)-1} ")     #gives the user an example range to enter

            else:

                return menu_input   #returns the number as an output of the function.

        except:

            print("\nPlease only enter a whole number")

""""

Example

input:

print(menu_select("Please select your option","option #1","option #2","option #3","option#4"))

output:

Please select your option:
(1) option #1
(2) option #2
(3) option #3
(4) option#4
Please type the number corosponding to your selection:

if the selects one of the options, its returned, so if the user inputed 1 here, it would output 1

returns entered number while checking to make sure it fits the paramaters set 

If you want to be fancy with it, and have the user create their own menu, you can do print(menu_select(input("message: "),input("paramater 1: "),input("paramater 2: "),input("paramater 3: "),input("paramater 4: ")))
"""
#end of menu select function



def caesar_cipher_encrypt(text, shift=3):
    #Encrypts text using Caesar Cipher.
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift=3):
    #Decrypts text using Caesar Cipher.
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text



#START OF INQUIRE PY MENU SELECT FUNCTION

def inqpy_menu(*args):
    while True: #loop because having a recursive function wouldnt work



        items = [] #creatres an empty list so it can be appended to later



        for i in range(len(args)-1): #loops for each item in paramater aside from message


                                                    #if the input was "example input" then it would print (1) example input
            items.append(f"({i+1}) {args[i+1]}") #appends objects in the list to items in the format (1) example input



        menu_input = inquirer.select( #creates the menu, the function behind it all
            


            message = args[0], #the message at the top of the question.



            choices = items, #items is displayed in a menu navigatable by arrow keys and enter



            filter = lambda result: result.split()[0].lower() #Allows the user to be able to input their response correctly.



        ).execute() #runs everything inside of inquirer.select



        return menu_input

print(inqpy_menu("Please select your option:","option #1","option #2","option #3","option#4"))