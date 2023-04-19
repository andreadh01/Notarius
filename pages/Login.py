from doctest import master
import os
import sys
from resources_rc import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from bdConexion import obtener_conexion
from ui_functions import centerOnScreen
from usuarios import saveSession, tablaToDict

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

class LoginScreen(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(self.__class__, self).__init__(parent)
        loadUi("ui/login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.setMinimumHeight(800)
        self.setMinimumWidth(1200)
        self.setWindowTitle('Notarius - Login')
        centerOnScreen(self)
        self.show()

    def closeEvent(self, event):
        sys.exit()
    
    def loginfunction(self):
        user = self.user.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Porfavor escribe tu usuario o contraseña")
            self.passwordfield.setText('')
            self.user.setText('')
        else:
            # SI APARECE UN ERROR SIMILAR A  Access denied for user 'j'@'localhost' (using password: YES),
            # COMENTAR EL TRY CATCH Y DESCOMENTAR ESTAS LINEAS
            conn = obtener_conexion(user, password)
            saveSession(user, password)
            tablaToDict(user, password)
            cur = conn.cursor()
            print("Successfully logged in.")
            self.error.setText("")
            cur.close()
            conn.close()
            self.accept()
            # try:
            #     conn = obtener_conexion(user, password)
            #     saveSession(user, password)
            #     tablaToDict(user, password)

            #     cur = conn.cursor()
            #     print("Successfully logged in.")
            #     self.error.setText("")
            #     cur.close()
            #     conn.close()
            #     self.accept()
            # except:
            #     self.error.setText("Usuario o contraseña incorrectos. Consulta al administrador.")
            #     self.passwordfield.setText('')
            #     self.user.setText('')
    def reject(self) -> None:
        return
