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
        query.prepare("""SELECT
                         Invoice.InvoiceID,
                         Parent.ParentFirstName,
                         Parent.ParentLastName,
                         Invoice.PriceID,
                         Invoice.WasInvoicePaid,
                         Invoice.DateInvoiceWasSent
                         FROM Invoice
                         INNER JOIN Parent
                         ON Invoice.ParentID=Parent.ParentID""")
        query.exec_()
        return query

    def report_invoices_old(self):
        query = QSqlQuery()
        query.prepare("""select * from Invoice where WasInvoicePaid = 'No'""")
        query.exec_()
        return query

    def report_invoices(self):
        query = QSqlQuery()
        query.prepare("""SELECT
                         Invoice.InvoiceID,
                         Parent.ParentFirstName,
                         Parent.ParentLastName,
                         Invoice.PriceID,
                         Invoice.WasInvoicePaid,
                         Invoice.DateInvoiceWasSent
                         FROM Invoice
                         INNER JOIN Parent
                         ON Invoice.ParentID=Parent.ParentID
                         WHERE WasInvoicePaid = 'No'""")
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

    def order_member_data(self,column,order):
        query = QSqlQuery()
        query.prepare("""select * from Member order by {0} {1}""".format(column,order))
        #query.prepare("""select * from Member order by MemberDateOfBirth ASC""")
        query.exec_()
        return query

    def order_parent_data(self,column,order):
        query = QSqlQuery()
        query.prepare("""select * from Parent order by {0} {1}""".format(column,order))
        query.exec_()
        return query

    def order_invoice_data_old(self,column,order):
        query = QSqlQuery()
        query.prepare("""select * from Invoice order by {0} {1}""".format(column,order))
        query.exec_()
        return query

    def order_invoice_data(self,column,order):
        query = QSqlQuery()
        query.prepare("""SELECT
                         Invoice.InvoiceID,
                         Parent.ParentFirstName,
                         Parent.ParentLastName,
                         Invoice.PriceID,
                         Invoice.WasInvoicePaid,
                         Invoice.DateInvoiceWasSent
                         FROM Invoice
                         INNER JOIN Parent
                         ON Invoice.ParentID=Parent.ParentID

                         ORDER BY {0} {1}""".format(column,order))
        query.exec_()
        return query

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
