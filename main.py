# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from PyQt5 import QtWidgets,QtGui

from ui.ui_dashboard import Ui_Dashboard
from ui_functions import *
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.return_to_login = False
        self.setMinimumHeight(800)
        self.setMinimumWidth(1200)
        self.doLogin()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Notarius - Sistema administrativo"
        self.setWindowTitle(title)
        centerOnScreen(self)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(
            lambda: toggleMenu(self, True))

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_tablas.clicked.connect(self.buttonClick)
        widgets.btn_agregar.clicked.connect(self.buttonClick)
        widgets.btn_registrar.clicked.connect(self.buttonClick)
        widgets.btn_usuarios.clicked.connect(self.buttonClick)
        widgets.logout.clicked.connect(self.logOut)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        
        self.show()
        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.verTabla)
        widgets.btn_tablas.setStyleSheet(selectMenu(widgets.btn_tablas.styleSheet()))
        
    def logOut(self):
        self.hide()  # hide main window
        self.doLogin()  # show login
        self.show()
        
    def doLogin(self):
        from pages.Login import LoginScreen
        login = LoginScreen()
        if login.exec_() != QtWidgets.QDialog.Accepted:
            self.close()  # exit app
    # def logOut(self):
    #     self.return_to_login = True
    #     self.close()

    # def closeEvent(self, event):
    #     if not self.return_to_login:
    #         sys.exit()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()


        # SHOW HOME PAGE
        if btnName == "btn_tablas":
            widgets.stackedWidget.setCurrentWidget(widgets.verTabla)
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_agregar":
            widgets.stackedWidget.setCurrentWidget(widgets.agregar)
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_registrar":
            widgets.stackedWidget.setCurrentWidget(
                widgets.registrar)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_usuarios":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("ui/resources/imagenes/carpeta.png"))
    window = MainWindow()
    app.exec_()
