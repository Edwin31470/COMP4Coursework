from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MainWindow(QMainWindow):
    """ This is a test for the printing function """

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Printing Test")
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)
        self.mainLayout()

        
    def mainLayout(self):

        self.layout = QHBoxLayout()
        self.printButton = QPushButton("Print")

        self.layout.addWidget(self.printButton)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)

        self.setCentralWidget(self.mainWidget)

        self.printButton.clicked.connect(self.printViaHtml)

    def getCurrentDate(self,dateFormat):
        date = QDate.currentDate().toString(dateFormat)
        return date
        

    def printViaHtml(self):

        html = self.statementHtml()
        html += ("<h1> Hello this is a test print!</h1>"
                 "<hr/><p style='font-family:times;color:red;'> {0} This is testing the print functionality"
                 "of printing something in html from PyQt4.</p>").format(date)

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)
        else:
            print("The print process has failed!")

        print(html)
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
