import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name = ?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you with to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The table {0} will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_member_table():
    sql = """create table Member(
        MemberID integer,
        MemberFirstName text,
        MemberLastName text,
        MemberTownName text,
        MemberStreetName text,
        MemberHouseNameOrNumber text,
        MemberDateOfBirth text,
        primary key(MemberID))"""
    create_table(db_name,"Member",sql)

def create_parent_table():
    sql = """create table Parent(
        ParentID integer,
        ParentFirstName text,
        ParentLastName text,
        ParentTownName text,
        ParentStreetName text,
        ParentHouseNameOrNumber text,
        ParentEmail text,
        ParentPhoneNumber integer,
        primary key(ParentID))"""
    create_table(db_name,"Parent",sql)

def create_price_table():
    sql = """create table Price(
        PriceID integer,
        TermPrice real,
        SiblingDiscount real,
        primary key(PriceID))"""
    create_table(db_name,"Price",sql)

def create_invoice_table():
    sql = """create table Invoice(
        InvoiceID integer,
        ParentID integer,
        PriceID integer,
        WasInvoicePaid boolean,
        DateInvoiceWasSent text,
        primary key(InvoiceID)
        foreign key(ParentID) references Parent(ParentID)
        foreign key(PriceID) references Price(PriceID))"""
    create_table(db_name,"Invoice",sql)

def create_parent_member_table():
    sql = """create table ParentMember(
        ParentMemberID integer,
        ParentID integer,
        MemberID integer,
        primary key(ParentMemberID)
        foreign key(ParentID) references Parent(ParentID)
        foreign key(MemberID) references Member(MemberID))"""
    create_table(db_name,"ParentMember",sql)

def insert_price():
    print("Price: ")
    termPrice = float(input("Starting Price per Term: £"))
    siblingDiscountAmount = float(input("Discount Per Sibling(percentage off): "))

    values = (termPrice,siblingDiscountAmount)
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "insert into Price(TermPrice,siblingDiscount) values (?,?)"
        cursor.execute(sql,values)
        db.commit()


if __name__ == "__main__":
    db_name = "scout_database.db"
    create_member_table()
    create_parent_table()
    create_price_table()
    create_invoice_table()
    create_parent_member_table()
    insert_price()
    

