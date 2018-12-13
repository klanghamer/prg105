import tkinter
import tkinter.messagebox
import savedcharacter
import human
import halforc
import sunelf
import drow
import tiefling
import dwarf
import dragonborn


class MainMenu:
    def __init__(self, master, input_file):
        self.master = master
        self.master.title('Welcome Menu')
        self.input_file = input_file
        self.upper_frame = tkinter.Frame(self.master)
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        # Top Image ----------------------------------------------------
        # http://effbot.org/tkinterbook/canvas.htm how to insert images and use label for master window

        self.canvas = tkinter.Canvas(self.master, width=0, height=0)
        self.pop = tkinter.Canvas(self.master)
        topimage = tkinter.PhotoImage(file='neverwinter.png')
        w = tkinter.Label(master, image=topimage)
        w.photo = topimage
        w.pack()
        self.canvas.pack()

        # Title / Directions ----------------------------------------------------

        self.title_label = tkinter.Label(self.upper_frame, text='Welcome Adventurer!\n View Saved characters\n'
                                                                'Or please choose a race.')
        self.title_label.pack(side='left')

        # Radio Options ----------------------------------------------------
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

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
        self.dragonborn = tkinter.Radiobutton(self.top_frame, text='Dragonborn: +2 STR, +2 CON',
                                              variable=self.radio_var, value=7)

        self.human.pack(anchor='w', padx=20)
        self.half_orc.pack(anchor='w', padx=20)
        self.sun_elf.pack(anchor='w', padx=20)
        self.drow.pack(anchor='w', padx=20)
        self.tiefling.pack(anchor='w', padx=20)
        self.dwarf.pack(anchor='w', padx=20)
        self.dragonborn.pack(anchor='w', padx=20)

        # Okay / Quit Buttons ----------------------------------------------------
        # http://www.pythonlake.com/tkinterbuttongrid How to use grid instead of pack

        self.roll_button = tkinter.Button(self.bottom_frame, text='Create', command=self.open_menu)
        self.roll_button.grid(row=1, column=0, padx=20, pady=10)
        self.gen_button = tkinter.Button(self.bottom_frame, text='View Saved', command=self.saved_char)
        self.gen_button.grid(row=1, column=1, padx=20, pady=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.master.destroy)
        self.back_button.grid(row=1, column=2, padx=20, pady=10)

        # Pack Frames ----------------------------------------------------

        self.upper_frame.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            human.Human(self.master, self.input_file)
        elif self.radio_var.get() == 2:
            halforc.HalfOrc(self.master, self.input_file)
        elif self.radio_var.get() == 3:
            sunelf.SunElf(self.master, self.input_file)
        elif self.radio_var.get() == 4:
            drow.Drow(self.master, self.input_file)
        elif self.radio_var.get() == 5:
            tiefling.Tiefling(self.master, self.input_file)
        elif self.radio_var.get() == 6:
            dwarf.Dwarf(self.master, self.input_file)
        else:
            dragonborn.Dragonborn(self.master, self.input_file)

    def saved_char(self):

        savedcharacter.CharSaved(self.master, self.input_file)


def main():
    input_file = 'charlog.dat'
    root = tkinter.Tk()
    MainMenu(root, input_file)
    root.mainloop()


main()
