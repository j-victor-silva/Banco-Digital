from qt_core import *


class Registro(object):
    # FONT
    font = 'JetBrains Mono'
    # STYLE LABEL
    label_style = f"""font: 9pt {font}; 
                        color: white;
                        background-color: #183e89;"""
    # STYLE LINE EDIT
    line_style = f"""font: 8pt {font};
                        background-color: white;
                        border-radius: 10px"""
              
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")

        # ////////////////////////////////////////////////////////////////////
        # REGISTRO - PÁGINA 2
        self.registro = QWidget()
        self.registro.setObjectName(u"registro")
        StackedWidget.addWidget(self.registro)
        # ////////////////////////////////////////////////////////////////////
        
        # SIZE POLICY
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy_label = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy_label.setHorizontalStretch(0)
        sizePolicy_label.setVerticalStretch(0)
        
        
        # ////////////////////////////////////////////////////////////////////
        # REGISTRO WINDOW
        self.registro_frame = QFrame(self.registro)
        self.registro_frame.setObjectName('registro_frame')
        self.registro_frame.setStyleSheet("""#registro_frame {
                                            background-color: #183e89; }""")
        # ////////////////////////////////////////////////////////////////////
        
        # ////////////////////////////////////////////////////////////////////
        # CREATE REGISTRO LAYOUT
        self.registro_layout = QGridLayout(self.registro_frame)        
        self.registro_layout.setContentsMargins(30,20,30,20)
        self.registro_layout.setSpacing(20)
        
        # Spacer Top
        self.spacer_top = QSpacerItem(0,20)
        
        # Label Registro
        self.label_registro = QLabel(self.registro_frame)
        self.label_registro.setText('Registro')
        self.label_registro.setStyleSheet(self.label_style)
        self.label_registro.setMaximumWidth(341)
        self.label_registro.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)

        # Layout Labels and Lines
        self.form_layout = QFormLayout()
        
        # Line Username
        self.label_username = QLabel('Usuário:')
        self.label_username.setStyleSheet(self.label_style)
        self.label_username.setSizePolicy(sizePolicy_label)
        
        sizePolicy_label.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setAlignment(Qt.AlignBottom)
        
        self.line_user_regi = QLineEdit(placeholderText='Username')
        self.line_user_regi.setMinimumSize(150, 44)
        self.line_user_regi.setStyleSheet(self.line_style)
        self.line_user_regi.setPalette(self.text_color)
        
        sizePolicy.setHeightForWidth(self.line_user_regi.sizePolicy().hasHeightForWidth())
        self.line_user_regi.setSizePolicy(sizePolicy)
        
        # Line Password INIT
        self.label_password = QLabel('Senha:')
        self.label_password.setStyleSheet(self.label_style)
        self.label_password.setSizePolicy(sizePolicy_label)
        self.label_password.setAlignment(Qt.AlignBottom)
        
        self.line_pass_regi = QLineEdit(placeholderText='Password')
        self.line_pass_regi.setMinimumSize(150, 44)
        self.line_pass_regi.setStyleSheet(self.line_style)
        self.line_pass_regi.setPalette(self.text_color)
        self.line_pass_regi.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Line Password CONFIRM
        self.label_password_conf = QLabel('Confirmar senha:')
        self.label_password_conf.setStyleSheet(self.label_style)
        self.label_password_conf.setSizePolicy(sizePolicy_label)
        self.label_password_conf.setAlignment(Qt.AlignBottom)
        
        self.line_pass_conf = QLineEdit(placeholderText='Password')
        self.line_pass_conf.setMinimumSize(150, 44)
        self.line_pass_conf.setStyleSheet(self.line_style)
        self.line_pass_conf.setPalette(self.text_color)
        self.line_pass_conf.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Line Email
        self.label_email = QLabel('Email:')
        self.label_email.setStyleSheet(self.label_style)
        self.label_email.setSizePolicy(sizePolicy_label)
        self.label_email.setAlignment(Qt.AlignBottom)
        
        self.line_email_regi = QLineEdit(placeholderText='Email')
        self.line_email_regi.setMinimumSize(150, 44)
        self.line_email_regi.setStyleSheet(self.line_style)
        self.line_email_regi.setPalette(self.text_color)
        
        # Sign Up Button
        self.sign_up_btn = QPushButton(text='Registrar')
        self.sign_up_btn.setMinimumHeight(43)
        self.sign_up_btn.setMaximumWidth(282)
        self.sign_up_btn.setStyleSheet(f"""background-color: #0d81a5;
                                            border: none;
                                            border-radius: 10px;
                                            font: 7.5pt {self.font}""")
        
        # Back Button
        self.voltar = QPushButton(text='Voltar')
        self.voltar.setStyleSheet(f"""background-color: #183e89;
                                        border: none;
                                        color: white;
                                        font: 7.5pt {self.font}""")
        
        # Spacer Inter-Lines
        self.spacer = QSpacerItem(0, 20)      
        
        # ADD TO FORM LAYOUT
        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.label_username)  
        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.line_user_regi)  
        
        self.form_layout.setWidget(1, QFormLayout.LabelRole, self.label_password)  
        self.form_layout.setWidget(1, QFormLayout.FieldRole, self.line_pass_regi)  
        
        self.form_layout.setWidget(2, QFormLayout.LabelRole, self.label_password_conf)  
        self.form_layout.setWidget(2, QFormLayout.FieldRole, self.line_pass_conf)  
        
        self.form_layout.setWidget(3, QFormLayout.LabelRole, self.label_email)  
        self.form_layout.setWidget(3, QFormLayout.FieldRole, self.line_email_regi)  
        
        # ADD TO LAYOUT
        self.registro_layout.addItem(self.spacer_top)
        self.registro_layout.addWidget(self.label_registro)
        self.registro_layout.addItem(self.spacer)
        self.registro_layout.addLayout(self.form_layout, 3, 0)
        self.registro_layout.addWidget(self.sign_up_btn, 4, 0)
        self.registro_layout.addWidget(self.voltar, 5, 0)
