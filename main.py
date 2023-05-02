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
from PyQt5 import QtWidgets,QtGui


from ui_functions import *
from usuarios import clearSession, getUsuarioLogueado
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
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        from ui.ui_dashboard import Ui_Dashboard
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
       
        global widgets
        widgets = self.ui
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Notarius - Sistema administrativo"
        self.setWindowTitle(title)
        centerOnScreen(self)
        uiDefinitions(self)
        self.ui.leftMenuBg.hide()
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(
            lambda: toggleMenu(self.ui, True))

        # BUTTON CLICK
        widgets.logout.clicked.connect(self.logOut)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            toggleLeftBox(self.ui, True)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        
        
        self.show()
        if self.ui.login.exec_() == QtWidgets.QDialog.Accepted:
            user, pwd = getUsuarioLogueado()
            self.ui.leftMenuBg.show()
            checarPermisos(self.ui)
            createButtons(self.ui)
            self.ui.titleLeftDescription.setText(QCoreApplication.translate(
            "MainWindow", f"Usuario: {user}", None))
            nombre_btn = getListaBotones()[0][0].lower()
            startPage = getattr(self.ui, nombre_btn)
            button = getattr(self.ui, f"btn_{nombre_btn}")
            self.ui.stackedWidget.setCurrentWidget(startPage)
            button.setStyleSheet(selectMenu(button.styleSheet()))
        else:
            self.close()
        # ///////////////////////////////////////////////////////////////
        # SET HOME PAGE AND SELECT MENU
        
         # SHOW APP
        
        
    def logOut(self):
        clearSession()
        self.return_to_login = True
        self.close()
        #self.ui.stackedWidget.setCurrentWidget(self.ui.login)


    def closeEvent(self, event):
        if not self.return_to_login:
            sys.exit()


if __name__ == "__main__":
    from pages.Login import LoginScreen

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("ui/resources/imagenes/carpeta.png"))
    while True:
        win = MainWindow()
        app.exec_()

