# IMPORT QT_CORE
from logging import PlaceHolder
from qt_core import *


# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')
        
        # ////////////////////////////////////////////////////////////////////
        # SET INITIAL PARAMETERS
        parent.resize(960, 600)
        parent.setMinimumSize(960, 600)
        
        # SET CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet('background-color: #00153f')
        # ////////////////////////////////////////////////////////////////////
        
        # ////////////////////////////////////////////////////////////////////
        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # LOGIN WINDOW
        self.login_window = QFrame()
        self.login_window.setObjectName('login_window')
        self.login_window.setStyleSheet('#login_window {background-color: #183e89;}')
        self.login_window.setMinimumSize(341, 385)
        self.login_window.setMaximumWidth(341)
        self.login_window.setMaximumHeight(385)
        self.login_window.setMaximumHeight(385)
        # ////////////////////////////////////////////////////////////////////
        
        # ////////////////////////////////////////////////////////////////////
        # LOGIN MENU LAYOUT
        self.login_menu = QGridLayout(self.login_window)
        self.login_menu.setContentsMargins(30, 20, 30, 20)
        self.login_menu.setSpacing(20)
        
        # Spacer Top
        self.spacer_top = QSpacerItem(0, 20)
        
        # Label Login
        self.login_label = QLabel(self.central_frame)
        self.login_label.setText('Login')
        self.login_label.setStyleSheet("""font: jetbrains Mono; 
                                            color: white;
                                            background-color: #183e89;
                                            font-size: 12pt""")
        self.login_label.setAlignment(Qt.AlignHCenter)
        
        # Placeholder Text Color
        pal = QLineEdit().palette()
        text_color = QColor('#b4b4b4')
        pal.setColor(QPalette.PlaceholderText, text_color)
        
        # Line Username
        self.line_user = QLineEdit(placeholderText='Username')
        self.line_user.setMinimumSize(269, 44)
        self.line_user.setStyleSheet("""background-color: white;
                                        border-radius: 10px
                                     """)
        self.line_user.setPalette(text_color)
        
        # Line Password
        self.line_password = QLineEdit(placeholderText='Password')
        self.line_password.setMinimumSize(269, 44)
        self.line_password.setStyleSheet("""background-color: white;
                                            border-radius: 10px
                                         """)
        self.line_password.setPalette(text_color)
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Login Button
        self.login_btn = QPushButton()
        self.login_btn.setMinimumSize(269, 44)
        self.login_btn.setStyleSheet("""background-color: #0d81a5;
                                        border: none;
                                        font: 12px jetstreams mono""")
        self.login_btn.setText('Login')
        
        # Spacer Inter-Lines
        self.spacer = QSpacerItem(268, 85)
        # ////////////////////////////////////////////////////////////////////
        
        # ////////////////////////////////////////////////////////////////////
        # ADD TO LOGIN LAYOUT
        self.login_menu.addItem(self.spacer_top)
        self.login_menu.addWidget(self.login_label)
        self.login_menu.addWidget(self.line_user)
        self.login_menu.addWidget(self.line_password)
        self.login_menu.addItem(self.spacer)
        self.login_menu.addWidget(self.login_btn)
        
        # ADD TO LAYOUT
        self.main_layout.addWidget(self.login_window)
        
        # SET TO CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
        # ////////////////////////////////////////////////////////////////////
