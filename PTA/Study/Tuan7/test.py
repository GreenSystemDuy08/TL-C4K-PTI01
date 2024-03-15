import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QFont

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
    
        self.username = 'admin@example.com'
        self.password = 'admin'

        self.setWindowTitle("Log In") 
        self.resize(400, 200)

        # Create widgets
        self.usernameLabel = QLabel("Username:")
        self.usernameLineEdit = QLineEdit()

        self.passwordLabel = QLabel("Password:")
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.checkBox = QCheckBox('Keep me logged in')

        self.loginButton = QPushButton("Log In")
        self.loginButton.clicked.connect(self.on_button_clicked)

        self.registerLabel = QLabel('Register')
        self.registerLabel.setStyleSheet("color: blue; text-decoration: underline;")
        self.registerLabel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        

        self.forgotPasswordLabel = QLabel('Forget Password')
        self.forgotPasswordLabel.setStyleSheet("color: blue; text-decoration: underline;")
        self.forgotPasswordLabel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        

        # Create layout and add widgets
        layout = QVBoxLayout()

        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.usernameLineEdit)

        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordLineEdit)
        layout.addWidget(self.checkBox)

        layout.addWidget(self.loginButton)

        layout.addWidget(self.registerLabel)
        layout.addWidget(self.forgotPasswordLabel)

        # Set the layout for a central widget
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def on_button_clicked(self):
        entered_username = self.usernameLineEdit.text()
        entered_password = self.passwordLineEdit.text()
        if entered_username == self.username and entered_password == self.password:
            QMessageBox.information(None, 'Login Status', 'Log in successful')
        else:
            QMessageBox.warning(None, 'Login Status', 'Wrong email or password')

    def register(self, event):
        # Implement registration logic here
        pass
    
    def forgotpassword(self, event):
        # Implement forgot password logic here
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())