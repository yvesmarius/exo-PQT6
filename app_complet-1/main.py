import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from launcher.launcher_connection import *



if __name__=="__main__":
    app = QApplication(sys.argv)        
    window = MainWindow()
    window.show()        
    sys.exit(app.exec())

# sys.exit(app.exec())