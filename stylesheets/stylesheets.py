# IMPORT QT_CORE
from qt_core import *


# FONT
font = 'JetBrains Mono'

label_style = f"""font: 9pt {font}; 
                    color: white;
                    background-color: none;"""
                    
# LINE                    
line_style = f"""QLineEdit {{font: 8pt {font};
                    background-color: white;
                    border: 2px solid #b2b2b2;
                    border-radius: 10px;}}
                    
                    QLineEdit:focus {{border: 2px solid #3abfdc}}
                    """

# LABEL                    
label_error = f"""background-color: none;
                    font: 700 9pt {font};
                    color: #EF5350"""
                    
label_sucess = f"""background-color: none;
                    font: 700 9pt {font};
                    color: #7fba00"""

# BUTTONS
main_button = f"""QPushButton {{background-color: #0d81a5;
                    border-radius: 10px;
                    border: none;
                    font: 10pt {font};
                    color: white}}
                    
                    QPushButton:hover {{background-color: #10a0cc}}
                    
                    QPushButton:pressed {{background-color: #0b6a88}}"""
                
alter_button = f"""QPushButton {{font: 7.5pt {font};
                    background-color: #183e89;
                    color: white;
                    border-radius: 10px;
                    border: none}}
                    
                    QPushButton:hover {{color: #10a0cc}}
                
                    QPushButton:pressed {{color: #0d81a5}}"""
                    
# ICONS
icon_user = QIcon('template\\icons\\login\\user.svg')
icon_password = QIcon('template\\icons\\login\\lock.svg')
icon_email = QIcon('template\\icons\\login\\email.svg')
icon_code = QIcon('template\\icons\\login\\smartphone.svg')
