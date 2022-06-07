# IMPORT MODULES
import pymysql

# CLASS CONNECTION
class ConexaoDB():
    '''Conexão com o banco de dados'''
    def __init__(self, conexao: str = '127.0.0.1') -> None:
        self.conexao = pymysql.connect(
            host=conexao,
            user='root',
            password='',
            db='contas_banco',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cursor = self.conexao.cursor()
        
    def data(self, table) -> dict:
        command = f'SELECT * FROM {table}'
        self.cursor.execute(command)
        self.listar = self.cursor.fetchall()
        
    def encerrar(self):
        self.cursor.close()
        self.conexao.close()
        