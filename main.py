# IMPORT MODULES
from cProfile import label
import os
import sys
import time

# IMPORT QT_CORE
from qt_core import *

# IMPORT LOGIN WINDOW
from Login.loginUI.login_window import Ui_MainWindow

# IMPORT CONNECTION
from conexaoDB.conexao import ConexaoDB

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

# MAIN WINDOW
class MainWindow(QMainWindow): 
    def __init__(self) -> None:
        super().__init__()
        
        self.timer = QBasicTimer()
        
        # CHAMA A CLASSE DE LOGIN
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
           
        self.conexao = ConexaoDB()
        
        self.show()
        
        # BOTÕES DA TELA DE LOGIN
        self.ui.pagina_inicial.login_btn.clicked.connect(self.autenticar)
        self.ui.pagina_inicial.sign_btn.clicked.connect(self.show_registro)
        
        # BOTÕES DA TELA DE REGISTRO        
        self.ui.registro.sign_up_btn.clicked.connect(self.registrar)
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
        
    def registrar(self) -> None:
        user = self.ui.registro.line_user_regi.text()
        password = self.ui.registro.line_pass_regi.text()
        password_conf = self.ui.registro.line_pass_conf.text()
        email = self.ui.registro.line_email_regi.text()
        label_error = self.ui.registro.error_registro
        
        if user == '' or password == '' or password_conf == '' or email == '':
            label_error.setText('Preencha todos os campos')
            label_error.show()
            return
                        
        if not password == password_conf:
            label_error.setText('As senhas não conferem')
            label_error.show()
            return
        
        index = 0
        while True:
            self.conexao.data('cadastro')  
            try:
                if user == self.conexao.listar[index]['user'] or email == self.conexao.listar[index]['email']:
                    label_error.setText('Usuário ou Email já existentes')
                    label_error.show()
                    return
                else:
                    index += 1
                    
                # if user == self.conexao.listar[index]['user'] and password == self.conexao.listar[index]['password']:
                #     return

            except IndexError as e:
                return
        
        
            
                
    def label_error_transition(self):
        self.timer.start(5000, self)
        self.ui.pagina_inicial.error_label.setText('Usuário ou senha inválidos!')
        self.ui.pagina_inicial.error_label.setStyleSheet(self.ui.pagina_inicial.error_label_style_default)
        self.ui.pagina_inicial.error_label.show()
        
    def autenticar(self):
        index = 0
        while True:
            self.conexao.data('cadastro')
            user = self.ui.pagina_inicial.line_user.text()
            password = self.ui.pagina_inicial.line_password.text()
            
            try:
                if user == '' or password == '':
                    self.label_error_transition()
                    return
              
                if not user == self.conexao.listar[index]['user'] or not password == self.conexao.listar[index]['password']:
                    index += 1

                if user == self.conexao.listar[index]['user'] and password == self.conexao.listar[index]['password']:
                    if self.timer.isActive():
                        self.timer.stop()
                        self.timer.start(5000, self)
                        self.ui.pagina_inicial.error_label.setText('Logado!')
                        self.ui.pagina_inicial.error_label.setStyleSheet(self.ui.pagina_inicial.error_label_style_logged)
                        self.ui.pagina_inicial.error_label.show()
                    return

            except IndexError as e:
                self.label_error_transition()
                return
                
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
