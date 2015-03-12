import sqlite3

def print_menu():
    print("\n---------------Menu-----------------\n")
    print("1. Edit a Member")
    print("2. Edit a Parent")
    print("3. Edit a Parent-Member connection")
    print("4. Edit an Invoice")
    print("5. Exit")
    print("\n------------------------------------\n")

def edit_member():
    memberID = int(input("ID of member to be edited: "))
    field = input("Field to be edited: ")
    data = input("New data: ")
    values = (data,memberID)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "update Member set {0}=? where MemberID=?".format(field)
        cursor.execute(sql,values)
        db.commit()

def edit_parent():
    parentID = int(input("ID of parent to be edited: "))
    field = input("Field to be edited: ")
    data = input("New data: ")
    values = (data,parentID)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "update Parent set {0}=? where ParentID=?".format(field)
        cursor.execute(sql,values)
        db.commit()

def edit_parent_member():
    parentMemberID = int(input("ID of parent-member connection to be edited: "))
    field = input("Field to be edited: ")
    data = input("New data: ")
    values = (data,parentMemberID)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "update ParentMember set {0}=? where ParentMemberID=?".format(field)
        cursor.execute(sql,values)
        db.commit()

def edit_invoice():
    invoiceID = int(input("ID of invoice to be edited: "))
    field = input("Field to be edited: ")
    data = input("New data: ")
    values = (data,invoiceID)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "update Invoice set {0}=? where InvoiceID=?".format(field)
        cursor.execute(sql,values)
        db.commit()

def menu_choice():
    done = False
    while done == False:
        print_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            edit_member()
        elif choice == 2:
            edit_parent()
        elif choice == 3:
            edit_parent_member()
        elif choice == 4:
            edit_invoice()
        elif choice == 5:
            done = True
            print("\nExiting Program\n")
        else:
            print("\nInvalid input\n")

def EditData():
    menu_choice()

if __name__ == "__main__":
    menu_choice()


