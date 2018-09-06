"""A mobile phone service provider has three different subscription packages for its customers:

Package A:	For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.
Package B:	For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.
Package C:	For $69.99 per month unlimited minutes provided.
Write a program that calculates a customer's monthly bill.
It should ask which package the customer has purchased and how many minutes were used.
It should then display the total amount due. Use a dollar sign and two decimal places for currency.

Use nested ifs for this assignment.
The outer chained if statement should be used to select the package entered.
For packages A and B, an inner if statement will be needed to determine if there is an overage of minutes.
"""

package_selected = input("Which package did you purchase?: ")
minutes_used = 0

if package_selected == "A" or package_selected == "a" or package_selected == "B" or package_selected == "b" \
        or package_selected == "C" or package_selected == "c":
    minutes_used = int(input("How many minutes did you use this month?: "))

if package_selected == 'A' or package_selected == 'a':
    package_cost = 39.99
    if minutes_used > 450:
        price = package_cost + ((minutes_used - 450) * .45)
        print("You owe $" + format(price, ",.2f"))

elif package_selected == 'B' or package_selected == 'b':
    package_cost = 59.99
    if minutes_used > 900:
        price = package_cost + ((minutes_used - 900) * .40)
        print("You owe $" + format(price, ",.2f"))
else:
    print("You owe $0 extra for unlimited minutes.")
