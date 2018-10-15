"""
Write a program that gets a string from the user containing a person's first, middle,
and last names and then displays their first, middle, and last initials.
(Creating a new variable and concatenating each letter plus a '.' is the easiest way to do this.)
"""


def main():
    name = input("Please enter your name in the format, First Middle Last: ")
    initials = name.split()

    first = initials[0][0]  # creating variable for each name
    middle = initials[1][0]  # how to pick the first letter in each variable
    last = initials[2][0]

    print(first.upper() + ". " + middle.upper() + ". " + last.upper() + ".")  # .upper() to change to uppercase


main()
