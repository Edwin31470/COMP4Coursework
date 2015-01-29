import sqlite3, smtplib

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SendInvoiceData(QWidget):
    """this class provides a widget for sending invoices"""
    def __init__(self):
        super().__init__()
        
        self.dialog_layout = QVBoxLayout()
        
        self.setLayout(self.dialog_layout)

        

    def create_html(self):
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

        html += """<h1>Invoice to: {0}</h1>""".format("John Smith")

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
    
    def print_preview(self):
        html = self.create_html()
        document = QTextDocument()
        document.setHtml(html)
        print(html)
        self.printer = QPrinter()
        PrintPreview = QPrintPreviewDialog(self.printer, self)
        PrintPreview.paintRequested.connect(document.print_)
        PrintPreview.resize(1600,1000)
        PrintPreview.exec()

    def email_document(self,addressFrom,addressTo,password):
        content = "Test"
        mail = smtplib.SMTP('smtp.hotmail.co.uk','587')

        mail.ehlo()

        mail.starttls()
        
        mail.login(addressFrom,password)

        mail.sendmail(addressFrom,addressTo,content)

        mail.close()
