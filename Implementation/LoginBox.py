import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from StyleSheet import *


class LoginScreen(QDialog):
    """this class provides a dialog for logging in"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Screen")
        self.setStyleSheet(css_login)
        
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.usernameLabel = QLabel("Username:")
        self.passwordLabel = QLabel("Password:")
        self.accept_button = QPushButton("Enter")
        self.label = QLabel("Please enter the username and password")

        self.username.setPlaceholderText("Username")
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(2)

        self.login_layout = QGridLayout()

        self.login_layout.addWidget(self.usernameLabel, 0, 0)
        self.login_layout.addWidget(self.passwordLabel, 1, 0)
        self.login_layout.addWidget(self.username, 0, 1)
        self.login_layout.addWidget(self.password, 1, 1)
        self.login_layout.addWidget(self.accept_button, 1, 2)
        self.login_widget = QWidget()
        self.login_widget.setLayout(self.login_layout)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.login_widget)
        
        self.setLayout(self.layout)

class IncorrectDetails(QDialog):
    """this class provides feedback to the user's username and password"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.setStyleSheet(css_login)

        self.close_button = QPushButton("Close")
        self.blank_label = QLabel()

        self.button_layout =  QHBoxLayout()
        self.button_layout.addWidget(self.blank_label)
        self.button_layout.addWidget(self.close_button)
        self.button_widget = QWidget()
        self.button_widget.setLayout(self.button_layout)

        self.close_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
        
    def incorrect_username(self):
        self.label = QLabel("The username you entered was incorrect.")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_widget)
        
        self.setLayout(self.layout)
        self.show()


    def incorrect_password(self):
        self.label = QLabel("The password you entered was incorrect.")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_widget)
        
        self.setLayout(self.layout)
        self.show()


    def incorrect_username_and_password(self):
        self.label = QLabel("The username and password you entered were incorrect.")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_widget)
        
        self.setLayout(self.layout)
        self.show()
