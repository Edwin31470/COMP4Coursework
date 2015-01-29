
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SearchWidget(QWidget):
    """this class provides a widget for entering data"""
    updatedData = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.main_layout = QHBoxLayout()

        self.label = QLabel("Order by:")
        self.label.setFixedWidth(50)
        self.order_combobox = QComboBox()
        #self.order_combobox.setFixedWidth(150)

        self.blank_widget = QWidget()
        self.blank_widget.setFixedWidth(1000)
        
        items = "Date of Birth","First Name (A-Z)","First name (Z-A)"
        self.order_combobox.addItems(items)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.order_combobox)
        self.main_layout.addWidget(self.blank_widget)
        
        self.setLayout(self.main_layout)

    def return_value(self):
        return self.order_combobox.currentIndex()
