"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import pickle

# TODO 9.1 Dictionaries
# Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14', 'Trent': 'September 10', 'Kelly': 'April 26', 'Nika': 'May 28'}

# 1.Print Meri's Birthday

print(birthdays['Meri'])

# 2.Create an empty dictionary named registration

registration = {}

# 3.You will use the following dictionary for many of the remaining exercises

miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# print the keys and the values of miles_ridden using a for loop

for key in miles_ridden:
    print(key, miles_ridden[key])

# get the value for June 3 and print it, if not found display 'Entry not found', replace the ""

value = "June 3"
print(value)

if value in miles_ridden:
    print("The miles ridden for: " + value + " " + str(miles_ridden[value]))
else:
    print(value + " was not found.")


# get the value for June 6 and print it, if not found display 'Entry not found' replace the ""

value2 = "June 6"
print(value2)

if value2 in miles_ridden:
    print("The miles ridden for: " + value2 + " " + str(miles_ridden[value2]))
else:
    print(value2 + " was not found.")

# Use the items method to print the miles_ridden dictionary

for items in miles_ridden.items():
    print(items)

# Use the keys method to print all of the keys in miles_ridden

for key in miles_ridden.keys():
    print(key)

# Use the pop method to remove june 4 then print the contents of the dictionary

miles_ridden.pop('June 4')
print(miles_ridden.items())

# Use the values method to print the contents of the miles_ridden dictionary

for val in miles_ridden.values():
    print(val)

# TODO 9.2 Sets
# Create an empty set named my_set

my_set = set()

# Create a set named days that contains the days of the week

days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}

# get the number of elements from the days set and print it

print("There were: " + str(len(days)) + " elements in the set.")

# Remove Saturday and Sunday from the days set

days.remove('Saturday')
days.remove('Sunday')
print(days)

# Determine if 'Mon' is in the days set

if 'Mon' in days:
    print("Mon is in this dictionary")

if 'Mon' not in days:
    print("Mon is not in this dictionary")

# TODO 9.3 Serializing Objects (Pickling)

# import the pickle library

# create the output file log and open it for binary writing

output_file = open('miles_ridden.dat', 'wb')

# pickle the miles_ridden dictionary and output it to the log file

pickle.dump(miles_ridden, output_file)

# close the log file

output_file.close()
