"""
Write a program that asks the user to enter the monthly costs for the following expenses incurred
from operating his or her automobile: loan payment, insurance, gas, and maintenance. The program
 should then display the total monthly cost of these expenses, and the total annual cost of these expenses.
"""


def main():
    monthly_total = monthly()
    print("You spend $" + format(monthly_total, ",.2f") + " on your car each month")
    yearly_total = yearly(monthly_total)  # monthly_total has to be here and in yearly function
    print("You spend $" + format(yearly_total, ",.2f") + " per year on your car.")


def monthly():
    loan_monthly = float(input("How much do you pay for your car loan each month?: "))
    insurance_monthly = float(input("How much do you pay for your car insurance each month?: "))
    gas_monthly = float(input("How much do you spend on gas each month?: "))
    ma_monthly = float(input("What is the average amount you spend on maintenance monthly?: "))
    monthly_total = loan_monthly + insurance_monthly + gas_monthly + ma_monthly  # cannot format str, do not use
    return monthly_total


def yearly(monthly_total):
    yearly_total = monthly_total * 12
    return yearly_total


main()
