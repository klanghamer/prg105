"""
Write a program that uses the numbers.txt file, which contains a series of integers.
Your program will calculate the average of all of the numbers stored in the file and display
the total on the screen. Format to show a maximum of two numbers to the right of the decimal point.
"""


def main():
    input_file = open("numbers.txt", "r")
    total = 0
    num_lines = 0
    line = input_file.readline()

    while line != "":
        num_lines += 1
        total += int(line)
        line = input_file.readline()

    average = total / num_lines

    print("There were " + str(num_lines) + " numbers")
    print("The total of all numbers was: " + format(total, ","))
    print("The average of the numbers was: " + format(average, ",.2f"))

    input_file.close()


main()
