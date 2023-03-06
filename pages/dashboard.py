from functools import partial
import os
import re
import sys
from PyQt5 import QtWidgets, uic,QtGui
from PyQt5.QtGui import QIcon,QPixmap
from pages.EditarPrivilegios import EditarPrivilegios
from pages.RegistrarUsuario import RegistrarUsuario
from usuarios import clearSession, getAllPermisos
import importlib
from ui.icons import dash

Form, Base = uic.loadUiType("ui/dashboard.ui")

class Dashboard(Base, Form):
    lista_botones = []
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.checarPermisos()
        self.setupButtons(self)
        self.logout.clicked.connect(self.cerrarSesion)
        self.cargar_resources()
        #self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
        # for i, button in enumerate(self.lista_botones):
        #     button.clicked.connect(partial(self.stackedWidget.setCurrentIndex,i))
            # button.clicked.connect(partial(self.findChild(EditarPrivilegios).label_guardado_exitoso.setText,""))
            # button.clicked.connect(partial(self.findChild(RegistrarUsuario).label_exito.setText,""))
            # button.clicked.connect(partial(self.findChild(RegistrarUsuario).label_error.setText,""))

	## para checar los botones a los que los usuarios tienen acceso, se deben cumplir las siguientes condiciones:
	# si el usuario tiene acceso a read al menos una tabla, agregar botonTabla <-- ojo aqui ya que si el usuario no puede modificar no debe salir el campo modificar
	# si el usuario tiene acceso a agregar un registro en al menos una tabla, agregar botonAgregar
	# si el usuario tiene acceso a los usuarios, agregar botonEditarPrivilegios, botonUsuarios y botonRegistrar
    
    def cargar_resources(self):
        self.label.setStyleSheet(
"   QLabel {\n"
"    image: url(:/icons/carpeta.png);\n"
"\n"
"}\n"
        )
        self.logout.setText("Cerrar sesión")
        font = QtGui.QFont("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.logout.setFont(font)
        self.logout.setIcon(QtGui.QIcon(":/icons/logout.png"))
        self.logout.setStyleSheet("QPushButton {\n"
"    color: #957F5F;\n"
"    border: none;\n"
"    height: 30px;\n"
"    border-radius: 20px;\n"
"    font: 16pt;\n"
"    padding: 5 50;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #957F5F;\n"
"    color: rgb(255, 255, 255);\n"
"    height: 30px;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")

    def checarPermisos(self):
        permisos_usuario = getAllPermisos()
        for tabla, permisos in permisos_usuario.items():
            if permisos['read'] != '': 
                if 'VerTabla' not in self.lista_botones:
                    self.lista_botones.append('VerTabla')
            if permisos['write'] != '': 
                if 'AgregarRegistro' not in self.lista_botones:
                    self.lista_botones.append('AgregarRegistro')
            if tabla == 'usuario':
                self.lista_botones.clear() 
                self.lista_botones.extend(['VerTabla','AgregarRegistro','VerUsuario','EditarPrivilegios', 'RegistrarUsuario'])
                return

    def setupButtons(self, Form):
        for i, button in enumerate(self.lista_botones):
            btn = self.createButton(self,button) # <------ funcion de dashboardButton()
            # agregar boton a stack
            self.buttonsLayout.addWidget(btn)
            #stacked.setCurrentIndex(stacked.indexOf(stacked.findChild(btn)))
            #print(stacked.indexOf(stacked.findChild(btn)))
            #btn.clicked.connect(partial(self.stackedWidget.setCurrentIndex,i+1))
        
    def createButton(self, Form,name): # cambiar nombre a addToStack
        button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        button.setFont(font)
        button.setAutoFillBackground(False)
                                             # <------------ hasta aqui llega dashboardButton()
        module = importlib.import_module(f"pages.{name}")

        instance = getattr(module, name)()
        instance.setObjectName(name.lower())
        self.stackedWidget.addWidget(instance)
        button.setObjectName(name)
        stacked = self.stackedWidget
        button.setText(re.sub(r"(\w)([A-Z])", r"\1 \2",name))
        pag = str(name)
        if pag == "VerTabla":
            button.setIcon(QtGui.QIcon(":/icons/tabla.png"))
        elif pag == "AgregarRegistro":
            button.setIcon(QtGui.QIcon(":/icons/AgregarRegistro.png"))
        elif pag == "VerUsuario":
            button.setIcon(QtGui.QIcon(":/icons/VerUsuario.png"))
        elif pag == "EditarPrivilegios":
            button.setIcon(QtGui.QIcon(":/icons/EditarPrivilegios.png"))
        elif pag == "RegistrarUsuario":
            button.setIcon(QtGui.QIcon(":/icons/RegistrarUsuario.png"))

        button.setStyleSheet("QPushButton {\n"
"    color: #957F5F;\n"
"    border: none;\n"
"    height: 30px;\n"
"    border-radius: 20px;\n"
"    font: 16pt;\n"
"    padding: 5 50;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #957F5F;\n"
"    color: rgb(255, 255, 255);\n"
"    height: 30px;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")

        button.clicked.connect(partial(stacked.setCurrentIndex,stacked.indexOf(stacked.findChild(getattr(module, name)))))

        return button

    def cerrarSesion(self):
        clearSession()
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    def reject(self) -> None:
        return
