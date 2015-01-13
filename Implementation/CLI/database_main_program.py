from database_create import *
from database_delete_data import *
from database_edit_data import *
from database_add_data import *

def display_menu():
    print("\n----------Main Menu----------\n")
    print("1. Create database")
    print("2. Add data to database")
    print("3. Edit data in database")
    print("4. Delete data from database")
    print("5. Exit Program")
    print("\n-----------------------------\n")

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Select and option: "))
            if choice in (1,2,3,4,5):
                valid_option = True
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice

if __name__ == "__main__":
    done = False
    while not done:
        display_menu()
        choice = select_option()
        if choice == 1:
            CreateDatabase()
        elif choice == 2:
            AddData()
        elif choice == 3:
            EditData()
        elif choice == 4:
            DeleteData()
        elif choice == 5:
            done = True
            print("\nExiting Program\n")
