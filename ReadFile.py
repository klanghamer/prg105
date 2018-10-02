"""
Your Python file will:

Read and Display the list of names from the file
Display the number of names that are read from the file
(You will need a variable to keep a count of the number of items read from the file.)
"""


def main():
    count = 0
    names_list = open("names.txt", "r")

    record = names_list.readline()
    record = record.rstrip('\n')

    while record != "":
        print(record)
        record = names_list.readline()
        record = record.strip('\n')

    with open("names.txt", "r") as f:
        for line in f:
            print(line)
            count += 1
    print("There are " + str(count) + " names in this file.")

    names_list.close()


main()
