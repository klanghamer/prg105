"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""


# TODO 11.1 Introduction to Inheritance
# You are going to create a Dwelling class based on the Automobile
# Sample from the chapter

class Dwelling:

    def __init__(self, number_of_rooms, square_feet, floors):
        self.__number_of_rooms = number_of_rooms
        self.__square_feet = square_feet
        self.__floors = floors

    # add the mutators for all of the data attributes (number_of_rooms, square_feet, floors)

    def set_number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self.__square_feet = square_feet

    def set_floors(self, floors):
        self.__floors = floors

    # add the accessors for all of  the data attributes

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    def get_square_feet(self):
        return self.__square_feet

    def get_floors(self):
        return self.__floors


# Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# call the superclass of Dwelling and pass the required arguments, remember to include self
# initialize the garage_type and yard_size attributes
# create the mutator and accessor methods for the garage_type and yard_size attributes

class SingleFamilyHome(Dwelling):

    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        self.__garage_type = garage_type
        self.__yard_size = yard_size

    def set_garage_type(self, garage_type):
        self.__garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.__yard_size = yard_size

    def get_garage_type(self):
        return self.__garage_type

    def get_yard_size(self):
        return self.__yard_size


# demonstrate the Single_family_home class, no need to import because you are in the same file

# create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
# Display the data using the accessor methods
# create the main function
#  call the main function

def main():
    house = SingleFamilyHome("6", "1,200sqft", "1 Story", "Single Car Garage", ".25 Acres")
    print("Rooms: " + house.get_number_of_rooms())
    print("Square Footage: " + house.get_square_feet())
    print("Stories: " + house.get_floors())
    print("Garage Size: " + house.get_garage_type())
    print("Acreage: " + house.get_yard_size())


main()


# TODO 11.2 Polymorphism
# Type in the mammal class from program 11-9    lines 1 - 22

class Mammal:

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print("I am a " + self.__species)

    def make_sound(self):
        print("Grrrr")


# create a Mouse class as a sub class of the mammal class following the Dog example

class Mouse(Mammal):

    def __init__(self):
        Mammal.__init__(self, "Mouse")

    def make_sound(self):
        print("Squeak, squeak")


class Bird(Mammal):

    def __init__(self):
        Mammal.__init__(self, "Bird")

    def make_sound(self):
        print("Chirp, Chirp")


# create a Bird class as a sub class of the mammal class following the Cat Example


# Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Bird class that you created

def main2():
    mouse = Mouse()
    mouse.show_species()
    mouse.make_sound()

    bird = Bird()
    bird.show_species()
    bird.make_sound()


main2()
