import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditDataDialog(QWidget):
    """this class provides a dialog for editing data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)
        

class SearchDialog(QWidget):
    """this class provides a dialog for searching the database"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.dialog_layout = QHBoxLayout()

        self.label = QLabel("Search for a member:")
        self.search_for_member = QLineEdit()

        self.search_for_member.textChanged.connect(self.update_data)        

        self.dialog_layout.addWidget(self.label)
        self.dialog_layout.addWidget(self.search_for_member)

        self.setLayout(self.dialog_layout)

    def return_searched(self):
        values = (self.search_for_member.text(),)
        print("Raw value: ",values)

        return values

    def update_data(self):
        self.updatedData.emit()
        print("Emitted")

class SearchDialogParent(SearchDialog):
    """This class provides a widget for searching for a parent"""
    def __init__(self):
        super().__init__()

        self.label = QLabel("Search for a parent:")
        
class EditMemberDataDialog(EditDataDialog):
    """this class provides a dialog for editing member data"""
    def __init__(self):
        super().__init__()

        self.member_to_search = QLineEdit()
        
        self.memberID_button = QLineEdit()
        self.field_to_edit = QLineEdit()
        self.data_to_add_button = QLineEdit()
        self.accept_button = QPushButton("Accept")

        self.member_to_search.setPlaceholderText("Search for a member")
        
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
