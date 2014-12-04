import sqlite3

def insert_data(values):
    with sqlite3.connect("scout_database.db") as db:
        cursor = db.cursor()
        sql = "insert into Member (MemberFirstName,MemberLastName,MemberTownName,MemberStreetName,MemberHouseNameOrNumber,MemberDateOfBirth) values (?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    name = input("Name: ")
    price = float(input("Price: "))
    product = (firstName,lastName,townName,streetName,houseNameOrNum,dateOfBirth)
    insert_data(product)
