import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication,QWidget
# from importlib.machinery import SourceFileLoader
# MODULE_PATH = "C:\Users\ykoua\Desktop\app_complet\Widgets\interface\interface_connexion\interface_conn.py"
# MODULE_NAME = "interface_conn"
# modulevar = SourceFileLoader(MODULE_NAME, MODULE_PATH).load_module()
# modulevar.printingstatement()
# from interface_connexion import  Ui_App_connenction

from Widgets.interface.interface_main.interface_menu import Ui_Form 
from Widgets.interface import img_rc
class MainWindow2(QWidget, Ui_Form):
    def __init__(self) :
        super(MainWindow2,self).__init__()
        self.setupUi(self)
        
      
if __name__=="__main__":
    app3 = QApplication(sys.argv) 
    window2 = MainWindow2()
    window2.show()
    sys.exit(app3.exec())

    