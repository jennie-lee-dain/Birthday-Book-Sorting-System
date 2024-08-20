"""
Jennie Lee  HW9   April 8 2024

This program is an terminal interactive program which allows the user 
to save and delete birthdays in a list. There are several functions to 
this program, including:
    1. add: adding birthdays to the list
    2. delete: delete a birthday from the list
    3. search: search for a certain person in the list
    4. save: save the current list to a file with a chosen name
    5. load: load the birthdays in a saved file to the current list
    6. help: displays the available commands for the command
    7. echo on: "echos"/repeats anything you have inputted
    8. echo off: turns off the "echo on" function

With these functions the user can save and delete their friends, family, or own birthday 
to keep track of the several birthdays in their live. 

"""

import os


def print_help():
    """This function can be used to print out the help message."""
    print("Allowed commands:")
    print("add firstName lastName month day year")
    print("list")
    print("delete number")
    print("search name")
    print("save filename")
    print("load filename")
    print("help")
    print("echo on")
    print("echo off")


def print_error_messsage():
    """
    This function can be used to print out the error message.
    """
    print("I am sorry, but that is not a recognized command, or")
    print("you have entered an incorrect number of arguments.")
    print("You may enter 'help' to see a list of commands.")


class BirthdayBook():
    """
    This class stores the list of birthdays
    """

    def __init__(self, birthday_list=list()):
        self.birthday_list = birthday_list

    def add(self, birthday):
        """        
        This function takes in a user inputted birthday
        and adds it to the birthday list
            Input: birthday
            Output: single birthday gets added to
                    the birthday list
        """
        # creating single_birthday list
        single_birthday = list()

        # adding birthday to single_birthday list
        single_birthday.append(birthday.first_name)
        single_birthday.append(birthday.last_name)
        single_birthday.append(birthday.month)
        single_birthday.append(birthday.day)
        single_birthday.append(birthday.year)

        # adding single_birthday to birthday book list
        self.birthday_list.append(single_birthday)


class Birthday():
    """
    This class stores a single birthday
    """

    def __init__(self, first_name="", last_name="", month="", day="", year=""):
        self.first_name = first_name
        self.last_name = last_name
        self.month = month
        self.day = day
        self.year = year


def get_user_command(user_input):
    """
    This functions takes the user input and determines which command 
    the user has inputted
        Input: test user has inputted
        Output: returns the command the user has inputted
    """
    user_input_list = user_input.split()
    user_command = user_input_list[0]
    # special case for echo function
    if (user_command == "echo"):
        user_command = user_input_list[1]

    return user_command


def format_birthday(birthday_list):
    """
    This functions takes the list of a single birthday and formats it to
    be printed out when the user asks for the "list"
        Input: single birthday list
        Output: returns the formatted birthday: "firstName lastName, MM/DD/YYY"
    """
    return (f'{birthday_list[0]} {birthday_list[1]}, {birthday_list[2]}/{birthday_list[3]}/{birthday_list[4]}')


def add_bday_to_book(user_input, birthday_book):
    """
    This functions takes the user input and the birthday book class and adds the 
    user inputted birthday to the birthday book, while catching to see if 
    the user has entered the correct value for each input. 
        Input: user's command and the birthday book
        Output: adds birthday to birthday book
    """
    try:
        # checking if month, day, and year values are integers
        int(user_input[2])
        int(user_input[3])
        int(user_input[4])

        # create birthday class
        birthday = Birthday()

        # adding the birthday elements to the birthday class
        birthday.first_name = user_input[0]
        birthday.last_name = user_input[1]
        birthday.month = user_input[2]
        birthday.day = user_input[3]
        birthday.year = user_input[4]

        # adding the birthday to the birthday book
        birthday_book.add(birthday)

        print(
            f"Added \"{format_birthday(user_input)}\" to birthday book.")
    # in case of a ValueError
    except ValueError:
        print("Error: Unable to add birthday to book. Please use integers for dates")


