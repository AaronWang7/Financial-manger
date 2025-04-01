#From page: saving_goal_tracker import everything
from saving_goal_tracker import *
#A function that loads data from csv file and display the goal to the user
def load_data():
#With open mode = r
    with open("","r")
    print(f"This is your goal{goal}")


def user_progress():
    # let user enter the money they saved, or load from other pages
    print("Enter the money you saved:")
    save_amount = input(":")

def progress_save():#Dispaly the progress, how much user need to save
    # Save amount_saved + save_amount as amount_saved
    amount_saved = amount_saved + save_amount
    # Save goal_amount - amount_saved as amount_left
    amount_left = goal_amount - amount_saved
    #Display the amount the user have already saved
    print(f"This is how much you saved{amount_saved}")
    #Display the amount lefted
    print(f"This how much mor you need to save{amount_left}")
    #Display the due date
    print(f"This the the due date{due_date}")
    #Display date for today
    print(f"This is the date: {date}")
    if amount_saved >= goal_amount:
        print("Goal reached!")
        #Check if date in sec is bigger than due date in sec
        if date_sec >= due_date_sec:
            print("You didn't reach your goal in time!")
        elif due_date_sec <= date_sec:
            print("Your reached your goal in time")
    #Later save the updated amount to csv file