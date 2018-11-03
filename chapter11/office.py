"""

 In the first step, you will create a parent class. Create a parent class for Office Furniture.
 Set the class variables to be a category (desk, chair, filing cabinet would be examples), material,
 length, width, height, and price. Include a method that returns a string about the object.

 In the second step create a subclass for Desk that includes location_of_drawers
 (left, right both are options) and number_drawers. Override the parents __str__ method
 to include drawer location and count.

 Implement each class in a separate file. Import these into your main program.
 Your main program should implement and display an instance of each, the parent class and the child class.

"""


class OfficeFurniture:

    def __init__(self, material, length, width, height, price):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price


class Desk(OfficeFurniture):
    def __init__(self, material, length, width, height, price, location_of_drawers, number_drawers):
        OfficeFurniture.__init__(self, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers


def main():

    plastic = OfficeFurniture("Plastic Chair", "16in", "32in", "16in", "$10.00")
    leather = OfficeFurniture("Leather Chair", "31in", "33in", "36in", "$1,000.00")
    floral = OfficeFurniture("Floral Chair", "23in", "31in", "34in", "$250.00")

    print("Item:", plastic.get_material())
    print("Dimensions:", plastic.get_length() + "x", plastic.get_width(), "x", plastic.get_height())
    print("Price:", plastic.get_price())
    print("------------------------------")

    print("Item:", leather.get_material())
    print("Dimensions:", leather.get_length(), "x", leather.get_width(), "x", leather.get_height())
    print("Price:", leather.get_price())
    print("------------------------------")

    print("Item:", floral.get_material())
    print("Dimensions:", floral.get_length(), "x", floral.get_width(), "x", floral.get_height())
    print("Price:", floral.get_price())


main()
