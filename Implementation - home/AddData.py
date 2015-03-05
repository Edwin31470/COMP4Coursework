import sqlite3, re, datetime, calendar

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class EnterDataDialog(QWidget):
    """this class provides a dialog for entering data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.add_first_name = QLineEdit()
        self.add_first_name.textChanged.connect(self.validate_first_name)
        self.add_last_name = QLineEdit()
        self.add_last_name.textChanged.connect(self.validate_last_name)      
        self.add_town_name = QLineEdit()
        self.add_town_name.textChanged.connect(self.validate_town_name)
        self.add_street_name = QLineEdit()
        self.add_street_name.textChanged.connect(self.validate_street_name)
        self.add_house_name = QLineEdit()
        self.add_house_name.textChanged.connect(self.validate_house_name)
        self.accept_button = QPushButton("Accept")

        self.add_first_name.setPlaceholderText("Enter First Name")
        self.add_last_name.setPlaceholderText("Enter Last Name")
        self.add_town_name.setPlaceholderText("Enter Town Name")
        self.add_street_name.setPlaceholderText("Enter Street Name")
        self.add_house_name.setPlaceholderText("Enter House Name")

        self.dialog_layout = QVBoxLayout()

        self.dialog_layout.addWidget(self.add_first_name)
        self.dialog_layout.addWidget(self.add_last_name)
        self.dialog_layout.addWidget(self.add_town_name)
        self.dialog_layout.addWidget(self.add_street_name)
        self.dialog_layout.addWidget(self.add_house_name)
        self.dialog_layout.addWidget(self.accept_button)
        
        
        self.setLayout(self.dialog_layout)

        
    def validate(self, regularExpression, text):
        self.pattern = re.compile(regularExpression)
        valid = self.pattern.match(text.upper())
        return valid
    
    def validate_first_name(self):
        text = self.add_first_name.text()
        self.add_first_name.setText(text.capitalize())
        valid = self.validate("^[A-Z-\s]{1,20}$",text)
        if valid:
            self.add_first_name.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_first_name.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_last_name(self):
        text = self.add_last_name.text()
        self.add_last_name.setText(text.capitalize())
        valid = self.validate("^[A-Z-\s]{1,20}$",text)
        if valid:
            self.add_last_name.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_last_name.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_town_name(self):
        text = self.add_town_name.text()
        self.add_town_name.setText(text.capitalize())
        valid = self.validate("^[A-Z-\s]{1,20}$",text)
        if valid:
            self.add_town_name.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_town_name.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_street_name(self):
        text = self.add_street_name.text()
        self.add_street_name.setText(text.capitalize())
        valid = self.validate("^[A-Z-\s]{1,20}$",text)
        if valid:
            self.add_street_name.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_street_name.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_house_name(self):
        text = self.add_house_name.text()
        self.add_house_name.setText(text.capitalize())
        valid = self.validate("^[A-Z1-9-\s]{1,20}$",text)
        if valid:
            self.add_house_name.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_house_name.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

        
class EnterMemberDataDialog(EnterDataDialog):
    """this class provides a dialog for entering member data"""
    def __init__(self):
        super().__init__()
        
        #Creating DoB widget
        self.dob_label = QLabel("Date of birth:")
        self.add_dob_day = QComboBox()
        self.add_dob_month = QComboBox()
        self.add_dob_year = QComboBox()
        self.spacer = QLabel()

        self.dob_label.setFixedWidth(100)
        self.add_dob_day.setFixedWidth(100)
        self.add_dob_month.setFixedWidth(100)
        self.add_dob_year.setFixedWidth(100)

        currentYear = int(datetime.date.today().strftime("%Y"))
        print(currentYear)

        for count in range(1,32):
            self.add_dob_day.addItem(str(count))
        for count in range(1,13):
            self.add_dob_month.addItem(str(count))
        for count in range(currentYear - 16,currentYear - 8):
            self.add_dob_year.addItem(str(count))
        
        self.dob_layout = QHBoxLayout()
        self.dob_widget = QWidget()
        self.dob_layout.addWidget(self.dob_label)
        self.dob_layout.addWidget(self.add_dob_day)
        self.dob_layout.addWidget(self.add_dob_month)
        self.dob_layout.addWidget(self.add_dob_year)
        self.dob_layout.addWidget(self.spacer)
        self.dob_widget.setLayout(self.dob_layout)

        self.dialog_layout.insertWidget(5,self.dob_widget)
        
        
        self.accept_button.clicked.connect(self.insert_member)


    def insert_member(self):
        day = self.add_dob_day.itemText(self.add_dob_day.currentIndex()) 
        month = self.add_dob_month.itemText(self.add_dob_month.currentIndex())
        year = self.add_dob_year.itemText(self.add_dob_year.currentIndex())
        
        if int(day) in range(1,10):
            day = "0" + day
        if int(month) in range(1,10):
            month = "0" + month
        
        dob = year + "/" + month + "/" + day
        print(dob)
        values = (self.add_first_name.text(),
                  self.add_last_name.text(),
                  self.add_town_name.text(),
                  self.add_street_name.text(),
                  self.add_house_name.text(),
                  dob)
    
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

        self.add_email = QLineEdit()
        self.add_phone_number = QLineEdit()


        self.add_email.setPlaceholderText("Enter Email Address")
        self.add_email.textChanged.connect(self.validate_email)
        self.add_phone_number.setPlaceholderText("Enter Phone Number")
        self.add_phone_number.textChanged.connect(self.validate_phone_number)

        
        self.dialog_layout.insertWidget(5,self.add_email)
        self.dialog_layout.insertWidget(6,self.add_phone_number)


        self.accept_button.clicked.connect(self.insert_parent)
        

    def insert_parent(self):
        values = (self.add_first_name.text(),
                  self.add_last_name.text(),
                  self.add_town_name.text(),
                  self.add_street_name.text(),
                  self.add_house_name.text(),
                  self.add_email.text(),
                  self.add_phone_number.text())
        
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = "insert into Parent(ParentFirstName,ParentLastName,ParentTownName,ParentStreetName,ParentHouseNameOrNumber,ParentEmail,parentPhoneNumber) values (?,?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()


    def validate_email(self):
        text = self.add_email.text()
        valid = self.validate("^[A-Z1-9-]{1,20}[@][A-Z1-9.]{0,20}$",text)
        if valid:
            self.add_email.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        elif '@' not in text:
            self.add_email.setStyleSheet("QLineEdit { background-color : rgb(255,194,0);}")
        elif not valid:
            self.add_email.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")
                

    def validate_phone_number(self):
        text = self.add_phone_number.text()
        valid = self.validate("^[0-9]*$",text)
        if valid and len(text) < 11:
            self.add_phone_number.setStyleSheet("QLineEdit { background-color : rgb(255,194,0);}")
        elif valid and len(text) == 11:
            self.add_phone_number.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_phone_number.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")
