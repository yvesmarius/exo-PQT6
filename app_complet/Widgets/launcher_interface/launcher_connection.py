import sys
from turtle import color
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication,QWidget
sys.path.append('/Users/imac_02/Desktop/app_complet/Widgets/interface/interface_connexion/')
# from interface_connexion import  Ui_App_connenction
from interface_connexion import Ui_App_connenction  

class MainWindow(QWidget, Ui_App_connenction):
    def __init__(self) :
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.photo.setPixmap(QPixmap(u"/Users/imac_02/Desktop/app_complet/Static/mdl_connexion/tete-de-lit-en-bois-et-tissu.jpeg"))
      
if __name__=="__main__":
    app = QApplication(sys.argv)        

    window = MainWindow()
    window.show()

    sys.exit(app.exec())