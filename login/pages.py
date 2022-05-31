from qt_core import *


class PaginaLogin(object):
    # FONT
    font = 'JetBrains Mono'
    # STYLE LABEL
    label_style = f"""font: 10pt {font}; 
                        color: white;
                        background-color: #183e89;"""
    # STYLE LINE EDIT
    line_style = f"""font: 8pt {font};
                        background-color: white;
                        border-radius: 10px""" 
                        
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        
        
        # LOGIN - PÁGINA 1
        self.login = QWidget()
        self.login.setObjectName(u"login")
        StackedWidget.addWidget(self.login)
        
        # ////////////////////////////////////////////////////////////////////
        # LOGIN WINDOW
        self.login_window = QFrame(self.login)
        self.login_window.setObjectName('login_window')
        self.login_window.setStyleSheet("""#login_window {
                                            background-color: #183e89;
                                            }""")
        # ////////////////////////////////////////////////////////////////////
        
        # ////////////////////////////////////////////////////////////////////
        # LOGIN MENU LAYOUT
        self.login_menu = QGridLayout(self.login_window)
        self.login_menu.setContentsMargins(30, 20, 30, 20)
        self.login_menu.setSpacing(20)
        
        # Spacer Top
        self.spacer_top = QSpacerItem(0, 20)
        
        # Label Login
        self.login_label = QLabel(self.login_window)
        self.login_label.setText('Login')
        self.login_label.setStyleSheet(self.label_style)
        self.login_label.setAlignment(Qt.AlignHCenter)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)
  
        # Line Username
        self.line_user = QLineEdit(placeholderText='Username')
        self.line_user.setMinimumSize(269, 44)
        self.line_user.setStyleSheet(self.line_style)
        self.line_user.setPalette(self.text_color)
        
        # Line Password
        self.line_password = QLineEdit(placeholderText='Password')
        self.line_password.setMinimumSize(269, 44)
        self.line_password.setStyleSheet(self.line_style)
        self.line_password.setPalette(self.text_color)
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Login Button
        self.login_btn = QPushButton(text='Entrar')
        self.login_btn.setMinimumSize(269, 44)
        self.login_btn.setStyleSheet(f"""background-color: #0d81a5;
                                        border-radius: 10px;
                                        border: none;
                                        font: 10pt {self.font}""")
        
        # Spacer Inter-Lines
        self.spacer = QSpacerItem(268, 85)
        
        # Bottom Layout
        self.bottom_layout = QHBoxLayout()
        
        # Registro Button
        self.sign_btn = QPushButton(text='Registrar')
        self.sign_btn.setStyleSheet(f"""font: 7.5pt {self.font};
                                        background-color: #183e89;
                                        color: white;
                                        border-radius: 10px;
                                        border: none""")
        
        # Bottom Spacer
        self.bottom_spacer = QSpacerItem(80, 15)
        
        # Forgot Password Button
        self.forgot_btn = QPushButton()
        self.forgot_btn.setText('Esqueci minha senha')
        self.forgot_btn.setStyleSheet(f"""font: 7.5pt {self.font};
                                          background-color: #183e89;
                                          color: white;
                                          border: none""")
        
        # Add to Bottom Layout 
        self.bottom_layout.addWidget(self.sign_btn)
        self.bottom_layout.addItem(self.bottom_spacer)
        self.bottom_layout.addWidget(self.forgot_btn)
        # ////////////////////////////////////////////////////////////////////
        
        # ////////////////////////////////////////////////////////////////////
        # ADD TO LOGIN LAYOUT
        self.login_menu.addItem(self.spacer_top)
        self.login_menu.addWidget(self.login_label)
        self.login_menu.addWidget(self.line_user)
        self.login_menu.addWidget(self.line_password)
        self.login_menu.addItem(self.spacer)
        self.login_menu.addWidget(self.login_btn)
        self.login_menu.addLayout(self.bottom_layout, 8, 0)
        # ////////////////////////////////////////////////////////////////////

        self.recuperar_conta = QWidget()
        self.recuperar_conta.setObjectName(u"recuperar_conta")
        StackedWidget.addWidget(self.recuperar_conta)
