"""
    Create a CRUD application with a GUI interface
"""

import pickle
import tkinter
import tkinter.messagebox


class CrudGUI:
    def __init__(self, master, input_file):
        self.master = master
        self.master.title('Welcome Menu')
        self.input_file = input_file

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create radio buttons

        self.look = tkinter.Radiobutton(self.top_frame, text="Look up customer", variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text="Add a customer", variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text="Change customer information", variable=self.radio_var,
                                          value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text="Delete a customer", variable=self.radio_var, value=4)

        # pack radio buttons

        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons

        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUIT", command=self.master.destroy)

        # pack buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            LookGUI(self.master, self.input_file)
        elif self.radio_var.get() == 2:
            AddGUI(self.master, self.input_file)
        elif self.radio_var.get() == 3:
            UpdateGUI(self.master, self.input_file)
        else:
            DeleteGUI(self.master, self.input_file)


class LookGUI:
    def __init__(self, master, input_file):
        self.master = master
        self.input_file = input_file
        self.look = tkinter.Toplevel(master)
        self.look.title("Search for customer")
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # widget for middle frame
        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.middle_frame, text='Results: ')
        self.results = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack middle frame
        self.results_label.pack(side='left')
        self.results.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.look.destroy)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        try:
            my_input = open(self.input_file, 'rb')
            customers = pickle.load(my_input)
            my_input.close()
        except(FileNotFoundError, IOError):
            customers = {}

        name = self.search_entry.get()
        result = customers.get(name, 'That name was not found')
        self.value.set(result)


class AddGUI:
    def __init__(self, master, input_file):
        self.master = master
        self.input_file = input_file
        self.add = tkinter.Toplevel(master)
        self.add.title('Add a Customer')
        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        self.add_label = tkinter.Label(self.top_frame, text='Enter customers name: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.add_label2 = tkinter.Label(self.top_frame, text='Enter customers email: ')
        self.add_entry2 = tkinter.Entry(self.top_frame, width=15)

        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.add_label2.pack(side='left')
        self.add_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add_value)  # shadow error
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add_value(self):  # Don't let shadow error happen
        tkinter.messagebox.showinfo("Hey Listen", "add")
        try:
            customer_file = open(self.input_file, 'rb')
            customers = pickle.load(customer_file)
            customer_file.close()
        except FileNotFoundError:
            customers = {}

        name = self.add_entry.get()
        email = self.add_entry2.get()
        customers[email] = name

        file = open("customers.dat", 'wb')
        pickle.dump(customers, file)
        file.close()

    def back(self):
        self.add.destroy()


class UpdateGUI:
    def __init__(self, master, input_file):
        self.master = master
        self.input_file = input_file
        self.update = tkinter.Toplevel(master)
        self.update.title('Update a Customer')
        self.top_frame = tkinter.Frame(self.update)
        self.middle_frame = tkinter.Frame(self.update)
        self.bottom_frame = tkinter.Frame(self.update)

        self.update_label = tkinter.Label(self.top_frame, text='Enter customers email: ')
        self.update_entry = tkinter.Entry(self.top_frame, width=15)
        self.update_label2 = tkinter.Label(self.top_frame, text='Enter new email: ')
        self.update_entry2 = tkinter.Entry(self.top_frame, width=15)

        self.update_label.pack(side='left')
        self.update_entry.pack(side='left')
        self.update_label2.pack(side='left')
        self.update_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.update_button = tkinter.Button(self.bottom_frame, text='Update', command=self.update_value)  # shadow error
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.update_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def update_value(self):  # Don't let shadow error happen
        tkinter.messagebox.showinfo("Hey Listen", "update")

        try:
            customer_file = open(self.input_file, 'rb')
            customers = pickle.load(customer_file)
            customer_file.close()
        except FileNotFoundError:
            customers = {}

        change_name = self.update_entry2.get()
        customer_change = self.update_entry.get()
        customers[customer_change] = change_name

        file = open("customers.dat", 'wb')
        pickle.dump(customers, file)
        file.close()

    def back(self):
        self.update.destroy()


def main():
    input_file = "customers.dat"
    root = tkinter.Tk()
    CrudGUI(root, input_file)
    root.mainloop()


class DeleteGUI:
    def __init__(self, master, input_file):
        self.master = master
        self.input_file = input_file
        self.delete = tkinter.Toplevel(master)
        self.delete.title('Update a Customer')
        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        self.delete_label = tkinter.Label(self.top_frame, text='Enter customers email you want to delete: ')
        self.delete_entry = tkinter.Entry(self.top_frame, width=15)

        self.delete_label.pack(side='left')
        self.delete_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.delete_button = tkinter.Button(self.bottom_frame, text='Update', command=self.delete_value)  # shadow error
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete_value(self):  # Don't let shadow error happen

        try:
            customer_file = open(self.input_file, 'rb')
            customers = pickle.load(customer_file)
            customer_file.close()
        except FileNotFoundError:
            customers = {}

        name_delete = self.delete_entry.get()

        if name_delete in customers:
            del customers[name_delete]

        result = customers.get(name_delete, 'Customer Deleted')
        self.value.set(result)

        file = open("customers.dat", 'wb')
        pickle.dump(customers, file)
        file.close()

    def back(self):
        self.delete.destroy()


"""
def save_file(customer_pickle):
    # pickle and dump the file
    input_file = open('customers_file.dat', 'wb')
    pickle.dump(customer_pickle, input_file)
    input_file.close()
"""

main()
