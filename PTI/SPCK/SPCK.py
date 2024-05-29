import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import json

# Đọc dữ liệu từ tệp JSON
with open('account.json', 'r') as file:
    data = json.load(file)

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
        path = self.le_path.text()
        if not path:
            msg_box.setText("Please enter the path to start the installation process!")
            msg_box.exec()
            return
        else:
            Setup2.show()
            self.close()
    def browsecsv(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select the destination path")
        if folder_path:
            self.le_path.setText(folder_path)
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
        self.bt_start.clicked.connect(self.showStart)
        self.bt_admin.clicked.connect(self.showAdmin)
        self.bt_register.clicked.connect(self.showSignUp)
        self.bt_continue.clicked.connect(self.showMainPage)
        self.bt_forgot.clicked.connect(self.showForgotPass)
    def showAdmin(self):
        Admin.show()
    def showStart(self):
        Start.show()
    def showForgotPass(self):
        forgotPass.show()
    def showMainPage(self):
        MainNote.show()
        self.close()
    def showSignUp(self):
        SignUp2.show()
        self.close()
    def quit(self):
        self.close()

class SignInPage2(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/dangnhap2.ui", self)
        self.bt_google.clicked.connect(self.showGoogle)
        self.bt_microsoft.clicked.connect(self.showMicrosoft)
        self.bt_apple.clicked.connect(self.showApple)
        self.bt_outlook.clicked.connect(self.showOutlook)
        self.bt_finish.clicked.connect(self.checkLogin)
    def showGoogle(self):
        Google.show()
        self.close()
    def showMicrosoft(self):
        Microsoft.show()
        self.close()
    def showApple(self):
        Apple.show()
        self.close()
    def showOutlook(self):
        Outlook.show()
        self.close()
    def checkLogin(self):
        email = self.le_email.text()
        password = self.le_password.text()
        found = False

        if not email:
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
            msg_box.exec()
            return
        for account in data:
            if account['email'] == email and account['password'] == password:
                # msg_box1.setText("Welcome to Note for WOW! Application!")
                # msg_box1.exec()
                # MainNote.show()
                # SignIn.close()
                # Start.close()
                found = True
                if account["type"] == "local":
                    msg_box1.setText("Welcome to Note for WOW! Application!")
                    msg_box1.exec()
                    MainNote.show()
                    SignIn.close()
                    Start.close()
                    return
                if account["type"] == "admin":
                    msg_box1.setText("Hello, Administrator!")
                    msg_box1.exec()
                    AdminTool.show()
                    SignIn.close()
                    Start.close()
                    return

        if not found:
            QMessageBox.warning(self, 'ERROR AT LOGIN!', '=(((\nAccount or password is incorrect or has not been registered!')
            return

class AdminSignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/admin.ui", self)
        self.bt_login.clicked.connect(self.showMainPage)
    def showMainPage(self):
        email = self.le_email.text()
        password = self.le_password.text()

        if not email:
            msg_box.setText("Please enter your admin email!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter admin password!")
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
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
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
            Start.close()
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
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
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
            Start.close()
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
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
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
            Start.close()
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
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        elif email == "admin@gmail.com":
            msg_box.setText("Admin account does not support normal account login form!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
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
            Start.close()
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
        found = False
        if not email: 
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        
        for account in data:
            if account["email"] == email:
                found == True
                forgotPass2.show()
                self.close()
                return
        if not found:
            QMessageBox.warning(self, 'ERROR!', '=(((\nAccount or password is incorrect or has not been registered!')
            return

        elif email == "admin@gmail.com":
            msg_box.setText("ERROR: This account is built into the System.\nYou cannot change the password for this account!")
            msg_box.exec()
            return

class forgotPassword2(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/forgotPassword.ui", self)
        self.bt_ok.clicked.connect(self.Close)
    def Close(self):
        current = self.le_current.text()
        email = forgotPass.le_email.text()
        new = self.le_new.text()
        re_enter = self.le_re_enter.text()
        found = False
        if not current:
            msg_box.setText("Please enter your current password!")
            msg_box.exec()
            return
        if not new:
            msg_box.setText("Please enter your new password!")
            msg_box.exec()
            return
        elif not re_enter:
            msg_box.setText("Please re-enter your new password!")
            msg_box.exec()
            return
        elif len(new) < 8:
            msg_box.setText("Your new password is too short! The program requires password more than 8 characters!")
            msg_box.exec()
            return
        elif not new == re_enter:
            msg_box.setText("Please re-enter your new password! Your new password and your new re-enter password do not match!")
            msg_box.exec()
            return
        if new == current or re_enter == current:
            QMessageBox.warning(self, 'ERROR!', '=(((\nYour new password is similar to the current password!')
            return
        
        if self.rb_admin.isChecked() or self.rb_local.isChecked():
            if self.rb_admin.isChecked():
                Account_type = "admin"
            if self.rb_local.isChecked():
                Account_type = "local"
            for account in data:
                if account['password'] == current:
                    self.close()
                    msg_box1.setText("Your new password has been set successfully!")
                    msg_box1.exec()
                    found == True
                    if "email" and "password" in account:
                        del account["email"]
                        del account["password"]
                        with open('account.json', "w") as f:
                            json.dump(data, f, indent=4)
                            data.clear()
                    new_account = {
                    "email": email,
                    "password": new,
                    "type": Account_type
                    }
                    data.append(new_account)
                    with open('account.json', "w") as json_file:
                        json.dump(data, json_file, indent=4)
                        return
            if not found:
                QMessageBox.warning(self, 'ERROR!', '=(((\nThe current password is not right!')
                return
            
        if not self.rb_admin.isChecked():
            msg_box.setText("You have not confirmed your account type!")
            msg_box.exec()
            return
        if not self.rb_local.isChecked():
            msg_box.setText("You have not confirmed your account type!")
            msg_box.exec()
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
        SignUp2.close()
    def SignUp(self):
        self.name = self.le_fullname.text()
        email = self.le_account.text()
        password = self.le_password.text()
        # Account_type = ""
        
        if not email: 
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "Please enter your email!")
            return
        if SignUp2.rb_google.isChecked():
            if email == "admin@gmail.com" and password == "admin":
                QMessageBox.information(self, 'Sign Up Information', "Hello, Administrator!")
                AdminTool.show()
                self.close()
                SignUp2.close()
                return
            elif "@gmail.com" in email:
                pass
            else:
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "You have selected email type: @gmail.com\nThe email you entered is not the same as the account type you selected!")
                QMessageBox.information(self, 'Sign Up Information', "Email Type: Example: @abc.com")
                return
        
        if SignUp2.rb_apple.isChecked():
            if "@apple.com" in email:
                pass
            else:
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "You have selected email type: @apple.com\nThe email you entered is not the same as the account type you selected!")
                QMessageBox.information(self, 'Sign Up Information', "Email Type: Example: @abc.com")
                return

        if SignUp2.rb_microsoft.isChecked():
            if "@microsoft.com" in email:
                pass

            else:
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "You have selected email type: @microsoft.com\nThe email you entered is not the same as the account type you selected!")
                QMessageBox.information(self, 'Sign Up Information', "Email Type: Example: @abc.com")
                return
        
        if SignUp2.rb_outlook.isChecked():
            if "@outlook.com" in email:
                pass

            else:
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "You have selected email type: @outlook.com\nThe email you entered is not the same as the account type you selected!")
                QMessageBox.information(self, 'Sign Up Information', "Email Type: Example: @abc.com")
                return
        elif email == "admin@gmail.com" and password == "admin":
            msg_box1.setText("Hello, Administrator!")
            msg_box1.exec()
            AdminTool.show()
            SignUp2.close()
            self.close()
            return

        elif '@' not in email:
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Invalid email!')
            return
        
        for account in data:
            if account['email'] == email:
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', '=(((\nExisting or previously registered account!')
                return

        if not password:
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Please enter your password!')
            return
        
        elif password == "admin":
            pass

        elif len(password) < 8:
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Password is too short! The program requires a password of more than 8 characters!')
            return
        if not self.name:
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Please enter your display name!')
            return
        if not self.chb_skip.isChecked():
            if not self.cb_day.currentIndex():
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Please select your date of birth\nOr check the box "Skip choosing your date of birth"')
                return

            elif not self.cb_month.currentIndex():
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Please select your date of birth\nOr check the box "Skip choosing your date of birth"')
                return

            elif not self.cb_year.currentIndex():
                QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Please select your date of birth\nOr check the box "Skip choosing your date of birth"')
                return

        if not self.chb_agree.isChecked():
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', 'Please agree to the terms of this Application!')
            return
        
        if self.rb_admin.isChecked():
            Account_type = "admin"
            msg_box1.setText("Hello, Administrator!")
            msg_box1.exec()
            AdminTool.show()
            SignUp2.close()
            self.close()
            return

        if self.rb_local.isChecked():
            Account_type = "local"
            msg_box1.setText("Welcome to Note for WOW! Application!")
            msg_box1.exec()
            MainNote.show()
            SignUp2.close()
            self.close()
        
        elif not self.rb_admin.isChecked():
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "YOU HAVEN'T CHOOSED AN ACCOUNT TYPE TO REGISTER!\nNote: Exception admin account!")
            return
        
        elif not self.rb_local.isChecked():
            QMessageBox.warning(self, 'ERROR WHEN REGISTERING ACCOUNT!', "YOU HAVEN'T CHOOSED AN ACCOUNT TYPE TO REGISTER!\nNote: Exception admin account!")
            return
        
        if email and password:
            new_account = {
            "email": email,
            "password": password,
            "type": Account_type
            }
            data.append(new_account)    
            with open('account.json', "w") as json_file:
                json.dump(data, json_file, indent=4) 

class MainNotePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/mainnote.ui", self)
        self.bt_edit.clicked.connect(self.showEditNote)
        self.bt_add.clicked.connect(self.showCreateNote)
        self.bt_quit.clicked.connect(self.Close)
        self.bt_save.clicked.connect(self.showSignIn)
        self.bt_search.clicked.connect(self.check)
        self.bt_tool.clicked.connect(self.showTool)
        self.bt_remove.clicked.connect(self.remove)
    def remove(self):
        selected_items = self.noteList.selectedItems()
        if not selected_items:
            msg_box2.setText("You have not selected a note page to delete or there are no more note pages to delete!")
            msg_box2.exec()
            return
        else:
            self.noteList.takeItem(self.noteList.row(selected_items[0]))
    def showTool(self):
        Tool3.show()
    def showSignIn(self):
        SignIn.show()
        self.close()
    def Close(self):
        self.close()
    def showCreateNote(self):
        Create1.show()
    def showEditNote(self):
        selected = self.noteList.selectedItems()
        if not selected:
            msg_box2.setText("ERROR! You haven't selected the note page you want to edit!")
            msg_box2.exec()
            return
        else:
            EditNote1.show()
    def check(self):
        name = self.le_name.text()

        if not name:
            msg_box.setText("Please enter the note page name to start searching!")
            msg_box.exec()
            return
        else:
            msg_box2.setText("Failed!")
            msg_box2.exec()
            return
        
class Tool3Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/tool2.ui", self)
        self.bt_close.clicked.connect(self.close)
        self.bt_add.clicked.connect(self.showAdd)
        self.bt_font.clicked.connect(self.showFont)
    def showFont(self):
        Font.show()    
    def showAdd(self):
        Add.show()

class AddPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/task.ui", self)
        self.bt_ok.clicked.connect(self.close)
        
class Create1Page(QMainWindow, QWidget):
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
        
        text = self.le_name.text()
        if text:
            item = QListWidgetItem(text)
            MainNote.noteList.addItem(item)
            self.close()
            msg_box1.setText("The notes page has been added successfully!")
            msg_box1.exec()
            return
    
class Create2Page(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/create1.ui", self)
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

        text = self.le_name.text()
        if text:
            item = QListWidgetItem(text)
            AdminTool.noteList.addItem(item)
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
        
class EditNotePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/editNote.ui", self)
        self.bt_save.clicked.connect(self.Close)
    def Close(self):
        selected = AdminTool.noteList.selectedItems()
        if selected:
            text = self.le_name.text()
            if text:
                selected[0].setText(text)
        self.close()

class EditNotePage_Local(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/editNote.ui", self)
        self.bt_save.clicked.connect(self.Close)
    def Close(self):
        selected = MainNote.noteList.selectedItems()
        if selected:
            text = self.le_name.text()
            if text:
                selected[0].setText(text)
        self.close()

class AdminPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/AdminPage.ui", self)
        self.bt_add.clicked.connect(self.showAdd)
        self.bt_save.clicked.connect(self.showSignIn)
        self.bt_exit.clicked.connect(self.Close)
        self.bt_edit.clicked.connect(self.showEditNote)
        self.bt_setting.clicked.connect(self.showSetting)
        self.bt_search.clicked.connect(self.check)
        self.bt_remove.clicked.connect(self.remove)
        self.bt_detail.clicked.connect(self.showDetail)
        self.bt_task.clicked.connect(self.showTask)
    def showTask(self):
        Add.show()
    def showDetail(self):
        NoteDetail.show()
    def remove(self):
        selected_items = self.noteList.selectedItems()
        if not selected_items:
            msg_box2.setText("You have not selected a note page to delete or there are no more note pages to delete!")
            msg_box2.exec()
            return
        else:
            self.noteList.takeItem(self.noteList.row(selected_items[0]))
    def Close(self):
        self.close()
    def showAdd(self):
        Create2.show()
    def showSignIn(self):
        SignIn.show()
        self.close()
    def showEditNote(self):
        selected = self.noteList.selectedItems()
        if not selected:
            msg_box2.setText("ERROR! You haven't selected the note page you want to edit!")
            msg_box2.exec()
            return
        else:
            EditNote.show()
    def showSetting(self):
        Setting.show()
        self.close()
    def check(self):
        name = self.le_name.text()

        if not name:
            msg_box.setText("Please enter the note page name to start searching!")
            msg_box.exec()
            return
        else:
            msg_box2.setText("Failed!")
            msg_box2.exec()
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
        AdminTool.show()
        self.close()
    def showCautionDelete(self):
        msg_box2.setText("Process cannot be done!")
        msg_box2.exec()
        return
    def showCautionReset(self):
        msg_box2.setText("Process cannot be done!")
        msg_box2.exec()
        return
    
class AboutPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/about.ui", self)
        self.bt_ok.clicked.connect(self.Close)
    def Close(self):
        self.close()

class DetailPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/noteDetail.ui", self)
        self.bt_close.clicked.connect(self.back)
    def back(self):
        AdminTool.show()
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
    Create1 = Create1Page()
    Create2 = Create2Page()
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
    EditNote = EditNotePage()
    EditNote1 = EditNotePage_Local()
    NoteDetail = DetailPage()
    Start = SignInPage2()
    Setting = SettingPage()
    About = AboutPage()
    Tool3 = Tool3Page()
    Add = AddPage()
    msg_box = QMessageBox()
    msg_box1 = QMessageBox()
    msg_box2 = QMessageBox()
    msg_box1.setWindowTitle("App Notification")
    msg_box1.setIcon(QMessageBox.Icon.Information)
    msg_box.setWindowTitle("App Warning")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box2.setWindowTitle("App Error!")
    msg_box2.setIcon(QMessageBox.Icon.Critical)
    sys.exit(app.exec())