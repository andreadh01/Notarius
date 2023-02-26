from PyQt5 import uic,QtWidgets
import os

from bdConexion import obtener_conexion
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-privilegios.ui")))


class EditarPrivilegios(Base, Form):
	cols = []
	diccionario_permisos = {'Agregar':{},
							'Modificar':{},
							'Ver':{}}
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		# se mandan llamar los metodos al correr el programa
		self.setupUsers(self)
		self.setupTables(self)
		self.setupColumns(self)
		# cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
		self.usuarioslist.currentTextChanged.connect(self.limpiarDict)
		self.tablaslist.currentTextChanged.connect(self.setupColumns)
		self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
  
	# en esta funcion se van a cargar los usuarios de la base de datos al combobox de usuarios
	def setupUsers(self, Form):
		conn = obtener_conexion()
		cur = conn.cursor()
		query = 'SELECT nombre_usuario FROM usuario'
		cur.execute(query)
		usuarios = cur.fetchall()
		cur.close()
		conn.close()
		lista_usuarios = [usu[0] for usu in usuarios]
		self.usuarioslist.addItems(lista_usuarios)

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
	def setupTables(self, Form):
		conn = obtener_conexion()
		cur = conn.cursor()
		query = 'SHOW TABLES'
		cur.execute(query)
		tablas = cur.fetchall()
		cur.close()
		conn.close()
		lista_tablas = [tabla[0] for tabla in tablas]
		self.tablaslist.addItems(lista_tablas)
	
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
	def setupColumns(self, Form):
		# se eliminan los combobox anteriores
		self.resetCombobox(self)
		conn = obtener_conexion()
		cur = conn.cursor()
		tabla_seleccionada = self.tablaslist.currentText()
		query = ' SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= \''+tabla_seleccionada+'\''
		cur.execute(query)
		columnas = cur.fetchall()
		cur.close()
		conn.close()
		lista_columnas = [col[0] for col in columnas]
		# aqui se crea el widget del checkbox y se agrega al gui
		for i, col in enumerate(lista_columnas):
			name = f"acceso_{i}"
			setattr(self, name, QtWidgets.QCheckBox(Form))
			attr = getattr(self,name)
			attr.setStyleSheet("\n"
			"font: 75 16pt;\n"
			"color: rgb(149, 117, 61);")
			attr.setObjectName(name)
			attr.setText(col)
			self.gridLayout.addWidget(attr, i+1, 3, 1, 1)
			self.cols.append(attr)
		self.connectCheckboxes(self)
		self.resetCheckboxes(self)

	def resetCombobox(self, Form):
		for obj in self.cols:
			self.gridLayout.removeWidget(obj)
			obj.deleteLater()
			del obj
		self.cols = []

	def connectCheckboxes(self, Form):
		for obj in self.cols:
			obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	def resetCheckboxes(self, Form):
		for obj in self.cols:
			if self.tablaslist.currentText() not in self.diccionario_permisos[self.accioneslist.currentText()]:
				self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()] = {}
			if obj.text() in self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()]:
				obj.setChecked(self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()][obj.text()])
			else:
				obj.setChecked(False)

	def guardar_opcion(self, obj):
		self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()][obj.text()] = obj.isChecked()

	def limpiarDict(self):
		self.diccionario_permisos = {'Agregar':{},
								'Modificar':{},
								'Ver':{}}
		print(self.diccionario_permisos)
		self.resetCheckboxes(Form)

	# al seleccionar guardar se llevara a cabo el comando en la base de datos
	#	ejemplo: GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO 'someuser'@'somehost';
	# seria buena opcion que aparezca un aviso una vez que se ha guardado correctamente
