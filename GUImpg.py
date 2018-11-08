import tkinter

"""

Write a GUI program that calculates a car’s gas mileage. The program’s
window should have Entry widgets that let the user enter the number of
gallons of gas the car holds, and the number of miles it can be driven
on a full tank. When a Calculate MPG button is clicked, the program should
display the number of miles that the car may be driven per gallon of gas.
Use the following formula to calculate miles per gallon:

MPG = miles / gallons
Make sure you label Entry widgets and results appropriately.

"""


class Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # self.canvas = tkinter.Canvas(self.main_window, width=300, height=200)
        # self.pop = tkinter.Canvas(self.main_window)
        # gif_1 = tkinter.PhotoImage(file='Car.gif')
        # ^ For images

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # self.canvas.create_image(150, 150, image=gif_1)

        self.tank_label = tkinter.Label(self.top_frame, text='Enter how many gallons your car holds: ')
        self.tank_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_label = tkinter.Label(self.top_frame, text='How many miles you traveled: ')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        # self.canvas.pack()
        self.tank_label.pack()
        self.tank_entry.pack()
        self.miles_label.pack()
        self.miles_entry.pack()

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.describe_label = tkinter.Label(self.mid_frame, text='Converted Miles per Gallons: ')

        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.describe_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        tanks = float(self.tank_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles / tanks

        self.value.set(format(mpg, ',.2'))


gui = Gui()
