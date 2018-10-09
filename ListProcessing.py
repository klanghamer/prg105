"""

Have a function that creates a list of 20 random integers between 1 and 100
(Assign them dynamically, store the list in a variable.)

Have a function get a number from the user that is between 1 and 100
(validate to ensure a number between 1 and 100 was entered instead of text or
something out of range using a try and except statement).

Pass both the list and the user's number to a function and have it display all numbers
in the list that is greater than the user's number. If there are not any, display a message
that explains there are no numbers in the list greater than the entered number.

"""

import random


def main():
    random_numbers = generate_random()
    user_num = get_info()
    display(random_numbers, user_num)  # Display, not print.


def get_info():
    user_number = -1  # helps validate the catch
    while 100 < user_number or 0 > user_number:  # forces the program to keep asking for a number
        user_number = float(input("Please enter a number between 1 and 100: "))
        if user_number >= 100 or user_number < 0:  # How to check to validate a correct number
            print("That number is not in the valid range.")
    return user_number


def generate_random():
    random_integers = []
    for num in range(1, 20):
        my_random = random.randint(0, 100)  # To import the random numbers
        random_integers.append(my_random)
        return random_integers


def display(num_list, input_num):
    found = False  # How to check/validate
    for number in num_list:
        if number > input_num:
            found = True
            print(number)
    if not found:
        print("There were no matches found.")


main()
