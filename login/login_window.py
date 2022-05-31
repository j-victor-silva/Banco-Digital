# IMPORT QT_CORE
from qt_core import *
from login.pages import *


# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')
        parent.setWindowTitle('Login')      
        
        self.font = 'JetBrains Mono'  
            
        # ////////////////////////////////////////////////////////////////////
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
        # ////////////////////////////////////////////////////////////////////
        
        # CREATE MAIN LAYOUT
        self.main_layout = QVBoxLayout(self.central_frame)
        
        # CREATE CENTRAL LAYOUT
        self.central_layout = QFrame()
        
        # CREATE SUB LAYOUT
        self.sub_layout = QHBoxLayout(self.central_layout)
        
        # CREATE SPACERS
        self.spacer_w_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_w_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_h_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spacer_h_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # CREATE PAGES
        self.pages = QStackedWidget(self.central_frame)
        self.pages.setMinimumSize(QSize(341, 385))
        self.pages.setMaximumSize(QSize(341, 385))
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.login)
        
        # SET TO SUB LAYOUT
        self.sub_layout.addItem(self.spacer_w_1)
        self.sub_layout.addWidget(self.pages)
        self.sub_layout.addItem(self.spacer_w_2)
        
        # SET TO MAIN LAYOUT
        self.main_layout.addItem(self.spacer_h_1)
        self.main_layout.addWidget(self.central_layout)
        self.main_layout.addItem(self.spacer_h_2)
                
        # SET TO CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
        # ////////////////////////////////////////////////////////////////////
