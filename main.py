# IMPORT MODULES
import sys
import random
from email.message import EmailMessage
from conexaoAPI.google_authenticate import service, our_email
from base64 import urlsafe_b64encode

# IMPORT QT_CORE
from qt_core import *

# IMPORT LOGIN WINDOW
from Login.loginUI.login_window import Ui_MainWindow

# IMPORT CONNECTION
from conexaoDB.conexao import ConexaoDB

# IMPORT STYLESHEETS
from stylesheets.stylesheets import *

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
        
        # BOTÕES DA TELA DE RECUPERAR SENHA - EMAIL
        self.ui.pagina_inicial.forgot_btn.clicked.connect(self.show_forgot)
        self.ui.forgot_pass.back.clicked.connect(self.show_login)
        self.ui.forgot_pass.recuperar_btn.clicked.connect(self.send_email)
        
        # BOTÕES DA TELA DE RECUPERAR SENHA - CÓDIGO
        self.ui.code.back.clicked.connect(self.show_forgot)
        self.ui.code.recuperar_btn.clicked.connect(self.authenticate_code)
        self.ui.code.resend_code.clicked.connect(self.send_email)
        
        # BOTÃO DA TELA DE RECUPERAR SENHA - NOVA SENHA
        self.ui.pass_page.alter_pass.clicked.connect(self.change_pass)
                
    def show_registro(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.registro.registro)
        self.ui.registro.label_registro.setText('Registro')
        self.ui.registro.label_registro.setStyleSheet(label_style)
        self.ui.registro.line_user_regi.setText('')
        self.ui.registro.line_pass_regi.setText('')
        self.ui.registro.line_pass_conf.setText('')
        self.ui.registro.line_email_regi.setText('')
        
    def show_login(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.pagina_inicial.login)
        self.ui.pagina_inicial.line_user.setText('')
        self.ui.pagina_inicial.line_password.setText('')
        
    def show_forgot(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.forgot_pass.recuperar_conta)
        self.ui.forgot_pass.line_email.setText('')
    
    def show_code(self) -> None:
        self.ui.pages.setCurrentWidget(self.ui.code.code_page)
        self.ui.code.line_code.setText('')
              
    def label_error_transition(self) -> None:
        self.timer.start(5000, self)
        self.ui.pagina_inicial.error_label.setText('Usuário ou senha inválidos!')
        self.ui.pagina_inicial.error_label.setStyleSheet(label_error)
        self.ui.pagina_inicial.error_label.show()
        
    def autenticar(self) -> None:
        user = self.ui.pagina_inicial.line_user.text()
        password = self.ui.pagina_inicial.line_password.text()
        
        self.conexao.data('cadastro')
        
        for i in range(len(self.conexao.listar)):     
            if not user == self.conexao.listar[i]['user'] or not password == self.conexao.listar[i]['password']:
                self.label_error_transition()
                continue
            else:
                if self.timer.isActive():
                    self.timer.stop()
                    self.timer.start(5000, self)
                    self.ui.pagina_inicial.error_label.setText('Logado!')
                    self.ui.pagina_inicial.error_label.setStyleSheet(label_sucess)
                    self.ui.pagina_inicial.error_label.show()
                return
        
    def registrar(self) -> None:
        email = self.ui.registro.line_email_regi.text()
        user = self.ui.registro.line_user_regi.text()
        password = self.ui.registro.line_pass_regi.text()
        password_conf = self.ui.registro.line_pass_conf.text()
        label_error_ = self.ui.registro.label_registro
        
        if user == '' or password == '' or password_conf == '' or email == '':
            label_error_.setText('Preencha todos os campos')
            label_error_.setStyleSheet(label_error)
            return
                        
        if not password == password_conf:
            label_error_.setText('As senhas não conferem')
            label_error_.setStyleSheet(label_error)
            return
    
        valido = True
        self.conexao.data('cadastro')
        for i in range(len(self.conexao.listar)):
            if user == self.conexao.listar[i]['user'] or email == self.conexao.listar[i]['email']:
                label_error_.setText('Usuário ou Email já existentes')
                label_error_.setStyleSheet(label_error)
                valido = False
                return
        
        if valido:
            self.conexao.cursor.execute(f'INSERT INTO `cadastro` VALUES (DEFAULT, "{user}", "{password}", "{email}")')
            self.conexao.conexao.commit()
            self.show_login()
            self.ui.pagina_inicial.error_label.setText('Conta criada!')
            self.ui.pagina_inicial.error_label.setStyleSheet(label_sucess)
            self.ui.pagina_inicial.error_label.show()
            
    # Método para construção do email a ser enviado
    def build_message(self) -> None:
        self.code = random.randint(00000, 99999)
        self.reciever = self.ui.forgot_pass.line_email.text()
        
        msg = EmailMessage()
        msg['subject'] = 'Código de Verificação'      
        msg['from'] = our_email
        msg['to'] = self.reciever
        msg.set_content(str(self.code))

        return {'raw': urlsafe_b64encode(msg.as_bytes()).decode()}

    # Método para enviar o email
    def send_email(self) -> None:
        try:
            service.users().messages().send(
                userId='me',
                body=self.build_message()
            ).execute()
            self.show_code()
        except:
            self.ui.forgot_pass.label.setText('Digite um email válido!')
            self.ui.forgot_pass.label.setStyleSheet(label_error)
    
    def authenticate_code(self) -> None:
        if self.ui.code.line_code.text() == str(self.code):
            self.ui.pages.setCurrentWidget(self.ui.pass_page.pass_page)         
        else:
            self.ui.code.label.setText('O código digitado está incorreto')
            self.ui.code.label.setStyleSheet(label_error)
            
    def change_pass(self) -> None:
        password = self.ui.pass_page.first_pass.text()
        pass_conf = self.ui.pass_page.conf_pass.text()

        if password == pass_conf:
            self.conexao.cursor.execute(f'UPDATE `cadastro` SET `password` = "{password}" WHERE `email` = "{self.reciever}"')
            self.conexao.conexao.commit()
            self.show_login()
            self.ui.pagina_inicial.error_label.setText('Senha alterada com sucesso!')
            self.ui.pagina_inicial.error_label.setStyleSheet(label_sucess)
            self.ui.pagina_inicial.error_label.show()
        else:
            self.ui.pass_page.top_label.setText('As senhas não conferem')
            self.ui.pass_page.top_label.setStyleSheet(label_error)
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
