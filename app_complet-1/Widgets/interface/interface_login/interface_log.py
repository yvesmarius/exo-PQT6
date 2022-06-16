# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'T3.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)


class Ui_Applogin(object):
    def setupUi(self, Applogin):
        if not Applogin.objectName():
            Applogin.setObjectName(u"Applogin")
        Applogin.resize(1021, 748)
        self.label_main_image = QLabel(Applogin)
        self.label_main_image.setObjectName(u"label_main_image")
        self.label_main_image.setGeometry(QRect(-10, -30, 1031, 781))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_main_image.setFont(font)
        self.label_main_image.setPixmap(QPixmap(u":/IMG/main-img.jpg"))
        self.label_main_image.setScaledContents(True)
        self.label_3 = QLabel(Applogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 50, 181, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white")
        self.frame_login = QFrame(Applogin)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setGeometry(QRect(470, 30, 511, 671))
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
        font2 = QFont()
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:white")
        self.label_works = QLabel(self.frame_login)
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
        self.label_about = QLabel(self.frame_login)
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
        self.label_contacts = QLabel(self.frame_login)
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
        self.label_conn_text.setFont(font2)
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
        self.lineEdit_email = QLineEdit(self.frame_login)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(61, 312, 381, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.lineEdit_email.setFont(font3)
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
        self.lineEdit_password = QLineEdit(self.frame_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(60, 378, 381, 31))
        self.lineEdit_password.setFont(font3)
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
        self.label_10 = QLabel(Applogin)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 270, 381, 61))
        font4 = QFont()
        font4.setPointSize(36)
        font4.setBold(True)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:white")
        self.label_11 = QLabel(Applogin)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 330, 341, 51))
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color:white")
        self.label_12 = QLabel(Applogin)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 380, 261, 71))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color:white")

        self.retranslateUi(Applogin)

        QMetaObject.connectSlotsByName(Applogin)
    # setupUi

    def retranslateUi(self, Applogin):
        Applogin.setWindowTitle(QCoreApplication.translate("Applogin", u"Form", None))
        self.label_main_image.setStyleSheet(QCoreApplication.translate("Applogin", u"color:grey;border:1px solid grey;hover {\n"
"  background-color: yellow;\n"
"}\n"
"\n"
"    \n"
"", None))
        self.label_main_image.setText("")
        self.label_3.setText(QCoreApplication.translate("Applogin", u"ZERO GRAVITY", None))
        self.pushButton.setText(QCoreApplication.translate("Applogin", u"UI/UX designs", None))
        self.pushButton_2.setText(QCoreApplication.translate("Applogin", u"Branding", None))
        self.pushButton_3.setText(QCoreApplication.translate("Applogin", u"Design System", None))
        self.pushButton_4.setText(QCoreApplication.translate("Applogin", u"Website", None))
        self.pushButton_5.setText(QCoreApplication.translate("Applogin", u"Other", None))
        self.label_2.setText(QCoreApplication.translate("Applogin", u"I'm interesed in...", None))
        self.label_works.setText(QCoreApplication.translate("Applogin", u"works", None))
        self.label_about.setText(QCoreApplication.translate("Applogin", u"about", None))
        self.label_contacts.setText(QCoreApplication.translate("Applogin", u"contacts", None))
        self.pushButton_sent_request.setText(QCoreApplication.translate("Applogin", u"SENT REQUEST", None))
        self.label_conn_text.setText(QCoreApplication.translate("Applogin", u"CONNEXION", None))
        self.label_error_login_email.setText("")
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Applogin", u"Your Email", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("Applogin", u"password", None))
        self.label_10.setText(QCoreApplication.translate("Applogin", u"Have a project ?", None))
        self.label_11.setText(QCoreApplication.translate("Applogin", u"we would love", None))
        self.label_12.setText(QCoreApplication.translate("Applogin", u"to help.", None))
    # retranslateUi

