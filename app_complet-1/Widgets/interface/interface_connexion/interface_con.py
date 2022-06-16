# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tconnection_full.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)


class Ui_App_connenction(object):
    def setupUi(self, App_connenction):
        if not App_connenction.objectName():
            App_connenction.setObjectName(u"App_connenction")
        App_connenction.resize(1032, 778)
        App_connenction.setMinimumSize(QSize(1032, 778))
        App_connenction.setMaximumSize(QSize(1032, 778))
        icon = QIcon()
        icon.addFile(u":/IMG/cyclone.png", QSize(), QIcon.Normal, QIcon.Off)
        App_connenction.setWindowIcon(icon)
        self.stackedWidget_INSCRIPTION = QStackedWidget(App_connenction)
        self.stackedWidget_INSCRIPTION.setObjectName(u"stackedWidget_INSCRIPTION")
        self.stackedWidget_INSCRIPTION.setGeometry(QRect(0, 0, 1031, 781))
        self.page_connexion = QWidget()
        self.page_connexion.setObjectName(u"page_connexion")
        self.label = QLabel(self.page_connexion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -1, 1332, 861))
        self.label.setPixmap(QPixmap(u":/IMG/4404912.jpg"))
        self.label.setScaledContents(True)
        self.frame_inscription = QFrame(self.page_connexion)
        self.frame_inscription.setObjectName(u"frame_inscription")
        self.frame_inscription.setGeometry(QRect(510, 50, 491, 671))
        self.frame_inscription.setStyleSheet(u"background-color:b;")
        self.frame_inscription.setFrameShape(QFrame.StyledPanel)
        self.frame_inscription.setFrameShadow(QFrame.Raised)
        self.label_inscription = QLabel(self.frame_inscription)
        self.label_inscription.setObjectName(u"label_inscription")
        self.label_inscription.setGeometry(QRect(170, 120, 171, 31))
        font = QFont()
        font.setPointSize(20)
        self.label_inscription.setFont(font)
        self.label_inscription.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:rgb(14, 4, 64)\n"
"}")
        self.label_works = QLabel(self.frame_inscription)
        self.label_works.setObjectName(u"label_works")
        self.label_works.setGeometry(QRect(310, 10, 49, 16))
        self.label_works.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.label_about = QLabel(self.frame_inscription)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setGeometry(QRect(370, 10, 49, 16))
        self.label_about.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.label_contacts = QLabel(self.frame_inscription)
        self.label_contacts.setObjectName(u"label_contacts")
        self.label_contacts.setGeometry(QRect(420, 10, 51, 16))
        self.label_contacts.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.checkBox_other = QCheckBox(self.frame_inscription)
        self.checkBox_other.setObjectName(u"checkBox_other")
        self.checkBox_other.setGeometry(QRect(180, 480, 85, 20))
        self.checkBox_other.setStyleSheet(u"QCheckBox{color:white}QCheckBox:hover\n"
"{\n"
"	color:rgb(128, 128, 128)\n"
"}")
        self.checkBox_strategie_consulting = QCheckBox(self.frame_inscription)
        self.checkBox_strategie_consulting.setObjectName(u"checkBox_strategie_consulting")
        self.checkBox_strategie_consulting.setGeometry(QRect(180, 450, 151, 20))
        self.checkBox_strategie_consulting.setStyleSheet(u"QCheckBox{color:white}QCheckBox:hover\n"
"{\n"
"	color:rgb(128, 128, 128)\n"
"}")
        self.checkBox_2_user_rechear = QCheckBox(self.frame_inscription)
        self.checkBox_2_user_rechear.setObjectName(u"checkBox_2_user_rechear")
        self.checkBox_2_user_rechear.setGeometry(QRect(60, 480, 101, 20))
        self.checkBox_2_user_rechear.setStyleSheet(u"QCheckBox\n"
"{\n"
"	color:white\n"
"}\n"
"QCheckBox:hover\n"
"{\n"
"	color:rgb(128, 128, 128)\n"
"}")
        self.checkBox_web = QCheckBox(self.frame_inscription)
        self.checkBox_web.setObjectName(u"checkBox_web")
        self.checkBox_web.setGeometry(QRect(60, 420, 111, 20))
        self.checkBox_web.setStyleSheet(u"QCheckBox{color:white}QCheckBox:hover\n"
"{\n"
"	color:rgb(128, 128, 128)\n"
"}")
        self.checkBox_Uxdesign = QCheckBox(self.frame_inscription)
        self.checkBox_Uxdesign.setObjectName(u"checkBox_Uxdesign")
        self.checkBox_Uxdesign.setGeometry(QRect(60, 450, 85, 20))
        self.checkBox_Uxdesign.setStyleSheet(u"QCheckBox{color:white}QCheckBox:hover\n"
"{\n"
"	color:rgb(128, 128, 128)\n"
"}")
        self.pushButton_started = QPushButton(self.frame_inscription)
        self.pushButton_started.setObjectName(u"pushButton_started")
        self.pushButton_started.setGeometry(QRect(60, 550, 191, 41))
        self.pushButton_started.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color:rgb(39, 12, 114);\n"
