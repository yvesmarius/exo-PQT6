# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tconnection.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_App_connenction(object):
    def setupUi(self, App_connenction):
        if not App_connenction.objectName():
            App_connenction.setObjectName(u"App_connenction")
        App_connenction.resize(839, 630)
        self.frame_connection = QFrame(App_connenction)
        self.frame_connection.setObjectName(u"frame_connection")
        self.frame_connection.setGeometry(QRect(420, 0, 511, 631))
        self.frame_connection.setFrameShape(QFrame.StyledPanel)
        self.frame_connection.setFrameShadow(QFrame.Raised)
        self.lineEdit_name = QLineEdit(self.frame_connection)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(80, 120, 261, 21))
        self.lineEdit_email = QLineEdit(self.frame_connection)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(80, 180, 261, 21))
        self.lineEdit_number = QLineEdit(self.frame_connection)
        self.lineEdit_number.setObjectName(u"lineEdit_number")
        self.lineEdit_number.setGeometry(QRect(120, 240, 221, 21))
        self.plainText_conn = QPlainTextEdit(self.frame_connection)
        self.plainText_conn.setObjectName(u"plainText_conn")
        self.plainText_conn.setGeometry(QRect(80, 310, 261, 81))
        self.label_main = QLabel(self.frame_connection)
        self.label_main.setObjectName(u"label_main")
        self.label_main.setGeometry(QRect(80, 10, 241, 71))
        font = QFont()
        font.setPointSize(24)
        self.label_main.setFont(font)
        self.checkBox_web = QCheckBox(self.frame_connection)
        self.checkBox_web.setObjectName(u"checkBox_web")
        self.checkBox_web.setGeometry(QRect(80, 430, 111, 20))
        self.checkBox_2_user_rechear = QCheckBox(self.frame_connection)
        self.checkBox_2_user_rechear.setObjectName(u"checkBox_2_user_rechear")
        self.checkBox_2_user_rechear.setGeometry(QRect(80, 490, 101, 20))
        self.checkBox_other = QCheckBox(self.frame_connection)
        self.checkBox_other.setObjectName(u"checkBox_other")
        self.checkBox_other.setGeometry(QRect(200, 490, 85, 20))
        self.checkBox_strategie_consulting = QCheckBox(self.frame_connection)
        self.checkBox_strategie_consulting.setObjectName(u"checkBox_strategie_consulting")
        self.checkBox_strategie_consulting.setGeometry(QRect(200, 460, 151, 20))
        self.checkBox_Uxdesign = QCheckBox(self.frame_connection)
        self.checkBox_Uxdesign.setObjectName(u"checkBox_Uxdesign")
        self.checkBox_Uxdesign.setGeometry(QRect(80, 460, 85, 20))
        self.checkBox_content_creat = QCheckBox(self.frame_connection)
        self.checkBox_content_creat.setObjectName(u"checkBox_content_creat")
        self.checkBox_content_creat.setGeometry(QRect(200, 430, 121, 20))
        self.buttonvalid = QPushButton(self.frame_connection)
        self.buttonvalid.setObjectName(u"buttonvalid")
        self.buttonvalid.setGeometry(QRect(80, 530, 261, 41))
        self.buttonvalid.setStyleSheet(u"")
        self.label_2 = QLabel(self.frame_connection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 410, 58, 16))
        self.label_name = QLabel(self.frame_connection)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(80, 90, 58, 16))
        self.label_email = QLabel(self.frame_connection)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(80, 150, 58, 16))
        self.label_5 = QLabel(self.frame_connection)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 210, 91, 16))
        self.label_text_plain = QLabel(self.frame_connection)
        self.label_text_plain.setObjectName(u"label_text_plain")
        self.label_text_plain.setGeometry(QRect(80, 270, 111, 16))
        self.comboBox = QComboBox(self.frame_connection)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(70, 240, 51, 21))
        self.comboBox.setEditable(True)
        self.photo = QLabel(App_connenction)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(0, 0, 421, 631))
        self.photo.setPixmap(QPixmap(u"../Static/mdl_connexion/tete-de-lit-en-bois-et-tissu.jpeg"))
        self.photo.setScaledContents(True)

        self.retranslateUi(App_connenction)

        QMetaObject.connectSlotsByName(App_connenction)
    # setupUi

    def retranslateUi(self, App_connenction):
        App_connenction.setWindowTitle(QCoreApplication.translate("App_connenction", u"Form", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("App_connenction", u"your name", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("App_connenction", u"you@gmail.com", None))
        self.lineEdit_number.setText("")
        self.lineEdit_number.setPlaceholderText(QCoreApplication.translate("App_connenction", u"           +1(255) 0000-0000", None))
        self.plainText_conn.setPlaceholderText(QCoreApplication.translate("App_connenction", u"Tell us a little about the project", None))
        self.label_main.setText(QCoreApplication.translate("App_connenction", u"<html><head/><body><p>-&gt;<span style=\" font-size:24pt;\"> Let's level up your </span></p><p><span style=\" font-size:24pt;\">      brand , together</span></p></body></html>", None))
        self.checkBox_web.setText(QCoreApplication.translate("App_connenction", u"website design", None))
        self.checkBox_2_user_rechear.setText(QCoreApplication.translate("App_connenction", u"user reseach", None))
        self.checkBox_other.setText(QCoreApplication.translate("App_connenction", u"other", None))
        self.checkBox_strategie_consulting.setText(QCoreApplication.translate("App_connenction", u"Strategie & consulting", None))
        self.checkBox_Uxdesign.setText(QCoreApplication.translate("App_connenction", u"UX design", None))
        self.checkBox_content_creat.setText(QCoreApplication.translate("App_connenction", u"Content creation", None))
        self.buttonvalid.setText(QCoreApplication.translate("App_connenction", u"Get started", None))
        self.label_2.setText(QCoreApplication.translate("App_connenction", u"Services", None))
        self.label_name.setText(QCoreApplication.translate("App_connenction", u"name", None))
        self.label_email.setText(QCoreApplication.translate("App_connenction", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("App_connenction", u"Phone number", None))
        self.label_text_plain.setText(QCoreApplication.translate("App_connenction", u"how can he help?", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("App_connenction", u"Us", None))
        self.photo.setText("")
    # retranslateUi

