import sys
import pymysql
import PyQt6

from login import *
from signUp import *
from main import *
import mysql
from mysql import *

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit


class winLogin(QMainWindow, Ui_Form):

    def __init__(self) :
        super(winLogin, self).__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login)
        self.edtPassword.returnPressed.connect(self.login)
        self.edtPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton_2.clicked.connect(self.openWinSignUp)

    def openWinSignUp(self):
        self.winSignUp = winSignUp()
        self.winSignUp.show()
        self.close()
    
    def openWinMain(self):
        self.winMain = winMain()
        self.winMain.show()
        self.close()


    def login(self):
        login_user = self.edtUsername.text().strip()                                               
        login_passwrod = self.edtPassword.text().strip()

        if login_user != "" and login_passwrod != "" : #判断账号与密码是否为空
            if_userno_exist = mysql.query("select username from userInfo where username = %s", login_user)  #用sql语句查询输入的账号是否存在
            if len(if_userno_exist) > 0:	#长度>0，则表示存在
                if_matched = mysql.query("select username from userInfo where username = %s and password = %s", login_user,login_passwrod)	
                #用sql语句判断输入的账号和密码是否匹配
                if len(if_matched) > 0:	#长度>0，则表示匹配            
                    # QMessageBox.warning(None, '通知', '登陆成功!')
                    self.openWinMain()
                else:
                    QMessageBox.warning(None, '警告', '密码输入错误!')
            else:
                QMessageBox.warning(None, '警告', '该账号不存在!')
        else:
            QMessageBox.warning(None, '警告', '有信息未输入!')

class winSignUp(QMainWindow, Ui_widget):
    def __init__(self) :
        super(winSignUp, self).__init__()
        self.setupUi(self)
        self.signupButton.clicked.connect(self.signup)
        self.edtPassword.returnPressed.connect(self.signup)


    def signup(self):
        signup_name = self.adtUsername.text().strip()
        signup_password = self.edtPassword.text().strip()

        if signup_name != "" and signup_password != "":
            if_registered = mysql.query("select username from userInfo where username = %s", signup_name)
            if len(if_registered) > 0:  #长度>0，则说明存在该用户
                QMessageBox.warning(None, '警告', '该账号已存在，请登录。')#提示已经存在，请跳转登录

            else:

                result = mysql.exec("insert into userInfo(username, password) value (%s, %s)", (signup_name, signup_password))
                if result > 0: 
                    QMessageBox.warning(None, '通知', '已成功注册!') 
        else:
            QMessageBox.warning(None, '警告', '有注册信息未输入!') 

class winMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(winMain, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.closeMain)
    
    def closeMain(self):
        self.close()

        

def main_():
	app = QApplication(sys.argv)
	login = winLogin()
	login.show()
	sys.exit(app.exec())

 
if __name__ == '__main__':
	main_()