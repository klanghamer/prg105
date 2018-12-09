import tkinter
import tkinter.messagebox
import random


class Human:
    def __init__(self, master):
        self.master = master
        self.human = tkinter.Toplevel(master)
        self.human.title('Race, Human')
        self.img_frame = tkinter.Frame(self.human)
        self.desc_frame = tkinter.Frame(self.human)
        self.name_frame = tkinter.Frame(self.human)
        self.stat_frame = tkinter.Frame(self.human)
        self.bottom_frame = tkinter.Frame(self.human)
        self.human.grid()

        # Top Image ----------------------------------------------------
        self.canvas = tkinter.Canvas(self.human, width=400, height=125)
        self.pop = tkinter.Canvas(self.human)
        topimage = tkinter.PhotoImage(file='neverwinter.png')

        self.canvas.create_image(200, 75, image=topimage)
        self.canvas.pack()

        # Character Image ----------------------------------------------------
        self.canvas2 = tkinter.Canvas(self.img_frame, width=400, height=150)
        self.pop = tkinter.Canvas(self.img_frame)
        raceimage = tkinter.PhotoImage(file='placeholder.png')

        self.canvas2.create_image(200, 75, image=raceimage)
        self.canvas2.pack()

        # Description ----------------------------------------------------

        self.desc = tkinter.Label(self.desc_frame, text='Hello Adventurer!'
                                                        '\n(+2 STR/+2 DEX)'
                                                        '\nEnter your name and click Roll to see your starter stats. '
                                                        '\nYour race bonus will already be calculated in the roll. '
                                                        '\nRecord your numbers and click generate. '
                                                        '\nClick back to return to the main menu.\n')
        self.desc.grid(row=0, column=0)

        # Add Name ----------------------------------------------------

        self.name_label = tkinter.Label(self.name_frame, text='Name your character: ')
        self.name_entry = tkinter.Entry(self.name_frame, width=15)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        # Stats Area ----------------------------------------------------

        self.randomstr = tkinter.StringVar()
        self.str = tkinter.Label(self.stat_frame, text='STR: ')
        self.str_label = tkinter.Label(self.stat_frame, textvariable=self.randomstr)
        self.str.grid(row=0, column=0)
        self.str_label.grid(row=0, column=1)

        self.randomdex = tkinter.StringVar()
        self.dex = tkinter.Label(self.stat_frame, text='DEX: ')
        self.dex_label = tkinter.Label(self.stat_frame, textvariable=self.randomdex)
        self.dex.grid(row=1, column=0)
        self.dex_label.grid(row=1, column=1)

        self.randomcon = tkinter.StringVar()
        self.con = tkinter.Label(self.stat_frame, text='CON: ')
        self.con_label = tkinter.Label(self.stat_frame, textvariable=self.randomcon)
        self.con.grid(row=2, column=0)
        self.con_label.grid(row=2, column=1)

        self.randomwis = tkinter.StringVar()
        self.wis = tkinter.Label(self.stat_frame, text='WIS: ')
        self.wis_label = tkinter.Label(self.stat_frame, textvariable=self.randomwis)
        self.wis.grid(row=3, column=0)
        self.wis_label.grid(row=3, column=1)

        self.randomint = tkinter.StringVar()
        self.int = tkinter.Label(self.stat_frame, text='INT: ')
        self.int_label = tkinter.Label(self.stat_frame, textvariable=self.randomint)
        self.int.grid(row=4, column=0)
        self.int_label.grid(row=4, column=1)

        self.randomcha = tkinter.StringVar()
        self.cha = tkinter.Label(self.stat_frame, text='CHA: ')
        self.cha_label = tkinter.Label(self.stat_frame, textvariable=self.randomcha)
        self.cha.grid(row=5, column=0)
        self.cha_label.grid(row=5, column=1)

        # Class Chooser ----------------------------------------------------

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.cw = tkinter.Radiobutton(self.stat_frame, text="Control Wizard", variable=self.radio_var, value=1)
        self.dc = tkinter.Radiobutton(self.stat_frame, text="Devoted Cleric", variable=self.radio_var, value=2)
        self.gwf = tkinter.Radiobutton(self.stat_frame, text="Guardian Warrior", variable=self.radio_var,
                                       value=3)
        self.gf = tkinter.Radiobutton(self.stat_frame, text="Guardian Fighter", variable=self.radio_var, value=4)
        self.hr = tkinter.Radiobutton(self.stat_frame, text="Hunter Ranger", variable=self.radio_var, value=5)
        self.op = tkinter.Radiobutton(self.stat_frame, text="Oathbound Paladin", variable=self.radio_var, value=6)
        self.sw = tkinter.Radiobutton(self.stat_frame, text="Scourge Warlock", variable=self.radio_var, value=7)
        self.tr = tkinter.Radiobutton(self.stat_frame, text="Trickster Rogue", variable=self.radio_var, value=8)

        self.cw.grid(row=0, column=2)
        self.dc.grid(row=1, column=2)
        self.gwf.grid(row=2, column=2)
        self.gf.grid(row=3, column=2)
        self.hr.grid(row=4, column=2)
        self.op.grid(row=5, column=2)
        self.sw.grid(row=6, column=2)
        self.tr.grid(row=7, column=2)

        # Buttons ----------------------------------------------------
        self.roll_button = tkinter.Button(self.bottom_frame, text='Roll', command=self.rollin)
        self.roll_button.grid(row=1, column=0, padx=20, pady=10)
        self.gen_button = tkinter.Button(self.bottom_frame, text='Generate', command=self.generate)
        self.gen_button.grid(row=1, column=1, padx=20, pady=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.back)
        self.back_button.grid(row=1, column=2, padx=20, pady=10)

        # Frame Pack ----------------------------------------------------

        self.img_frame.pack()
        self.desc_frame.pack()
        self.name_frame.pack()
        self.stat_frame.pack()
        self.bottom_frame.pack()
        self.human.mainloop()

        # Random ----------------------------------------------------

    def rollin(self):
        result = random.randint(8, 18)
        self.randomstr.set(result + 2)

        result = random.randint(8, 18)
        self.randomdex.set(result + 2)

        result = random.randint(8, 18)
        self.randomcon.set(result)

        result = random.randint(8, 18)
        self.randomwis.set(result)

        result = random.randint(8, 18)
        self.randomint.set(result)

        result = random.randint(8, 18)
        self.randomcha.set(result)

        # Generate ----------------------------------------------------

    def generate(self):

        if self.radio_var.get() == 1:
            self.nwclass = 'Control Wizard'
        elif self.radio_var.get() == 2:
            self.nwclass = 'Devoted Cleric'
        elif self.radio_var.get() == 3:
            self.nwclass = 'Guardian Warrior'
        elif self.radio_var.get() == 4:
            self.nwclass = 'Guardian Fighter'
        elif self.radio_var.get() == 5:
            self.nwclass = 'Hunter Ranger'
        elif self.radio_var.get() == 6:
            self.nwclass = 'Oathbound Paladin'
        elif self.radio_var.get() == 7:
            self.nwclass = 'Scourge Warlock'
        else:
            self.nwclass = 'Trickster Rogue'

        name = self.name_entry.get()
        message = 'Hello, ' + name + ' the ' + self.nwclass + '.\nWelcome to Neverwinter.'

        tkinter.messagebox.showinfo('The Adventure Begins', message)

        # Back ----------------------------------------------------

    def back(self):
        self.human.destroy()
