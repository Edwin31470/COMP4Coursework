
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SearchWidget(QWidget):
    """this class provides a widget for entering data"""
    def __init__(self):
        super().__init__()
        
        self.main_layout = QHBoxLayout()

        self.label = QLabel("Order by:")
        self.label.setFixedWidth(50)
        self.order_combobox = QComboBox()
        #self.order_combobox.setFixedWidth(150)

        self.blank_widget = QWidget()
        self.blank_widget.setFixedWidth(1000)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.order_combobox)
        self.main_layout.addWidget(self.blank_widget)
        
        self.setLayout(self.main_layout)

    def return_value(self):
        return self.order_combobox.currentIndex()

class SearchWidgetMembers(SearchWidget):
    """This class provides a widget for chosing which way to order data"""
    def __init__(self):
        super().__init__()

        items = "","Date of Birth","First Name (A-Z)","First name (Z-A)","Last Name (A-Z)","Last Name (Z-A)","Town Name (A-Z)","Town Name (Z-A)"

        self.order_combobox.addItems(items)
        
class SearchWidgetParents(SearchWidget):
    """This class provides a widget for chosing which way to order data"""
    def __init__(self):
        super().__init__()

        items = "","First Name (A-Z)","First name (Z-A)","Last Name (A-Z)","Last Name (Z-A)","Town Name (A-Z)","Town Name (Z-A)"
                
        self.order_combobox.addItems(items)

class SearchWidgetInvoice(SearchWidget):
    """This class provides a widget for chosing which way to order data"""
    def __init__(self):
        super().__init__()

        items = "","Date Sent","Parent First Name (A-Z)","Parent First name (Z-A)","Parent Last Name (A-Z)","Parent Last Name (Z-A)","Was Invoice Paid"
                
        self.order_combobox.addItems(items)
