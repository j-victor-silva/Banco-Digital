# IMPORT QT_CORE
from qt_core import *
from login.pages import PaginaLogin
from login.pages_.registro import Registro
from login.pages_.recuperar_conta_1 import RecuperarConta
from login.pages_.recuperar_conta_2 import CodigoPage
from login.pages_.recuperar_conta_3 import PasswordPage


# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')
        parent.setWindowTitle('Login')      
        
        self.font = 'JetBrains Mono'  
            
        # SET INITIAL PARAMETERS
        parent.resize(960, 600)
        
        self.size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.size_policy.setHorizontalStretch(0)
        self.size_policy.setVerticalStretch(0)
        self.size_policy.setHeightForWidth(parent.sizePolicy().hasHeightForWidth())
        
        parent.setSizePolicy(self.size_policy)
        parent.setMinimumSize(960, 600)
        
        # SET CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("""background-color: #00153f""")
        
        # CREATE MAIN LAYOUT
        self.main_layout = QGridLayout(self.central_frame)
                
        # CREATE PAGES
        self.pages = QStackedWidget(self.central_frame)
        self.pages.setMinimumSize(QSize(341, 385))
        self.pages.setMaximumSize(QSize(341, 385))
        
        # Login Page
        self.pagina_inicial = PaginaLogin()
        self.pagina_inicial.setupUi(self.pages)
        
        # Sign Up Page
        self.registro = Registro()
        self.registro.setupUi(self.pages)
        
        # Forgot Password Page
        self.forgot_pass = RecuperarConta()
        self.forgot_pass.setupUi(self.pages)
        
        # Code Page
        self.code = CodigoPage()
        self.code.setupUi(self.pages)
        
        # Password Page
        self.pass_page = PasswordPage()
        self.pass_page.setupUi(self.pages)
        
        # Main Page
        self.pages.setCurrentWidget(self.pagina_inicial.login)
        
        # ADD TO MAIN LAYOUT
        self.main_layout.addWidget(self.pages)
                
        # SET TO CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
