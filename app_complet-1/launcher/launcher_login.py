
import sys
import sqlite3
from PySide6.QtWidgets import QApplication,QWidget,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from Widgets.interface.interface_login.interface_log import Ui_Applogin 
from Widgets.interface import img_rc
from launcher.launcher_main import *
from launcher.launcher_connection import *

class LoginValidator(QWidget,Ui_Applogin):
    def __init__(self,App_connenction):
        super().__init__()

    def login(self):    
        connexion=sqlite3.connect('Data_user.db')
        curseur=connexion.cursor()
        curseur.execute("SELECT * FROM data_users_sec WHERE EMAIL=? and PASSWORD=?", [self.lineEdit_email.text(), self.lineEdit_password.text()])
        
        if curseur.fetchone() == None:
            self.label_error_login_email.setText('invalid')
            self.label_error_login_email.setStyleSheet('color: red;')
            self.label_error_login_password.setText('invalid')
            self.label_error_login_password.setStyleSheet('color: red')
        else:
            self.label_error_login_email.setText('valid')
            self.label_error_login_email.setStyleSheet('color: green;')
            self.label_error_login_password.setText('valid')
            self.label_error_login_password.setStyleSheet('color: green')
            self.label_conn_text.setText('CONNECTE')
            self.label_conn_text.setStyleSheet('color: green')
            
                  
           
               
    
    def start_button(self):
        self.login()



class MainWindow1(LoginValidator,QWidget,QApplication):
    def __init__(self) :
        super(LoginValidator,MainWindow1).__init__(self)
        self.setupUi(self)
        self.pushButton_sent_request.setCheckable(False)
        self.pushButton_sent_request.clicked.connect(self.start_button)
        

      
if __name__=="__main__":
    app2 = QApplication(sys.argv)        

    window1 = MainWindow1()
    window1.show()

    sys.exit(app2.exec())