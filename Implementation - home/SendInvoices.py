import sqlite3, smtplib

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SendInvoiceData(QWidget):
    """this class provides a widget for sending invoices"""
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)

        
class PrintInvoice(QDialog):
    """This class provides a dialog box for getting email information"""
    def __init__(self):
        super().__init__()

        


    def create_html(self,name):
        html = ""
        html += """<html>
<head>
<style>
	table, th, td
		{
			border: 1px solid black;
			border-collapse: collapse;
			width: 70%;
		}
	th, td
		{
			padding: 15px;
			text-align: center;
		}
</style>
</head>

<body>"""

        html += """<h1>Invoice to: {0}</h1>""".format(name)

        html += """<h2>Test</h2>

  <p></p>

   <table>
   <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Price</th>
   </tr>
   <tr>
    <td>John</td>
    <td>Smith</td>
    <td>£30</td>
   </tr>
   <tr>
    <td>Edwin</td>
    <td>Jacobs</td>
    <td>£22</td>
   </tr>
   </table>

</body>

</html>"""
        
        return html
    
    def print_preview(self,name):
        html = self.create_html(name)
        document = QTextDocument()
        document.setHtml(html)
        print(html)
        self.printer = QPrinter()
        PrintPreview = QPrintPreviewDialog(self.printer, self)
        PrintPreview.paintRequested.connect(document.print_)
        PrintPreview.resize(1600,1000)
        PrintPreview.exec()


class EmailInvoice(QDialog):
    """This class provides a dialog box to email invoices"""
    def __init__(self):
        super().__init__()

        self.dialog_layout = QVBoxLayout()
        
        self.invoiceID = QLineEdit()
        self.email_address_from = QLineEdit()
        self.email_address_to = QLineEdit()
        self.password = QLineEdit()
        self.accept_button = QPushButton("Accept")
        
        self.invoiceID.setPlaceholderText("Enter InvoiceID to Email")
        self.email_address_from.setPlaceholderText("Enter Email Address")
        self.email_address_to.setPlaceholderText("Enter Parent's Email Address")
        self.password.setPlaceholderText("Enter Email Password")
        self.password.setEchoMode(2)

        self.dialog_layout.addWidget(self.invoiceID)
        self.dialog_layout.addWidget(self.email_address_from)
        self.dialog_layout.addWidget(self.email_address_to)
        self.dialog_layout.addWidget(self.password)
        self.dialog_layout.addWidget(self.accept_button)

        self.setLayout(self.dialog_layout)
        
        self.accept_button.clicked.connect(self.close)

    def return_values(self):
        values = (self.invoiceID.text(),
                  self.email_address_from.text(),
                  self.email_address_to.text(),
                  self.password.text())

        return values
        
    def email_document(self,invoiceID,addressFrom,addressTo,password):
        content = "Test"
        
        mail = smtplib.SMTP('smtp.longroad.ac.uk','587')

        mail.ehlo()

        mail.starttls()
        
        mail.login(addressFrom,password)

        mail.sendmail(addressFrom,addressTo,content)

        mail.close()

