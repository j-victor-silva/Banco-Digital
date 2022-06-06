# IMPORT MODULES
import os
import sys

# IMPORT QT_CORE
from qt_core import *

# IMPORT LOGIN WINDOW
from Login.loginUI.login_window import Ui_MainWindow

# IMPORT CONNECTION
from conexaoDB.conexao import ConexaoDB

# MAIN WINDOW
class MainWindow(QMainWindow): 
    def __init__(self) -> None:
        super().__init__()
        
        # CHAMA A CLASSE DE LOGIN
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
           
        # CHAMA A CLASSE DE CONEXAO
        self.conexao = ConexaoDB()
        
        # EXIBE A APLICAÇÃO
        self.show()
        
        # BOTÃO DE LOGIN
        self.ui.pagina_inicial.login_btn.clicked.connect(self.autenticar)
        
        # EXIBE A TELA DE REGISTRO
        self.ui.pagina_inicial.sign_btn.clicked.connect(self.show_registro)
        
        # VOLTA PARA A TELA DE LOGIN A PARTIR DA TELA DE REGISTRO
        self.ui.registro.voltar.clicked.connect(self.show_login)
        
        # EXIBE A TELA DE RECUPERAR SENHA
        self.ui.pagina_inicial.forgot_btn.clicked.connect(self.show_forgot)
        
        # VOLTA PARA A TELA DE LOGIN A PARTIR DA TELA DE RECUPERAÇÃO
        self.ui.forgot_pass.back.clicked.connect(self.show_login)
        
        # VAI PARA A TELA DE CÓDIGO DE RECUPERAÇÃO
        self.ui.forgot_pass.recuperar_btn.clicked.connect(self.show_code)
        
        # VOLTA PARA A TELA DE EMAIL A PARTIR DA TELA DE CÓDIGO
        self.ui.code.back.clicked.connect(self.show_forgot)
        
        # VAI PARA A TELA DE CRIAÇÃO DE NOVA SENHA
        self.ui.code.recuperar_btn.clicked.connect(self.show_new_pass)
        
    def show_registro(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.registro.registro)
        
    def show_login(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.pagina_inicial.login)
        
    def show_forgot(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.forgot_pass.recuperar_conta)
    
    def show_code(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.code.code_page)
        
    def show_new_pass(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.pass_page.pass_page)
        
    def autenticar(self):
        # Irá autenticar o usuário caso ele exista no banco de dados
        index = 0
        while True:
            self.conexao.data('cadastro')
            user = self.ui.pagina_inicial.line_user.text()
            password = self.ui.pagina_inicial.line_password.text()

            try:
                if not user == self.conexao.listar[index]['user'] or not password == self.conexao.listar[index]['password']:
                    index += 1

                if user == self.conexao.listar[index]['user'] and password == self.conexao.listar[index]['password']:
                    valido = True
                    print('Deu certo')
                    return

            except IndexError as e:
                valido = False
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
