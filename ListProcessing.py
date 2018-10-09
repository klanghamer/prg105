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
    random_integers = []

    for num in range[1,20]:
        random_int = random
        random_integers.append(random_integers)
        user_num = float(input("Please enter a number between 1 and 100: "))

    print(random_integers, user_num)

# I'm completely lost on how to set this up. 

main()
