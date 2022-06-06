# IMPORT MODULES
import pymysql

# IMPORT CONNECTION
from conexaoDB.conexao import ConexaoDB

# IMPORT LOGIN WINDOW
from Login.loginUI.login_window import Ui_MainWindow


# Chamando a classe de conexão
conexao = ConexaoDB()
# Chamando a classe da tela principal
login_window = Ui_MainWindow()
    
def autenticar(self):
    # Irá autenticar o usuário caso ele exista no banco de dados
    index = 0
    while True:
        conexao.data('cadastro')
        user = login_window.pagina_inicial.line_user.text()
        password = login_window.pagina_inicial.line_password.text()

        try:
            if not user == conexao.listagem[index]['user'] or not password == conexao.listagem[index]['password']:
                index += 1

            if user == conexao.listagem[index]['user'] and password == conexao.listagem[index]['password']:
                valido = True
                print('Deu certo')
                return

        except IndexError as e:
            valido = False
                