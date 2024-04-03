import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox , QWidget
from PyQt6 import uic

class MainNotePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/mainnote.ui", self)
        self.bt_edit1.clicked.connect(self.showEditNote)
        self.bt_edit2.clicked.connect(self.showEditNote)
        self.bt_add.clicked.connect(self.showCaution)
        self.bt_quit.clicked.connect(self.Close)
        self.bt_save.clicked.connect(self.showSignIn)
    def showSignIn(self):
        SignIn.show()
        self.close()
    def Close(self):
        self.close()
    def showCaution(self):
        msg_box1.setText("The notes page has been added successfully!")
        msg_box1.exec()
        return
    def showEditNote(self):
        EditNote.show()

class EditNotePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/editNote.ui", self)
        self.bt_save.clicked.connect(self.Close)
    def Close(self):
        self.close()

class AdminPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/AdminPage.ui", self)
        self.bt_add.clicked.connect(self.showCaution)
        self.bt_save.clicked.connect(self.showSignIn)
        self.bt_exit.clicked.connect(self.showSignIn)
        self.bt_tool1.clicked.connect(self.showTool1)
        self.bt_tool2.clicked.connect(self.showTool2)
        self.bt_edit1.clicked.connect(self.showEditNote)
        self.bt_edit2.clicked.connect(self.showEditNote)
    def showCaution(self):
        msg_box1.setText("The notes page has been added successfully!")
        msg_box1.exec()
        return
    def showTool1(self):
        Tool1.show()
        self.close()
    def showTool2(self):
        Tool2.show()
        self.close()
    def showSignIn(self):
        SignIn.show()
        self.close()
    def showEditNote(self):
        EditNote.show()
        self.close()
class Tool1Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/AdminTool - note1.ui", self)
        self.bt_back.clicked.connect(self.back)
        self.bt_remove.clicked.connect(self.Caution)
    def back(self):
        AdminTool.show()
        self.close()
    def Caution(self):
        msg_box1.setText("The notes page has been successfully removed!")
        msg_box1.exec()
        return

class Tool2Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/AdminTool - note2.ui", self)
        self.bt_back.clicked.connect(self.back)
        self.bt_remove.clicked.connect(self.Caution)
    def Caution(self):
        msg_box1.setText("The notes page has been successfully removed!")
        msg_box1.exec()
        return
    def back(self):
        AdminTool.show()
        self.close()


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
        if not self.cb_language.currentIndex():
            msg_box.setText("Please check and select language to install!")
            msg_box.exec()
            return

        elif not self.cb_edition.currentIndex():
            msg_box.setText("Please check and select this app edtion!")
            msg_box.exec()
            return

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
        self.bt_install.clicked.connect(self.showSetupFinish)
    def showSetupFinish(self):
        SetupFinish.show()
        self.close()

class SetupFinishPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/SetupFinish.ui", self)
        self.bt_finish.clicked.connect(self.showSignIn)
    def showSignIn(self):
        SignIn.show()
        self.close()

class SignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/dangnhap.ui", self)
        self.bt_login.clicked.connect(self.checkLogin)
        self.bt_register.clicked.connect(self.showSignUp)
        self.bt_continue.clicked.connect(self.showMainPage)
    def showMainPage(self):
        msg_box1.setText("Going forward, sign in if you want more features!")
        msg_box1.exec()
        MainNote.show()
        self.close()
    def showSignUp(self):
        SignUp.show()
        self.close()
    def quit(self):
        self.close()
    def checkLogin(self):
        email = self.le_email.text()
        password = self.le_password.text()

        if not email:
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        if email == "admin@gmail.com" and password == "admin":
            self.close()
            AdminTool.show()
        elif len(password) < 8:
            msg_box.setText("Password is too short! The program requires a password of more than 8 characters!")
            msg_box.exec()
            return
        elif '@' in email:
            msg_box.setText("Standard Account")
            msg_box.exec()
            MainNote.show()
            self.close()
            return
        else:
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()

class SignUpPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/dangky.ui", self)
        self.bt_signup.clicked.connect(self.SignUp)
        self.bt_already.clicked.connect(self.Back)
    def Back(self):
        SignIn.show()
        self.close()
    def SignUp(self):
        self.name = self.le_fullname.text()
        email = self.le_account.text()
        password = self.le_password.text()
        

        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
        elif '@' not in email:
            msg_box.setText("Email invalidate!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        elif len(password) < 8:
            msg_box.setText("Password is too short! The program requires a password of more than 8 characters!")
            msg_box.exec()
            return
        if not self.name:
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec()
            return
        if not self.cb_day.currentIndex():
            msg_box.setText("Please check and select your date of birth!")
            msg_box.exec()
            return

        elif not self.cb_month.currentIndex():
            msg_box.setText("Please check and select your date of birth!")
            msg_box.exec()
            return

        elif not self.cb_year.currentIndex():
            msg_box.setText("Please check and select your date of birth!")
            msg_box.exec()
            return

        if not self.chb_agree.isChecked():
            msg_box.setText("Please read and agree to the terms of this Application!")
            msg_box.exec()
            return
        

        

        
            
        MainNote.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainPage = Setup1()
    MainPage.show()
    AdminTool = AdminPage()
    MainNote = MainNotePage()
    Setup2 = Setup2Page()
    Setup3 = Setup3Page()
    SetupFinish = SetupFinishPage()
    SignIn = SignInPage()
    SignUp = SignUpPage()
    EditNote = EditNotePage()
    Tool1 = Tool1Page()
    Tool2 = Tool2Page()
    msg_box = QMessageBox()
    msg_box1 = QMessageBox()
    msg_box1.setWindowTitle("Note for WOW! Notification")
    msg_box1.setIcon(QMessageBox.Icon.Information)
    msg_box.setWindowTitle("Note for WOW! Warning")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    sys.exit(app.exec())