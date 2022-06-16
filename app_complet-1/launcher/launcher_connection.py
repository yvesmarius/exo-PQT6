import sqlite3
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,)
import sys
import re
# from tkinter import messagebox
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit
from Widgets.interface import img_rc
from Widgets.interface.interface_connexion.interface_con import Ui_App_connenction
# from Widgets.interface.interface_login.interface_log import Ui_Applogin

class Formular_verify(QWidget,Ui_App_connenction):
    def __init__(self):
        
        super().__init__()

    def validate_all_entry(self):
        self.Struct={
        # 'NOM':self.lineEdit_name.text(),
        # 'EMAIL':self.lineEdit_email.text(),
        # 'PASSWORD':self.lineEdit_password.text(),
        # 'VP
                }    
        def validate_email():
            self.lineEdit_email.setMaxLength(20)
            regex=re.compile('^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
            if re.fullmatch(regex,self.lineEdit_email.text()):
                if " " in self.lineEdit_email.text():
                    self.label_4_error_email.setStyleSheet('color: red;')
                    self.label_4_error_email.setText("ne doit pas contenir d espace")
                else:
                    self.Struct['EMAIL']=self.lineEdit_email.text()
                    self.label_4_error_email.setStyleSheet('color: green;')
                    self.label_4_error_email.setText("valide")
            else:
                self.label_4_error_email.setStyleSheet('color: red;')
                self.label_4_error_email.setText("email invalid")
                


        def validate_nom():
            self.lineEdit_name.setMaxLength(20)
            if len(self.lineEdit_name.text())>5:        
                if " " in self.lineEdit_name.text():
                    self.label_error_name.setStyleSheet('color: red;')
                    self.label_error_name.setText("""pas d'espace dans le nom""")
                else:    
                    self.Struct['NOM']=self.lineEdit_name.text()
                    self.label_error_name.setStyleSheet('color: green;')
                    self.label_error_name.setText('validé')
            else:
                self.label_error_name.setStyleSheet('color: red;')
                self.label_error_name.setText("""usermane doit etre supérieur a 5 caractères""") 
        

        def valide_passw():
            self.lineEdit_password.setMaxLength(20)
            regex_passw=re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
            if re.fullmatch(regex_passw,self.lineEdit_password.text()):
                if " " in self.lineEdit_password.text():
                    self.label_5_error_passwor.setStyleSheet('color: red;')
                    self.label_5_error_passwor.setText("le mot de pass ne doit pas contenir d espace")
                    
                else:
                    self.Struct['PASSWORD']=self.lineEdit_password.text()
                    self.label_5_error_passwor.setStyleSheet('color: green;')
                    self.label_5_error_passwor.setText("validé")
                    self.lineEdit_Vpassword.setMaxLength(20)
                    if self.lineEdit_password.text()!=self.lineEdit_Vpassword.text():
                        self.label_6_error_Vpassword.setStyleSheet('color:red')
                        self.label_6_error_Vpassword.setText("les mots de pass sont différents")
                    else:
                        self.label_6_error_Vpassword.setStyleSheet('color: green;')
                        self.label_6_error_Vpassword.setText("valide")    
            else:
                self.label_5_error_passwor.setStyleSheet('color: red;')
                self.label_5_error_passwor.setText("mot de pass invalid")
#                 messagebox.showerror('erreur',"""le mot de pass doit contenir au moins:"
# une lettre majuscule
# une miniscule
# un nombre
# un caractere spécial
# " superieur a 8 caractères"""
#                                         )
        
        def VerifyIdempassword():
            self.lineEdit_Vpassword.setMaxLength(20)
            if self.lineEdit_password.text()!=self.lineEdit_Vpassword.text():
                self.label_6_error_Vpassword.setStyleSheet('color:red')
                self.label_6_error_Vpassword.setText("les mots de pass sont différents")
            else:
                self.Struct['VPASSWORD']=self.lineEdit_Vpassword.text()
                self.label_6_error_Vpassword.setStyleSheet('color: green;')
                self.label_6_error_Vpassword.setText("valide")
        def sql_DB():
            if self.Struct['NOM']!="" and self.Struct['EMAIL']!="" and self.Struct['PASSWORD']!="" and self.Struct['VPASSWORD']!="":
                connexion=sqlite3.connect('Data_user.db')
                curseur=connexion.cursor()
                curseur.execute("""CREATE TABLE IF NOT EXISTS data_users_sec(
                    NOM text,
                    EMAIL text,
                    PASSWORD text) """)
                
                curseur.execute("SELECT EMAIL FROM data_users_sec")    
                list_email=curseur.fetchall()
                verify_mail_box=[]
                for i in list_email:
                    for u in i:
                        print('ok')
                        verify_mail_box.append(u)            
                print(verify_mail_box)
                if self.lineEdit_email.text() in verify_mail_box: 
                    self.label_4_error_email.setStyleSheet('color: red;')
                    self.label_4_error_email.setText("l' email existe déja")
                else:
                    self.label_4_error_email.setStyleSheet('color: green;')
                    self.label_4_error_email.setText("valide")
                    curseur.execute("INSERT INTO data_users_sec VALUES (:NOM,:EMAIL,:PASSWORD)",self.Struct)
                    connexion.commit()        
                    connexion.close()
                    self.stackedWidget_INSCRIPTION.setCurrentWidget(self.page_login)

        VerifyIdempassword()
        validate_email()
        valide_passw()
        validate_nom()
        sql_DB()

    # def sql_DB(self):
    #     if self.Struct['NOM']!="" and self.Struct['EMAIL']!="" and self.Struct['PASSWORD']!="" and self.Struct['VPASSWORD']!="":
    #         connexion=sqlite3.connect('Data_user.db')
    #         curseur=connexion.cursor()
    #         curseur.execute("""CREATE TABLE IF NOT EXISTS data_users_sec(
    #             NOM text,
    #             EMAIL text,
    #             PASSWORD text) """)
            
    #         curseur.execute("SELECT EMAIL FROM data_users_sec")    
    #         list_email=curseur.fetchall()
    #         verify_mail_box=[]
    #         for i in list_email:
    #             for u in i:
    #                 print('ok')
    #                 verify_mail_box.append(u)            
    #         print(verify_mail_box)
    #         if self.lineEdit_email.text() in verify_mail_box: 
    #             self.label_4_error_email.setStyleSheet('color: red;')
    #             self.label_4_error_email.setText("l' email existe déja")
    #         else:
    #             self.label_4_error_email.setStyleSheet('color: green;')
    #             self.label_4_error_email.setText("valide")
    #             curseur.execute("INSERT INTO data_users_sec VALUES (:NOM,:EMAIL,:PASSWORD)",self.Struct)
    #             connexion.commit()        
    #             connexion.close()
    #             self.stackedWidget_INSCRIPTION.setCurrentWidget(self.page_login)
               

                

        # else:
        #     pass  

class LoginValidator(Formular_verify):
    def __init__(self):
        super().__init__()

    def login(self):    
        connexion=sqlite3.connect('Data_user.db')
        curseur=connexion.cursor()
        try:
            curseur.execute("SELECT * FROM data_users_sec WHERE EMAIL=? and PASSWORD=?", [self.lineEdit_email_2.text(), self.lineEdit_password_2.text()])
        except sqlite3.OperationalError:
            curseur.execute("""CREATE TABLE IF NOT EXISTS data_users_sec(
                NOM text,
                EMAIL text,
                PASSWORD text) """)
        else:        
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
                self.stackedWidget_INSCRIPTION.setCurrentWidget(self.page_main)
               
    
    def start_button(self):
        self.login()
    def move_on_conn(self):
        self.stackedWidget_INSCRIPTION.setCurrentWidget(self.page_login)
        self.label_error_name.clear()
        self.label_4_error_email.clear()
        self.label_5_error_passwor.clear()
        self.label_6_error_Vpassword.clear()
        
    def move_on_login(self):
        self.stackedWidget_INSCRIPTION.setCurrentWidget(self.page_connexion)
        self.label_error_login_email.clear()
        self.label_error_login_password.clear()

    def view_show_ins(self,check):
        if check:
            self.icon1 = QIcon()
            self.icon1.addFile(u":/IMG/hide1.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton_show_view_pass.setIcon(self.icon1)
            
            self.lineEdit_password.setEchoMode(QLineEdit.Password)
            self.lineEdit_Vpassword.setEchoMode(QLineEdit.Password)
        else:
            self.icon1.addFile(u":/IMG/red-eye1.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton_show_view_pass.setIcon(self.icon1)
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
            self.lineEdit_Vpassword.setEchoMode(QLineEdit.Normal)
        # self.stackedWidget_INSCRIPTION.addWidget()

    def view_show_con(self,check1):
        if check1:
            self.icon2 = QIcon()
            self.icon2.addFile(u":/IMG/hide2.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton_show_view_pass_2.setIcon(self.icon2)
            self.lineEdit_password_2.setEchoMode(QLineEdit.Password)
            
        else:
            self.icon2.addFile(u":/IMG/red-eye2.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton_show_view_pass_2.setIcon(self.icon2)
            self.lineEdit_password_2.setEchoMode(QLineEdit.Normal)
            


        
      

# class MainWindow1(LoginValidator,QWidget,QApplication):
#     def __init__(self) :
#         super().__init__(self)
class MainWindow(LoginValidator):
    def __init__(self) :
        super(LoginValidator,MainWindow).__init__(self)
        self.setupUi(self)
        self.pushButton_started.setCheckable(False)
        self.pushButton_started.clicked.connect(self.button_clicked) 
        self.stackedWidget_INSCRIPTION.setCurrentWidget(self.page_connexion)
        self.pushButton_sent_request.setCheckable(False)
        self.pushButton_sent_request.clicked.connect(self.start_button)
        self.pushButton_CMD_SE_CONN.clicked.connect(self.move_on_conn)
        self.pushButton_CMD_SE_CONN_2.clicked.connect(self.move_on_login)
        self.pushButton_show_view_pass.clicked.connect(self.view_show_ins)
        self.pushButton_show_view_pass.setCheckable(True)
        self.pushButton_show_view_pass_2.clicked.connect(self.view_show_con)
        self.pushButton_show_view_pass_2.setCheckable(True)
    def button_clicked(self):
        self.validate_all_entry()  
           
        
      
if __name__=="__main__":
    app = QApplication(sys.argv)        

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

# class MainWindow1(LoginValidator,QWidget,QApplication):
#     def __init__(self) :
#         super(LoginValidator,MainWindow1).__init__(self)
#         self.setupUi(self)
#         self.pushButton_sent_request.setCheckable(False)
#         self.pushButton_sent_request.clicked.connect(self.start_button)
    


      
# if __name__=="__main__":
#     app2 = QApplication(sys.argv)        

#     window1 = MainWindow1()
#     window1.show()

# sys.exit(app2.exec())