# Import csv, time and os
import csv
import time
import os
# welcome screen
def welcome():
    #Display welcome
    print("Welcome to the Savings Goal Tracker!")
    #Check if path exists
    if not os.path.exists("savings.csv"):
        # With open, mode = w
        with open("savings.csv", "w", newline='') as file:
            writer = csv.writer(file)
            #Store in csv file, goal_amount, amount_saved,due date(To store them in order)
            writer.writerow(["goal_amount", "amount_saved", "due_date"])
            data_reader()
    else:
         with open("savings.csv", "r") as file:
            reader = csv.reader(file)
            #Skip
            next(reader)  
            data = list(reader)
            if data:
                data_reader()
            else:
                goal_input()
            


def data_reader():
    try:
        #With open, mode = r
        with open("savings.csv", "r") as file:
            reader = csv.reader(file)
            #Skip
            next(reader)  
            data = list(reader)
            #If data is not empty
            if data:
                print(f"Current goal: {data[0][0]}, Saved: {data[0][1]}, Due Date: {data[0][2]}")
                user_progress()
            #Else calls goal_input
            elif {data[0][0]}<= {data[0][1]}:
                goal_input()
            else:
                goal_input()
    #If file not found, display no savings data found
    except FileNotFoundError:
        print("No savings data found")



def goal_input():
    #lets user enter goal amount and due date
    try:
        goal_amount = input("Enter your goal amount: ")
        due_date = input("Enter your due date (YYYY-MM-DD): ")
        #With open, more = w
        with open("savings.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["goal_amount", "amount_saved", "due_date"])
            writer.writerow([goal_amount, 0, due_date])
             #Display goal saved
            print("Goal saved!")
    except ValueError:
        print("Enter numbers!")



def new_input():
    try:
        goal_amount = input("Enter your goal amount: ")
        due_date = input("Enter your due date (YYYY-MM-DD): ")
        #With open, more = w
        with open("savings.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["goal_amount", "amount_saved", "due_date"])
            writer.writerow([goal_amount, 0, due_date])
             #Display goal saved
            print("Goal saved!")
            data_reader()
    except ValueError:
        print("Enter numbers!")




def user_progress():
    #User enter the amount of money they saved
    amount_saved = float(input("Enter the amount you saved: "))
    with open("savings.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)
        if data:
            #To get the amount and saved as total_saved
            total_saved = float(data[0][1]) + amount_saved
            goal_amount = float(data[0][0])
            #Get date and store as due_date
            due_date = data[0][2]
        else:
            print("Goal not found")
            return
    #With Open mode = w
    with open("savings.csv", "w", newline='') as file:
        writer = csv.writer(file)
        #Store both goal_amount on top and the number under
        writer.writerow(["goal_amount", "amount_saved", "due_date"])
        writer.writerow([goal_amount, total_saved, due_date])
    # Display the amount saved, remaining, and due date
    print(f"You have saved: {total_saved}")
    print(f"Remaining: {goal_amount - total_saved}")
    print(f"Due date: {due_date}")
    #Check if reached the goal
    if total_saved >= goal_amount:
        print("Goal reached!")
        check_due_date(due_date)
# Check due date
def check_due_date(due_date):
    #store current time
    current_time = time.strftime("%Y-%m-%d")
    #Check if passed due date
    if current_time > due_date:
        print("You reached your goal, but after the due date")
        new_input()


    elif current_time <= due_date:
        print("You reached your goal on time!")
        new_input()

if __name__ == "__main__":
    welcome()


