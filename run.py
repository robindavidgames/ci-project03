"""
Program to track a single user's writing progress for National Novel Writing
Month.
"""

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def see_target():
    """
    Present the daily writing target.
    Receives progress from target_message().
    """
    print("Present daily target")


def target_message():
    """
    Present a motivational message related to the user being on or off target.
    Recieves the total words and the number of completed dates.
    Passes progress to see_target().
    """
    print("Present target message")


def total_words():
    """
    Present total number of words written.
    Recieves current date.
    Passes total words and current date to target_message().
    """
    print("See total words")


def log_day():
    """
    Update daily writing log.
    Add a new line to the worksheet to represent the current day.
    Passes current date to total_words().
    """
    print("Log a new day")


def prev_day():
    """
    Update a previous daily writing log.
    Allow user to input a previous date and then change the value in that date.
    Passes current date to total_words()
    """
    print("Update previous day")


def see_progress():
    """
    See all progress made so far.
    Print the values for all dates input so far.
    Passes current date to total_words()
    """
    print("See progress")


def main():
    """
    On program launch.
    Provide 4 options to user:
    log update; change previous log; see daily goal; see all progress.
    """
    print("Choose which action you would like to perform. (Type number 1-4)")
    print("1. Add a new day's progress.")
    print("2. Update a previous day's progress.")
    print("3. See your daily goal.")
    print("4. See all your progress.\n")

    choice = input("Your choice: ")

    if choice == "1":
        log_day()
    elif choice == "2":
        prev_day()
    elif choice == "3":
        total_words()
    elif choice == "4":
        see_progress()
    else:
        print("\n Invalid choice. Please input a number between 1 and 4.")
        choice = input("Your choice: ")
        #this doesn't work because it comes after the if/elif. Need to make a seperate function.


print("Welcome to your National Novel Writing Month progress tracker.\n")
main()
