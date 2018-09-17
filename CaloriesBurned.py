# Running on a treadmill you burn 4.2 calories per minute.
# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25 and 30 minutes.

cal_minute = 4.2

for minutes in range(10, 31, 5):
    cal_burned = (minutes / 1) * cal_minute
    print("You burned " + str(cal_burned) + "in " + str(minutes))
