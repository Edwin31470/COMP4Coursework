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
