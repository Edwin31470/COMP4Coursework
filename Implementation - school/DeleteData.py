import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DeleteDataDialog(QDialog):
    """this class provides a dialog for editing data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)      

    
class DeleteMemberDataDialog(DeleteDataDialog):
    """this class provides a dialog for editing member data"""
    def __init__(self):
        super().__init__()

        self.memberID_button = QLineEdit()
        self.accept_button = QPushButton("Delete")

        self.memberID_button.setPlaceholderText("ID of member to delete")
        
        self.dialog_layout.addWidget(self.memberID_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.delete_member)
        

    def delete_member(self):
        values = (self.memberID_button.text(),)

        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            sql = "delete from Member where MemberID = ?"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()

        self.memberID_button.setText("")

class DeleteParentDataDialog(DeleteDataDialog):
    """this class provides a dialog for editing member data"""
    def __init__(self):
        super().__init__()

        self.parentID_button = QLineEdit()
        self.accept_button = QPushButton("Delete")

        self.parentID_button.setPlaceholderText("ID of parent to delete")
        
        self.dialog_layout.addWidget(self.parentID_button)
        self.dialog_layout.addWidget(self.accept_button)

        self.accept_button.clicked.connect(self.delete_parent)

    def delete_parent(self):
        values = (self.parentID_button.text(),)

        with sqlite3.connect("scout_database.db") as db:
            cursor = db.cursor()
            sql = "delete from Parent where ParentID = ?"
            cursor.execute(sql,values)
            db.commit()

        self.updatedData.emit()

        self.parentID_button.setText("")
