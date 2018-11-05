import employee

"""

 Once you have written the classes, write a program that creates an object of the
 ProductionWorker class and prompts the user to enter data for each of the object’s 
 data attributes. Store the data in the object and then use the object’s accessor methods 
 to retrieve it and display it on the screen.
 
 
 em_name, em_num, shift_num, hourly_rate
 
"""


def main():

    name = input("Enter Employee Name: ")
    num = int(input("Enter Employee Number: "))
    hourly = float(input("Enter Hourly Pay Rate: "))
    shift = int(input("Enter Shift Number: "))

    if shift == 1:
        shift = 'Day'
    else:
        shift = 'Night'

    main_info = employee.Employee(name, num)
    shift_info = employee.ProductionWorker(name, num, shift, hourly)

    print("")
    print("--------------------------")
    print("Details of Employee:")
    print("--------------------------")
    print("Name:", main_info.get_em_name())
    print("Employee Number:", main_info.get_em_num())
    print("Pay Rate:", shift_info.get_hourly_rate())
    print("Shift Number:", shift_info.get_shift_num())

main()