"	color:white\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color:white;\n"
"	font-size:20px;\n"
"	font-family:arial\n"
"}\n"
"")
        self.pushButton_started.setCheckable(True)
        self.label_error_name = QLabel(self.frame_inscription)
        self.label_error_name.setObjectName(u"label_error_name")
        self.label_error_name.setGeometry(QRect(200, 230, 241, 20))
        self.label_error_name.setLayoutDirection(Qt.LeftToRight)
        self.label_error_name.setAutoFillBackground(False)
        self.label_error_name.setStyleSheet(u"color:white")
        self.label_error_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4_error_email = QLabel(self.frame_inscription)
        self.label_4_error_email.setObjectName(u"label_4_error_email")
        self.label_4_error_email.setGeometry(QRect(200, 280, 241, 20))
        self.label_4_error_email.setStyleSheet(u"color:white")
        self.label_4_error_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5_error_passwor = QLabel(self.frame_inscription)
        self.label_5_error_passwor.setObjectName(u"label_5_error_passwor")
        self.label_5_error_passwor.setGeometry(QRect(200, 330, 241, 20))
        self.label_5_error_passwor.setStyleSheet(u"color:white")
        self.label_5_error_passwor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6_error_Vpassword = QLabel(self.frame_inscription)
        self.label_6_error_Vpassword.setObjectName(u"label_6_error_Vpassword")
        self.label_6_error_Vpassword.setGeometry(QRect(200, 380, 241, 20))
        self.label_6_error_Vpassword.setLayoutDirection(Qt.LeftToRight)
        self.label_6_error_Vpassword.setStyleSheet(u"color:white")
        self.label_6_error_Vpassword.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_Vpassword = QLineEdit(self.frame_inscription)
        self.lineEdit_Vpassword.setObjectName(u"lineEdit_Vpassword")
        self.lineEdit_Vpassword.setGeometry(QRect(61, 348, 381, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_Vpassword.setFont(font1)
        self.lineEdit_Vpassword.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border:0px solid;\n"
"	border-bottom:1px solid grey;\n"
"	color:grey\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"	border-bottom:2px solid white;\n"
"	\n"
"}")
        self.lineEdit_email = QLineEdit(self.frame_inscription)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(61, 248, 381, 31))
        self.lineEdit_email.setFont(font1)
        self.lineEdit_email.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border:0px solid;\n"
"	border-bottom:1px solid grey;\n"
"	color:grey\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"	border-bottom:2px solid white;\n"
"	\n"
"}")
        self.lineEdit_name = QLineEdit(self.frame_inscription)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(61, 198, 381, 31))
        self.lineEdit_name.setFont(font1)
        self.lineEdit_name.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border:0px solid;\n"
"	border-bottom:1px solid grey;\n"
"	color:grey\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"	border-bottom:2px solid white;\n"
"	\n"
"}")
        self.lineEdit_password = QLineEdit(self.frame_inscription)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(61, 298, 381, 31))
        self.lineEdit_password.setFont(font1)
        self.lineEdit_password.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border:0px solid;\n"
