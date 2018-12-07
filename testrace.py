import tkinter
import tkinter.messagebox

"""
class Human:
    def __init__(self, master, input_file):
        self.master = master
        self.input_file = input_file
        self.human = tkinter.Toplevel(master)
        self.human.title('Race - Human')
        self.top_frame = tkinter.Frame(self.human)
        self.middle_frame = tkinter.Frame(self.human)
        self.bottom_frame = tkinter.Frame(self.human)

        self.human_label = tkinter.Label(self.top_frame, text='Enter customers name: ')
        self.human_entry = tkinter.Entry(self.top_frame, width=15)
        self.human_label2 = tkinter.Label(self.top_frame, text='Enter customers email: ')
        self.human_entry2 = tkinter.Entry(self.top_frame, width=15)

        self.human_label.pack(side='left')
        self.human_entry.pack(side='left')
        self.human_label2.pack(side='left')
        self.human_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.human_button = tkinter.Button(self.bottom_frame, text='Add', command=self.human_value)  # shadow error
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.human_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def human_value(self):  # Don't let shadow error happen
        try:
            charlog_file = open(self.input_file, 'rb')
            charlog = pickle.load(charlog_file)
            charlog_file.close()
        except FileNotFoundError:
            charlog = {}

        name = self.human_entry.get()
        email = self.human_entry2.get()
        charlog[email] = name

        result = charlog.get(name, 'Customer info added.')
        self.value.set(result)

        file = open("charlog.dat", 'wb')
        pickle.dump(charlog, file)
        file.close()

    def back(self):
        self.human.destroy()

"""


class Human:
    def __init__(self):
        # self.master = master
        self.human = tkinter.Tk()
        # Toplevel(master)
        self.human.title('Race, Human')
        self.top_frame = tkinter.Frame(self.human)
        self.left_frame = tkinter.Frame(self.human)
        self.right_frame = tkinter.Frame(self.human)
        self.bottom_frame = tkinter.Frame(self.human)

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.top_frame, text='stuff here')
        self.top_label = tkinter.Label(self.top_frame, textvariable=self.value)
        self.info.pack(side='left')
        self.top_label.pack(side='left')

        self.value2 = tkinter.StringVar()
        self.info2 = tkinter.Label(self.top_frame, text='picture here')
        self.top_label2 = tkinter.Label(self.top_frame, textvariable=self.value2)
        self.info2.pack(side='left')
        self.top_label2.pack(side='left')

        """ self.stats_section = tkinter.Label(self.left_frame, 'Stats Here')
        self.picture_section = tkinter.Label(self.right_frame, 'Picture Here')
        self.stats_section.pack(side='left')
        self.right_frame.pack(side='left') """

        self.roll_button = tkinter.Button(self.bottom_frame, text='Roll', command=self.back)
        self.gen_button = tkinter.Button(self.bottom_frame, text='Generate', command=self.back)
        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.back)

        self.roll_button.pack(side='left')
        self.gen_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.left_frame.pack()
        self.right_frame.pack()
        self.bottom_frame.pack()
        self.human.mainloop()

    def back(self):
        self.human.destroy()


def main():
    input_file = 'charlog.dat'
    # create a window
    # root = tkinter.Tk()
    # call the GUI and send it the root menu
    menu_gui = Human()
    # control the mainloop from main instead of the class
    # root.mainloop()


main()
