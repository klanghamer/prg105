"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""


# TODO 6.1 Introduction to File Input and Output
# Assign the variable file_variable to open states.txt in read mode

def main0():
    file_variable = open('states.txt', 'r')

    # Close the file

    file_variable.close()


main0()


# Assign the variable state_capitals to open capitals.txt in write mode.
# Please note, the file does not currently exist, and by opening it in
# write mode you will create it

def main():
    state_capitals = open("capitals.txt", "w")
    state_capitals.write("Illinois, Springfield\n")
    state_capitals.write("Alaska, Juneau\n")
    state_capitals.write("Arizona, Phoenix\n")
    state_capitals.close()


main()


# Write three state capitals to the file
# There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
# sample
#   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol


# close the file


# TODO reading data in from a file
# Assign the variable states_data to open states.txt in read mode

# read in three lines from the file, assign to the variables below, Remove """   """ to test

def main2():
    states_data = open("states.txt", "r")

    line1 = states_data.readline()
    line2 = states_data.readline()
    line3 = states_data.readline()

    states_data.close()

    print(line1)
    print(line2)
    print(line3)


main2()

# close the file

# print the three variables

# TODO 6.2 Using loops to process files
# Complete the program below to read in and count all of the entries in the states file

# open the file in read mode
"""
states_file =
counter = 0
"""


# write a for loop to read in all of the lines, and print them on the screen, add 1 to counter for each line

def main3():
    states_file = open("states.txt", "r")
    counter = 0
    for state in states_file:
        print(state)
        counter += 1
    states_file.close()


main3()

# close the file

# TODO 6.3 Processing records

# You are going to finish the program below to write data to a file
# entering book information
# open the file books.txt for writing remove the """ """ to test
"""books_file = """


# use a for loop to get title and author from the user use the range 1, books + 1
# get the data in the loop
# write the data as a record in the loop, make sure to include the \n at the end of the line
# close the file

def main4():
    books = 3
    books_file = open("books.txt", "w")
    for book in range(1, books + 1):
        author = input("Please enter the author's name: ")
        title = input("Please enter the title of the book: ")
        books_file.write(title + ", " + author + "\n")

    books_file.close()


main4()


# TODO 6.4 Exceptions
# In this exercise you will try to open a file that does not exist, capture the error, and display a custom error message

# create a try statement:
def main5():
    try:
        get_superheros = open("superheros.txt", "r")
        get_superheros.close()

    except IOError:
        print("An Error has occured.\nThis file does not exist.")


main5()

# open the file superheros.txt for reading (we are not writing, it would create the file)
# close the file
# create an except IOError, and a print statement telling the user that the file doesn't exist
