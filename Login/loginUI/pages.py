# IMPORT QT CORE
from qt_core import *

# IMPORT STYLESHEETS
from stylesheets.stylesheets import *

# CLASSE DA PÁGINA DE LOGIN
class PaginaLogin(object):
    def setupUi(self, StackedWidget) -> None:
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        
        
        # LOGIN - PÁGINA 1
        self.login = QWidget()
        self.login.setObjectName(u"login")
        StackedWidget.addWidget(self.login)
        
        # LOGIN WINDOW
        self.login_window = QFrame(self.login)
        self.login_window.setObjectName('login_window')
        self.login_window.setStyleSheet("""#login_window {
                                            background-color: #183e89;
                                            }""")
        self.login_window.setMinimumSize(QSize(341, 310))
        self.login_window.setMaximumSize(QSize(341, 310))
        
        # LOGIN MENU LAYOUT
        self.login_menu = QGridLayout(self.login_window)
        self.login_menu.setContentsMargins(30, 20, 30, 20)
        self.login_menu.setSpacing(20)
        
        # Error Label
        self.error_label = QLabel(self.login_window)
        self.error_label.hide()

        # Label Login
        self.login_label = QLabel(self.login_window)
        self.login_label.setText('Login')
        self.login_label.setStyleSheet(label_style)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)
  
        # Line Username
        self.line_user = QLineEdit(self.login_window, placeholderText='Username')
        self.line_user.setMinimumSize(269, 44)
        self.line_user.setStyleSheet(line_style)
        self.line_user.setPalette(self.text_color)
        self.line_user.addAction(icon_user, QLineEdit.LeadingPosition)
        self.line_user.setFocus()
        
        # Line Password
        self.line_password = QLineEdit(self.login_window, placeholderText='Password')
        self.line_password.setMinimumSize(269, 44)
        self.line_password.setStyleSheet(line_style)
        self.line_password.setPalette(self.text_color)
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_password.addAction(icon_password, QLineEdit.LeadingPosition)
        
        # Login Button
        self.login_btn = QPushButton(self.login_window, text='Entrar')
        self.login_btn.setMinimumSize(269, 44)
        self.login_btn.setStyleSheet(main_button)
        
        # Spacer Inter-Lines
        self.spacer = QSpacerItem(268, 85)
        
        # Bottom Layout
        self.bottom_layout = QHBoxLayout()
        
        # Registro Button
        self.sign_btn = QPushButton(self.login_window, text='Registrar')
        self.sign_btn.setStyleSheet(alter_button)
        
        # Bottom Spacer
        self.bottom_spacer = QSpacerItem(80, 15)
        
        # Forgot Password Button
        self.forgot_btn = QPushButton(self.login_window)
        self.forgot_btn.setText('Esqueci minha senha')
        self.forgot_btn.setStyleSheet(alter_button)
        
        # Add to Bottom Layout 
        self.bottom_layout.addWidget(self.sign_btn)
        self.bottom_layout.addItem(self.bottom_spacer)
        self.bottom_layout.addWidget(self.forgot_btn)
        
        # ADD TO LOGIN LAYOUT
        self.login_menu.addWidget(self.error_label,0,0, Qt.AlignHCenter)
        self.login_menu.addWidget(self.login_label,1,0, Qt.AlignHCenter)
        self.login_menu.addWidget(self.line_user,2,0,Qt.AlignHCenter)
        self.login_menu.addWidget(self.line_password,3,0,Qt.AlignHCenter)
        self.login_menu.addItem(self.spacer,4,0,Qt.AlignHCenter)
        self.login_menu.addWidget(self.login_btn,5,0,Qt.AlignHCenter)
        self.login_menu.addLayout(self.bottom_layout, 6, 0, Qt.AlignHCenter)
