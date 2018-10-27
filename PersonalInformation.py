"""

Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate
accessor and mutator methods (get and set). Write a program that creates three instances of the class. One
instance should hold your information and the other two should hold your friends or family members' information.
Just add information, don't get it from the user.  Print the data from each object, make sure to format the
output for clarity and ease of reading.

"""


class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


def main():
    me = Person("Kate", "566 Somerset Ln", "26", "847-354-1108")
    trent = Person("Trent", "157 Bristol Ave", "24", "815-354-6457")
    nika = Person("Nika", "8408 Russell St", "8", "847-354-1150")

    print("--------------------")
    print(me.get_name())
    print(me.get_address())
    print(me.get_age())
    print(me.get_phone())

    print("--------------------")
    print(trent.get_name())
    print(trent.get_address())
    print(trent.get_age())
    print(trent.get_phone())

    print("--------------------")
    print(nika.get_name())
    print(nika.get_address())
    print(nika.get_age())
    print(nika.get_phone())


main()
