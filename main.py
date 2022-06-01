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
        
        # EXIBE A TELA DE REGISTRO
        self.ui.pagina_inicial.sign_btn.clicked.connect(self.show_registro)
        
        # VOLTA PARA A TELA DE LOGIN
        self.ui.registro.voltar.clicked.connect(self.show_login)
        
        # EXIBE A TELA DE RECUPERAR SENHA
        self.ui.pagina_inicial.forgot_btn.clicked.connect(self.show_forgot)
        
        # Teste
        self.ui.forgot_pass.back.clicked.connect(self.show_login)
    def show_registro(self):
        # self.ui.pages.setMaximumSize(QSize(341, 465))
        self.ui.pages.setCurrentWidget(self.ui.registro.registro)
        
    def show_login(self):
        # self.ui.pages.setMaximumSize(QSize(341, 385))
        self.ui.pages.setCurrentWidget(self.ui.pagina_inicial.login)
        
    def show_forgot(self):
        self.ui.pages.setCurrentWidget(self.ui.forgot_pass.recuperar_conta)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
