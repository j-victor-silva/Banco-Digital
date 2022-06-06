# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwHZqWX.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QStackedWidget, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(576, 416)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        StackedWidget.addWidget(self.login)
        self.registro = QWidget()
        self.registro.setObjectName(u"registro")
        StackedWidget.addWidget(self.registro)
        self.recuperar_conta = QWidget()
        self.recuperar_conta.setObjectName(u"recuperar_conta")
        StackedWidget.addWidget(self.recuperar_conta)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
    # retranslateUi