def print_list(birthday_book):
    """
    This functions is used to print the list of birthdays. It takes in
    the birthday book as a parameter
        Input: Birthday Book
        Output: prints the list of birthdays
    """
    for i in range(len(birthday_book.birthday_list)):
        print(f'{i+1}. {format_birthday(birthday_book.birthday_list[i])}')


def check_delete_num(delete_number, birthday_book):
    """
    This functions is used to check if the number the user has
    inputted for the delete function is an integer. After 
    validating the number, it calls the 'delete bday' function. 
        Input: user's "delete number" and the birthday book class
        Output: returns the command the user has inputted
    """
    # checking if the delete number is an integer
    try:
        delete_number = int(delete_number)
        success = True

    # in case of a ValueError
    except ValueError:
        print("Error: Please use an integer for the number")
        success = False

    delete_bday(delete_number, success, birthday_book)


def delete_bday(delete_number, success, birthday_book):
    """
    This functions takes in the user's delete number, the success 
    variable (wheter the user's delete number is valid or not), and
    the birthday book and is used to delete the user selected 
    birthday from the birthday book.
        Input: user's "delete number" and the birthday book class, and 
                success variable
        Output: deletes the selected birthday from the birthday book list 
                in the birthday book class
    """
    # initializing yes_or_no variable
    yes_or_no = ''

    # run this loop if the error checking was a success in the check_delete_num function
    if (success == True):
        # checking if the delete number exists in the current list
        if (delete_number > 0 and delete_number <= len(birthday_book.birthday_list)):
            print(
                f"Really delete {birthday_book.birthday_list[delete_number - 1][0]} ", end='')
            print(
                f"{birthday_book.birthday_list[delete_number - 1][1]} ", end='')
            print("from the birthday book? (y/n) ", end='')
            # getting user input for yes and no
            yes_or_no = input()
        else:
            print("I'm sorry, but there is no such entry in the book.")
            success = False

        # while the user has not given "valid" input
        while (yes_or_no != 'y' and yes_or_no != 'n' and success == True):
            yes_or_no = input("Please enter \"y\" or \"n\" (y/n) ")

        # when the user inputs "y" or "n"
        if (yes_or_no == 'y'):
            birthday_book.birthday_list.pop(delete_number - 1)
            success = False
        elif (yes_or_no == 'n'):
            success = False


def search_bday(name_search, birthday_book):
    """
    This functions takes in the user's "search" input
    and checks if there is a same name in the birthday book
    and prints the result.
        Input: user's "serach" name and the birthday book class
        Output: prints the result of the search
    """
    # create match_entries
    match_entries = list()

    # checking for matches in birthday list and adding matches to match_entries
    for i in range(len(birthday_book.birthday_list)):
        if (name_search.casefold() == birthday_book.birthday_list[i][0].casefold()
                or name_search.casefold() == birthday_book.birthday_list[i][1].casefold()):
            match_entries.append(birthday_book.birthday_list[i])

    # printing out the matches
    if len(match_entries) != 0:
        print(f'Entries with a name of "{name_search}"')
        for bd in match_entries:
            print(f'   {format_birthday(bd)}')

    # case where there are no matches
    else:
        print(
            f'I\'m sorry, but there are no entries with a name of "{name_search}".')


def save_bday(filename, birthday_book):
    """
    This functions takes in a file name input and the birthday
    book class and saves the current list of birthdays to
    a file which the user has named.
        Input: file name
        Output: saves (writes) the list of birthdays in the .txt
                file
    """
    # initializing output_text
    output_text = ''

    # saving each birthday into a string
    for i in range(len(birthday_book.birthday_list)):
        output_text = output_text + \
            format_birthday(birthday_book.birthday_list[i]) + "\n"

    # re-formatted the output_text
    output_text = output_text.replace(",", " ")
    output_text = output_text.replace("/", " ")

    # creating a program file identifier
    program_file_identifier = 'j329lee bday file\n'

    # writing into text file
    with open(filename, "w") as outfile:
        outfile.write(program_file_identifier)
        outfile.write(output_text)

    print(f'Saved birthdays to "{filename}".')


