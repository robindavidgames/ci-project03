"""
Program to track a single user's writing progress for National Novel Writing
Month.
"""

# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('NaNoWriMo Tracker')

wordcount = SHEET.worksheet('wordcount')

data = wordcount.get_all_values()

# Check spreadsheet is connected to python
print(data)


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


def validate_data(daily_word_count):
    """
    Validates that data inputted by the user is an integer.
    Raises ValueError if value is not integer.
    """
    print("Validate data")


def log_day():
    """
    Update daily writing log.
    Add a new line to the worksheet to represent the current day.
    Passes value to validate_data() to validate.
    Passes current date to total_words().
    """
    print("Log a new day")


def prev_day():
    """
    Update a previous daily writing log.
    Allow user to input a previous date and then change the value in that date.
    Passes value to validate_data() to validate.
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

    while True:
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
            print("\n Invalid choice. Please input a number between 1 and 4.\n")


print("Welcome to your National Novel Writing Month progress tracker.\n")
main()
