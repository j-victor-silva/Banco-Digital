# IMPORT MODULES
import os
import sys

# IMPORT QT_CORE
from qt_core import *

# IMPORT LOGIN WINDOW
from login.login_window import Ui_MainWindow
from login.pages import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # CHAMA A CLASSE DE LOGIN
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        
        # EXIBE A APLICAÇÃO
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
