import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox , QWidget
from PyQt6 import uic

class Setup1(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup1.ui", self)
        self.bt_next.clicked.connect(self.showSetup2)
    def showSetup2(self):
        Setup2.show()
        self.close()

class Setup2Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup2.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainPage = Setup1()
    Setup2 = Setup2Page()
    MainPage.show()
    sys.exit(app.exec())