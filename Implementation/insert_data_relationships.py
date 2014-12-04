import sqlite3

def query(sql,data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def insert_product_type_data(records):
    sql = "insert into ProductType(Description) values (?)"
    for record in records:
        query(sql,record)

def insert_product_data(records):
    sql = "insert into Product(Name,Price,ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql,record)

if __name__ == "__main__":
    product_types = [("Coffee",),("Tea",),("Cold Drink",)]
    insert_product_type_data(product_types)
    products = [("Latte",1.35,1),("Mocha",2.40,1),("Green Tea",1.20,2),("Black Tea",1.00,2),
                ("Americano",1.50,2),("Raspberry",3.50,3),("Lemon",2.85,3)]
    insert_product_data(products)
