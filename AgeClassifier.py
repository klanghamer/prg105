"""Write a program that asks the user to enter a person's age.
The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.

Follow these guidelines:

If the person is 1 year old or less, he or she is an infant.
If the person is older than 1 year but younger than 13 years, he or she is a child.
If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
If the person is at least 20 years old, he or she is an adult.
"""

age = int(input("Enter a person's age: "))

if age < 1:
    print("He or she is an infant.")
elif age < 13:
    print("He or she is a child.")
elif age < 20:
    print("He or she is a teenager.")
else:
    print("He or she is an adult.")
