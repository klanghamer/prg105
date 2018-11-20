import pickle
import tkinter
import tkinter.messagebox


class CrudGUI:
    def __init__(self, master, cust):
        self.master = master
        self.master.title('Welcome Menu')
        self.customer_list = cust
        self.radio_var = 0

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.radio_var.set(2)
        self.radio_var.set(3)
        self.radio_var.set(4)

        # create radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look Up Customer', variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer', variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change Customer Info', variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete a Customer', variable=self.radio_var, value=4)

        # pack radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.master.destroy)

        # pack buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames

        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            search = LookGUI(self.master, self.customer_list)
        elif self.radio_var.get() == 2:
            search = AddGUI(self.master, self.customer_list)
        elif self.radio_var.get() == 3:
            search = UpdateGUI(self.master, self.customer_list)
        else:
            search = DeleteGUI(self.master, self.customer_list)


class LookGUI:
    def __init__(self, master, look_cust):
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for Customer')
        self.customer_list = look_cust
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.search_label = tkinter.Label(self.top_frame, text='Enter customers name to look up:')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Add', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customer_list.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master, add_cust):
        self.master = master
        self.add = tkinter.Toplevel(master)
        self.add.title('Add a Customer')
        self.customer_list = add_cust
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

        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add(self):
        name = self.add_entry.get()
        email = self.add_entry2.get()
        result = self.customer_list.get(name, email, 'Customer Added')
        self.value.set(result)
        # customers_add[add_email] = add_name
        # save_file(customers_add)

    def back(self):
        self.add.destroy()


class UpdateGUI:
    def __init__(self, master, update_cust):
        self.master = master
        self.update = tkinter.Toplevel(master)
        self.update.title('Update a Customer')
        self.customer_list = update_cust
        self.top_frame = tkinter.Frame(self.update)
        self.middle_frame = tkinter.Frame(self.update)
        self.bottom_frame = tkinter.Frame(self.update)

        self.update_label = tkinter.Label(self.top_frame, text='Enter customers name: ')
        self.update_entry = tkinter.Entry(self.top_frame, width=15)

        self.update_label.pack(side='left')
        self.update_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.add_button = tkinter.Button(self.bottom_frame, text='Update', command=self.update)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def update(self):
        name = self.update_entry.get()
        result = self.customer_list.get(name, 'Customers Information Updated')
        self.value.set(result)
        # customer_change[change_name] = name_change

    def back(self):
        self.update.destroy()


class DeleteGUI:
    def __init__(self, master, delete_cust):
        self.master = master
        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete a Customer')
        self.customer_list = delete_cust
        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        self.delete_label = tkinter.Label(self.top_frame, text='Enter customers name: ')
        self.delete_entry = tkinter.Entry(self.top_frame, width=15)

        self.delete_label.pack(side='left')
        self.delete_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.delete_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete(self):
        name = self.delete_entry.get()
        result = self.customer_list.get(name, 'Customers Information Deleted')
        self.value.set(result)
        # customer_delete[name_delete]

    def back(self):
        self.delete.destroy()

def main():
    try:
        input_file = open("customers.dat", 'rb')
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        customers = {}

    root = tkinter.Tk()
    menuGui = CrudGUI(root, customers)
    root.mainloop()


main()
