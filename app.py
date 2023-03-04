import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from bdConexion import obtener_conexion
from pages.dashboard import Dashboard
from usuarios import saveSession, tablesToDict

class WelcomeScreen(QtWidgets.QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("ui/login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        
    def loginfunction(self):
        user = self.user.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Porfavor escribe tu usuario o contraseña")
            self.passwordfield.setText('')
            self.user.setText('')
        else:
            conn = obtener_conexion(user, password)
            saveSession(user, password)
            tablesToDict(user, password)
            cur = conn.cursor()
            print("Successfully logged in.")
            dashboard = Dashboard()
            widget.addWidget(dashboard)
            widget.setCurrentIndex(1)
            self.error.setText("")
            cur.close()
            conn.close()
            # CUANDO YA ESTE LISTA APLICACION, SE VA A UTILIZAR EL TRY EXCEPT
            # try:
            #     conn = obtener_conexion(user, password)
            #     saveSession(user, password)
            #     cur = conn.cursor()
            #     print("Successfully logged in.")
            #     dashboard = Dashboard()
            #     #tabla = VerTabla(widget)
            #     widget.addWidget(dashboard)
            #     #widget.addWidget(tabla)
            #     print(widget.currentIndex())
            #     widget.setCurrentIndex(1)
            #     #widget.setCurrentIndex(widget.currentIndex()+1)
            #     self.error.setText("")
            #     cur.close()
            #     conn.close()
            # except:
            #     self.error.setText("Usuario o contraseña incorrectos. Consulta al administrador.")
            #     self.passwordfield.setText('')
            #     self.user.setText('')

# main
app = QtWidgets.QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setMinimumHeight(800)
widget.setMinimumWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")