import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(button)
        self.setWindowTitle("My App")
        button = QPushButton("Log In")
        lb_username = QLabel("Username")
        
        # button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
msg_box = QMessageBox()
msg_box.setWindowTitle("Application Warning!")
msg_box.setIcon(QMessageBox.Icon.Warning)
msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
msg_box.setStyleSheet("background-color: #F8F2EC")
sys.exit(msg_box.exec())