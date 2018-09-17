# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years. The outer loop will iterate once for each year. The inner
# loop will iterate 12 times, once for each month. Each iteration of the inner loop will ask the user for the inches
# of rainfall for that month. After all iterations, the program should display the number of months, the total inches
# of rainfall, and the average rainfall per month for the entire period.


print("This program will calculate total rainfall and average monthly rainfall for a period of years.")
years = int(input("How many years would you like to collect data for? "))
total_months = 0
total_rain = 0

for current_year in range(years):
    print("Year number " + str(current_year + 1))
    for current_month in ['January', 'February', 'March', "April", 'May', 'June', 'July', 'August',
                          'September', 'October', 'November', 'December']:
        monthly_rainfall = float(input("How much rain fell in the month of " + str(current_month) + ": "))
        total_months += 1
        total_rain += monthly_rainfall

average_rain = total_rain / total_months
print("Total amount of rainfall was: " + format(total_rain, ".2f") + " inches.")
print("Average monthly rainfall was: " + format(average_rain, ".2f") + " inches.")
