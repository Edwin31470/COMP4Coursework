from PyQt4.QtSql import *
from PyQt4.QtCore import *

class SQLConnection():
    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        opened_ok = self.db.open()
        return opened_ok

    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def show_members(self):
        query = QSqlQuery()
        query.prepare("""select * from Member""")
        query.exec_()
        return query
    
    def show_parents(self):
        query = QSqlQuery()
        query.prepare("""select * from Parent""")
        query.exec_()
        return query

    def show_invoices(self):
        query = QSqlQuery()
        query.prepare("""select * from Invoice""")
        query.exec_()
        return query

    def add_member_data(self):
        return "Working"

    def edit_member_data(self):
        query = QSqlQuery()
        query.prepare("""select MemberID, MemberFirstName, MemberLastName from Member""")
        query.exec_()
        return query

    def delete_member_data(self):
        return "Working"

    def add_parent_data(self):
        return "Working"

    def edit_parent_data(self):
        return "Working"

    def delete_parent_data(self):
        return "Working"

    def manage_invoice_data(self):
        return "Working"

    def print_invoice_data(self):
        return "Working"
    
    def closeEvent(self,event):
        self.close_database()
