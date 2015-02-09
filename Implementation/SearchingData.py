import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
