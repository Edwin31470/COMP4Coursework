import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SQLConnection import *
from DisplayWidget import *
from AddData import *
from EditData import *
from DeleteData import *
from ManageInvoices import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Program")
        
        #Create Actions
        self.display_member = QAction("Display Member",self)
        self.display_parent = QAction("Display Parent",self)
        self.display_invoices = QAction("Display Invoices",self)
        self.add_member = QAction("Add Member",self)
        self.edit_member = QAction("Edit Member",self)
        self.delete_member = QAction("Delete Member",self)
        self.add_parent = QAction("Add Parent",self)
        self.edit_parent = QAction("Edit Parent",self)
        self.delete_parent = QAction("Delete Parent",self)
        self.manage_invoices = QAction("Manage Invoices",self)
        self.print_invoices = QAction("Print Invoices",self)
        

        #Create the menu bar
        self.menu_bar = QMenuBar()
        self.database_toolbar = QToolBar()
        self.manage_data_toolbar = QToolBar()
        self.print_invoices_toolbar = QToolBar()
        self.display_database_menu = self.menu_bar.addMenu("Display Database")
        self.manage_data_menu = self.menu_bar.addMenu("Manage Data")
        self.print_invoices_menu = self.menu_bar.addMenu("Print Invoices")

        #Create toolbar
        self.display_database_menu.addAction(self.display_member)
        self.display_database_menu.addAction(self.display_parent)
        self.display_database_menu.addAction(self.display_invoices)
        self.manage_data_menu.addAction(self.add_member)
        self.manage_data_menu.addAction(self.edit_member)
        self.manage_data_menu.addAction(self.delete_member)
        self.manage_data_menu.addAction(self.add_parent)
        self.manage_data_menu.addAction(self.edit_parent)
        self.manage_data_menu.addAction(self.delete_parent)
        self.manage_data_menu.addAction(self.manage_invoices)
        self.print_invoices_menu.addAction(self.print_invoices)

        #Add toolbars to window
        self.database_toolbar.addAction(self.display_member)
        self.database_toolbar.addAction(self.display_parent)
        self.database_toolbar.addAction(self.display_invoices)
        self.manage_data_toolbar.addAction(self.add_member)
        self.manage_data_toolbar.addAction(self.edit_member)
        self.manage_data_toolbar.addAction(self.delete_member)
        self.manage_data_toolbar.addAction(self.add_parent)
        self.manage_data_toolbar.addAction(self.edit_parent)
        self.manage_data_toolbar.addAction(self.delete_parent)
        self.manage_data_toolbar.addAction(self.manage_invoices)
        self.print_invoices_toolbar.addAction(self.print_invoices)

        #Add toolbar
        self.addToolBar(self.database_toolbar)
        self.addToolBar(self.manage_data_toolbar)
        self.addToolBar(self.print_invoices_toolbar)

        #Set menu bar
        self.setMenuBar(self.menu_bar)

        #Create Connections
        self.display_member.triggered.connect(self.show_member)
        self.display_parent.triggered.connect(self.show_parent)
        self.display_invoices.triggered.connect(self.show_invoice)
        self.add_member.triggered.connect(self.add_member_data)
        self.edit_member.triggered.connect(self.edit_member_data)
        self.delete_member.triggered.connect(self.delete_member_data)
        self.add_parent.triggered.connect(self.add_parent_data)
        self.edit_parent.triggered.connect(self.edit_parent_data)
        self.delete_parent.triggered.connect(self.delete_parent_data)
        self.manage_invoices.triggered.connect(self.manage_invoice_data)
        self.print_invoices.triggered.connect(self.print_invoice_data)

        #Resizing
        self.resize(1200,800)

        #Opening Database
        self.open_database()
        self.show_member()
        
    def open_database(self):
        path = "scout_database.db"
        print("Path: ",path)
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print("Opened Ok: ",ok)


    def show_member(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        self.display_widget.show_table("Member")

    def show_parent(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        self.display_widget.show_table("Parent")

    def show_invoice(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        self.display_widget.show_table("Invoice")


        
    def add_member_data(self):
        self.show_member()

        self.data_dialog = EnterMemberDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        

    def edit_member_data(self):        
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.display_widget.show_table("Member")

        self.search_dialog = SearchDialog()
        
        self.search_dialog.updatedData.connect(self.return_searched_data_member)
        
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.display_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def return_searched_data_member(self):
        text = self.search_dialog.search_for_member.text()
        filter_query = "MemberFirstName like '%{0}%' or MemberLastName like '%{0}%'".format(text)
        self.display_widget.model.setFilter(filter_query)
        self.display_widget.model.select()
        self.display_widget.results_table.setModel(self.display_widget.model)
        
    def delete_member_data(self):
        self.show_member()

        self.data_dialog = DeleteMemberDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def add_parent_data(self):
        self.show_parent()

        self.data_dialog = EnterParentDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def edit_parent_data(self):        
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.display_widget.show_table("Parent")

        self.search_dialog = SearchDialogParent()
        
        self.search_dialog.updatedData.connect(self.return_searched_data_parent)
        
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.display_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def return_searched_data_parent(self):
        text = self.search_dialog.search_for_member.text()
        filter_query = "ParentFirstName like '%{0}%' or ParentLastName like '%{0}%'".format(text)
        self.display_widget.model.setFilter(filter_query)
        self.display_widget.model.select()
        self.display_widget.results_table.setModel(self.display_widget.model)

    def delete_parent_data(self):
        self.show_parent()

        self.data_dialog = DeleteParentDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def manage_invoice_data(self):
        self.show_invoice()

        if not hasattr(self,"display_widget_2"):
            self.display_widget_2 = DisplayWidget()
        self.display_widget_2.show_table("Parent")

        self.data_dialog = EnterInvoiceData()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.table_layout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.tables = QWidget()
        self.table_layout.addWidget(self.display_widget_2)
        self.table_layout.addWidget(self.display_widget)
        self.tables.setLayout(self.table_layout)
        self.layout.addWidget(self.tables)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def add_invoice_data(self):
        self.show_invoice()

        self.data_dialog = EnterInvoiceData()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def delete_invoice(self):
        self.show_invoice()

        self.data_dialog = DeleteParentDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    
    def print_invoice_data(self):
        print("Working")

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec()




    
