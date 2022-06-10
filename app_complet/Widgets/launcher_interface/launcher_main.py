import sys
from turtle import color
from PySide6.QtWidgets import QApplication,QWidget,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
sys.path.append('/Users/imac_02/Desktop/app_complet/Widgets/interface/interface_main')
from interface_main import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self) :
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.photo.setPixmap(QPixmap(u"/Users/imac_02/Desktop/app_complet/Static/mdl_connexion/tete-de-lit-en-bois-et-tissu.jpeg"))
      
if __name__=="__main__":
    app = QApplication(sys.argv)        

    window = MainWindow()
    window.show()

    sys.exit(app.exec())