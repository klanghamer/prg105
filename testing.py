import tkinter
import tkinter.messagebox
import pickle


class MainMenu:
    def __init__(self, master, input_file):
        self.master = master
        self.master.title('Create Your Character')
        self.radio_var = 0
        self.input_file = input_file

        # colors
        # self.master.configure(background='#0d0d0d')

        self.upper_frame = tkinter.Frame(self.master)
        self.top_frame = tkinter.Frame(self.master)
        self.side_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.title_label = tkinter.Label(self.upper_frame, text='Please choose your Race: ')

        self.title_label.pack(side='left')

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.human = tkinter.Radiobutton(self.top_frame, text='Human: +2 STR, +2 DEX',
                                         variable=self.radio_var, value=1)
        self.half_orc = tkinter.Radiobutton(self.top_frame, text='Half-Orc: +2 DEX, +2 CON',
                                            variable=self.radio_var, value=2)
        self.sun_elf = tkinter.Radiobutton(self.top_frame, text='Sun Elf: +2 INT, +2 CHA',
                                           variable=self.radio_var, value=3)
        self.drow = tkinter.Radiobutton(self.top_frame, text='Drow: +2 DEX, +2 WIS',
                                        variable=self.radio_var, value=4)
        self.tiefling = tkinter.Radiobutton(self.top_frame, text='Tiefling: +2 CHA, +2 INT',
                                            variable=self.radio_var, value=5)
        self.dwarf = tkinter.Radiobutton(self.top_frame, text='Dwarf: +2 CON, +2 WIS',
                                         variable=self.radio_var, value=6)
        self.wood_elf = tkinter.Radiobutton(self.top_frame, text='Wood Elf: +2 DEX, +2 INT',
                                            variable=self.radio_var, value=7)

        # pack the radio buttons
        self.human.pack(anchor='w', padx=20)
        self.half_orc.pack(anchor='w', padx=20)
        self.sun_elf.pack(anchor='w', padx=20)
        self.drow.pack(anchor='w', padx=20)
        self.tiefling.pack(anchor='w', padx=20)
        self.dwarf.pack(anchor='w', padx=20)
        self.wood_elf.pack(anchor='w', padx=20)

        self.str = tkinter.Radiobutton(self.side_frame, text='STR', variable=self.radio_var, value=1)
        self.dex = tkinter.Radiobutton(self.side_frame, text='DEX', variable=self.radio_var, value=2)
        self.con = tkinter.Radiobutton(self.side_frame, text='CON', variable=self.radio_var, value=3)
        self.int = tkinter.Radiobutton(self.side_frame, text='INT', variable=self.radio_var, value=4)
        self.wis = tkinter.Radiobutton(self.side_frame, text='WIS', variable=self.radio_var, value=5)
        self.cha = tkinter.Radiobutton(self.side_frame, text='CHA', variable=self.radio_var, value=6)

        self.str.pack(anchor='w', padx=20)
        self.dex.pack(anchor='w', padx=20)
        self.con.pack(anchor='w', padx=20)
        self.int.pack(anchor='w', padx=20)
        self.wis.pack(anchor='w', padx=20)
        self.cha.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='Next', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.upper_frame.pack()
        self.top_frame.pack(side='left')
        self.side_frame.pack(side='left')
        self.bottom_frame.pack(side='bottom')

    def open_menu(self):
        if self.radio_var.get() == 1:
            tkinter.messagebox.showinfo('Stats', 'still under construction')
        else:
            tkinter.messagebox.showinfo('Stats', 'still under construction')


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


def main():
    input_file = 'charlog.dat'
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    menu_gui = MainMenu(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
