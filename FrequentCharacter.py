"""

Write a program that lets the user enter a string and displays the letter that
appears most frequently in the string. Ignore spaces, punctuation, and uppercase vs lowercase.



Hints:

Create a list to hold letters based on the length of the user input
Convert all letters to the same case
Use a loop to check for each letter in the alphabet (create an alphabet list and step through it)
Have a variable to hold the largest number of times a letter appears, and replace the value
when a higher number is found

"""


def main():
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
             "T", "U", "V", "W", "X", "Y", "Z"]

    user_string = input("Enter a phrase: ")
    common_letters = ""
    maximum = 0
    count = 0

    for char in alpha:
        for letter in user_string:
            if char == letter.upper():
                count += 1

        if count > maximum:
            maximum = count
            common_letters = char
            count = 0
        elif count == maximum:
            common_letters = common_letters + " " + char
            count = 0
        else:
            count = 0

    print("The most common letter is ")
    print(common_letters + " appeared " + str(maximum) + " times.")


main()
