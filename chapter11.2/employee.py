"""

Write an Employee class that keeps data attributes for the following pieces of information:

Employee name
Employee number
Next, Write a class named ProductionWorker that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the following information

Shift numbered (an integer, such as 1, 2, or 3)
Hourly pay rate
The workday is divided into two shifts: day and night.
The shift attribute will hold an integer value representing the shift that the employee works.
The day shift is shift 1 and the night shift is shift 2.
Write the appropriate accessor and mutator methods (get and set) for each class.

"""


class Employee:

    def __init__(self, em_name, em_num):
        self.__em_name = em_name
        self.__em_num = em_num

    def set_em_name(self, em_name):
        self.__em_name = em_name

    def set_em_num(self, em_num):
        self.__em_num = em_num

    def get_em_name(self):
        return self.__em_name

    def get_em_num(self):
        return self.__em_num


class ProductionWorker(Employee):
    def __init__(self, em_name, em_num, shift_num, hourly_rate):
        Employee.__init__(self, em_name, em_num)
        self.__shift_num = shift_num
        self.__hourly_rate = hourly_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_rate(self):
        return self.__hourly_rate
