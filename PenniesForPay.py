# Write a program that calculates the amount of money a person would earn over a period of time
# if his or her salary is one penny the first day, two pennies the second day, and continues to
# double each day. The program should ask the user for the number of days. Display a table showing
# what the salary was for each day, and then show the total pay at the end of the period. The output
# should be displayed in a dollar amount, not the number of pennies.

# Hint: use Range, set the field size in formatting.

days_worked = int(input("Enter how many days did you work: "))
money = .01
pennies = 0

print("Days Worked | Amount Earned That Day")
print("------------------------------------")

for day in range(days_worked):
    money = 2 * money
    pennies += money
    print(format(day, "20,.0f") + " | $ " + format(money, "20,.2f"))

total = pennies * .01

print("\nTotal Earned over", str(days_worked), "is: $", format(money, ',.2f'))