"	border-bottom:1px solid grey;\n"
"	color:grey\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"	border-bottom:2px solid white;\n"
"	\n"
"}")
        self.lineEdit_password.setFrame(True)
        self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        self.checkBox_content_creat = QCheckBox(self.frame_inscription)
        self.checkBox_content_creat.setObjectName(u"checkBox_content_creat")
        self.checkBox_content_creat.setGeometry(QRect(180, 420, 121, 20))
        self.checkBox_content_creat.setStyleSheet(u"QCheckBox{color:white}QCheckBox:hover\n"
"{\n"
"	color:rgb(128, 128, 128)\n"
"}")
        self.pushButton_show_view_pass = QPushButton(self.frame_inscription)
        self.pushButton_show_view_pass.setObjectName(u"pushButton_show_view_pass")
        self.pushButton_show_view_pass.setGeometry(QRect(450, 303, 31, 31))
        self.pushButton_show_view_pass.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	border-radius:12px\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/IMG/red-eye1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_show_view_pass.setIcon(icon1)
        self.pushButton_show_view_pass.setIconSize(QSize(25, 25))
        self.pushButton_CMD_SE_CONN = QPushButton(self.frame_inscription)
        self.pushButton_CMD_SE_CONN.setObjectName(u"pushButton_CMD_SE_CONN")
        self.pushButton_CMD_SE_CONN.setGeometry(QRect(10, 10, 131, 24))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_CMD_SE_CONN.setFont(font2)
        self.pushButton_CMD_SE_CONN.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	color:rgb(49, 10, 92)	\n"
"}\n"
"QPushButton{color:white;}")
        self.label_7 = QLabel(self.page_connexion)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 40, 181, 31))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:white")
        self.stackedWidget_INSCRIPTION.addWidget(self.page_connexion)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.label_main_image = QLabel(self.page_login)
        self.label_main_image.setObjectName(u"label_main_image")
        self.label_main_image.setGeometry(QRect(-10, 0, 1051, 781))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_main_image.setFont(font4)
        self.label_main_image.setPixmap(QPixmap(u":/IMG/main-img.jpg"))
        self.label_main_image.setScaledContents(True)
        self.frame_login = QFrame(self.page_login)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setGeometry(QRect(500, 50, 501, 671))
        self.frame_login.setStyleSheet(u"background-color:b;")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_login)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 100, 121, 41))
        self.pushButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border: 2px solid white;\n"
"	color:white\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid grey;\n"
"	color:grey\n"
"} ")
        self.pushButton_2 = QPushButton(self.frame_login)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 100, 101, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border: 2px solid white;\n"
"	color:white\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid grey;\n"
"	color:grey\n"
"} ")
        self.pushButton_3 = QPushButton(self.frame_login)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 160, 121, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border: 2px solid white;\n"
"	color:white\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid grey;\n"
"	color:grey\n"
"} ")
        self.pushButton_4 = QPushButton(self.frame_login)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 100, 101, 41))
        self.pushButton_4.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border: 2px solid white;\n"
"	color:white\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid grey;\n"
"	color:grey\n"
"} ")
        self.pushButton_5 = QPushButton(self.frame_login)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(200, 160, 81, 41))
        self.pushButton_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border: 2px solid white;\n"
"	color:white\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid grey;\n"
"	color:grey\n"
"} ")
        self.label_2 = QLabel(self.frame_login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 60, 161, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:white")
        self.label_works_2 = QLabel(self.frame_login)
        self.label_works_2.setObjectName(u"label_works_2")
        self.label_works_2.setGeometry(QRect(310, 10, 49, 16))
        self.label_works_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.label_about_2 = QLabel(self.frame_login)
        self.label_about_2.setObjectName(u"label_about_2")
        self.label_about_2.setGeometry(QRect(370, 10, 49, 16))
        self.label_about_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.label_contacts_2 = QLabel(self.frame_login)
        self.label_contacts_2.setObjectName(u"label_contacts_2")
        self.label_contacts_2.setGeometry(QRect(420, 10, 51, 16))
        self.label_contacts_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.pushButton_sent_request = QPushButton(self.frame_login)
        self.pushButton_sent_request.setObjectName(u"pushButton_sent_request")
        self.pushButton_sent_request.setGeometry(QRect(50, 520, 191, 41))
        self.pushButton_sent_request.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color:rgb(39, 12, 114);\n"
"	color:white\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color:white;\n"
"	font-size:20px;\n"
"	font-family:arial\n"
"}\n"
"")
        self.pushButton_sent_request.setCheckable(True)
        self.label_conn_text = QLabel(self.frame_login)
        self.label_conn_text.setObjectName(u"label_conn_text")
        self.label_conn_text.setGeometry(QRect(180, 210, 181, 41))
        self.label_conn_text.setFont(font)
        self.label_conn_text.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:rgb(57, 21, 157)\n"
