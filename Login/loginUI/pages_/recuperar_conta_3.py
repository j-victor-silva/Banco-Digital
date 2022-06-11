# IMPORT MODULES
from qt_core import *

# IMPORT STYLESHEETS
from stylesheets.stylesheets import *


# CLASSE DA PÁGINA DE SENHA
class PasswordPage(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u'StackedWidget')
            
        # CRIAR NOVA SENHA - PÁGINA 5
        self.pass_page = QWidget()
        self.pass_page.setObjectName('pass_page')
        StackedWidget.addWidget(self.pass_page)
        
        # SIZE POLICY
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy_label = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy_label.setHorizontalStretch(0)
        sizePolicy_label.setVerticalStretch(0)
        
        # CREATE NEW PASS WINDOW
        self.pass_window = QFrame(self.pass_page)
        self.pass_window.setObjectName('pass_window')
        self.pass_window.setStyleSheet("""#pass_window {
                                            background-color: #183e89;}""")
        self.pass_window.setMinimumSize(QSize(341, 241))
        self.pass_window.setMaximumSize(QSize(341, 241))
        
        # MAIN LAYOUT
        self.pass_layout = QVBoxLayout(self.pass_window)
        self.pass_layout.setContentsMargins(30,20,30,20)
        self.pass_layout.setSpacing(20)
        
        # Label Top
        self.top_label = QLabel(self.pass_window, text='Digite a nova senha')
        self.top_label.setStyleSheet(label_style)
        
        # PLACEHOLDER TEXT COLOR
        pal = QLineEdit().palette()
        self.text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, self.text_color)
        
        # First Password
        self.first_pass = QLineEdit(self.pass_window, placeholderText='Digite a senha')
        self.first_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.first_pass.setStyleSheet(line_style)
        self.first_pass.setPalette(self.text_color)
        self.first_pass.setMinimumSize(QSize(269,44))
        self.first_pass.setMaximumSize(QSize(269,44))
        self.first_pass.addAction(icon_password, QLineEdit.LeadingPosition)
        
        # Conf. Password
        self.conf_pass = QLineEdit(self.pass_window, placeholderText='Digite a senha')
        self.conf_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.conf_pass.setStyleSheet(line_style)
        self.conf_pass.setPalette(self.text_color)
        self.conf_pass.setMinimumSize(QSize(269,44))
        self.conf_pass.setMaximumSize(QSize(269,44))
        self.conf_pass.addAction(icon_password, QLineEdit.LeadingPosition)
        
        # Alter Password Button
        self.alter_pass = QPushButton(self.pass_window, text='Alterar')
        self.alter_pass.setStyleSheet(main_button)
        self.alter_pass.setMinimumSize(QSize(269,44))
        self.alter_pass.setMaximumSize(QSize(269,44))
        
        # ADD TO MAIN LAYOUT
        self.pass_layout.addWidget(self.top_label, 0, Qt.AlignHCenter)
        self.pass_layout.addWidget(self.first_pass,1, Qt.AlignHCenter)
        self.pass_layout.addWidget(self.conf_pass,2, Qt.AlignHCenter)
        self.pass_layout.addWidget(self.alter_pass,3, Qt.AlignHCenter)
        