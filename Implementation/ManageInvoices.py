import sqlite3

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

        self.dialog_layout.addWidget(self.add_parentID_button)
        self.dialog_layout.addWidget(self.add_invoice_paid_button)
        self.dialog_layout.addWidget(self.add_date_sent_button)

        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.insert_invoice)


    def insert_invoice(self):
        values = [self.add_parentID_button.text(),
                  self.add_invoice_paid_button.text(),
                  self.add_date_sent_button.text()]
    
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = "insert into Invoice(ParentID,WasInvoicePaid,DateInvoiceWasSent,PriceID) values (?,?,?,1)"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()

class ChooseOption(QWidget):
    updatedData = pyqtSignal()
    """Provides a choice of add or delete invoices"""
    def __init__(self):
        super().__init__()
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")

        #self.stacked_layout = QStackedLayout()
        
        self.button_layout = QHBoxLayout()

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.delete_button)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.button_layout)
        
        #self.stacked_layout.addWidget(self.button_widget)
        
        #self.data_dialog = EnterInvoiceData()
        #self.data_widget.setLayout(self.data_dialog)
        #self.stacked_layout.addWidget(self.data_widget)
        
        self.setLayout(self.button_layout)
                
        self.add_button.clicked.connect(self.add_invoice)
        self.delete_button.clicked.connect(self.delete_invoice)

    def add_invoice_stacked(self):
        if self.stacked_layout.currentIndex == 0:
            print("Stack layout changed to 1")
            self.stacked_layout.setCurrentIndex(1)
        if self.stacked_layout.currentIndex == 1:
            self.stacked_layout.setCurrentIndex(0)

    def add_invoice(self):
        self.updatedData.emit()

    def delete_invoice(self):
        pass














    
