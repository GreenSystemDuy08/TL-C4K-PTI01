import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!!!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")
    def the_button_was_toggled(self, checked):
        print("Check?",checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
msg_box = QMessageBox()
msg_box.setWindowTitle("Application Warning!")
msg_box.setIcon(QMessageBox.Icon.Warning)
msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
sys.exit(msg_box.exec())