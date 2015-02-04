import sqlite3, re, datetime, calendar

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class EnterDataDialog(QWidget):
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
        self.add_first_name_button.textChanged.connect(self.validate_first_name)
        self.add_last_name_button = QLineEdit()
        self.add_last_name_button.textChanged.connect(self.validate_last_name)      
        self.add_town_name_button = QLineEdit()
        self.add_town_name_button.textChanged.connect(self.validate_town_name)
        self.add_street_name_button = QLineEdit()
        self.add_street_name_button.textChanged.connect(self.validate_street_name)
        self.add_house_name_button = QLineEdit()
        self.add_house_name_button.textChanged.connect(self.validate_house_name)
        self.accept_button = QPushButton("Accept")


        #Creating DoB widget
        self.dob_label = QLabel("Date of birth:")
        self.add_dob_day_button = QComboBox()
        self.add_dob_month_button = QComboBox()
        self.add_dob_year_button = QComboBox()

        currentYear = int(datetime.date.today().strftime("%Y"))
        print(currentYear)

        for count in range(1,32):
            self.add_dob_day_button.addItem(str(count))
        for count in range(1,13):
            self.add_dob_month_button.addItem(str(count))
        for count in range(currentYear - 16,currentYear - 8):
            self.add_dob_year_button.addItem(str(count))
        
        self.dob_layout = QHBoxLayout()
        self.dob_widget = QWidget()
        self.dob_layout.addWidget(self.dob_label)
        self.dob_layout.addWidget(self.add_dob_day_button)
        self.dob_layout.addWidget(self.add_dob_month_button)
        self.dob_layout.addWidget(self.add_dob_year_button)
        self.dob_widget.setLayout(self.dob_layout)
        
        
        self.add_first_name_button.setPlaceholderText("Enter First Name")
        self.add_last_name_button.setPlaceholderText("Enter Last Name")
        self.add_town_name_button.setPlaceholderText("Enter Town Name")
        self.add_street_name_button.setPlaceholderText("Enter Street Name")
        self.add_house_name_button.setPlaceholderText("Enter House Name")

        self.dialog_layout.addWidget(self.add_first_name_button)
        self.dialog_layout.addWidget(self.add_last_name_button)
        self.dialog_layout.addWidget(self.add_town_name_button)
        self.dialog_layout.addWidget(self.add_street_name_button)
        self.dialog_layout.addWidget(self.add_house_name_button)
        self.dialog_layout.addWidget(self.dob_widget)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.insert_member)


    def insert_member(self):
        day = self.add_dob_day_button.itemText(self.add_dob_day_button.currentIndex()) 
        month = self.add_dob_month_button.itemText(self.add_dob_month_button.currentIndex())
        year = self.add_dob_year_button.itemText(self.add_dob_year_button.currentIndex())
        
        if int(day) in range(1,10):
            day = "0" + day
        if int(month) in range(1,10):
            month = "0" + month
        
        dob = year + "/" + month + "/" + day
        print(dob)
        values = (self.add_first_name_button.text(),
                  self.add_last_name_button.text(),
                  self.add_town_name_button.text(),
                  self.add_street_name_button.text(),
                  self.add_house_name_button.text(),
                  dob)
    
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = "insert into Member(MemberFirstName,MemberLastName,MemberTownName,MemberStreetName,MemberHouseNameOrNumber,MemberDateOfBirth) values (?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()

    def validate(self, regularExpression, text):
        self.pattern = re.compile(regularExpression)
        valid = self.pattern.match(text.upper())
        return valid
    
    def validate_first_name(self):
        text = self.add_first_name_button.text()
        self.add_first_name_button.setText(text.capitalize())
        valid = self.validate("^[A-Z]{1,20}$",text)
        if valid:
            self.add_first_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_first_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_last_name(self):
        text = self.add_last_name_button.text()
        self.add_last_name_button.setText(text.capitalize())
        valid = self.validate("^[A-Z]{1,20}$",text)
        if valid:
            self.add_last_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_last_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_town_name(self):
        self.text = self.add_town_name_button.text()
        self.pattern = re.compile("^[A-Z]{1,20}$")
        self.add_town_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
            self.add_town_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_town_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_street_name(self):
        self.text = self.add_street_name_button.text()
        self.pattern = re.compile("^[A-Z\s]{1,20}$")
        self.add_street_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
            self.add_street_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_street_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_house_name(self):
        self.text = self.add_house_name_button.text()
        self.pattern = re.compile("^[A-Z1-9]{1,20}$")
        self.add_house_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
            self.add_house_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_house_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_dob(self):
        self.text = self.add_dob_button.text()
        self.pattern = re.compile("^[0-9]{2}[/][0-9]{2}[/][0-9]{2}$")
        self.add_dob_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
            self.add_dob_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_dob_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

##    def validate_text(self):
##        self.pattern = re.compile("^[A-Z]{1,20}$")
##        valid = self.pattern.match(self.text.upper())
##        
##        self.text = self.add_first_name_button.text()
##        self.add_first_name_button.setText(self.text.capitalize())
##        if valid:
##                self.add_first_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
##        else:
##            self.add_first_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    

    

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

    def validate_first_name(self):
        self.text = self.add_first_name_button.text()
        self.pattern = re.compile("^[A-Z]{1,20}$")
        self.add_first_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_first_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_first_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_last_name(self):
        self.text = self.add_last_name_button.text()
        self.pattern = re.compile("^[A-Z]{1,20}$")
        self.add_last_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_last_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_last_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_town_name(self):
        self.text = self.add_town_name_button.text()
        self.pattern = re.compile("^[A-Z]{1,20}$")
        self.add_town_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_town_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_town_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_street_name(self):
        self.text = self.add_street_name_button.text()
        self.pattern = re.compile("^[A-Z\s]{1,20}$")
        self.add_street_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_street_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_street_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_house_name(self):
        self.text = self.add_house_name_button.text()
        self.pattern = re.compile("^[A-Z1-9]{1,20}$")
        self.add_house_name_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_house_name_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_house_name_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")

    def validate_email(self):
        self.text = self.add_email_button.text()
        self.pattern = re.compile("^[A-Z1-9]{1,20}[@][A-Z1-9.]{1,20}$")
        self.add_email_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_email_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_email_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")


    def validate_house_name(self):
        self.text = self.add_phone_number_button.text()
        self.pattern = re.compile("^[1-9]{11}$")
        self.add_phone_number_button.setText(self.text.capitalize())
        valid = self.pattern.match(self.text.upper())
        if valid:
                self.add_phone_number_button.setStyleSheet("QLineEdit { background-color : rgb(170,255,150);}")
        else:
            self.add_phone_number_button.setStyleSheet("QLineEdit { background-color : rgb(255,70,70);}")            
