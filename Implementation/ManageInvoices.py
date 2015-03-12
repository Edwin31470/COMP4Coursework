import sqlite3,datetime

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ManageInvoiceData(QWidget):
    """this class provides a widget for entering data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)



class EnterInvoiceData(ManageInvoiceData):
    """this class provides a dialog for entering member data"""
    def __init__(self):
        super().__init__()
        
        self.add_parentID_button = QLineEdit()
        self.add_invoice_paid_button = QLineEdit()
        self.add_date_sent_button = QLineEdit()
        self.accept_button = QPushButton("Accept")
        
        self.add_parentID_button.setPlaceholderText("Enter ParentID to be attached to")
        self.add_invoice_paid_button.setPlaceholderText("Was the invoicew paid? (Yes/No)")
        self.add_date_sent_button.setPlaceholderText("Enter Date Sent (DD/MM/YY)")

        #Creating date widget
        self.date_label = QLabel("Date sent:")
        self.add_date_day = QComboBox()
        self.add_date_month = QComboBox()
        self.add_date_year = QComboBox()
        self.spacer = QLabel()

        self.date_label.setFixedWidth(80)
        self.add_date_day.setFixedWidth(100)
        self.add_date_month.setFixedWidth(100)
        self.add_date_year.setFixedWidth(100)
        
        currentYear = int(datetime.date.today().strftime("%Y"))

        for count in range(1,32):
            self.add_date_day.addItem(str(count))
        for count in range(1,13):
            self.add_date_month.addItem(str(count))
        for count in range(currentYear - 8,currentYear):
            self.add_date_year.addItem(str(count))
        
        self.date_layout = QHBoxLayout()
        self.date_widget = QWidget()
        self.date_layout.addWidget(self.date_label)
        self.date_layout.addWidget(self.add_date_day)
        self.date_layout.addWidget(self.add_date_month)
        self.date_layout.addWidget(self.add_date_year)
        self.date_layout.addWidget(self.spacer)
        self.date_widget.setLayout(self.date_layout)

        self.dialog_layout.addWidget(self.add_parentID_button)
        self.dialog_layout.addWidget(self.add_invoice_paid_button)
        self.dialog_layout.addWidget(self.date_widget)

        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.insert_invoice)


    def insert_invoice(self):
        day = self.add_date_day.itemText(self.add_date_day.currentIndex()) 
        month = self.add_date_month.itemText(self.add_date_month.currentIndex())
        year = self.add_date_year.itemText(self.add_date_year.currentIndex())
        
        if int(day) in range(1,10):
            day = "0" + day
        if int(month) in range(1,10):
            month = "0" + month
        
        date = year + "/" + month + "/" + day
        
        values = (self.add_parentID_button.text(),
                  self.add_invoice_paid_button.text(),
                  date)
    
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = "insert into Invoice(ParentID,WasInvoicePaid,DateInvoiceWasSent,PriceID) values (?,?,?,1)"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()       

class DeleteInvoiceData(ManageInvoiceData):
    """this class provides a dialog for deleting member data"""
    def __init__(self):
        super().__init__()
        
        self.delete_invoiceID_button = QLineEdit()
        self.accept_button = QPushButton("Accept")
        
        self.delete_invoiceID_button.setPlaceholderText("Enter InvoiceID to be deleted")

        self.dialog_layout.addWidget(self.delete_invoiceID_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.delete_invoice)


    def delete_invoice(self):
        values = (self.delete_invoiceID_button.text(),)
    
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            sql = "delete from Invoice where InvoiceID = ?"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()

class ChooseOption(QWidget):
    addData = pyqtSignal()
    deleteData = pyqtSignal()
    """Provides a choice of add or delete invoices"""
    def __init__(self):
        super().__init__()
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        
        self.button_layout = QHBoxLayout()

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.delete_button)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.button_layout)
        
        self.setLayout(self.button_layout)
                
        self.add_button.clicked.connect(self.add_invoice)
        self.delete_button.clicked.connect(self.delete_invoice)

    def add_invoice(self):
        self.addData.emit()

    def delete_invoice(self):
        self.deleteData.emit()
    
