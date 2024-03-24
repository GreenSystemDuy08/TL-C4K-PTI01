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
        self.bt_next.clicked.connect(self.showSetup3)
    def showSetup3(self):
        if not self.chb_accept.isChecked():
            msg_box.setText("Please read and agree to the terms of this Application!")
            msg_box.exec()
        if self.chb_accept.isChecked():
            Setup3.show()
            self.close()

class Setup3Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup3.ui", self)
        self.bt_install.clicked.connect(self.showSetup4)
        self.bt_repair.clicked.connect(self.showRepair)
    def showRepair(self):
        Repair.show()
    def showSetup4(self):
        Setup4.show()
        self.close()

class RepairPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/Repair.ui", self)

class Setup4Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup4.ui", self)
        self.bt_next.clicked.connect(self.showSetupFinish)
    def showSetupFinish(self):
        SetupFinish.show()
        self.close()

class SetupFinishPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/SetupFinish.ui", self)
        self.bt_finish.clicked.connect(self.showMain)
    def showMain(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainPage = Setup1()
    MainPage.show()
    Setup2 = Setup2Page()
    Setup3 = Setup3Page()
    Setup4 = Setup4Page()
    SetupFinish = SetupFinishPage()
    Repair = RepairPage()
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Online Shopping Warning")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    sys.exit(app.exec())