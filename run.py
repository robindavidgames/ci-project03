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


def target_message():
    """
    Present a motivational message related to the user being on or off target.
    Recieves the total words and the number of completed dates.
    Passes progress to see_target().
    """


def total_words():
    """
    Present total number of words written.
    Recieves current date.
    Passes total words and current date to target_message().
    """


def log_day():
    """
    Update daily writing log.
    Add a new line to the worksheet to represent the current day.
    Passes current date to total_words().
    """


def prev_day():
    """
    Update a previous daily writing log.
    Allow user to input a previous date and then change the value in that date.
    Passes current date to total_words()
    """


def see_progress():
    """
    See all progress made so far.
    Print the values for all dates input so far.
    Passes current date to total_words()
    """


def main():
    """
    On program launch.
    Provide 4 options to user:
    log update; change previous log; see daily goal; see all progress.
    """
    print("Choose which action you would like to perform. (Type number 1, 2, 3, or 4)")
    print("1. Add a new day's progress.")
    print("2. Update a previous day's progress.")
    print("3. See your daily goal.")
    print("4. See all your progress.\n")


print("Welcome to your National Novel Writing Month progress tracker.\n")
main()
