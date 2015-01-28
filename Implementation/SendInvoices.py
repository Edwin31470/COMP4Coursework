import sqlite3, smtplib

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SendInvoiceData(QWidget):
    """this class provides a widget for sending invoices"""
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)

    def create_document(self):
