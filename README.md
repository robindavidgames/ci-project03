Readme

National Novel Writing Month is a yearly event in which people attempt to write an 80000 word novel in the month of November. The event puts a lot of emphasis on daily word counts and reaching goals. The purpose of this piece of software is to provide a way for a user to track their daily writing progress, to see if they are on target, and what they need to do to stay on target or to catch up with their goals if they have fallen behind. It uses a googlesheet to hold information.

![Flow chart of operations](./assets/readme/NaNoWritMo-flow-chart.png)

# Features
* The total words function creates a dictionary of all users, containing username, word count, and current day. This is to allow the program to compare user performance. 

# Bugs and Issues

## Enumerating (remove this)
When creating a loop to iterate through a list, I used a range function. Gitpod suggested I try to enumerate to create cleaner code. I used resources at https://dev.to/wangonya/when-to-use-python-s-enumerate-instead-of-range-in-loops-3e03 to change this code:

    for i in range(len(list_splice)):

to this code:

    for i, value in enumerate(list_splice):

## Validating Data
I couldn't get my validate_data function to run correctly and check if inputted values were integers. I had created a while loop asking for an input and then within that while loop, would call validate_data(). Like this:

    while x == True:
        daily_word_count = input("Enter wordcount here: ")
        validate_data(daily_word_count)

But it didn't work! After some amount of searching forums, I asked for help on slack and was able to solve it. I hadn't assigned a varianble for validate_data() to assign its result.

    while x == True:
        daily_word_count = input("Enter wordcount here: ")
        x = validate_data(daily_word_count)

Having solved this, I was able to use validate_data() in all instances where I needed to check that inputted text was an integer.

## Managing Range of Iteration
In see_progress(), I needed to limit the number of pieces of data shown on the terminal (as there could be up to 30 pieces of data and the terminal is only 24 lines in height). As such a range set to len(data) did not work. When I tried setting the range to manual number (eg 20-30), it would result in a crash if there was less than 30 pieces of data (ie, if there were 28 days logged). To fix this error, I set the minimum at 20 and the maximum as len(data), so that the maximum boundary would be variable.

    for words in range(20, len(user_progress)):
        print(f"Day {words + 1}: {user_progress[words]} words")

# Future Features
## Multiple Users
By updating row_to_update in update_worksheet(), etc., it would be possible to create a program that handle multiple users. As it stands, each user in the googledoc is simply a different row.

# Credits
How to set up google drive and google sheets API is from the Love Sanwiches project.
Used gspread documentation to learn how update a googlesheet https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf
The code used to sort the dictionary in target_message is modified from https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
The code used to find the location of the current user in that sorted dictionary is modified from https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome robindavidgames,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!