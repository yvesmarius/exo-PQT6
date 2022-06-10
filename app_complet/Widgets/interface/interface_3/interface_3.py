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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1013, 748)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -30, 1031, 781))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"../Static/Appmdl2_2/main-img.jpg"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 50, 181, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(470, 30, 511, 671))
        self.frame.setStyleSheet(u"background-color:b;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
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
        self.pushButton_2 = QPushButton(self.frame)
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
        self.pushButton_3 = QPushButton(self.frame)
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
        self.pushButton_4 = QPushButton(self.frame)
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
        self.pushButton_5 = QPushButton(self.frame)
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 60, 161, 16))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:white")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 10, 49, 16))
        self.label_4.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 10, 49, 16))
        self.label_6.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 10, 51, 16))
        self.label_5.setStyleSheet(u"QLabel\n"
"{\n"
"	color:grey\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:white\n"
"}")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 300, 411, 22))
        self.lineEdit.setStyleSheet(u"border:0px solid;border-bottom:1px solid grey;color:grey")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 380, 411, 22))
        self.lineEdit_2.setStyleSheet(u"border:0px solid;border-bottom:1px solid grey;color:grey;")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 470, 411, 22))
        self.lineEdit_3.setStyleSheet(u"border:0px solid;border-bottom:1px solid grey;color:grey;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 530, 121, 16))
        font3 = QFont()
        font3.setPointSize(15)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:grey\n"
"}")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(50, 580, 161, 41))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color:rgb(39, 12, 114);\n"
"	color:white\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color:white\n"
"}\n"
"")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 530, 21, 16))
        self.label_8.setStyleSheet(u"")
        self.label_8.setPixmap(QPixmap(u"crayon (2).png"))
        self.label_8.setScaledContents(True)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 290, 351, 51))
        font4 = QFont()
        font4.setPointSize(45)
        font4.setBold(True)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:white")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 350, 301, 51))
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color:white")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 400, 171, 61))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color:white")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setStyleSheet(QCoreApplication.translate("Form", u"color:grey;border:1px solid grey;hover {\n"
"  background-color: yellow;\n"
"}\n"
"\n"
"    \n"
"", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"ZERO GRAVITY", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"UI/UX designs", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Branding", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Design System", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Website", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Other", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"I'm interesed in...", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"works", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"about", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"contacts", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Your Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Your Email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Tell us about project", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"add attachment", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"sent request", None))
        self.label_8.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Have a project ?", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"we would love", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"to help.", None))
    # retranslateUi

