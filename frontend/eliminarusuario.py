from PyQt5 import QtGui, uic, QtWidgets, QtCore
from pages.editarprivilegios import EditarPrivilegios
import os
from bdConexion import obtener_conexion
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/eliminar-usuario-dialog.ui")))

class RegistrarUsuario(Form, Base):
    cols=[]
    diccionario_permisos = {'Eliminar':{},
                            'Modificar':{},
                            'Ver':{}}