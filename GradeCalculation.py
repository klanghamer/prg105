"""
Write a program that asks a user to enter five test scores.
You will need to create five variables to hold these scores.

The purpose of this assignment is to get practice passing information
between functions, this is not a good example of the way programs are really
written, but it will help you to understand how to pass parameters.
"""


def main():
    score1 = float(input("What is your first test score?: "))
    score2 = float(input("What is your second test score?: "))
    score3 = float(input("What is your third test score?: "))
    score4 = float(input("What is your fourth test score?: "))
    score5 = float(input("What is your fifth test score?: "))
    average = calc_average(score1, score2, score3, score4, score5)
    determine_grade(average)  # Have to add average here in order to pass it down
    print("Your average score is a " + str(average))
    print("Your average letter grade is " + determine_grade(average))  # How to print the letter


def calc_average(score1, score2, score3, score4, score5):
    average = int(score1 + score2 + score3 + score4 + score5) / 5  # calculate the average
    return average


def determine_grade(average):
    if average < 60:
        return 'F'
    elif average < 70:
        return 'D'
    elif average < 80:
        return 'C'
    elif average < 90:
        return 'B'
    elif average < 101:
        return 'A'


main()
