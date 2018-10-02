"""
Copy your file from the previous exercise (Average numbers) and modify it so that it handles the following exceptions:

It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
It should handle any ValueError exceptions that are raised when the items that are read from the file
are converted to a number.

NOTE:

You can test for IOErrors by temporarily changing the name of your data file.
You can test for ValueErrors by using this data file: numbers2.txtPreview the document
"""


def main():
    count = 0
    total = 0
    record = ""
    filename = ""

    try:
        filename = "numbers.txt"
        input_file = open(filename, "r")
        record = input_file.readline()
        record = int(record.rstrip("\n"))

        while record:
            print(record)
            total += record
            count += 1
            record = input_file.readline()
            record = record.rstrip("\n")
            record = int(record)

        input_file.close()
        print("There were " + str(total) + " numbers.")
        print("The total of all numbers was: " + str(count))
        print("The average of the numbers was: " + format(total / count), ",.2f")

    except IOError:
        print("Could not find " + filename)

    except ValueError:
        print("There was non-numeric data in this file.")
        print("Processing of this file has stopped.\n", "\t", record)


main()
