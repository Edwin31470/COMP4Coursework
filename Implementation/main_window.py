import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SQLConnection import *
from DisplayWidget import *
from AddData import *
from EditData import *
from DeleteData import *
from ManageInvoices import *
from SendInvoices import *
from SortingTable import *
from SearchingData import *

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
        self.email_invoices = QAction("Email Invoices",self)
        self.report_invoice = QAction("Report Invoice",self)
        

        #Create the menu bar
        self.menu_bar = QMenuBar()
        self.database_toolbar = QToolBar()
        self.manage_data_toolbar = QToolBar()
        self.send_invoices_toolbar = QToolBar()
        self.reports_toolbar = QToolBar()
        self.display_database_menu = self.menu_bar.addMenu("Display Database")
        self.manage_data_menu = self.menu_bar.addMenu("Manage Data")
        self.send_invoices_menu = self.menu_bar.addMenu("Send Invoices")
        self.reports_menu = self.menu_bar.addMenu("Reports")
        

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
        self.send_invoices_menu.addAction(self.print_invoices)
        self.send_invoices_menu.addAction(self.email_invoices)
        self.reports_menu.addAction(self.report_invoice)

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
        self.send_invoices_toolbar.addAction(self.print_invoices)
        self.send_invoices_toolbar.addAction(self.email_invoices)
        self.reports_toolbar.addAction(self.report_invoice)

        #Add toolbar
        self.addToolBar(self.database_toolbar)
        self.addToolBar(self.manage_data_toolbar)
        self.addToolBar(self.send_invoices_toolbar)
        self.addToolBar(self.reports_toolbar)

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
        self.email_invoices.triggered.connect(self.email_invoice_data)
        self.report_invoice.triggered.connect(self.report_invoice_data)

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


    def show_member_table(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.display_widget.show_table("Member")

    def show_parent_table(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.display_widget.show_table("Parent")

    def show_invoice_table(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.display_widget.show_table("Invoice")
    
    def show_invoice_query(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()   
        query = self.connection.show_invoices()
        self.display_widget.show_results(query)
        




    def show_member(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        
        query = self.connection.show_members()
        self.display_widget.show_results(query)

        self.search_widget = SearchWidgetMembers()
        self.search_widget.order_combobox.currentIndexChanged.connect(self.search_member)
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.display_widget)

        self.main_widget.setLayout(self.main_layout)
        
        self.setCentralWidget(self.main_widget)

        
    def search_member(self):
        index = self.search_widget.order_combobox.currentIndex()
        if index == 0:
            query = self.connection.show_members()
        if index == 1:
            query = self.connection.order_member_data("MemberDateOfBirth","ASC")
        if index == 2:
            query = self.connection.order_member_data("MemberFirstName","ASC")
        if index == 3:
            query = self.connection.order_member_data("MemberFirstName","DESC")
        if index == 4:
            query = self.connection.order_member_data("MemberLastName","ASC")
        if index == 5:
            query = self.connection.order_member_data("MemberLastName","DESC")
        if index == 6:
            query = self.connection.order_member_data("MemberTownName","ASC")
        if index == 7:
            query = self.connection.order_member_data("MemberTownName","DESC")
        self.display_widget.model.setQuery(query)
        self.display_widget.results_table.show()

    def show_parent(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        
        query = self.connection.show_parents()
        self.display_widget.show_results(query)

        self.search_widget = SearchWidgetParents()
        self.search_widget.order_combobox.currentIndexChanged.connect(self.search_parent)
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.display_widget)

        self.main_widget.setLayout(self.main_layout)
        
        self.setCentralWidget(self.main_widget)

    def search_parent(self):
        index = self.search_widget.order_combobox.currentIndex()
        if index == 0:
            query = self.connection.show_parents()
        if index == 1:
            query = self.connection.order_parent_data("ParentFirstName","ASC")
        if index == 2:
            query = self.connection.order_parent_data("ParentFirstName","DESC")
        if index == 3:
            query = self.connection.order_parent_data("ParentLastName","ASC")
        if index == 4:
            query = self.connection.order_parent_data("ParentLastName","DESC")
        if index == 5:
            query = self.connection.order_parent_data("ParentTownName","ASC")
        if index == 6:
            query = self.connection.order_parent_data("ParentTownName","DESC")
        self.display_widget.model.setQuery(query)
        self.display_widget.results_table.show()

    def show_invoice(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        
        query = self.connection.show_invoices()
        self.display_widget.show_results(query)

        self.search_widget = SearchWidgetInvoice()
        self.search_widget.order_combobox.currentIndexChanged.connect(self.search_invoice)
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.display_widget)

        self.main_widget.setLayout(self.main_layout)
        
        self.setCentralWidget(self.main_widget)

    def search_invoice(self):
        index = self.search_widget.order_combobox.currentIndex()
        if index == 0:
            query = self.connection.show_invoices()
        if index == 1:
            query = self.connection.order_invoice_data("DateInvoiceWasSent","ASC")
        if index == 2:
            query = self.connection.order_invoice_data("ParentFirstName","ASC")
        if index == 3:
            query = self.connection.order_invoice_data("ParentFirstName","DESC")
        if index == 4:
            query = self.connection.order_invoice_data("ParentLastName","ASC")
        if index == 5:
            query = self.connection.order_invoice_data("ParentLastName","DESC")
        if index == 6:
            query = self.connection.order_invoice_data("WasInvoicePaid","ASC")
        self.display_widget.model.setQuery(query)
        self.display_widget.results_table.show()

        
    def add_member_data(self):
        self.show_member_table()

        self.data_dialog = EnterMemberDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        

    def edit_member_data(self):        
        self.show_member_table()

        self.search_dialog = SearchDialog()
        
        self.search_dialog.updatedData.connect(self.return_searched_data_member)

        self.label = QLabel("Click on a field to edit it.")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.label)
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
        self.show_member_table()

        self.search_dialog = SearchDialog()
        self.search_dialog.updatedData.connect(self.return_searched_data_member)

        self.display_widget.results_table.doubleClicked.connect(self.delete_row_clicked)

        self.label = QLabel("Double click a row to delete.")
        self.label.setAlignment(Qt.AlignCenter)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.display_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def delete_row_clicked(self):
        row = self.display_widget.results_table.selectedIndexes()[0].row()
        self.display_widget.model.removeRow(row)
        
    
    def add_parent_data(self):
        self.show_parent_table()

        self.data_dialog = EnterParentDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def edit_parent_data(self):        
        self.show_parent_table()
        
        self.search_dialog = SearchDialogParent()
        
        self.search_dialog.updatedData.connect(self.return_searched_data_parent)

        self.label = QLabel("Click on a field to edit it.")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.label)
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
        self.show_parent_table()

        self.search_dialog = SearchDialogParent()
        self.search_dialog.updatedData.connect(self.return_searched_data_parent)

        self.display_widget.results_table.doubleClicked.connect(self.delete_row_clicked)

        self.label = QLabel("Double click a row to delete.")
        self.label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.display_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def manage_invoice_data(self):
        self.show_invoice_query()

        self.display_widget_2 = DisplayWidget()
        self.display_widget_2.show_table("Parent")

        self.choose_button = ChooseOption()
        self.data_dialog = EnterInvoiceData()
        self.choose_button.addData.connect(self.add_invoice_data)
        self.choose_button.deleteData.connect(self.delete_invoice_data)

        self.label_layout = QHBoxLayout()
        self.parent_label = QLabel("Parent Table")
        self.parent_label.setAlignment(Qt.AlignCenter)
        self.invoice_label = QLabel("Invoice Table")
        self.invoice_label.setAlignment(Qt.AlignCenter)
        self.label_layout.addWidget(self.parent_label)
        self.label_layout.addWidget(self.invoice_label)
        self.label_widget = QWidget()
        self.label_widget.setLayout(self.label_layout)
        
        self.table_layout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.tables = QWidget()
        self.table_layout.addWidget(self.display_widget_2)
        self.table_layout.addWidget(self.display_widget)
        self.tables.setLayout(self.table_layout)
        self.layout.addWidget(self.label_widget)
        self.layout.addWidget(self.tables)
        self.layout.addWidget(self.choose_button)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def delete_invoice_data(self):
        self.show_invoice_query()

        self.search_dialog = SearchDialogParent()
        self.search_dialog.updatedData.connect(self.return_searched_data_parent)

        self.display_widget.results_table.doubleClicked.connect(self.delete_row_clicked)

        self.label = QLabel("Double click a row to delete.")
        self.label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.display_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def add_invoice_data(self):
        self.show_invoice_query()

        self.data_dialog = EnterInvoiceData()
        self.data_dialog.updatedData.connect(self.add_invoice_data)

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

    def print_invoice_data(self):
        invoice = SendInvoiceData()
        invoice.print_preview()

    def report_invoice_data(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.report_invoices()
        self.display_widget.show_results(query)

    def email_invoice_data(self):
        invoice = EmailInvoice()
        invoice.exec_()
        values = invoice.return_values()
        print(values)
        invoice.email_document(values[0],values[1],values[2],values[3])


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec()




    
