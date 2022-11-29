# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(200, 200)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(250, 200))
        MainWindow.setStyleSheet(u"background-color: #FFFFFF;\n"
"font-family: 'Century Gothic';")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #000000;")

        self.verticalLayout.addWidget(self.label)

        self.selected_video = QLabel(self.centralwidget)
        self.selected_video.setObjectName(u"selected_video")
        self.selected_video.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.selected_video)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_link = QLineEdit(self.centralwidget)
        self.select_link.setObjectName(u"select_link")

        self.horizontalLayout.addWidget(self.select_link)

        self.select_btn = QPushButton(self.centralwidget)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setMaximumSize(QSize(60, 16777215))
        self.select_btn.setStyleSheet(u"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.select_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setStyleSheet(u"font-weight: bold;\n"
"font-size: 13px;\n"
"letter-spacing: 1px;\n"
"color: black;\n"
"background-color: red;\n"
"")

        self.verticalLayout.addWidget(self.download_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"YouTube Downloader", None))
        self.selected_video.setText("")
        self.select_link.setText("")
        self.select_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the link", None))
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Best quality", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Worst quality", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Audio only (best)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Audio only (worst)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Video only (best)", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Video only (worst)", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

