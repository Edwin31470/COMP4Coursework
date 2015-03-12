import sqlite3

def print_menu():
    print("\n---------------Menu-----------------\n")
    print("1. Delete a Member")
    print("2. Delete a Parent")
    print("3. Delete a Parent-Member connection")
    print("4. Delete an Invoice")
    print("5. Exit")
    print("\n------------------------------------\n")
    print()

def delete_member():
    memberID = int(input("ID of member to be deleted: "))
    values = (memberID,)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "delete from Member where MemberID = ?"
        cursor.execute(sql,values)
        db.commit()

def delete_parent():
    parentID = int(input("ID of parent to be deleted: "))
    values = (parentID,)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "delete from Parent where ParentID = ?"
        cursor.execute(sql,values)
        db.commit()

def delete_invoice():
    invoiceID = int(input("ID of invoice to be deleted: "))
    values = (invoiceID,)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "delete from Invoice where InvoiceID = ?"
        cursor.execute(sql,values)
        db.commit()

def delete_parent_member():
    parentMemberID = int(input("ID of parent-member connection to be deleted: "))
    values = (parentMemberID,)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "delete from ParentMember where ParentMemberID = ?"
        cursor.execute(sql,values)
        db.commit()



def menu_choice():
    done = False
    while done == False:
        print_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            delete_member()
        elif choice == 2:
            delete_parent()
        elif choice == 3:
            delete_parent_member()
        elif choice == 4:
            delete_invoice()
        elif choice == 5:
            done = True
            print("\nExiting Program\n")
        else:
            print("\nInvalid input\n")

def DeleteData():
    menu_choice()

if __name__ == "__main__":
    menu_choice()
