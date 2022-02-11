"""
Program to track a single user's writing progress for National Novel Writing
Month.
"""

# Write your code to expect a terminal of 80 characters wide and 24 rows high

# gspread is used to read and write data in a google sheet.
import gspread
from google.oauth2.service_account import Credentials

# operator is used to sort list of dictionaries.
# import operator

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


def main():
    """
    On program launch.
    Provide 4 options to user:
    log update; change previous log; see daily goal; see all progress.
    """

    menu_loop = True

    while menu_loop is True:
        print(
            "\nChoose which action you would like to perform. (Number 1-4)")
        print("1. Add a new day's progress.")
        print("2. Update a previous day's progress.")
        print("3. See your daily goal.")
        print("4. See all your progress.\n")

        choice = input("Your choice: ")

        if choice == "1":
            menu_loop = False
            log_day()
        elif choice == "2":
            menu_loop = False
            prev_day()
        elif choice == "3":
            menu_loop = False
            total_words('0')
        elif choice == "4":
            menu_loop = False
            see_progress()
        else:
            print(
                "\n Invalid choice. Please input a number between 1 and 4.\n")


def log_day():
    """
    Update daily writing log.
    Add a new line to the worksheet to represent the current day.
    Passes value to validate_data() to validate.
    Passes current date to total_words().
    """
    print("\nEnter your wordcount for a new day.")
    print("This will create a new entry in your log.\n")

    validating_choice = True
    while validating_choice == True:
        daily_word_count = input("Enter wordcount here: ")
        validating_choice = validate_data(daily_word_count) # Confirm data is integer.

    # Determine which column/day to update in worksheet.
    current_day = len(data[0])
    column_to_update = current_day + 1

    # Update worksheet. Third argument is name of the worksheet to update.
    update_worksheet(column_to_update, daily_word_count, "wordcount")


def prev_day():
    """
    Update a previous daily writing log.
    Allow user to input a previous date and then change the value in that date.
    Passes value to validate_data() to validate.
    Passes current date to total_words()
    """
    validating_date = True
    validating_wordcount = True

    while validating_date == True:
        day_to_update = input("Enter the date you wish to update: ")
        validating_date = validate_data(day_to_update)
        # Check date is one that has been previously entered.
        if validating_date == False and int(day_to_update) >= len(data[0]):
            validating_date = True
            print(f"You must enter a date no higher than {len(data[0])}.\n")

    while validating_wordcount == True:
        updated_word_count = input(f"Enter the corrected wordcount for day {day_to_update}: ")
        validating_wordcount = validate_data(updated_word_count)

    # Determine which column/day to update in worksheet.
    column_to_update = int(day_to_update) + 1

    update_worksheet(column_to_update, updated_word_count, "wordcount")


def see_progress():
    """
    See all progress made so far.
    Print the values for all dates input so far.
    Passes current date to total_words()
    """
    print("See progress")


def validate_data(data_to_validate):
    """
    Validates that data inputted by the user is an integer.
    Converts inputted data to integer if possible.
    Raises ValueError if value is not integer.
    """
    try:
        int(data_to_validate)
        print("Data is valid.\n")
        return False
    except ValueError:
        print("\nData is invalid. You must input a whole number.\n")
        return True


def update_worksheet(column_to_update, daily_word_count, worksheet):
    """
    Updates the worksheet with the validated value.
    Heavily modified from Love Sandwiches.
    row_to_update could be changed to reflect current user.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    row_to_update = 1
    # Move these to other functions so they can be updated dynamically.
    # current_day = len(data[0])
    # column_to_update = current_day + 1
    worksheet_to_update.update_cell(
        row_to_update, column_to_update, daily_word_count)
    print(f"A new daily log has been added to the {worksheet} worksheet.")

    total_words(daily_word_count)


def total_words(daily_word_count):
    """
    Present total number of words written.
    Recieves wordcount for the current date.
    Passes total words and current date to target_message().
    """
    all_users = []

    for x in range(len(data)):
        # Select the list to work on.
        current_list = data[x]

        # Remove blank entries
        while '' in current_list:
            current_list.remove('')

        # Ignore the first entry (as it is the username).
        list_splice = current_list[1:len(current_list)]

        # Convert all entries to int.
        for i in range(len(list_splice)):
            list_splice[i] = int(list_splice[i])

        # Sum entries plus today's entry (if current user).
        if current_list == data[0]:
            total_count = sum(list_splice) + int(daily_word_count)
        else:
            total_count = sum(list_splice)

        all_users.append(
            {
                "user": current_list[0],
                "wordcount": total_count,
                "day": len(current_list)
            }
        )

    target_message(all_users)
    see_target(all_users)


def target_message(all_users):
    """
    Present a motivational message related to the user being on or off target.
    Recieves list of dictionaries that contains progress for all users and
    pulls relevant data.
    Passes progress to see_target().
    """
    current_wordcount = all_users[0]["wordcount"]
    print(f"\nYou have written a total of {current_wordcount} words.")
    average_wordcount = int(current_wordcount / all_users[0]["day"])
    print(f"\nEach day, you write an average of {average_wordcount} words.")

    return


def see_target(all_users):
    """
    Present the daily writing target, comparing to the 30 day deadline
    and 80000 word target.
    Recieves list of dictionaries that contains progress for all users
    and pulls relevant data.
    """
    words_remaining = 80000 - all_users[0]["wordcount"]
    days_remaining = 30 - all_users[0]["day"]
    daily_average = int(words_remaining / days_remaining)
    required_today = int((80000 / 30) * all_users[0]["day"])

    if words_remaining > 0:
        if days_remaining >= 0:
            if (all_users[0]["wordcount"] - 1000) > required_today:
                print("\nYou're making great progress.")
            elif (all_users[0]["wordcount"] + 1000) < required_today:
                print("\nYou're falling behind.")
            else:
                print("\nYou're on target.")
            print(f"\nTo stay on track, write {daily_average} words today.\n")
        else:
            print("\nYou ran out of time!")
            print(f"You have {words_remaining} words remaining.\n")
    else:
        print("\nYou reached your 80,000 word goal!\n")

    restart()


def restart():
    """
    Allows the user to return to the main menu.
    """
    return_to_menu = input("Press Enter to return to the menu: ")

    if return_to_menu == "":
        data = wordcount.get_all_values()
        main()


print("\nWelcome to your National Novel Writing Month progress tracker.")
main()
