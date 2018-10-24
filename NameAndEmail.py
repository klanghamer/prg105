import pickle

"""
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person's email address,
add a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file when
the user exits the program. Each time the program starts, it should retrieve the dictionary
from the file and unpickle it.


customers = dictionary {email:name}  # key = email, value = name

retrieve # have to create a file first, it won't work otherwise

"""


def main():
    # declare variables
    customers = get_info()
    choice = menu()
    if choice == "lookup":
        lookup(customers)
    elif choice == "add":
        add(customers)
    elif choice == "update":
        change(customers)
    elif choice == "delete":
        delete(customers)
    elif choice == "quit":
        save_file(customers)
    else:
        print("not valid entry")
        menu()
    if choice != "quit":
        main()


def get_info():
    # get file, unpickle, store in dictionary
    try:
        customer_file = open('customers.dat', 'rb')
        customers_dictionary = pickle.load(customer_file)
        customer_file.close()
    except FileNotFoundError:
        customers_dictionary = {}
    return customers_dictionary


def menu():
    # display menu
    chosen = 0
    print()
    print("--------------- Customer Accounts --------------")
    print("1:   Add new customer")
    print("2:   Look up existing customer")
    print("3:   Change existing customer")
    print("4:   Delete existing customer")
    print("5:   Quit")
    try:
        while chosen < 1 or chosen > 2:
            chosen = int(input("Please enter the number of the action you wish to initialize: "))
            if chosen < 1 or chosen > 5:
                print("Not a valid selection.")
            else:
                if chosen == 1:
                    return "add"
                elif chosen == 2:
                    return "lookup"
                elif chosen == 3:
                    return "update"
                elif chosen == 4:
                    return "delete"
                elif chosen == 5:
                    return "quit"

    except ValueError:
        print("You need a numeric entry.")
    main()


def lookup(customers_lookup):
    # look up and display a current customer
    found = False
    name = input("Please enter the name you want to look up: ")
    print()

    for key in customers_lookup:
        if customers_lookup[key].upper() == name.upper():
            print(customers_lookup[key] + ": " + key)
            found = True
    if not found:
        print("That name was not found")
    return customers_lookup


def add(customers_add):
    # add a new customer
    add_email = input("Enter the email you want to add: ")
    add_name = input("Enter the name associated with the email: ")
    customers_add[add_email] = add_name
    save_file(customers_add)


def change(customer_change):
    # update customer information
    change_name = input("Enter the email you wish to change: ")

    if change_name in customer_change:
        name_change = input("Enter the new name: ")
        customer_change[change_name] = name_change
    else:
        print("That email was not found.")
    save_file(customer_change)


def delete(customer_delete):
    # delete a customer
    name_delete = input("Enter the email you want to delete: ")

    if name_delete in customer_delete:
        del customer_delete[name_delete]
    else:
        print("That entry was not found.")
    save_file(customer_delete)


def save_file(customer_pickle):
    # pickle and dump the file
    customer_file = open('customers.dat', 'wb')
    pickle.dump(customer_pickle, customer_file)
    customer_file.close()
    print("Information has been saved.")


main()
