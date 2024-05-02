import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

class SetupPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup.ui", self)
        self.bt_next.clicked.connect(self.check)
    def check(self):
        if self.rb_portable.isChecked():
            Finish.show()
            self.close()
            return
        
        if self.rb_install.isChecked():
            Setup1.show()
            self.close()
            return
        
        elif not self.rb_portable.isChecked():
            msg_box.setText("Please choose the installation method!")
            msg_box.exec()
            return
        
        elif not self.rb_install.isChecked():
            msg_box.setText("Please choose the installation method!")
            msg_box.exec()
            return

class FinishPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/Finish.ui", self)
        self.bt_finish.clicked.connect(self.showSignIn)
        self.bt_back.clicked.connect(self.back)
    def back(self):
        Setup.show()
        self.close()
    def showSignIn(self):
        SignIn.show()
        self.close()

class Setup1Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup1.ui", self)
        self.bt_next.clicked.connect(self.showSetup2)
        self.bt_browse.clicked.connect(self.browsecsv)
        self.bt_back.clicked.connect(self.back)
    def back(self):
        Setup.show()
        self.close()
    def showSetup2(self):
        Setup2.show()
        self.close()
    def browsecsv(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select the destination path")
        if folder_path:
            self.lineEdit.setText(folder_path)
        else:
            pass

class Setup2Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/setup2.ui", self)
        self.bt_next.clicked.connect(self.showSetup3)
        self.bt_back.clicked.connect(self.back)
    def back(self):
        Setup1.show()
        self.close()
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
        self.bt_back.clicked.connect(self.back)
    def back(self):
        Setup2.show()
        self.close()
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
        self.bt_google.clicked.connect(self.showGoogle)
        self.bt_outlook.clicked.connect(self.showOutlook)
        self.bt_apple.clicked.connect(self.showApple)
        self.bt_microsoft.clicked.connect(self.showMicrosoft)
        self.bt_admin.clicked.connect(self.showAdmin)
        self.bt_register.clicked.connect(self.showSignUp)
        self.bt_continue.clicked.connect(self.showMainPage)
        self.bt_forgot.clicked.connect(self.showForgotPass)
    def showAdmin(self):
        Admin.show()
    def showMicrosoft(self):
        Microsoft.show()
    def showApple(self):
        Apple.show()
    def showOutlook(self):
        Outlook.show()
    def showGoogle(self):
        Google.show()
    def showForgotPass(self):
        forgotPass.show()
    def showMainPage(self):
        msg_box1.setText("Going forward, sign in if you want more features!")
        msg_box1.exec()
        # QMessageBox.warning(self, 'Warning', 'Going forward, sign in if you want more features!')
        MainNote.show()
        self.close()
    def showSignUp(self):
        SignUp2.show()
        self.close()
    def quit(self):
        self.close()

class AdminSignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/admin.ui", self)
        self.bt_login.clicked.connect(self.showMainPage)
    def showMainPage(self):
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
            msg_box1.setText("Hello, Administrator!")
            msg_box1.exec()
            AdminTool.show()
            self.close()
            SignIn.close()
            return
        elif not password == "admin":
            msg_box.setText("Wrong password for admin account!")
            msg_box.exec()
            return
        else:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return

class GoogleSignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/google.ui", self)
        self.bt_login.clicked.connect(self.showMainPage)
    def showMainPage(self):
        email = self.le_email.text()
        password = self.le_password.text()

        if not email:
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
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
        if '@gmail.com' in email:
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            self.close()
            SignIn.close()
            return
        elif "@gmail.com" not in email:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return
        
class AppleSignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/apple.ui", self)
        self.bt_login.clicked.connect(self.showMainPage)
    def showMainPage(self):
        email = self.le_email.text()
        password = self.le_password.text()

        if not email:
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
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
        if '@apple.com' in email:
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            self.close()
            SignIn.close()
            return
        elif "@apple.com" not in email:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return

class MicrosoftSignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/microsoft.ui", self)
        self.bt_login.clicked.connect(self.showMainPage)
    def showMainPage(self):
        email = self.le_email.text()
        password = self.le_password.text()

        if not email:
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
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
        if '@microsoft.com' in email:
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            self.close()
            SignIn.close()
            return
        elif "@microsoft.com" not in email:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return

class OutlookSignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/outlook.ui", self)
        self.bt_login.clicked.connect(self.showMainPage)
    def showMainPage(self):
        email = self.le_email.text()
        password = self.le_password.text()

        if not email:
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
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
        if '@outlook.com' in email:
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            self.close()
            SignIn.close()
            return
        elif "@outlook.com" not in email:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return

class forgotPassword1(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/forgotPassword1.ui", self)
        self.bt_next.clicked.connect(self.showforgotPass2)
    def showforgotPass2(self):
        email = self.le_email.text()
        if not email: 
            msg_box.setText("Please enter email or phone number!")
            msg_box.exec()
            return
        
        elif '@' not in email:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("ERROR: This account is built into the System.\nYou cannot change the password for this account!")
            msg_box.exec()
            return
        
        forgotPass2.show()
        self.close()

class forgotPassword2(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/forgotPassword.ui", self)
        self.bt_ok.clicked.connect(self.Close)
    def Close(self):
        new = self.le_new.text()
        re_enter = self.le_re_enter.text()
        if not new:
            msg_box.setText("Please enter your new password!")
            msg_box.exec()
            return
        elif not re_enter:
            msg_box.setText("Please re-enter your new password!")
            msg_box.exec()
            return
        elif len(new) < 8 or len(re_enter) < 8:
            msg_box.setText("Password is too short! The program requires a password of more than 8 characters!")
            msg_box.exec()
            return
        elif not new == re_enter:
            msg_box.setText("Please re-enter your new password! Your new password and your new re-enter password do not match!")
            msg_box.exec()
            return
        
        self.close()
        msg_box1.setText("Your new password has been set successfully!")
        msg_box1.exec()
        return
    
class SignUpPage2(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/dangky2.ui", self)
        self.bt_next.clicked.connect(self.check)
    def check(self):
        if self.rb_google.isChecked():
            SignUp.show()
            return
        if self.rb_apple.isChecked():
            SignUp.show()
            return
        if self.rb_microsoft.isChecked():
            SignUp.show()
            return
        if self.rb_outlook.isChecked():
            SignUp.show()
            return
        
        else:
            msg_box.setText("You have not chosen an account type to proceed to the next registration step!")
            msg_box.exec()
            return

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
        if SignUp2.rb_google.isChecked():
            if email == "admin@gmail.com" and password == "admin":
                msg_box1.setText("Hello, Administrator!")
                msg_box1.exec()
                AdminTool.show()
                self.close()
                SignUp2.close()
                return
            elif "@gmail.com" in email:
                pass
            else:
                msg_box.setText("ERROR! You have selected email type: @gmail.com\nThe email you entered is not the same as the account type you selected!")
                msg_box.exec()
                msg_box1.setText("Email Type: Example: @abc.com")
                msg_box1.exec()
                return
        
        if SignUp2.rb_apple.isChecked():
            if "@apple.com" in email:
                pass
            else:
                msg_box.setText("ERROR! You have selected email type: @apple.com\nThe email you entered is not the same as the account type you selected!")
                msg_box.exec()
                msg_box1.setText("Email Type: Example: @abc.com")
                msg_box1.exec()
                return

        if SignUp2.rb_microsoft.isChecked():
            if "@microsoft.com" in email:
                pass

            else:
                msg_box.setText("ERROR! You have selected email type: @microsoft.com\nThe email you entered is not the same as the account type you selected!")
                msg_box.exec()
                msg_box1.setText("Email Type: Example: @abc.com")
                msg_box1.exec()
                return
        
        if SignUp2.rb_outlook.isChecked():
            if "@outlook.com" in email:
                pass

            else:
                msg_box.setText("ERROR! You have selected email type: @outlook.com\nThe email you entered is not the same as the account type you selected!")
                msg_box.exec()
                msg_box1.setText("Email Type: Example: @abc.com")
                msg_box1.exec()
                return
        elif email == "admin@gmail.com" and password == "admin":
            msg_box1.setText("Hello, Administrator!")
            msg_box1.exec()
            AdminTool.show()
            SignUp2.close()
            self.close()
            return

        elif '@' not in email:
            msg_box.setText("Invalid email!")
            msg_box.exec()
            return

        if not password:
            msg_box.setText("Please enter a password!")
            msg_box.exec()
            return
        
        elif password == "admin":
            pass

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
                msg_box.setText("Please select your date of birth\nOr check the box 'Skip choosing your date of birth'")
                msg_box.exec()
                return

            elif not self.cb_month.currentIndex():
                msg_box.setText("Please select your date of birth\nOr check the box 'Skip choosing your date of birth'")
                msg_box.exec()
                return

            elif not self.cb_year.currentIndex():
                msg_box.setText("Please select your date of birth\nOr check the box 'Skip choosing your date of birth'")
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
            SignUp2.close()
            self.close()
            return

        if self.rb_local.isChecked():
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            SignUp2.close()
            self.close()
        
        elif not self.rb_admin.isChecked():
            msg_box.setText("ERROR 404!\nYOU HAVEN'T CHOOSED AN ACCOUNT TYPE TO REGISTER!\nNote: Exception admin account!")
            msg_box.exec()
            return
        
        elif not self.rb_local.isChecked():
            msg_box.setText("ERROR 404!\nYOU HAVEN'T CHOOSED AN ACCOUNT TYPE TO REGISTER!\nNote: Exception admin account!")
            msg_box.exec()
            return

class MainNotePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/mainnote.ui", self)
        self.bt_edit1.clicked.connect(self.showEditNote1)
        self.bt_edit2.clicked.connect(self.showEditNote2)
        self.bt_add.clicked.connect(self.showCreateNote)
        self.bt_quit.clicked.connect(self.Close)
        self.bt_save.clicked.connect(self.showSignIn)
        self.bt_apply.clicked.connect(self.checkName)
        self.bt_font.clicked.connect(self.showFont)
    def showFont(self):
        Font.show()
        self.close()
    def showSignIn(self):
        SignIn.show()
        self.close()
    def Close(self):
        self.close()
    def showCreateNote(self):
        Create.show()
    def showEditNote1(self):
        EditNote1.show()
    def showEditNote2(self):
        EditNote2.show()
    def checkName(self):
        name = self.le_name.text()

        if not name:
            msg_box.setText("Please enter a title name before clicking Apply!")
            msg_box.exec()
            return
        else:
            msg_box1.setText("Apply title name successfully!")
            msg_box1.exec()
            return
        
class CreatePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/create.ui", self)
        self.bt_close.clicked.connect(self.check)
    def check(self):
        title = self.le_title.text()
        name = self.le_name.text()
        if not title: 
            msg_box.setText("Please enter a title name!")
            msg_box.exec()
            return
        
        elif not name:
            msg_box.setText("Please enter a Note name!")
            msg_box.exec()
            return
        
        if not self.cb_type.currentIndex():
            msg_box.setText("Please select the type of Note you want to create!")
            msg_box.exec()
            return
        
        self.close()
        msg_box1.setText("The notes page has been added successfully!")
        msg_box1.exec()
        return
        
class FontPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/font.ui", self)
        self.bt_ok.clicked.connect(self.back)
    def back(self):
        MainNote.show()
        self.close()
        
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
        self.bt_add.clicked.connect(self.showCreateNote)
        self.bt_save.clicked.connect(self.showSignIn)
        self.bt_exit.clicked.connect(self.Close)
        self.bt_tool1.clicked.connect(self.showTool1)
        self.bt_tool2.clicked.connect(self.showTool2)
        self.bt_edit1.clicked.connect(self.showEditNote1)
        self.bt_edit2.clicked.connect(self.showEditNote2)
        self.bt_setting.clicked.connect(self.showSetting)
        self.bt_apply.clicked.connect(self.checkName)
    def Close(self):
        self.close()
    def showCreateNote(self):
        Create.show()
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
            msg_box.setText("Please enter a title name before clicking Apply!")
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
        self.bt_about.clicked.connect(self.showAbout)
    def showAbout(self):
        About.show()
    def back(self):
        if self.chb_enable.isChecked():
            msg_box.setText("ERROR: This feature is not currently available or being tested!\nThis Program will not enable this feature")
            msg_box.exec()
            return
        
        if self.chb_detail.isChecked():
            msg_box.setText("ERROR: This feature is not currently available or being tested!\nThis Program will not enable this feature")
            msg_box.exec()
            return
        
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
    
class AboutPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/about.ui", self)
        self.bt_ok.clicked.connect(self.Close)
    def Close(self):
        self.close()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainPage = SetupPage()
    Setup = SetupPage()
    MainPage.show()
    Finish = FinishPage()
    Setup1 = Setup1Page()
    AdminTool = AdminPage()
    MainNote = MainNotePage()
    Font = FontPage()
    Create = CreatePage()
    Setup2 = Setup2Page()
    Setup3 = Setup3Page()
    SetupFinish = SetupFinishPage()
    SignIn = SignInPage()
    Admin = AdminSignInPage()
    Google = GoogleSignInPage()
    Apple = AppleSignInPage()
    Microsoft = MicrosoftSignInPage()
    Outlook = OutlookSignInPage()
    forgotPass = forgotPassword1()
    forgotPass2 = forgotPassword2()
    SignUp = SignUpPage()
    SignUp2 = SignUpPage2()
    EditNote1 = EditNote1Page()
    EditNote2 = EditNote2Page()
    Tool1 = Tool1Page()
    Tool2 = Tool2Page()
    NoteDetail1 = DetailPage1()
    NoteDetail2 = DetailPage2()
    Setting = SettingPage()
    About = AboutPage()
    msg_box = QMessageBox()
    msg_box1 = QMessageBox()
    msg_box1.setWindowTitle("Note for WOW! Notification")
    msg_box1.setIcon(QMessageBox.Icon.Information)
    msg_box.setWindowTitle("Note for WOW! Warning")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    sys.exit(app.exec())