def load_bday(filename, birthday_book):
    """
    This functions takes in a file name and birthday 
    book class and checks if the file was saved by 
    this program and it loads birthdays in that file 
    to the current birthday list.
        Input: file name and the birthday book class
        Output: adds birthdays to current list
    """
    try:
        # reading the text file
        with open(filename, "r") as read_file:

            line = read_file.readline().strip()

            # checking for program file identifier
            if (line != 'j329lee bday file'):
                print(
                    f"I'm sorry, but \"{filename}\" is not in the correct")
                print(
                    "format. You can only load files saved by this same program.")
            else:
                # adding brithdays from text file to list
                line = read_file.readline().strip()
                while (line != ""):
                    bday = line.split()
                    birthday_book.birthday_list.append(bday)
                    line = read_file.readline().strip()

        print(f'Birthdays in "{filename}" added to birthday book.')

    # in case the inputed file does not exist
    except FileNotFoundError:
        print(f"I'm sorry, but \"{filename}\" does not exist.")


def main():
    """The main function of the Birthday Book program."""

    print("Welcome to the Birthday Book Manager")

    # declaring the quit and echo variables
    is_quit = False
    is_echo = False

    # creating the birthday book class and adding list to birthday list
    birthday_book = BirthdayBook()
    birthday_book.birthday_list = list()

    # running while loop so the code is continuous until user quits
    while (is_quit == False):

        # taking in user input
        user_input = input("> ")

        # echoing the user input
        if (is_echo == True):
            print(f'You entered: "{user_input}"')

        user_input = user_input.strip()

        # getting which command the user as entered
        user_command = get_user_command(user_input)

        # case when user inputs "add" function
        if (user_command == "add"):
            user_input = user_input.split()
            user_input.pop(0)
            # checking if user inputted correct number of inputs
            if (len(user_input) != 5):
                print_error_messsage()
            else:
                # adding birthday to birthday book
                add_bday_to_book(user_input, birthday_book)

        # case when user inputs "list" function
        elif (user_command == "list"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 1):
                print_error_messsage()
            # checking if the list is empty
            elif (len(birthday_book.birthday_list) == 0):
                print("The birthday book is empty.")
            else:
                # printing the list when there is no errors
                print_list(birthday_book)

        # case when user inputs "delete" function
        elif (user_command == "delete"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 2):
                print_error_messsage()
            else:
                # declaring the delete_number variable
                delete_number = user_input[1]
                check_delete_num(delete_number, birthday_book)

        # case when user inputs "search" function
        elif (user_command == "search"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 2):
                print_error_messsage()
            else:
                # declaring the name_search variable
                name_search = user_input[1]

                search_bday(name_search, birthday_book)

        # case when user inputs "save" function
        elif (user_command == "save"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 2):
                print_error_messsage()
            else:
                # declaring the filename variable
                filename = user_input[1]

                save_bday(filename, birthday_book)

        # case when user inputs "load" function
        elif (user_command == "load"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 2):
                print_error_messsage()
            else:
                # declaring the filename variable
                filename = user_input[1]

                load_bday(filename, birthday_book)

        # case when user inputs "help" function
        elif (user_command == "help"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 1):
                print_error_messsage()
            else:
                # print the help message
                print_help()

        # case when user inputs "echo on" function
        elif (user_command == "on"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 2):
                print_error_messsage()
            else:
                # declare is_echo variable as True
                is_echo = True
                print("Echo turned on.")

        # case when user inputs "echo on" function
        elif (user_command == "off"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 2):
                print_error_messsage()
            else:
                # declare is_echo variable as False
                is_echo = False
                print("Echo turned off.")

        # case when user inputs "quit" function
        elif (user_command == "quit"):
            user_input = user_input.split()
            # checking if user inputted correct number of inputs
            if (len(user_input) != 1):
                print_error_messsage()
            else:
                # declare is_quit variable as True
                is_quit = True
        # case when user doesn't input a valid function
        else:
            print_error_messsage()


# Do not modify the code below.  Write all of your code above.
if __name__ == "__main__":
    main()
