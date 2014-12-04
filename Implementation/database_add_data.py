import sqlite3

def insert_member():
    print("Member: ")
    memberFirstName = input("Member's First Name: ")
    memberLastName = input("Member's Last Name: ")
    memberTownName = input("Member's Town Name: ")
    memberStreetName = input("Member's Street Name: ")
    memberHouseNameOrNum = input("Member's House Name Or Number: ")
    dateOfBirth = input("Member's Date Of Birth(DD/MM/YY): ")
    values = (memberFirstName,memberLastName,memberTownName,memberStreetName,memberHouseNameOrNum,dateOfBirth)
    
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into Member(MemberFirstName,MemberLastName,MemberTownName,MemberStreetName,MemberHouseNameOrNumber,MemberDateOfBirth) values (?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def insert_parent():
    print("Parent: ")
    parentFirstName = input("Parent's First Name: ")
    parentLastName = input("Parent's Last Name: ")
    parentTownName = input("Parent's Town Name: ")
    parentStreetName = input("Parent's Street Name: ")
    parentHouseNameOrNum = input("Parent's House Name Or Number: ")
    parentEmail = input("Parent's Email: ")
    parentPhoneNumber = int(input("Parent's Phone Number: "))
    values = (parentFirstName,parentLastName,parentTownName,parentStreetName,parentHouseNameOrNum,parentEmail,parentPhoneNumber)
    
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "insert into Parent(ParentFirstName,ParentLastName,ParentTownName,ParentStreetName,ParentHouseNameOrNumber,ParentEmail,parentPhoneNumber) values (?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def insert_invoice():
    print("Invoice: ")
    wasInvoicePaid = input("Was Last Invoice Paid(yes/no): ").lower()
    if wasInvoicePaid[1] == "y":
        wasInvoicePaid = True
    elif wasInvoicePaid[1] == "n":
        wasInvoicePaid = False
    dateInvoiceWasSent = input("Date Last Invoice Was Sent(DD/MM/YY): ")
    values = (wasInvoicePaid,dateInvoiceWasSent)
    
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "insert into Invoice(WasInvoicePaid,DateInvoiceWasSent) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

def insert_parent_invoice_connection():
    print("Connection: ")

def print_menu():
    print()
    print("-------------------------")
    print("1. Add a Member")
    print("2. Add a Parent")
    print("3. Add a Parent-Member connection")
    print("4. Add an Invoice")
    print("5. Exit")
    print("-------------------------")
    print()

def menu_choice():
    done = False
    while done == False:
        print_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            insert_member()
        elif choice == 2:
            insert_parent()
        elif choice == 3:
            insert_parent_member()
        elif choice == 4:
            insert_invoice()
        elif choice == 5:
            done = True
            print("Exiting Program")
        else:
            print("Invalid input")

if __name__ == "__main__":
    menu_choice()


