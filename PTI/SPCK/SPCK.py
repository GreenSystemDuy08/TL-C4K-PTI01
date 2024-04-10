import sys
from tkinter import *
import csv
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox , QWidget
from PyQt6 import uic

class MainNotePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/mainnote.ui", self)
        self.bt_edit1.clicked.connect(self.showEditNote1)
        self.bt_edit2.clicked.connect(self.showEditNote2)
        self.bt_add.clicked.connect(self.showCaution)
        self.bt_quit.clicked.connect(self.Close)
        self.bt_save.clicked.connect(self.showSignIn)
        self.bt_apply.clicked.connect(self.checkName)
    def showSignIn(self):
        SignIn.show()
        self.close()
    def Close(self):
        self.close()
    def showCaution(self):
        msg_box1.setText("The notes page has been added successfully!")
        msg_box1.exec()
        return
    def showEditNote1(self):
        EditNote1.show()
    def showEditNote2(self):
        EditNote2.show()
    def checkName(self):
        name = self.le_name.text()

        if not name:
            msg_box.setText("Please enter a title name!")
            msg_box.exec()
            return
        else:
            msg_box1.setText("Apply title name successfully!")
            msg_box1.exec()
            return
        
class EditNote1Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/editNote1.ui", self)
        self.bt_save.clicked.connect(self.Close)
    def Close(self):
        self.close()

class EditNote2Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/editNote2.ui", self)
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
        self.bt_edit1.clicked.connect(self.showEditNote1)
        self.bt_edit2.clicked.connect(self.showEditNote2)
        self.bt_setting.clicked.connect(self.showSetting)
        self.bt_apply.clicked.connect(self.checkName)
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
    def showEditNote1(self):
        EditNote1.show()
    def showEditNote2(self):
        EditNote2.show()
    def showSetting(self):
        Setting.show()
        self.close()
    def checkName(self):
        name = self.le_name.text()

        if not name:
            msg_box.setText("Please enter a title name!")
            msg_box.exec()
            return
        else:
            msg_box1.setText("Apply title name successfully!")
            msg_box1.exec()
            return

class SettingPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setting.ui", self)
        self.bt_save.clicked.connect(self.back)
        self.bt_reset.clicked.connect(self.showCautionReset)
        self.bt_delete.clicked.connect(self.showCautionDelete)
    def back(self):
        AdminTool.show()
        self.close()
    def showCautionDelete(self):
        msg_box1.setText("All of the notes page has been successfully removed!")
        msg_box1.exec()
        return
    def showCautionReset(self):
        msg_box1.setText("Everything has been reset to factory defaults!")
        msg_box1.exec()
        return

class Tool1Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/AdminTool - note1.ui", self)
        self.bt_back.clicked.connect(self.back)
        self.bt_remove.clicked.connect(self.Caution)
        self.bt_detail.clicked.connect(self.showNoteDetail)
    def back(self):
        AdminTool.show()
        self.close()
    def Caution(self):
        msg_box1.setText("The notes page has been successfully removed!")
        msg_box1.exec()
        return
    def showNoteDetail(self):
        NoteDetail1.show()
        self.close()

class Tool2Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/AdminTool - note2.ui", self)
        self.bt_back.clicked.connect(self.back)
        self.bt_remove.clicked.connect(self.Caution)
        self.bt_detail.clicked.connect(self.showNoteDetail)
    def Caution(self):
        msg_box1.setText("The notes page has been successfully removed!")
        msg_box1.exec()
        return
    def back(self):
        AdminTool.show()
        self.close()
    def showNoteDetail(self):
        NoteDetail2.show()
        self.close()

class DetailPage1(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/noteDetail1.ui", self)
        self.bt_close.clicked.connect(self.back)
    def back(self):
        Tool1.show()
        self.close()

class DetailPage2(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/noteDetail2.ui", self)
        self.bt_close.clicked.connect(self.back)
    def back(self):
        Tool2.show()
        self.close()


class Setup1Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup1.ui", self)
        self.bt_next.clicked.connect(self.showSetup2)
        self.bt_browse.clicked.connect(self.browsecsv)
        # self.bt_browse.clicked.connect(self.showBrowse)
    def showSetup2(self):
        Setup2.show()
        self.close()
    # def showBrowse(self):
    #     msg_box.setText("ERROR! Browse not found!")
    #     msg_box.exec()
    def browsecsv(self):
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        # Hide the main Tkinter window
        Tk().withdraw()

        # Ask the user to select a file
        filename = askopenfilename()

        # Process the selected file (you can modify this part)
        with open(filename, 'rb') as csvfile:
            logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            rownum = 0
            for row in logreader:
                NumColumns = len(row)
                rownum += 1
                Matrix = [[0 for x in range(NumColumns)] for x in range(rownum)]

        csvfile.close()
        Setup1.show()

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
            msg_box.setText("Please agree to the terms of this Application!")
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
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter a password!")
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
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            self.close()
            return
        else:
            msg_box.setText("Email or password is incorrect!")
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
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        elif '@' not in email:
            msg_box.setText("Email invalidate!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter a password!")
            msg_box.exec()
            return
        elif len(password) < 8:
            msg_box.setText("Password is too short! The program requires a password of more than 8 characters!")
            msg_box.exec()
            return
        if not self.name:
            msg_box.setText("Please enter a name!")
            msg_box.exec()
            return
        if not self.chb_skip.isChecked():
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
            msg_box.setText("Please agree to the terms of this Application!")
            msg_box.exec()
            return
        
        if self.rb_admin.isChecked():
            msg_box1.setText("Hello, Administrator!")
            msg_box1.exec()
            AdminTool.show()
            self.close()
            return

        if self.rb_local.isChecked():
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            self.close()
            return
        
        elif not self.rb_admin.isChecked():
            msg_box.setText("ERROR 404!\nYOU HAVEN'T CHOOSED AN ACCOUNT TYPE TO REGISTER!")
            msg_box.exec()
            return
        
        elif not self.rb_local.isChecked():
            msg_box.setText("ERROR 404!\nYOU HAVEN'T CHOOSED AN ACCOUNT TYPE TO REGISTER!")
            msg_box.exec()
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainPage = Setup1Page()
    Setup1 = Setup1Page()
    MainPage.show()
    AdminTool = AdminPage()
    MainNote = MainNotePage()
    Setup2 = Setup2Page()
    Setup3 = Setup3Page()
    SetupFinish = SetupFinishPage()
    SignIn = SignInPage()
    SignUp = SignUpPage()
    EditNote1 = EditNote1Page()
    EditNote2 = EditNote2Page()
    Tool1 = Tool1Page()
    Tool2 = Tool2Page()
    NoteDetail1 = DetailPage1()
    NoteDetail2 = DetailPage2()
    Setting = SettingPage()
    msg_box = QMessageBox()
    msg_box1 = QMessageBox()
    msg_box1.setWindowTitle("Note for WOW! Notification")
    msg_box1.setIcon(QMessageBox.Icon.Information)
    msg_box.setWindowTitle("Note for WOW! Warning")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    sys.exit(app.exec())