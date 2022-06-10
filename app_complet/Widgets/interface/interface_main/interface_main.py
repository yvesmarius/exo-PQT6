# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(862, 521)
        Form.setMinimumSize(QSize(771, 521))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 871, 521))
        self.frame.setStyleSheet(u"background-color:white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, 0, 251, 521))
        self.widget.setStyleSheet(u"QWidget{background-color:rgb(26, 10, 30);}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 111, 101))
        self.label.setPixmap(QPixmap(u"../Static/Appmdl3_3/diamond.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 150, 191, 20))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:white")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-30, 300, 281, 61))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Static/Appmdl3_3/orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 170, 81, 20))
        self.label_3.setStyleSheet(u"color:white")
        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(-20, 240, 271, 61))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Static/Appmdl3_3/worldwide.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setIconSize(QSize(30, 30))
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(-50, 360, 301, 61))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../Static/Appmdl3_3/diamond.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-30, 420, 281, 61))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color:white\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(245, 163, 97)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../Static/Appmdl3_3/[cloud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(30, 30))
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(240, 0, 601, 521))
        self.widget_2.setStyleSheet(u"color:white")
        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(70, 60, 131, 131))
        self.pushButton_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon4 = QIcon()
        icon4.addFile(u"../Static/Appmdl3_3/add (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(25, 25))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 250, 131, 131))
        self.pushButton_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon5 = QIcon()
        icon5.addFile(u"../Static/Appmdl3_3/layers.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(80, 80))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(230, 60, 131, 131))
        self.pushButton_7.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon6 = QIcon()
        icon6.addFile(u"../Static/Appmdl3_3/android-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(80, 80))
        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(230, 250, 131, 131))
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
        icon7.addFile(u"../Static/Appmdl3_3/graphic-design.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QSize(80, 80))
        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(380, 60, 131, 131))
        self.pushButton_9.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border:1px solid;\n"
"} ")
        icon8 = QIcon()
        icon8.addFile(u"../Static/Appmdl3_3/stock-exchange-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(80, 80))
        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(0, 10, 111, 31))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	color:black\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:grey\n"
"}")
        self.pushButton_8.setFlat(True)
        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(120, 10, 111, 31))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	color:black\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color:grey\n"
"}\n"
"")
        self.pushButton_11.setFlat(True)
        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(390, 470, 75, 24))
        self.pushButton_13.setStyleSheet(u"QPushButton:hover\n"
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
        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(480, 470, 75, 24))
        self.pushButton_14.setStyleSheet(u"QPushButton:hover\n"
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
        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(60, 470, 141, 24))
        self.pushButton_12.setStyleSheet(u"QPushButton:hover\n"
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
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 200, 91, 16))
        self.label_4.setStyleSheet(u"color:black")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 200, 121, 16))
        self.label_9.setStyleSheet(u"color:black")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 390, 111, 16))
        self.label_10.setStyleSheet(u"color:black")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 390, 91, 16))
        self.label_11.setStyleSheet(u"color:black")
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(380, 200, 91, 16))
        self.label_12.setStyleSheet(u"color:black")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Welcome to sketch", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Join our newsletter\n"
"News and tips in your inbox", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"version 48.2", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u" New to sketch ?\n"
" Get started with these tutorials", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u" Get sketch Mirror\n"
" view your design on ios", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Join Sketch Cloud\n"
"Upload and share your designs", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Recents", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Templates", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"cancel", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"choose", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"Open a existing file...", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"New documents", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Android Icon Design", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Materials Design", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Web Design", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Ios App Icon", None))
    # retranslateUi

