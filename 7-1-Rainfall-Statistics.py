"""

Copy program 4.3 into the chapter 7 folder and rename it as "7-1-Rainfall-Statistics"

Modify the program so that the rainfall for each month is stored into a list.
Eliminate the user's ability to select the number of years, you will just work with one year's data.
The program should calculate and display the total rainfall for the year, the average monthly rainfall
the year, and the months with the highest and lowest amounts of rain for the year. Hint: convert months
to a list so you can use the index value to print the max and min months.

"""


def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    rainfall = []
    total_months = 0
    total_rain = 0

    for month in months:
        inches = float(input("Enter inches that fell in " + month + " : "))
        rainfall.append(inches)
        total_months += 1
        total_rain += inches

    for item in rainfall:
        total_rain += item
    average_rain = total_rain / total_months
    minimum = min(rainfall)
    maximum = max(rainfall)
    month_min = rainfall.index(minimum)
    month_max = rainfall.index(maximum)

    print("The month of " + months[month_min] + " had the least amount of rain with " + format(min(rainfall), ",.2f") +
          " inches of rain.")
    print("The month of " + months[month_max] + " had the most amount of rain with " + format(max(rainfall), ",.2f") +
          " inches of rain.")
    print("The total amount of rainfall was: " + format(total_rain, ".2f") + " inches.")
    print("Average monthly rainfall was: " + format(average_rain, ".2f") + " inches.")


main()
