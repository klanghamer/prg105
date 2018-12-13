import tkinter
import tkinter.messagebox
import pickle


class CharSaved:
    def __init__(self, master, input_file):
        self.master = master
        self.human = tkinter.Toplevel(master)
        self.input_file = input_file
        self.human.title('View your Saved Characters')
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

        # Description ----------------------------------------------------

        self.desc = tkinter.Label(self.desc_frame, text='Enter your name and click view to recall an old character '
                                                        'and stats.\n')
        self.desc.grid(row=0, column=0)

        # Look Up Name ----------------------------------------------------

        self.name_label = tkinter.Label(self.name_frame, text='Enter your characters name: ')
        self.name_entry = tkinter.Entry(self.name_frame, width=15)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        # Results Area ----------------------------------------------------

        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.stat_frame, text='Results: ')
        self.results = tkinter.Label(self.stat_frame, textvariable=self.value)

        self.results_label.pack()
        self.results.pack()

        # Buttons ----------------------------------------------------
        self.view_button = tkinter.Button(self.bottom_frame, text='View', command=self.view)
        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.back)
        self.view_button.grid(row=1, column=0, padx=20, pady=10)
        self.back_button.grid(row=1, column=1, padx=20, pady=10)

        # Frame Pack ----------------------------------------------------

        self.desc_frame.pack()
        self.name_frame.pack()
        self.stat_frame.pack()
        self.bottom_frame.pack()
        self.human.mainloop()

        # Search ----------------------------------------------------

    def view(self):
        try:
            my_input = open(self.input_file, 'rb')
            charlog = pickle.load(my_input)
            my_input.close()
        except(FileNotFoundError, IOError):
            charlog = {}

        name = self.name_entry.get()
        result = charlog.get(name, 'That character does not exist')
        self.value.set(result)

        # Back ----------------------------------------------------

    def back(self):
        self.human.destroy()
