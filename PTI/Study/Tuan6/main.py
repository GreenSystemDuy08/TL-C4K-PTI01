import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("listwidget.ui", self)

        self.ls = ["Dog", "Cat", "Duck"]
        self.ui.listWidget.addItems(self.ls)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())