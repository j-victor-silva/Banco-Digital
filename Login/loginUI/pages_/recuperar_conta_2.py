# IMPORT QT CORE
from qt_core import *

# IMPORT STYLESHEETS
from stylesheets.stylesheets import *


# CLASSE DA PÁGINA DE CÓDIGO
class CodigoPage(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u'StackedWidget')
            
        # RECUPERAR SENHA / CODIGO - PÁGINA 4
        self.code_page = QWidget()
        self.code_page.setObjectName('code_page')
        StackedWidget.addWidget(self.code_page)
        
        # SIZE POLICY
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy_label = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy_label.setHorizontalStretch(0)
        sizePolicy_label.setVerticalStretch(0)
        
        # CODE WINDOW
        self.code_window = QFrame(self.code_page)
        self.code_window.setObjectName('code_window')
        self.code_window.setStyleSheet("""#code_window {
                                            background-color: #183e89;}""")
        self.code_window.setMinimumSize(QSize(341, 260))
        self.code_window.setMaximumSize(QSize(341, 260))
        
        # CREATE LAYOUT
        self.code_layout = QVBoxLayout(self.code_window)
        self.code_layout.setContentsMargins(30,20,30,20)
        self.code_layout.setSpacing(20)
        
        # BACK BUTTON
        self.back = QPushButton(self.code_window, text='Voltar')
        self.back.setStyleSheet(alter_button)
        self.back.setMinimumSize(QSize(40, 20))
        self.back.setMaximumSize(QSize(40, 20))
        
        # Label Top
        self.label = QLabel(self.code_window)
        self.label.setText('Foi enviado um código para seu email\ncaso esteja registrado.')
        self.label.setStyleSheet(label_style)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)
        
        # Line Code
        self.line_code = QLineEdit(self.code_window, placeholderText='00000')
        self.line_code.setStyleSheet(line_style)
        self.line_code.setMaxLength(5)
        self.line_code.setMinimumSize(QSize(269,44))
        self.line_code.setMaximumSize(QSize(269,44))
        self.line_code.setPalette(self.text_color)
        self.line_code.addAction(icon_code, QLineEdit.LeadingPosition)
                
        # Recuperar Button
        self.recuperar_btn = QPushButton(self.code_window, text='Recuperar senha')
        self.recuperar_btn.setStyleSheet(main_button)
        self.recuperar_btn.setMinimumSize(QSize(269,44))
        self.recuperar_btn.setMaximumSize(QSize(269,44))
        
        # Send Again Button
        self.resend_code = QPushButton(self.code_window, text='Reenviar código')
        self.resend_code.setStyleSheet(alter_button)
                
        # ADD TO LAYOUT
        self.code_layout.addWidget(self.back, 0)
        self.code_layout.addWidget(self.label, 1, Qt.AlignHCenter)
        self.code_layout.addWidget(self.line_code, 2, Qt.AlignHCenter)
        self.code_layout.addWidget(self.recuperar_btn, 3, Qt.AlignHCenter)
        self.code_layout.addWidget(self.resend_code, 4, Qt.AlignHCenter)
        
        