import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox , QWidget
from PyQt6 import uic

class Shopping(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/shopping.ui", self)
        self.bt_buy1.clicked.connect(self.showAboutBurger)
        self.bt_buy2.clicked.connect(self.showAboutShoes)
        self.bt_buy3.clicked.connect(self.showAboutChocolate)
        self.bt_buy4.clicked.connect(self.showAboutPizza)
        self.bt_buy5.clicked.connect(self.showAboutCandy)
        self.bt_buy6.clicked.connect(self.showAboutShirt)
        self.bt_buy7.clicked.connect(self.showAboutJeans)
        self.bt_buy8.clicked.connect(self.showAboutIphone)
        self.bt_buy9.clicked.connect(self.showAboutKnife)
        self.bt_buy10.clicked.connect(self.showAboutSamsung)
        self.bt_signout.clicked.connect(self.showExit)
        self.bt_setting.clicked.connect(self.showSetting)
        self.bt_search.clicked.connect(self.showWarning)
        self.bt_cart.clicked.connect(self.showWarning1)
        self.bt_about.clicked.connect(self.showDeveloperInformation)
    def showDeveloperInformation(self):
        DeveloperInformation.show()
    def showAboutSamsung(self):
        Samsung.show()
        self.close()
    def showAboutKnife(self):
        Knife.show()
        self.close()
    def showAboutIphone(self):
        Iphone.show()
        self.close()
    def showAboutJeans(self):
        Jeans.show()
        self.close()
    def showAboutShirt(self):
        Shirt.show()
        self.close()
    def showAboutCandy(self):
        Candy.show()
        self.close()
    def showWarning1(self):
        msg_box.setText("ERROR 404: THIS FEATURE IS STILL NOT WORKING!")
        msg_box.exec()
    def showWarning(self):
        msg_box.setText("The product you were looking for was not found!")
        msg_box.exec()
    def showAboutPizza(self):
        Pizza.show()
        self.close()
    def showAboutChocolate(self):
        Chocolate.show()
        self.close()
    def showSetting(self):
        Setting.show()
    def showAboutBurger(self):
        Burger.show()
        self.close()
    def showExit(self):
        Exit.show()
        self.close()
    def showAboutShoes(self):
        Shoes.show()
        self.close()

class AboutJeansPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about jeans.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class DeveloperInformationPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/developer information.ui",self)
        self.bt_close.clicked.connect(self.showMainPage)
    def showMainPage(self):
        MainPage.show()
        self.close()

class AboutIphonePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about iphone14.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class AboutKnifePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about carrot knife.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class AboutSamsungPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about samsung phone.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class AboutShirtPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about shirt.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class AboutCandyPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about gummy.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class WarningPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/warning.ui", self)
        self.bt_close.clicked.connect(self.quit)
    def quit(self):
        self.close()

class AboutPizzaPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about pizza.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class ThankYouPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/thankyou.ui", self)
        self.bt_continue.clicked.connect(self.showMainPage)
    def showMainPage(self):
        MainPage.show()
        self.close()

class AboutChocolatePage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about feastable chocolate.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class SettingPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/setting.ui", self)
        self.bt_close.clicked.connect(self.quit)
        self.bt_about.clicked.connect(self.showAbout)
        self.bt_update.clicked.connect(self.showUpdate)
        self.bt_home.clicked.connect(self.showWarning)
        self.bt_appear.clicked.connect(self.showWarning)
        self.bt_account.clicked.connect(self.showWarning)
    def showUpdate(self):
        # msg_box.setText("New version: 1.3.2024 (RTM)\nYour current version: 4.2.2024 (Beta)")
        # msg_box.exec()
        msg_box.setText("There are no current update available!")
        msg_box.exec()
    def showAbout(self):
        About.show()
    def quit(self):
        self.close()
    def showWarning(self):
        msg_box.setText("ERROR 404: THIS FEATURE IS STILL NOT WORKING!")
        msg_box.exec()


class AboutPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/about.ui", self)
        self.bt_ok.clicked.connect(self.quit)
    def quit(self):
        self.close()

class AboutShoesPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/About shoes.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')
    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class ExitPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/dangxuatra.ui", self)
        self.bt_quit.clicked.connect(self.quit)
    def quit(self):
        msg_box.setText("Thank you for your shopping!")
        msg_box.exec()
        self.close()

class SignInPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/dangnhap.ui", self)
        self.bt_login.clicked.connect(self.checkLogin)
        self.bt_register.clicked.connect(self.showSignUp)
        self.bt_continue.clicked.connect(self.showMainPage)
    def showMainPage(self):
        msg_box.setText("Going forward, sign in if you want more features!")
        msg_box.exec()
        MainPage.show()
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
            MainPage.show()
        else:
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()


class AboutBurgerPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/About burger.ui", self)
        self.bt_back.clicked.connect(self.showMainPage)
        self.bt_buy.clicked.connect(self.check_spinbox_value)
    
    def check_spinbox_value(self):
        value = self.spinBox.value()

        if value > 0:
            ThankYou.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Must have 1 product or more!\nYour product quantity is 0!')

    def showThankYou(self):
        ThankYou.show()
        self.close()
    def showMainPage(self):
        MainPage.show()
        self.close()

class SignUpPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Register.ui", self)
        self.bt_signup.clicked.connect(self.SignUp)
        self.bt_already.clicked.connect(self.Back)
    def Back(self):
        SignIn.show()
        self.close()
    def SignUp(self):
        self.name = self.le_fullname.text()
        email = self.le_account.text()
        password = self.le_password.text()
        

        if not self.name:
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec()
            return
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
            msg_box.setText("Please read and agree to the terms of Online Shopping!")
            msg_box.exec()
            return
        

        

        
            
        MainPage.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainPage = Shopping()
    SignIn = SignInPage()
    SignIn.show()
    Burger = AboutBurgerPage()
    SignUp = SignUpPage()
    Exit = ExitPage()
    Shoes = AboutShoesPage()
    Setting = SettingPage()
    Chocolate = AboutChocolatePage()
    Shirt = AboutShirtPage()
    Pizza = AboutPizzaPage()
    ThankYou = ThankYouPage()
    About = AboutPage()
    Candy = AboutCandyPage()
    Jeans = AboutJeansPage()
    Iphone = AboutIphonePage()
    Knife = AboutKnifePage()
    Samsung = AboutSamsungPage()
    DeveloperInformation = DeveloperInformationPage()
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Online Shopping Warning")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    sys.exit(app.exec())