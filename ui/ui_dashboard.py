# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'maingnxZcz.ui'
##
# Created by: Qt User Interface Compiler version 6.0.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from functools import partial
import importlib
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pages.AgregarRegistro import AgregarRegistro
from pages.RegistrarUsuario import RegistrarUsuario
from pages.Tablas import Tablas
from pages.Login import LoginScreen

from resources_rc import *
from ui_functions import resetStyle, selectMenu
from usuarios import getAllPermisos, getUsuarioLogueado


class Ui_Dashboard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"""
                                      QWidget{
                                      	color: rgb(221, 221, 221);
                                      	font: 11pt \"Segoe UI\";
                                      }
                                      
          
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      Bg App */
                                      #bgApp {	
                                      	background-color: white;
                                      	border: 1px solid white;
                                      }
                                      
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      Left Menu */
                                      #leftMenuBg {	
                                      	background-color: rgb(245, 243, 240);
                                      }
                                      #topLogo {
                                      	background-color: rgb(245, 243, 240);
                                      	background-image: url(:/resources/resources/imagenes/folder.png);
                                      	background-position: centered;
                                      	background-repeat: no-repeat;
                                      }
                                      #titleLeftApp { font: 600 12pt \"Segoe UI Semibold\";color: rgb(116, 91, 47);}
                                      #titleLeftDescription { font: 8pt \"Segoe UI\"; color:#302512; }
                                      
                                      /* MENUS */
                                      #topMenu .QPushButton {	
                                      	background-position: left center;
                                          background-repeat: no-repeat;
                                      	border: none;
                                      	border-left: 22px solid transparent;
                                      	background-color: rgb(245, 243, 240);
                                      color: rgb(116, 91, 47);
                                      	text-align: left;
                                      	padding-left: 44px;
                                      }
                                      #topMenu .QPushButton:hover {
                                      	background-color: #e3ddcc;
                                      }
                                      #topMenu .QPushButton:pressed {	
                                      	background-color: #d3c393;
                                      	color: rgb(116, 91, 47);
                                      }
                                      #bottomMenu .QPushButton {	
                                      	background-position: left center;
                                          background-repeat: no-repeat;
                                      	border: none;
                                      	border-left: 20px solid transparent;
                                      	background-color:transparent;
                                      	text-align: left;
                                      	padding-left: 44px;
                                      }
                                      #bottomMenu .QPushButton:hover {
                                      	background-color: #e3ddcc;
                                      }
                                      #bottomMenu .QPushButton:pressed {	
                                      	background-color:#d3c393;
                                      	color: rgb(116, 91, 47);
                                      }
                                      #leftMenuFrame{
                                      	border-top: none;
                                      }
                                      
                                      /* Toggle Button */
                                      #toggleButton {
                                      	background-position: left center;
                                          background-repeat: no-repeat;
                                      	border: none;
                                      	border-left: 20px solid transparent;
                                      	background-color: rgb(245, 243, 240);
                                      	text-align: left;
                                      	padding-left: 44px;
                                      	color: #666;
                                      }
                                      #toggleButton:hover {
                                      	background-color: #e3ddcc;
                                      }
                                      #toggleButton:pressed {
                                      	background-color: #d3c393;
                                      	color: white;
                                      }
                                      

                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      LineEdit */
                                      QLineEdit {
                                      	background-color: white;
                                      	border-radius: 5px;
                                      	border: 1px solid #cccccc;
                                      color:#666666;
                                      	padding-left: 10px;
                                      	selection-color: rgb(27, 29, 35);
                                      	selection-background-color: #c2dbfe;
                                      }
                                      QLineEdit:hover {
                                      	border: 1px solid #c2dbfe;
                                      }
                                      QLineEdit:focus {
                                      	border: 1px solid #c2dbfe;
                                      }
                                      
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      PlainTextEdit */
                                      QPlainTextEdit {
                                      	background-color: white;
                                      	border-radius: 5px;
                                      	border: 1px solid #cccccc;
                                      color:#666666;
                                      	padding-left: 10px;
                                      	selection-color: rgb(27, 29, 35);
                                      	selection-background-color: #c2dbfe;
                                      }
                                      QPlainTextEdit:hover {
                                      	border: 1px solid #c2dbfe;
                                      }
                                      QPlainTextEdit:focus {
                                      	border: 1px solid #c2dbfe;
                                      }
                                      
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                        
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      CheckBox */
                                      QCheckBox::indicator {
                                          border: 1px solid #cccccc;
                                      	width: 16px;
                                      	height: 16px;
                                          background: white;
                                      }
                                      QCheckBox::indicator:hover {
                                          border: 1px solid #c2dbfe;
                                      }
                                      QCheckBox::indicator:checked {
                                          background: 3px solid #c2dbfe;
                                      	border: 1px solid #c2dbfe;	
                                      	background-image: url(:/resources/resources/icons/cheque.png);
                                      }
                                      
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      RadioButton */
                                      QRadioButton::indicator {
                                          border: 1px solid #cccccc;
                                      	width: 10px;
                                      	height: 10px;
                                      	border-radius: 30px;
                                          background: white;
                                      }
                                      QRadioButton::indicator:hover {
                                          border: 1px solid #c2dbfe;
                                      }
                                      QRadioButton::indicator:checked {
                                          background: 1px solid #c2dbfe;
                                      	border: 1px solid #c2dbfe;	
                                      }
                                      
                                     
                                      
                                      /* /////////////////////////////////////////////////////////////////////////////////////////////////
                                      """)
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(
            u"background-image: url(:/resources/resources/icons/menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.logout = QPushButton(self.bottomMenu)
        self.logout.setObjectName(u"logout")
        sizePolicy.setHeightForWidth(
            self.logout.sizePolicy().hasHeightForWidth())
        self.logout.setSizePolicy(sizePolicy)
        self.logout.setMinimumSize(QSize(0, 45))
        self.logout.setFont(font)
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout.setLayoutDirection(Qt.LeftToRight)
        self.logout.setStyleSheet(
            u"color: rgb(116, 91, 47);background-image: url(:/resources/resources/icons/logout.png);")

        self.verticalLayout_9.addWidget(self.logout)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.verticalLayout_5.addLayout(self.extraTopLayout)

        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

    

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)

        self.extraColumLayout.addWidget(self.extraContent)

        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        
        self.login = LoginScreen()
        self.login.setObjectName(u"login")
        self.stackedWidget.addWidget(self.login)
        self.stackedWidget.setCurrentWidget(self.login)
        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.verticalLayout_6.addWidget(self.content)

        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate(
            "MainWindow", u"NOTARIUS", None))
        self.toggleButton.setText(
            QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.logout.setText(
            QCoreApplication.translate("MainWindow", u"Cerrar sesión", None))

        self.logout.setText(QCoreApplication.translate(
            "MainWindow", u"Cerrar sesión", None))

    # retranslateUi
