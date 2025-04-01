#Import time to track date
import time
# Create a function that display the welcome screen
def welcome():
    print("This is saving goal tracker")
    data_reader()

# Read data from csv file
def data_reader():
    with open ("","r")
    # check if file is empty
    goal_input()

#Create a function to get user's input(goal amount, date) and save it to a csv file
def goal_input():
    print("Enter your goal amount ")
    goal_amount = input(":")
    print("Enter the due date(year)\nexample:2025")
    due_date_year = input(":")
    print("Enter the due date(month)\n1-12")
    due_date_month = input(":")
    print("Now, enter the due date(day,1-31)\nexample: 25")
    #check if user's input is right(goal amount and due date must be numbers)
    # Then save tham to a csv file


