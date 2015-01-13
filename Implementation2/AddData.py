import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EnterDataDialog(QDialog):
    """this class provides a dialog for entering data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)
        
    

        
class EnterMemberDataDialog(EnterDataDialog):
    """this class provides a dialog for entering member data"""
    def __init__(self):
        super().__init__()
        self.add_first_name_button = QLineEdit()
        self.add_last_name_button = QLineEdit()
        self.add_dob_button = QLineEdit()
        self.add_town_name_button = QLineEdit()
        self.add_street_name_button = QLineEdit()
        self.add_house_name_button = QLineEdit()
        self.accept_button = QPushButton("Accept")
        
        self.add_first_name_button.setPlaceholderText("Enter First Name")
        self.add_last_name_button.setPlaceholderText("Enter Last Name")
        self.add_dob_button.setPlaceholderText("Enter Date Of Birth (DD/MM/YY)")
        self.add_town_name_button.setPlaceholderText("Enter Town Name")
        self.add_street_name_button.setPlaceholderText("Enter Street Name")
        self.add_house_name_button.setPlaceholderText("Enter House Name")

        self.dialog_layout.addWidget(self.add_first_name_button)
        self.dialog_layout.addWidget(self.add_last_name_button)
        self.dialog_layout.addWidget(self.add_dob_button)
        self.dialog_layout.addWidget(self.add_town_name_button)
        self.dialog_layout.addWidget(self.add_street_name_button)
        self.dialog_layout.addWidget(self.add_house_name_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.insert_member)


    def insert_member(self):
        values = [self.add_first_name_button.text(),
                  self.add_last_name_button.text(),
                  self.add_dob_button.text(),
                  self.add_town_name_button.text(),
                  self.add_street_name_button.text(),
                  self.add_house_name_button.text()]

        #if values[0
    
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = "insert into Member(MemberFirstName,MemberLastName,MemberTownName,MemberStreetName,MemberHouseNameOrNumber,MemberDateOfBirth) values (?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()
        

class EnterParentDataDialog(EnterDataDialog):
    """this class provides a dialog for entering member data"""
    def __init__(self):
        super().__init__()

        self.add_first_name_button = QLineEdit()
        self.add_last_name_button = QLineEdit()
        self.add_town_name_button = QLineEdit()
        self.add_street_name_button = QLineEdit()
        self.add_house_name_button = QLineEdit()
        self.add_email_button = QLineEdit()
        self.add_phone_number_button = QLineEdit()
        self.accept_button = QPushButton("Accept")

        self.add_first_name_button.setPlaceholderText("Enter First Name")
        self.add_last_name_button.setPlaceholderText("Enter Last Name")
        self.add_town_name_button.setPlaceholderText("Enter Town Name")
        self.add_street_name_button.setPlaceholderText("Enter Street Name")
        self.add_house_name_button.setPlaceholderText("Enter House Name")
        self.add_email_button.setPlaceholderText("Enter Email Address")
        self.add_phone_number_button.setPlaceholderText("Enter Phone Number")
        
        self.dialog_layout.addWidget(self.add_first_name_button)
        self.dialog_layout.addWidget(self.add_last_name_button)
        self.dialog_layout.addWidget(self.add_town_name_button)
        self.dialog_layout.addWidget(self.add_street_name_button)
        self.dialog_layout.addWidget(self.add_house_name_button)
        self.dialog_layout.addWidget(self.add_email_button)
        self.dialog_layout.addWidget(self.add_phone_number_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.insert_parent)
        

    def insert_parent(self):
        values = (self.add_first_name_button.text(),
                  self.add_last_name_button.text(),
                  self.add_town_name_button.text(),
                  self.add_street_name_button.text(),
                  self.add_house_name_button.text(),
                  self.add_email_button.text(),
                  self.add_phone_number_button.text())
        
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = "insert into Parent(ParentFirstName,ParentLastName,ParentTownName,ParentStreetName,ParentHouseNameOrNumber,ParentEmail,parentPhoneNumber) values (?,?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()
            
