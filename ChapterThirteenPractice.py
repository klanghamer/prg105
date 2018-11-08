"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox


# TODO 13.2 Using the tkinter Module

# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter
#  create the class MyGUI2

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        tkinter.mainloop()


my_gui = MyGUI()


# TODO 13.3 Adding a label widget
# add a label that prints your first and last name

class MyGUI2:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text="Kate Langhamer")
        self.label.pack()
        tkinter.mainloop()


my_gui2 = MyGUI2()


# pack the label

# enter the main loop

# create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
# Create a window in the MyGUI3 class that has two frames
# In the top Frame add a labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester

class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Kate Langhamer, Web Development")
        self.label1.pack(side='top')

        self.label2 = tkinter.Label(self.bottom_frame, text="PRG 105 and WEB 105")
        self.label2.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


my_gui3 = MyGUI3()


# TODO 13.5 Button Widgets and info Dialog Boxes
# Tell a joke with a button to show the punch line, which should appear in a dialog box

class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text="Click Me!", command=self.do_something)
        self.my_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thank you for clicking the button.')


my_gui4 = MyGUI4()


# TODO 13.6 getting input / 13.7 Using Labels as output fields
# Using the program in 13.10 kilo converter as a sample, create a program
# to convert inches to centimeters


class InchesConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in inches: ")
        self.inches_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.inches_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to centimeters: ")
        self.value = tkinter.StringVar()
        self.centimeters_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.descr_label.pack(side='left')
        self.centimeters_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        inches = float(self.inches_entry.get())
        centimeters = inches * 2.54
        self.value.set(centimeters)


inches_conv = InchesConverterGUI()
