import tkinter
import tkinter.messagebox
import random


class Human:
    def __init__(self):
        # self.master = master
        self.human = tkinter.Tk()
        # Toplevel(master)
        self.human.title('Race, Human')
        self.img_frame = tkinter.Frame(self.human)
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
        self.canvas2 = tkinter.Canvas(self.img_frame, width=250, height=300)
        self.pop = tkinter.Canvas(self.img_frame)
        raceimage = tkinter.PhotoImage(file='placeholder.png')

        self.canvas2.create_image(125, 150, image=raceimage)
        self.canvas2.pack()

        # Add Name ----------------------------------------------------
        self.name_label = tkinter.Label(self.name_frame, text='Name your character: ')
        self.name_entry = tkinter.Entry(self.name_frame, width=15)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        # Stats Area ----------------------------------------------------

        self.rando1 = tkinter.StringVar()
        self.str = tkinter.Label(self.stat_frame, text='STR: ')
        self.str_label = tkinter.Label(self.stat_frame, textvariable=self.rando1)
        self.str.grid(row=0, column=0)
        self.str_label.grid(row=0, column=1)

        self.rando2 = tkinter.StringVar()
        self.dex = tkinter.Label(self.stat_frame, text='DEX: ')
        self.dex_label = tkinter.Label(self.stat_frame, textvariable=self.rando2)
        self.dex.grid(row=1, column=0)
        self.dex_label.grid(row=1, column=1)

        self.rando3 = tkinter.StringVar()
        self.con = tkinter.Label(self.stat_frame, text='CON: ')
        self.con_label = tkinter.Label(self.stat_frame, textvariable=self.rando3)
        self.con.grid(row=2, column=0)
        self.con_label.grid(row=2, column=1)

        self.rando4 = tkinter.StringVar()
        self.wis = tkinter.Label(self.stat_frame, text='WIS: ')
        self.wis_label = tkinter.Label(self.stat_frame, textvariable=self.rando4)
        self.wis.grid(row=3, column=0)
        self.wis_label.grid(row=3, column=1)

        self.rando5 = tkinter.StringVar()
        self.int = tkinter.Label(self.stat_frame, text='INT: ')
        self.int_label = tkinter.Label(self.stat_frame, textvariable=self.rando5)
        self.int.grid(row=4, column=0)
        self.int_label.grid(row=4, column=1)

        self.rando6 = tkinter.StringVar()
        self.cha = tkinter.Label(self.stat_frame, text='CHA: ')
        self.cha_label = tkinter.Label(self.stat_frame, textvariable=self.rando6)
        self.cha.grid(row=5, column=0)
        self.cha_label.grid(row=5, column=1)

        # Buttons ----------------------------------------------------
        self.roll_button = tkinter.Button(self.bottom_frame, text='Roll', command=self.rollin)
        self.roll_button.grid(row=1, column=0, padx=20, pady=10)
        self.gen_button = tkinter.Button(self.bottom_frame, text='Generate', command=self.back)
        self.gen_button.grid(row=1, column=1, padx=20, pady=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.back)
        self.back_button.grid(row=1, column=2, padx=20, pady=10)

        self.img_frame.pack()
        self.name_frame.pack()
        self.stat_frame.pack()
        self.bottom_frame.pack()
        self.human.mainloop()

        # Random ----------------------------------------------------

    def rollin(self):
        result = random.randint(8, 18)
        self.rando1.set(result)

        result = random.randint(8, 18)
        self.rando2.set(result)

        result = random.randint(8, 18)
        self.rando3.set(result)

        result = random.randint(8, 18)
        self.rando4.set(result)

        result = random.randint(8, 18)
        self.rando5.set(result)

        result = random.randint(8, 18)
        self.rando6.set(result)

        # Generate ----------------------------------------------------

    #def generate(self):

        # Back ----------------------------------------------------

    def back(self):
        self.human.destroy()


def main():
    # input_file = 'charlog.dat'
    # create a window
    # root = tkinter.Tk()
    # call the GUI and send it the root menu
    menu_gui = Human()
    # control the mainloop from main instead of the class
    # root.mainloop()


main()
