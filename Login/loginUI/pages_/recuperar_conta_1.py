# IMPORT QT CORE
from qt_core import *

# IMPORT STYLESHEETS
from stylesheets.stylesheets import *


# CLASSE DA PÁGINA DE RECUPERAR CONTA
class RecuperarConta(object):
    def setupUi(self, StackedWidget) -> None:
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u'StackedWidget')
            
        # RECUPERAR SENHA - PÁGINA 3
        self.recuperar_conta = QWidget()
        self.recuperar_conta.setObjectName(u'recuperar_conta')
        StackedWidget.addWidget(self.recuperar_conta)
        
        # SIZE POLICY
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy_label = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy_label.setHorizontalStretch(0)
        sizePolicy_label.setVerticalStretch(0)

        # FORGOT PASS WINDOW
        self.forgot_pass_frame = QFrame(self.recuperar_conta)
        self.forgot_pass_frame.setObjectName(u'forgot_pass_frame')
        self.forgot_pass_frame.setStyleSheet("""#forgot_pass_frame {
                                                background-color: #183e89;
                                                }""")
        self.forgot_pass_frame.setMinimumSize(QSize(341,199))
        self.forgot_pass_frame.setMaximumSize(QSize(341,199))
        
        # CREATE LAYOUT
        self.layout = QVBoxLayout(self.forgot_pass_frame)
        self.layout.setContentsMargins(30,20,30,20)
        self.layout.setSpacing(20)
        
        # Label Top
        self.label = QLabel(self.forgot_pass_frame)
        self.label.setText('Recuperar Conta')
        self.label.setStyleSheet(label_style)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)
        
        # Line Email
        self.line_email = QLineEdit(self.forgot_pass_frame, placeholderText='Email')
        self.line_email.setStyleSheet(line_style)
        self.line_email.setMinimumSize(QSize(269,44))
        self.line_email.setMaximumSize(QSize(269,44))
        self.line_email.setPalette(self.text_color)
        self.line_email.addAction(icon_email, QLineEdit.LeadingPosition)
        
        # Recuperar Button
        self.recuperar_btn = QPushButton(self.forgot_pass_frame, text='Recuperar')
        self.recuperar_btn.setStyleSheet(main_button)
        self.recuperar_btn.setMinimumSize(QSize(269,44))
        self.recuperar_btn.setMaximumSize(QSize(269,44))
        
        # Voltar Button
        self.back = QPushButton(self.forgot_pass_frame, text='Voltar')
        self.back.setStyleSheet(alter_button)
        
        # ADD TO MAIN LAYOUT
        self.layout.addWidget(self.label,0, Qt.AlignHCenter)
        self.layout.addWidget(self.line_email,1, Qt.AlignHCenter)
        self.layout.addWidget(self.recuperar_btn,2, Qt.AlignHCenter)
        self.layout.addWidget(self.back,3, Qt.AlignHCenter)
        