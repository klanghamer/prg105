import tkinter
import tkinter.messagebox
import random


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
        self.human.grid()

        # top image stuff
        self.canvas = tkinter.Canvas(self.human, width=400, height=125)
        self.pop = tkinter.Canvas(self.human)
        topimage = tkinter.PhotoImage(file='neverwinter.png')

        self.canvas.create_image(200, 75, image=topimage)
        self.canvas.grid(row=0, column=0)

        # Top title
        self.value = tkinter.StringVar()
        self.info3 = tkinter.Label(self.top_frame, text='Human')
        self.top_label3 = tkinter.Label(self.top_frame, textvariable=self.value)
        self.info3.pack()
        self.top_label3.grid(row=0, column=4)

        # Stats Area
        self.rando1 = tkinter.StringVar()
        self.str = tkinter.Label(self.left_frame, text='STR: ')
        self.str_label = tkinter.Label(self.left_frame, textvariable=self.rando1)
        self.str.grid(row=0, column=0)
        self.str_label.grid(row=0, column=1)

        self.rando2 = tkinter.StringVar()
        self.dex = tkinter.Label(self.left_frame, text='DEX: ')
        self.dex_label = tkinter.Label(self.left_frame, textvariable=self.rando2)
        self.dex.grid(row=1, column=0)
        self.dex_label.grid(row=1, column=1)

        self.rando3 = tkinter.StringVar()
        self.con = tkinter.Label(self.left_frame, text='CON: ')
        self.con_label = tkinter.Label(self.left_frame, textvariable=self.rando3)
        self.con.grid(row=2, column=0)
        self.con_label.grid(row=2, column=1)

        self.rando4 = tkinter.StringVar()
        self.wis = tkinter.Label(self.left_frame, text='WIS: ')
        self.wis_label = tkinter.Label(self.left_frame, textvariable=self.rando4)
        self.wis.grid(row=3, column=0)
        self.wis_label.grid(row=3, column=1)

        self.rando5 = tkinter.StringVar()
        self.int = tkinter.Label(self.left_frame, text='INT: ')
        self.int_label = tkinter.Label(self.left_frame, textvariable=self.rando5)
        self.int.grid(row=4, column=0)
        self.int_label.grid(row=4, column=1)

        self.rando6 = tkinter.StringVar()
        self.cha = tkinter.Label(self.left_frame, text='CHA: ')
        self.cha_label = tkinter.Label(self.left_frame, textvariable=self.rando6)
        self.cha.grid(row=5, column=0)
        self.cha_label.grid(row=5, column=1)

        # Random
        result = random.randint(7, 19)
        self.rando1.set(result)

        result = random.randint(7, 19)
        self.rando2.set(result)

        result = random.randint(7, 19)
        self.rando3.set(result)

        result = random.randint(7, 19)
        self.rando4.set(result)

        result = random.randint(7, 19)
        self.rando5.set(result)

        result = random.randint(7, 19)
        self.rando6.set(result)

        # side image
        self.canvas2 = tkinter.Canvas(self.right_frame, width=250, height=300)
        self.pop = tkinter.Canvas(self.right_frame)
        raceimage = tkinter.PhotoImage(file='placeholder.png')

        self.canvas2.create_image(125, 150, image=raceimage)
        self.canvas2.grid(row=0, column=0)

        # buttons
        self.roll_button = tkinter.Button(self.bottom_frame, text='Roll', command=self.back)
        self.roll_button.grid(row=1, column=0)
        self.gen_button = tkinter.Button(self.bottom_frame, text='Generate', command=self.back)
        self.gen_button.grid(row=1, column=1)
        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.back)
        self.back_button.grid(row=1, column=2)
        
        self.top_frame.grid(row=0, column=0)
        self.left_frame.grid(row=1, column=1)
        self.right_frame.grid(row=1, column=2)
        self.bottom_frame.grid(row=2, column=0)

        """
        self.top_frame.pack()
        self.left_frame.pack()
        self.right_frame.pack()
        self.bottom_frame.pack()
        self.human.mainloop()
        """
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
