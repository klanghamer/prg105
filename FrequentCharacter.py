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

# this is a mess.

def main():
    user_string = input("Enter a phrase: ")
    common_letters = " "
    new_string = user_string.split()
    old_count = 0

    for char in range(len(new_string)):
        count = 0
        length = len(new_string)
        alpha = 0
        character = new_string[char]
        while length > 0:
            if character == new_string[alpha]:
                count += 1
            alpha += 1
            length -= 1
            if old_count <= count:
                old_count = count
                common_letters = character
    total = str(common_letters)
    print("The most common letter is: " + total.upper())


main()