"}")
        self.label_error_login_email = QLabel(self.frame_login)
        self.label_error_login_email.setObjectName(u"label_error_login_email")
        self.label_error_login_email.setGeometry(QRect(168, 350, 271, 16))
        self.label_error_login_email.setStyleSheet(u"color:white")
        self.label_error_login_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_error_login_password = QLabel(self.frame_login)
        self.label_error_login_password.setObjectName(u"label_error_login_password")
        self.label_error_login_password.setGeometry(QRect(168, 410, 271, 20))
        self.label_error_login_password.setStyleSheet(u"color:white")
        self.label_error_login_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_email_2 = QLineEdit(self.frame_login)
        self.lineEdit_email_2.setObjectName(u"lineEdit_email_2")
        self.lineEdit_email_2.setGeometry(QRect(61, 312, 381, 31))
        self.lineEdit_email_2.setFont(font1)
        self.lineEdit_email_2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border:0px solid;\n"
"	border-bottom:1px solid grey;\n"
"	color:grey\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"	border-bottom:2px solid white;\n"
"	\n"
"}")
        self.lineEdit_password_2 = QLineEdit(self.frame_login)
        self.lineEdit_password_2.setObjectName(u"lineEdit_password_2")
        self.lineEdit_password_2.setGeometry(QRect(60, 378, 381, 31))
        self.lineEdit_password_2.setFont(font1)
        self.lineEdit_password_2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border:0px solid;\n"
"	border-bottom:1px solid grey;\n"
"	color:grey\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"	border-bottom:2px solid white;\n"
"	\n"
"}")
        self.pushButton_show_view_pass_2 = QPushButton(self.frame_login)
        self.pushButton_show_view_pass_2.setObjectName(u"pushButton_show_view_pass_2")
        self.pushButton_show_view_pass_2.setGeometry(QRect(450, 380, 31, 31))
        self.pushButton_show_view_pass_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	border-radius:12px\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/IMG/red-eye2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_show_view_pass_2.setIcon(icon2)
        self.pushButton_show_view_pass_2.setIconSize(QSize(25, 25))
        self.pushButton_CMD_SE_CONN_2 = QPushButton(self.frame_login)
        self.pushButton_CMD_SE_CONN_2.setObjectName(u"pushButton_CMD_SE_CONN_2")
        self.pushButton_CMD_SE_CONN_2.setGeometry(QRect(0, 10, 131, 24))
        self.pushButton_CMD_SE_CONN_2.setFont(font2)
        self.pushButton_CMD_SE_CONN_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	color:rgb(49, 10, 92)	\n"
