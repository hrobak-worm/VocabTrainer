# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(344, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbAddWord = QPushButton(self.centralwidget)
        self.pbAddWord.setObjectName(u"pbAddWord")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAddWord.sizePolicy().hasHeightForWidth())
        self.pbAddWord.setSizePolicy(sizePolicy)
        self.pbAddWord.setMinimumSize(QSize(200, 40))
        self.pbAddWord.setMaximumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.pbAddWord, 0, 0, 1, 1)

        self.pbLearn = QPushButton(self.centralwidget)
        self.pbLearn.setObjectName(u"pbLearn")
        sizePolicy.setHeightForWidth(self.pbLearn.sizePolicy().hasHeightForWidth())
        self.pbLearn.setSizePolicy(sizePolicy)
        self.pbLearn.setMinimumSize(QSize(200, 40))
        self.pbLearn.setMaximumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.pbLearn, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 344, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VocabTrainer", None))
        self.pbAddWord.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pbLearn.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
    # retranslateUi

