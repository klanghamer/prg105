import tkinter
import tkinter.messagebox
import human


class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.upper_frame = tkinter.Frame(self.master)
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        # Top Image ----------------------------------------------------
        self.canvas = tkinter.Canvas(self.master, width=400, height=125)
        self.pop = tkinter.Canvas(self.master)
        topimage = tkinter.PhotoImage(file='neverwinter.png')

        self.canvas.create_image(200, 75, image=topimage)
        self.canvas.pack()

        # Title / Directions ----------------------------------------------------

        self.title_label = tkinter.Label(self.upper_frame, text='Welcome Adventurer!\n Please choose your race. ')
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
        self.wood_elf = tkinter.Radiobutton(self.top_frame, text='Wood Elf: +2 DEX, +2 INT',
                                            variable=self.radio_var, value=7)

        self.human.pack(anchor='w', padx=20)
        self.half_orc.pack(anchor='w', padx=20)
        self.sun_elf.pack(anchor='w', padx=20)
        self.drow.pack(anchor='w', padx=20)
        self.tiefling.pack(anchor='w', padx=20)
        self.dwarf.pack(anchor='w', padx=20)
        self.wood_elf.pack(anchor='w', padx=20)

        # Okay / Quit Buttons ----------------------------------------------------
        self.ok_button = tkinter.Button(self.bottom_frame, text='Next', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.master.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack Frames ----------------------------------------------------
        self.upper_frame.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            human.Human(self.master)
        else:
            tkinter.messagebox.showinfo('Stats', 'still under construction')


def main():
    root = tkinter.Tk()
    MainMenu(root)
    root.mainloop()


main()
