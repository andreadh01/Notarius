from functools import partial
import os
import re
import sys
from PyQt5 import QtWidgets, uic,QtGui
from pages.EditarPrivilegios import EditarPrivilegios
from pages.RegistrarUsuario import RegistrarUsuario
from usuarios import clearSession, getAllPermisos
import importlib

Form, Base = uic.loadUiType("ui/dashboard.ui")


class Dashboard(Base, Form):
    lista_botones = []
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.checarPermisos()
        self.setupButtons(self)
        self.logout.clicked.connect(self.cerrarSesion)
        #self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
        # for i, button in enumerate(self.lista_botones):
        #     button.clicked.connect(partial(self.stackedWidget.setCurrentIndex,i))
            # button.clicked.connect(partial(self.findChild(EditarPrivilegios).label_guardado_exitoso.setText,""))
            # button.clicked.connect(partial(self.findChild(RegistrarUsuario).label_exito.setText,""))
            # button.clicked.connect(partial(self.findChild(RegistrarUsuario).label_error.setText,""))

	## para checar los botones a los que los usuarios tienen acceso, se deben cumplir las siguientes condiciones:
	# si el usuario tiene acceso a ver al menos una tabla, agregar botonTabla <-- ojo aqui ya que si el usuario no puede modificar no debe salir el campo modificar
	# si el usuario tiene acceso a agregar un registro en al menos una tabla, agregar botonAgregar
	# si el usuario tiene acceso a los usuarios, agregar botonEditarPrivilegios, botonUsuarios y botonRegistrar
    def checarPermisos(self):
        permisos_usuario = getAllPermisos()
        for tabla, permisos in permisos_usuario.items():
            if permisos['SELECT'] != '' or permisos['UPDATE'] != '': self.lista_botones.append('VerTabla')
            if permisos['INSERT'] != '': self.lista_botones.append('AgregarRegistro')
            if tabla == 'usuario':
                self.lista_botones.clear() 
                self.lista_botones.extend(['VerTabla','AgregarRegistro','VerUsuario','EditarPrivilegios', 'RegistrarUsuario'])
                return
            
            

    def setupButtons(self, Form):
        print('botonesssss')
        print(self.lista_botones)
        for i, button in enumerate(self.lista_botones):
            print(button)
            btn = self.createButton(self,button)
            self.buttonsLayout.addWidget(btn)
            #stacked.setCurrentIndex(stacked.indexOf(stacked.findChild(btn)))
            #print(stacked.indexOf(stacked.findChild(btn)))
            #btn.clicked.connect(partial(self.stackedWidget.setCurrentIndex,i+1))
        
    def createButton(self, Form,name):
        button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        button.setFont(font)
        button.setAutoFillBackground(False)
        button.setStyleSheet("QPushButton {\n"
"    color: rgb(141, 110, 58);\n"
"    border: none;\n"
"    height: 25px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        module = importlib.import_module(f"pages.{name}")
        print(name, module)
        instance = getattr(module, name)()
        instance.setObjectName(name.lower())
        self.stackedWidget.addWidget(instance)
        button.setObjectName(name)
        stacked = self.stackedWidget
        button.setText(re.sub(r"(\w)([A-Z])", r"\1 \2",name))
        button.clicked.connect(partial(stacked.setCurrentIndex,stacked.indexOf(stacked.findChild(getattr(module, name)))))
        print("INDEX  "+str(stacked.indexOf(stacked.findChild(getattr(module, name)))))
        return button
    
    def cerrarSesion(self):
        print('AQUIIII')
        clearSession()
        os.execl(sys.executable, sys.executable, *sys.argv)
