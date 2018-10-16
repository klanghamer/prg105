"""
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for
their customers to remember. On a standard telephone the alphabetic letters are mapped
to numbers in the following fashion:

A, B, C = 2

D, E, F = 3

G, H, I = 4

J, K, L = 5

M, N, O = 6

P, Q, R, S = 7

T,U, V, = 8

W, X, Y, Z = 9

Write a program that asks the user to enter a 10-character telephone
number in the format XXX-XXX-XXXX. The application should display the telephone number
with any alphabetic characters that appeared in the original translated to their numeric equivalent.


Hint: Create a variable to hold the converted phone number and concatenate one number at a time on to the end of it.

Suggestion: Try using Parallel Lists (see optional references).
"""


def main():
    digits = ("1", "2", "2", "2", "3", "3", "3", "4", "4", "4", "5", "5", "5", "6", "6", "6", "7", "7", "7", "7",
              "8", "8", "8", "9", "9", "9", "9", "-")

    alpha = ("1", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z", "-")

    phone_num = input("Please enter the phone number (1-800-get-food) that you want to convert to numbers: ")

    num = 0  # This is supposed to make the lines not skip but I can't figure out why I can't get it to work
    for num in range(len(phone_num)):
        if phone_num[num].isalpha():  # How to recognize the letters within the input
            print(digits[alpha.index(phone_num[num])])  # Print the numeric numbers and convert to alphabetic
        else:
            print(phone_num[num])  # Prints statement with numbers if no alphabetic is input


main()
