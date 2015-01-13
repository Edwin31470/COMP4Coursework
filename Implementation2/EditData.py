import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditDataDialog(QDialog):
    """this class provides a dialog for editing data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)      
    

class SearchDialog(QDialog):
    """this class provides a dialog for searching the database"""
    def __init__(self):
        super().__init__()

        self.dialog_layout = QVBoxLayout()

        self.search_first_name = QLineEdit()
        self.search_last_name = QLineEdit()
        self.search_town_name = QLineEdit()
        self.search_street_name = QLineEdit()
        self.accept_button = QPushButton("Accept")

        self.search_first_name.setPlaceholderText("First Name")
        self.search_last_name.setPlaceholderText("Last Name")
        self.search_town_name.setPlaceholderText("Town Name")
        self.search_street_name.setPlaceholderText("Street Name")

        self.dialog_layout.addWidget(self.search_first_name)
        self.dialog_layout.addWidget(self.search_last_name)
        self.dialog_layout.addWidget(self.search_town_name)
        self.dialog_layout.addWidget(self.search_street_name)

        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.close)

        

class EditMemberDataDialog(EditDataDialog):
    """this class provides a dialog for editing member data"""
    def __init__(self):
        super().__init__()

        self.memberID_button = QLineEdit()
        self.field_to_edit = QLineEdit()
        self.data_to_add_button = QLineEdit()
        self.accept_button = QPushButton("Accept")

        self.memberID_button.setPlaceholderText("ID of member to edit")
        self.field_to_edit.setPlaceholderText("Field to edit")
        self.data_to_add_button.setPlaceholderText("New data")

        self.dialog_layout.addWidget(self.memberID_button)
        self.dialog_layout.addWidget(self.field_to_edit)
        self.dialog_layout.addWidget(self.data_to_add_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.edit_member)

    def edit_member(self):
        values = (self.data_to_add_button.text(),
                  self.memberID_button.text())
        field = self.field_to_edit.text()
            
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            sql = "update Member set {0}=? where MemberID=?".format(field)
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()

class EditParentDataDialog(EditDataDialog):
    """this class provides a dialog for editing member data"""
    def __init__(self):
        super().__init__()

        self.parentID_button = QLineEdit()
        self.field_to_edit = QLineEdit()
        self.data_to_add_button = QLineEdit()
        self.accept_button = QPushButton("Accept")

        self.parentID_button.setPlaceholderText("ID of member to edit")
        self.field_to_edit.setPlaceholderText("Field to edit")
        self.data_to_add_button.setPlaceholderText("New data")

        self.dialog_layout.addWidget(self.parentID_button)
        self.dialog_layout.addWidget(self.field_to_edit)
        self.dialog_layout.addWidget(self.data_to_add_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.edit_parent)

    def edit_parent(self):
        values = (self.data_to_add_button.text(),
                  self.parentID_button.text())
        field = self.field_to_edit.text()
            
        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            sql = "update Parent set {0}=? where ParentID=?".format(field)
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()
