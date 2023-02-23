import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from bdConexion import obtener_conexion
from functools import partial

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("ui/login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        #self.create.clicked.connect(self.gotocreate)

    # def gototabla(self):
    #     login = Tabla()
    #     widget.addWidget(login)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    # def gotocreate(self):
    #     create = CreateAccScreen()
    #     widget.addWidget(create)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def loginfunction(self):
        user = self.user.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Porfavor escribe tu usuario o contraseña")
            self.passwordfield.setText('')
            self.user.setText('')

        else:
            conn = obtener_conexion()
            cur = conn.cursor()
            query = 'SELECT contrasena FROM usuario WHERE nombre_usuario =\''+user+"\'"
            cur.execute(query)
            print(password+" contra")
            
            result_pass = cur.fetchone()
            print(result_pass)
            cur.close()
            conn.close()
            if result_pass is not None and result_pass[0] == password:
                print("Successfully logged in.")
                dashboard = Dashboard()
                widget.addWidget(dashboard)
                widget.setCurrentIndex(widget.currentIndex()+1)
                self.error.setText("")
            else:
                self.error.setText("Usuario o contraseña incorrectos. Consulta al administrador.")
                self.passwordfield.setText('')
                self.user.setText('')



class Tabla(QDialog):
    def __init__(self):
        super(Tabla, self).__init__()
        loadUi("interfaces/ver-tabla.ui",self)
        self.agregar.clicked.connect(self.gotocreate)
        self.create.clicked.connect(self.gotocreate)
        self.create.clicked.connect(self.gotocreate)
        self.create.clicked.connect(self.gotocreate)
        
    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("interfaces/createacc.ui",self)

#     def signupfunction(self):
#         user = self.emailfield.text()
#         password = self.passwordfield.text()
#         confirmpassword = self.confirmpasswordfield.text()

#         if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
#             self.error.setText("Please fill in all inputs.")

#         elif password!=confirmpassword:
#             self.error.setText("Passwords do not match.")
#         else:
#             conn = sqlite3.connect("shop_data.db")
#             cur = conn.cursor()

#             user_info = [user, password]
#             cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)

#             conn.commit()
#             conn.close()

#             fillprofile = FillProfileScreen()
#             widget.addWidget(fillprofile)
#             widget.setCurrentIndex(widget.currentIndex()+1)

# class FillProfileScreen(QDialog):
#     def __init__(self):
#         super(FillProfileScreen, self).__init__()
#         loadUi("fillprofile.ui",self)
#         self.image.setPixmap(QPixmap('placeholder.png'))

Form, Base = uic.loadUiType("ui/dashboard.ui")

class Dashboard(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		buttons = (self.botonTabla,self.botonAgregar, self.botonEditarPrivilegios)
		for i, button in enumerate(buttons):
			button.clicked.connect(partial(self.stackedWidget.setCurrentIndex, i))

# main
app = QApplication(sys.argv)
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