from PyQt5 import QtGui, uic,QtWidgets, QtCore
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/agregar-registros.ui")))


class AgregarRegistro(Form, Base):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

	# dentro de este método se podran actualizar los campos de forma dinamica,
	# segun la tabla que se haya seleccionado	
	# def setupUi(self, Form):
		# print("agregar campos de tabla")
		# primero se obtendra la tabla seleccionada, por default sera escritura
		# se hara un fetch a la base de datos con todos los campos de esa tabla 
		# se debe renderizar la pantalla con los inputs de los campos a llenar
		# si es posible, que existan condiciones para poner el mejor tipo de campo
		# 	ejemplo 1, si es boolean que aparezca un radio button si y otro no
		# 	ejemplo 2, si es tipo datetime que aparezca uno de seleccionar fecha
		# al picar guardar, almacenar datos en la tabla. En caso de errores alertar al usuario
		# se redirige a la tabla
		# en caso de cancelar, redirigir a la tabla
		