"}\n"
"QPushButton{color:white;}")
        self.label_10 = QLabel(self.page_login)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 280, 381, 61))
        font5 = QFont()
        font5.setPointSize(36)
        font5.setBold(True)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color:white")
        self.label_4 = QLabel(self.page_login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 60, 181, 41))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:white")
        self.label_12 = QLabel(self.page_login)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 390, 261, 71))
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"color:white")
        self.label_11 = QLabel(self.page_login)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 340, 341, 51))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color:white")
        self.stackedWidget_INSCRIPTION.addWidget(self.page_login)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.frame = QFrame(self.page_main)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1031, 781))
        self.frame.setStyleSheet(u"background-color:white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, 0, 251, 711))
        self.widget.setStyleSheet(u"QWidget{background-color:rgb(26, 10, 30);}")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 30, 141, 131))
        self.label_3.setPixmap(QPixmap(u":/IMG/diamond.png"))
        self.label_3.setScaledContents(True)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 180, 181, 21))
        font6 = QFont()
        font6.setPointSize(16)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color:white")
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(-10, 360, 261, 91))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setItalic(True)
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/IMG/orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 230, 81, 20))
        self.label_6.setStyleSheet(u"color:white")
        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(0, 270, 251, 91))
        self.pushButton_15.setFont(font7)
        self.pushButton_15.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/IMG/worldwide.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setIconSize(QSize(30, 30))
        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(-30, 450, 281, 91))
        self.pushButton_8.setFont(font7)
        self.pushButton_8.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/IMG/diamond.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(30, 30))
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 540, 241, 91))
        self.pushButton_9.setFont(font7)
        self.pushButton_9.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/IMG/[cloud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(240, -10, 801, 791))
        self.widget_2.setStyleSheet(u"color:white")
        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(60, 70, 170, 170))
        self.pushButton_10.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon7 = QIcon()
        icon7.addFile(u":/IMG/add (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QSize(25, 25))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)
        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(60, 270, 170, 170))
        self.pushButton_11.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon8 = QIcon()
        icon8.addFile(u":/IMG/layers.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setIconSize(QSize(80, 80))
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(310, 70, 170, 170))
        self.pushButton_12.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon9 = QIcon()
        icon9.addFile(u":/IMG/stock-exchange-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon9)
        self.pushButton_12.setIconSize(QSize(80, 80))
        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(310, 270, 170, 170))
        self.pushButton_13.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon10 = QIcon()
        icon10.addFile(u":/IMG/graphic-design.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon10)
        self.pushButton_13.setIconSize(QSize(80, 80))
        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(560, 70, 170, 170))
        self.pushButton_14.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon11 = QIcon()
        icon11.addFile(u":/IMG/android-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon11)
        self.pushButton_14.setIconSize(QSize(80, 80))
        self.pushButton_16 = QPushButton(self.widget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(40, 20, 101, 31))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(True)
        self.pushButton_16.setFont(font8)
        self.pushButton_16.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	color:black\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:grey\n"
"}")
        self.pushButton_16.setFlat(True)
        self.pushButton_17 = QPushButton(self.widget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(170, 20, 111, 31))
        self.pushButton_17.setFont(font8)
        self.pushButton_17.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	color:black\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:grey;\n"
"	\n"
"}\n"
"")
        self.pushButton_17.setFlat(True)
        self.pushButton_18 = QPushButton(self.widget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(480, 730, 75, 24))
        self.pushButton_18.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color:rgb(102, 237, 250)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:black;\n"
"	border:0px solid;\n"
"	background-color:rgb(231, 230, 232)\n"
"	\n"
"}")
        self.pushButton_19 = QPushButton(self.widget_2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(640, 730, 75, 24))
        self.pushButton_19.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color:rgb(102, 237, 250)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:black;\n"
"	border:0px solid;\n"
"	background-color:rgb(231, 230, 232)\n"
"	\n"
"}")
        self.pushButton_20 = QPushButton(self.widget_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(80, 730, 141, 24))
        self.pushButton_20.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color:rgb(102, 237, 250)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:black;\n"
