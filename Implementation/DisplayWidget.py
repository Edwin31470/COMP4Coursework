from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.display_results_layout()
        self.model = None
        

    def display_results_layout(self):
        self.results_table = QTableView()
        #self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.results_table.setAlternatingRowColors(True)
        self.results_layout = QVBoxLayout()
        self.results_layout.addWidget(self.results_table)
        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)
        self.layout.addWidget(self.results_widget)

    def show_results(self,query):
        if not self.model or not isinstance(self.model,QSqlQueryModel):
            self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.resizeColumnsToContents()
        self.results_table.show()
        

    def show_table(self,tableName):
        if not self.model or not isinstance(self.model,QSqlTableModel):
            self.model = QSqlTableModel()
        self.model.setTable(tableName)
        self.model.select()
        self.results_table.setModel(self.model)
        self.results_table.resizeColumnsToContents()
        self.results_table.show()

    def search_table(self,tableName,sqlFilter):
        if not self.model or not isinstance(self.model,QSqlTableModel):
            self.model = QSqlTableModel()
        self.model.setTable(tableName)
        self.model.setFilter(sqlFilter)
        self.results_table.setModel(self.model)
        self.results_table.show()

    def refresh(self):
        self.model.select()
        self.results_table.setModel(self.model)
