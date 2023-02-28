import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from bdConexion import obtener_conexion
from functools import partial

from pages.editarprivilegios import EditarPrivilegios
from pages.registrarusuario import RegistrarUsuario
from pages.vertabla import VerTabla



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
            try:
                conn = obtener_conexion(user, password)
                cur = conn.cursor()
                print("Successfully logged in.")
                dashboard = Dashboard()
                tabla = VerTabla(widget)
                widget.addWidget(dashboard)
                widget.addWidget(tabla)
                widget.setCurrentIndex(widget.currentIndex()+1)
                self.error.setText("")
                cur.close()
                conn.close()
            except:
                self.error.setText("Usuario o contraseña incorrectos. Consulta al administrador.")
                self.passwordfield.setText('')
                self.user.setText('')
            # query = 'SELECT contrasena FROM usuario WHERE nombre_usuario =\''+user+"\'"
            # cur.execute(query)
            # print(password+" contra")
            
            # result_pass = cur.fetchone()
            # print(result_pass)
            
            # if result_pass is not None and result_pass[0] == password:
            #     print("Successfully logged in.")
            #     dashboard = Dashboard()
            #     tabla = VerTabla(widget)
            #     widget.addWidget(dashboard)
            #     widget.addWidget(tabla)
            #     widget.setCurrentIndex(widget.currentIndex()+1)
            #     self.error.setText("")
            # else:
            #     self.error.setText("Usuario o contraseña incorrectos. Consulta al administrador.")
            #     self.passwordfield.setText('')
            #     self.user.setText('')

Form, Base = uic.loadUiType("ui/dashboard.ui")

class Dashboard(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        buttons = (self.botonTabla,self.botonAgregar, self.botonEditarPrivilegios, self.botonRegistrar, self.botonUsuarios)
        for i, button in enumerate(buttons):
            button.clicked.connect(partial(self.stackedWidget.setCurrentIndex,i))
            button.clicked.connect(partial(self.findChild(EditarPrivilegios).label_guardado_exitoso.setText,""))
            button.clicked.connect(partial(self.findChild(RegistrarUsuario).label_exito.setText,""))
            button.clicked.connect(partial(self.findChild(RegistrarUsuario).label_error.setText,""))

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