"	border:0px solid;\n"
"	background-color:rgb(231, 230, 232)\n"
"	\n"
"}")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 240, 91, 16))
        self.label_8.setStyleSheet(u"color:black")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 240, 121, 16))
        self.label_9.setStyleSheet(u"color:black")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 440, 111, 16))
        self.label_13.setStyleSheet(u"color:black")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(310, 440, 91, 16))
        self.label_14.setStyleSheet(u"color:black")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(560, 240, 91, 16))
        self.label_15.setStyleSheet(u"color:black")
        self.pushButton_21 = QPushButton(self.widget_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(560, 270, 170, 170))
        self.pushButton_21.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon12 = QIcon()
        icon12.addFile(u":/IMG/padlock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon12)
        self.pushButton_21.setIconSize(QSize(80, 80))
        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(560, 440, 91, 16))
        self.label_16.setStyleSheet(u"color:black")
        self.pushButton_22 = QPushButton(self.widget_2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(60, 480, 170, 170))
        self.pushButton_22.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon13 = QIcon()
        icon13.addFile(u":/IMG/house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_22.setIcon(icon13)
        self.pushButton_22.setIconSize(QSize(80, 80))
        self.pushButton_22.setCheckable(False)
        self.pushButton_22.setFlat(False)
        self.pushButton_23 = QPushButton(self.widget_2)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(310, 480, 170, 170))
        self.pushButton_23.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon14 = QIcon()
        icon14.addFile(u":/IMG/cracking.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_23.setIcon(icon14)
        self.pushButton_23.setIconSize(QSize(80, 80))
        self.pushButton_23.setCheckable(False)
        self.pushButton_23.setFlat(False)
        self.pushButton_24 = QPushButton(self.widget_2)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(560, 470, 170, 170))
        self.pushButton_24.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon15 = QIcon()
        icon15.addFile(u":/IMG/muscle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon15)
        self.pushButton_24.setIconSize(QSize(80, 80))
        self.pushButton_24.setCheckable(False)
        self.pushButton_24.setFlat(False)
        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 650, 111, 16))
        self.label_17.setStyleSheet(u"color:black")
        self.label_18 = QLabel(self.widget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(310, 650, 111, 16))
        self.label_18.setStyleSheet(u"color:black")
        self.label_19 = QLabel(self.widget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(560, 640, 111, 16))
        self.label_19.setStyleSheet(u"color:black")
        self.stackedWidget_INSCRIPTION.addWidget(self.page_main)

        self.retranslateUi(App_connenction)

        self.stackedWidget_INSCRIPTION.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(App_connenction)
    # setupUi

    def retranslateUi(self, App_connenction):
        App_connenction.setWindowTitle(QCoreApplication.translate("App_connenction", u"VORTEX", None))
        self.label.setText("")
        self.label_inscription.setText(QCoreApplication.translate("App_connenction", u"INSCRIPTION", None))
        self.label_works.setText(QCoreApplication.translate("App_connenction", u"works", None))
        self.label_about.setText(QCoreApplication.translate("App_connenction", u"about", None))
        self.label_contacts.setText(QCoreApplication.translate("App_connenction", u"contacts", None))
        self.checkBox_other.setText(QCoreApplication.translate("App_connenction", u"other", None))
        self.checkBox_strategie_consulting.setText(QCoreApplication.translate("App_connenction", u"Strategie & consulting", None))
        self.checkBox_2_user_rechear.setText(QCoreApplication.translate("App_connenction", u"user reseach", None))
        self.checkBox_web.setText(QCoreApplication.translate("App_connenction", u"website design", None))
        self.checkBox_Uxdesign.setText(QCoreApplication.translate("App_connenction", u"UX design", None))
        self.pushButton_started.setText(QCoreApplication.translate("App_connenction", u"Started", None))
        self.label_error_name.setText("")
        self.label_4_error_email.setText("")
        self.label_5_error_passwor.setText("")
        self.label_6_error_Vpassword.setText("")
        self.lineEdit_Vpassword.setPlaceholderText(QCoreApplication.translate("App_connenction", u" confirmer password", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("App_connenction", u"Your Email", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("App_connenction", u"Your Name", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("App_connenction", u"password", None))
        self.checkBox_content_creat.setText(QCoreApplication.translate("App_connenction", u"Content creation", None))
        self.pushButton_show_view_pass.setText("")
        self.pushButton_CMD_SE_CONN.setText(QCoreApplication.translate("App_connenction", u"SE CONNECTER", None))
        self.label_7.setText(QCoreApplication.translate("App_connenction", u"ZERO GRAVITY", None))
        self.label_main_image.setStyleSheet(QCoreApplication.translate("App_connenction", u"color:grey;border:1px solid grey;hover {\n"
"  background-color: yellow;\n"
"}\n"
"\n"
"    \n"
"", None))
        self.label_main_image.setText("")
        self.pushButton.setText(QCoreApplication.translate("App_connenction", u"UI/UX designs", None))
        self.pushButton_2.setText(QCoreApplication.translate("App_connenction", u"Branding", None))
        self.pushButton_3.setText(QCoreApplication.translate("App_connenction", u"Design System", None))
        self.pushButton_4.setText(QCoreApplication.translate("App_connenction", u"Website", None))
        self.pushButton_5.setText(QCoreApplication.translate("App_connenction", u"Other", None))
        self.label_2.setText(QCoreApplication.translate("App_connenction", u"I'm interesed in...", None))
        self.label_works_2.setText(QCoreApplication.translate("App_connenction", u"works", None))
        self.label_about_2.setText(QCoreApplication.translate("App_connenction", u"about", None))
        self.label_contacts_2.setText(QCoreApplication.translate("App_connenction", u"contacts", None))
        self.pushButton_sent_request.setText(QCoreApplication.translate("App_connenction", u"SENT REQUEST", None))
        self.label_conn_text.setText(QCoreApplication.translate("App_connenction", u"CONNEXION", None))
        self.label_error_login_email.setText("")
        self.lineEdit_email_2.setPlaceholderText(QCoreApplication.translate("App_connenction", u"Your Email", None))
        self.lineEdit_password_2.setPlaceholderText(QCoreApplication.translate("App_connenction", u"password", None))
        self.pushButton_show_view_pass_2.setText("")
        self.pushButton_CMD_SE_CONN_2.setText(QCoreApplication.translate("App_connenction", u"INSCRIPTION", None))
        self.label_10.setText(QCoreApplication.translate("App_connenction", u"Have a project ?", None))
        self.label_4.setText(QCoreApplication.translate("App_connenction", u"ZERO GRAVITY", None))
        self.label_12.setText(QCoreApplication.translate("App_connenction", u"to help.", None))
        self.label_11.setText(QCoreApplication.translate("App_connenction", u"we would love", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("App_connenction", u"Welcome to sketch", None))
        self.pushButton_7.setText(QCoreApplication.translate("App_connenction", u"Join our newsletter \n"
"News and tips in your inbox", None))
        self.label_6.setText(QCoreApplication.translate("App_connenction", u"version 48.2", None))
        self.pushButton_15.setText(QCoreApplication.translate("App_connenction", u" New to sketch ?\n"
" Get started with these tutorials", None))
        self.pushButton_8.setText(QCoreApplication.translate("App_connenction", u" Get sketch Mirror\n"
" view your design on ios", None))
        self.pushButton_9.setText(QCoreApplication.translate("App_connenction", u"Join Sketch Cloud\n"
"Upload and share your designs", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("App_connenction", u"Recents", None))
        self.pushButton_17.setText(QCoreApplication.translate("App_connenction", u"Templates", None))
        self.pushButton_18.setText(QCoreApplication.translate("App_connenction", u"cancel", None))
        self.pushButton_19.setText(QCoreApplication.translate("App_connenction", u"choose", None))
        self.pushButton_20.setText(QCoreApplication.translate("App_connenction", u"Open a existing file...", None))
        self.label_8.setText(QCoreApplication.translate("App_connenction", u"New documents", None))
        self.label_9.setText(QCoreApplication.translate("App_connenction", u"Android Icon Design", None))
        self.label_13.setText(QCoreApplication.translate("App_connenction", u"Materials Design", None))
        self.label_14.setText(QCoreApplication.translate("App_connenction", u"Web Design", None))
        self.label_15.setText(QCoreApplication.translate("App_connenction", u"Ios App Icon", None))
        self.pushButton_21.setText("")
        self.label_16.setText(QCoreApplication.translate("App_connenction", u"PadLock", None))
        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
        self.pushButton_24.setText("")
        self.label_17.setText(QCoreApplication.translate("App_connenction", u"House save", None))
        self.label_18.setText(QCoreApplication.translate("App_connenction", u"Cracking", None))
        self.label_19.setText(QCoreApplication.translate("App_connenction", u"Power", None))
    # retranslateUi

