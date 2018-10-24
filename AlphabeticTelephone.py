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
    digits = ["0", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6",
              "7", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "9", "-"]

    alpha = ["0", "1", "2", "A", "B", "C", "3", "D", "E", "F", "4", "G", "H", "I", "5", "J", "K", "L", "6", "M", "N",
             "O", "7", "P", "Q", "R", "S", "8", "T", "U", "V", "9", "W", "X", "Y", "Z", "-"]

    phone_num = input("Please enter the phone number (1-800-get-food) that you want to convert to numbers: ")

    translated_phone = ""

    # This is supposed to make the lines not skip but I can't figure out why I can't get it to work
    for num in phone_num:
        for item in range(0, len(alpha)):
            if num.isalpha():  # How to recognize the letters within the input
                num = num.upper()  # Print the numeric numbers and convert to alphabetic
            if num == alpha[item]:
                translated_phone = translated_phone + digits[item]

    print(translated_phone)


main()
