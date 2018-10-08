"""

Write a program that reads the contents of the two files into two separate lists.
The user should be able to enter a boy's name or a girl's name. The application should
check both lists, and then display messages indicating whether the names were among the
 most popular if the name was on one of the lists or that the name was not on the lists of popular names.

"""


def main():
    girls = []
    boys = []

    girl_file = open('GirlNames.txt', 'r')
    boy_file = open('BoyNames.txt', 'r')

    for girl in girl_file:    # Shadow Errors, do not use 'girls' as it goes to the open file.
        the_girl = girl.strip('\n')   # Use from for loop for strip
        girls.append(the_girl)   # applies to shadow error, use different variable

    for boy in boy_file:    # Remember Shadow Error rule ^
        the_boy = boy.strip('\n')   # Use from for loop for strip
        boys.append(the_boy)   # applies to shadow error, use different variable

    girl_file.close()
    boy_file.close()

    name = input("Please enter a name: ")

    if name in boys:
        print(name + " was one of the most popular boys names.")
    elif name in girls:
        print(name + " was one of the most popular girls names.")
    else:
        print(name + " was not a popular name.")


main()
