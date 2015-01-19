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
        #query = self.connection.show_invoices()
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
        
##    def edit_member_data_old(self):
##        search_dialog = SearchDialog()
##        search_dialog.exec_()
##        searched_values = search_dialog.return_searched()
##        print("Searched Values: ",searched_values)
##        for count in range(0,4):
##            print(searched_values[count])
##
##        values = []
##        string = "select * from Member where"
##        if searched_values[0] != "":
##            string += " MemberFirstName = :firstName and"
##            values.append(searched_values[0])
##        if searched_values[1] != "":
##            string += " MemberLastName = :lastName and"
##            values.append(searched_values[1])
##        if searched_values[2] != "":
##            string += " MemberTownName = :townName and"
##            values.append(searched_values[2])
##        if searched_values[3] != "":
##           string += " MemberStreetName = :streetName and"
##           values.append(searched_values[3])
##        print("Pre snipping:",string)
##        string = string[:-4]
##        print("Post snipping:",string)
##
##        query = QSqlQuery(string)
##        #query.prepare(string)
##        print("Values: ",values)
##        print("Values 0: ",values[0])
##        if len(values) > 0:
##            query.bindValue(":firstName",values[0])
##            print("Bound ",values[0])
##        if len(values) > 1:
##            query.bindValue(":lastName",values[1])
##            print("Bound ",values[1])
##        if len(values) > 2:
##            query.bindValue(":townName",values[2])
##            print("Bound ",values[2])
##        if len(values) > 3:
##            query.bindValue(":streetName",values[3])
##            print("Bound ",values[3])
##        
##        if not hasattr(self,"display_widget"):
##            self.display_widget = DisplayWidget()
##        self.display_widget.show_results(query)
##
##        self.data_dialog = EditMemberDataDialog()
##        self.data_dialog.updatedData.connect(self.display_widget.refresh)
##        
##        self.layout = QVBoxLayout()
##        self.layout.addWidget(self.display_widget)
##        self.layout.addWidget(self.data_dialog)
##        self.main_widget = QWidget()
##        self.main_widget.setLayout(self.layout)
##        self.setCentralWidget(self.main_widget)

    def edit_member_data(self):        
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.display_widget.show_table("Member")

        self.search_dialog = SearchDialog()
        searched_values = self.search_dialog.updatedData.connect(self.search_dialog.return_searched)
        #searched_values = self.search_dialog.return_searched()
        print(searched_values)

        self.data_dialog = EditMemberDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_dialog)
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        
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
        self.search_dialog = SearchDialog()

        self.display_widget.show_table("Parent")
        
        self.data_dialog = EditParentDataDialog()
        self.data_dialog.updatedData.connect(self.display_widget.refresh)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.data_dialog)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

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

        self.data_dialog = EnterInvoiceData()
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




    
