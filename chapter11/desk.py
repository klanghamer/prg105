import office


def main():

    cedar = office.Desk("Cedar Desk", "8ft", "5ft", "3ft", "$250.00", "left", "3")
    spruce = office.Desk("Spruce Desk", "10ft", "4ft", "3.5ft", "$1,500.00", "both", "6")
    oak = office.Desk("Oak Desk", "5ft", "3ft", "3ft", "$450.00", "right", "2")

    print("Item:", cedar.get_material())
    print("Dimensions:", cedar.get_length() + "x", cedar.get_width(), "x", cedar.get_height())
    print("Drawers:", cedar.get_number_drawers(), "drawers located on the", cedar.get_location_of_drawers(), "side.")
    print("Price:", cedar.get_price())
    print("------------------------------")

    print("Item:", spruce.get_material())
    print("Dimensions:", spruce.get_length(), "x", spruce.get_width(), "x", spruce.get_height())
    print("Drawers:", spruce.get_number_drawers(), "drawers located on", spruce.get_location_of_drawers(), "sides.")
    print("Price:", spruce.get_price())
    print("------------------------------")

    print("Item:", oak.get_material())
    print("Dimensions:", oak.get_length(), "x", oak.get_width(), "x", oak.get_height())
    print("Drawers:", oak.get_number_drawers(), "drawers located on the", oak.get_location_of_drawers(), "side.")
    print("Price:", spruce.get_price())
    print("-----------------------------")


main()
