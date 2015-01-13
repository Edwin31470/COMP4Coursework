from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None
        

    def display_results_layout(self):
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()
        self.results_layout.addWidget(self.results_table)
        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)
        self.stacked_layout.addWidget(self.results_widget)

    def show_results(self,query):
        self.display_results_layout()
        if not self.model or not isinstance(self.model,QSqlQueryModel):
            self.model = QSqlQueryModel()
        self.model.setQuery(query)      
        self.results_table.setModel(self.model)
        self.results_table.show()

    def show_table(self,tableName):
        self.display_results_layout()
        if not self.model or not isinstance(self.model,QSqlTableModel):
            self.model = QSqlTableModel()
        self.model.setTable(tableName)
        self.model.select()
        self.results_table.setModel(self.model)
        self.results_table.show()

    def refresh(self):
        self.model.select()
        self.results_table.setModel(self.model)
