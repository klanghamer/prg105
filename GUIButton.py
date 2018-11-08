import tkinter
import tkinter.messagebox


class MarketGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Crunchy Tacos', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Soft Tacos', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Mexican Pizza', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Chalupa', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Burrito Supreme', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Nacho Bell Grande', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Medium Drink', variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame, text='Cinnamon Twists', variable=self.cb_var8)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='ok', command=self.total)
        self.quit_button = tkinter.Button(self.bottom_frame, text='quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def total(self):
        self.message = 'your total is \n'
        self.total = 0.0

        if self.cb_var1.get() == 1:
            self.total += 1.19
        if self.cb_var2.get() == 1:
            self.total += 1.39
        if self.cb_var3.get() == 1:
            self.total += 3.45
        if self.cb_var4.get() == 1:
            self.total += 3.25
        if self.cb_var5.get() == 1:
            self.total += 2.29
        if self.cb_var6.get() == 1:
            self.total += 4.37
        if self.cb_var7.get() == 1:
            self.total += 1.19
        if self.cb_var8.get() == 1:
            self.total += 0.98

        tkinter.messagebox.showinfo('selection', self.total)


button = MarketGui()
