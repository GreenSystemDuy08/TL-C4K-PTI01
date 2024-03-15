import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox #Thêm thư viện
from PyQt6 import uic # dùng để connect QTDesigner

class Login(QMainWindow):
    def __init__(self):
        super().__init__() #tổng hợp
        uic.loadUi("tuan8.ui", self) # connect QTDesigner
        self.bt_login.clicked.connect(self.check_login)
        self.bt_register.clicked.connect(self.showRegister)

    def check_login(self):
        msg_box = QMessageBox()
        email = self.le_email.text()
        password = self.le_password.text()
        if not email:
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
         
        if email == 'admin@example.com' and password == "admin":
            msg_box.setText("Xin chào Admin!")
            msg_box.exec()
        else:
            msg_box.setText("Úi dồi! Sư phụ nhập sai email hay mật khẩu rồi!!")
            msg_box.exec()
    def showRegister(self):
        RegisterPage.show()
        self.close()
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("tuan8_1.ui", self)
        self.bt_register.clicked.connect(self.Register)
    def Register(self):

        self.name = self.le_fullname.text()
        account = self.le_account.text()
        password = self.le_password.text()
        msg_box = QMessageBox
        
        if not self.name:
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec()
        if not account:
            msg_box.setText("Vui lòng nhập sđt/email!")
            msg_box.exec()
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
        if not self.chb_agree.isChecked():
            msg_box.setText('Vui lòng đọc và đồng ý các điều khoản trên')
            msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginPage = Login()
    LoginPage.show()
    RegisterPage = Register()
    sys.exit(app.exec())
