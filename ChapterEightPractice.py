"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
# Print all the characters from the name variable by accessing one character at a time

name = "John Jacob Jingleheimer Schmidt"
for ch in name:
    print(ch)

# Use the index to access and print the capital s in Schmidt from the variable name

print()

name = "John Jacob Jingleheimer Schmidt"
print(name[24])

print()

# Use the index with negative numbers to print the letters from the last name "Schmidt" in the
# name variable

print(name[-7], name[-6], name[-5], name[-4], name[-3], name[-2], name[-1])

# TODO 8.2 String slicing
# use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""

middle = name[5:10]
print(middle)

# TODO 8.3 Testing, Searching, and manipulating strings
# test to see if the string "Jacob" is in name
if 'Jacob' in name:
    print("Yes, Jacob is in the string.")
else:
    print("No, Jacob is not in the string.")

# test to see if the string "Michael" is in name

if 'Michael' in name:
    print("Yes, Michael is in the string.")
else:
    print("No, Michael is not in the string.")

# Test to see if name is a number

if name.isdigit():
    print(name + " is a number")
else:
    print(name + " is not a number.")

# Test to see if number is a number

number = "42"

if number.isdigit():
    print(number + " is a number.")
else:
    print(number + " is not a number.")

# Search for "J" in name, replace with "j" (lower case)

new_name = name.replace('J', 'j')
print(new_name)

# split the string name into the variable name_list, replace the ""

name_list = name.split()
print(name_list)
