# IMPORT QT CORE
from qt_core import *

# IMPORT STYLESHEETS
from stylesheets.stylesheets import *


# CLASSE DA TELA DE REGISTRO
class Registro(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")

        # REGISTRO - PÁGINA 2
        self.registro = QWidget()
        self.registro.setObjectName(u"registro")
        StackedWidget.addWidget(self.registro)
        
        # SIZE POLICY
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy_label = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy_label.setHorizontalStretch(0)
        sizePolicy_label.setVerticalStretch(0)
        
        
        # REGISTRO WINDOW
        self.registro_frame = QFrame(self.registro)
        self.registro_frame.setObjectName('registro_frame')
        self.registro_frame.setStyleSheet("""#registro_frame {
                                            background-color: #183e89; 
                                            }""")
        self.registro_frame.setMinimumSize(QSize(341, 465))
        self.registro_frame.setMaximumSize(QSize(341, 465))
        
        # CREATE REGISTRO LAYOUT
        self.registro_layout = QGridLayout(self.registro_frame)        
        self.registro_layout.setContentsMargins(30,20,30,20)
        self.registro_layout.setSpacing(22)
        
        # Spacer Top
        self.spacer_top = QSpacerItem(0,20)
        
        # Label Registro
        self.label_registro = QLabel(self.registro_frame)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)

        # Layout Labels and Lines
        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignLeft|Qt.AlignBottom)
        
        # Line Username
        self.label_username = QLabel(self.registro_frame,text='Usuário:')
        self.label_username.setStyleSheet(label_style)
        self.label_username.setSizePolicy(sizePolicy_label)
        
        sizePolicy_label.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setAlignment(Qt.AlignBottom)
        
        self.line_user_regi = QLineEdit(self.registro_frame,placeholderText='Username')
        self.line_user_regi.setMinimumSize(QSize(197, 35))
        self.line_user_regi.setMaximumSize(QSize(197, 35))
        self.line_user_regi.setStyleSheet(line_style)
        self.line_user_regi.setPalette(self.text_color)
        self.line_user_regi.addAction(icon_user, QLineEdit.LeadingPosition)
        
        sizePolicy.setHeightForWidth(self.line_user_regi.sizePolicy().hasHeightForWidth())
        self.line_user_regi.setSizePolicy(sizePolicy)
        
        # Line Password INIT
        self.label_password = QLabel(self.registro_frame,text='Senha:')
        self.label_password.setStyleSheet(label_style)
        self.label_password.setSizePolicy(sizePolicy_label)
        self.label_password.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        
        self.line_pass_regi = QLineEdit(self.registro_frame,placeholderText='Password')
        self.line_pass_regi.setMinimumSize(QSize(197,35))
        self.line_pass_regi.setMaximumSize(QSize(197,35))
        self.line_pass_regi.setStyleSheet(line_style)
        self.line_pass_regi.setPalette(self.text_color)
        self.line_pass_regi.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_pass_regi.addAction(icon_password, QLineEdit.LeadingPosition)
        
        # Line Password CONFIRM
        self.label_password_conf = QLabel(self.registro_frame,text='C. Senha:')
        self.label_password_conf.setStyleSheet(label_style)
        self.label_password_conf.setSizePolicy(sizePolicy_label)
        self.label_password_conf.setAlignment(Qt.AlignBottom)
        
        self.line_pass_conf = QLineEdit(self.registro_frame,placeholderText='Password')
        self.line_pass_conf.setMinimumSize(QSize(197,35))
        self.line_pass_conf.setMaximumSize(QSize(197,35))
        self.line_pass_conf.setStyleSheet(line_style)
        self.line_pass_conf.setPalette(self.text_color)
        self.line_pass_conf.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_pass_conf.addAction(icon_password, QLineEdit.LeadingPosition)
        
        # Line Email
        self.label_email = QLabel(self.registro_frame,text='Email:')
        self.label_email.setStyleSheet(label_style)
        self.label_email.setSizePolicy(sizePolicy_label)
        self.label_email.setAlignment(Qt.AlignBottom)
        
        self.line_email_regi = QLineEdit(self.registro_frame,placeholderText='Email')
        self.line_email_regi.setMinimumSize(QSize(197, 35))
        self.line_email_regi.setMaximumSize(QSize(197, 35))
        self.line_email_regi.setStyleSheet(line_style)
        self.line_email_regi.setPalette(self.text_color)
        self.line_email_regi.addAction(icon_email, QLineEdit.LeadingPosition)
        
        # Sign Up Button
        self.sign_up_btn = QPushButton(self.registro_frame,text='Registrar')
        self.sign_up_btn.setMinimumHeight(44)
        self.sign_up_btn.setMaximumWidth(283)
        self.sign_up_btn.setStyleSheet(main_button)
        
        # Back Button
        self.voltar = QPushButton(self.registro_frame,text='Voltar')
        self.voltar.setStyleSheet(alter_button)
        
        # Spacer Inter-Lines
        self.spacer = QSpacerItem(0,20)      
        
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
        self.registro_layout.addWidget(self.label_registro,0,0, Qt.AlignHCenter)
        self.registro_layout.addLayout(self.form_layout, 1, 0)
        self.registro_layout.addWidget(self.sign_up_btn, 2, 0, Qt.AlignTop)
        self.registro_layout.addWidget(self.voltar, 3, 0, Qt.AlignTop | Qt.AlignHCenter)
        self.registro_layout.addItem(self.spacer, 4, 0, Qt.AlignTop)
