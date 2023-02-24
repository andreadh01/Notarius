from PyQt5 import QtGui, uic
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-privilegios.ui")))


class EditarPrivilegios(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
  
	# en este metodo se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
	# def setupUi(self, Form):
		# print("editar privilegios")
		# el usuario sera redirigido a esta pagina al seleccionar un usuario de la tabla
		# la otra opcion es que lo seleccione dentro de esta pantalla, en caso de ser asi, rellenar un combo box con un fetch de los usuarios
		# despues de tener un usuario seleccionado, se selecciona el tipo de permiso a otorgar 
		# el cual puede ser SELECT, INSERT, UPDATE
  		# se selecciona una tabla, por default sera escrituras
		# se cargaran cada uno de los campos de la tabla seleccionada, a partir de un fetch de la base de datos
		# estos campos seran del tipo combo box
		# al seleccionar guardar se llevara a cabo el comando en la base de datos
		#	ejemplo: GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO 'someuser'@'somehost';
