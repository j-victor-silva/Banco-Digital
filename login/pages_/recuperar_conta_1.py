# IMPORT QT CORE
from logging import PlaceHolder
from qt_core import *


# CLASSE DA PÁGINA DE RECUPERAR CONTA
class RecuperarConta(object):
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
            StackedWidget.setObjectName(u'StackedWidget')
            
        # ////////////////////////////////////////////////////////////////////
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

        # ////////////////////////////////////////////////////////////////////
        # FORGOT PASS WINDOW
        self.forgot_pass_frame = QFrame(self.recuperar_conta)
        self.forgot_pass_frame.setObjectName(u'forgot_pass_frame')
        self.forgot_pass_frame.setStyleSheet("""#forgot_pass_frame {
                                                background-color: #183e89;
                                                }""")
        self.forgot_pass_frame.setMinimumSize(QSize(341,199))
        self.forgot_pass_frame.setMaximumSize(QSize(341,199))
        # ////////////////////////////////////////////////////////////////////
        
        # CREATE LAYOUT
        self.layout = QVBoxLayout(self.forgot_pass_frame)
        self.layout.setContentsMargins(30,20,30,20)
        self.layout.setSpacing(20)
        
        # Label Top
        self.label = QLabel(self.forgot_pass_frame)
        self.label.setText('Recuperar Conta')
        self.label.setStyleSheet(self.label_style)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)
        
        # Line Email
        self.line_email = QLineEdit(self.forgot_pass_frame, placeholderText='Email')
        self.line_email.setStyleSheet(self.line_style)
        self.line_email.setMinimumSize(QSize(269,44))
        self.line_email.setMaximumSize(QSize(269,44))
        self.line_email.setPalette(self.text_color)
        
        # Recuperar Button
        self.recuperar_btn = QPushButton(self.forgot_pass_frame, text='Recuperar')
        self.recuperar_btn.setStyleSheet(f"""background-color: #0d81a5;
                                            border: none;
                                            border-radius: 10px;
                                            font: 7.5pt {self.font};
                                            color: white
                                         """)
        self.recuperar_btn.setMinimumSize(QSize(269,44))
        self.recuperar_btn.setMaximumSize(QSize(269,44))
        
        # Voltar Button
        self.back = QPushButton(self.forgot_pass_frame, text='Voltar')
        self.back.setStyleSheet(f"""background-color: #183e89;
                                    color: white;
                                    border: none""")
        
        
        
        # ADD TO MAIN LAYOUT
        self.layout.addWidget(self.label,0, Qt.AlignHCenter)
        self.layout.addWidget(self.line_email,1, Qt.AlignHCenter)
        self.layout.addWidget(self.recuperar_btn,2, Qt.AlignHCenter)
        self.layout.addWidget(self.back,3, Qt.AlignHCenter)
        