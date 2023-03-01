from lib2to3.pgen2.pgen import generate_grammar
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
		#self.showGrants()

		self.button_guardar.clicked.connect(self.guardarCambios)

		# cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
		self.usuarioslist.currentTextChanged.connect(self.limpiarDict)
		self.tablaslist.currentTextChanged.connect(self.setupColumns)
		self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
  
	# def showGrants(self):
	# 	conn = obtener_conexion()
	# 	cur = conn.cursor()
	# 	usuario_seleccionado = self.usuarioslist.currentText()
	# 	query=f"SHOW GRANTS FOR '{usuario_seleccionado}'@'localhost';"
	# 	cur.execute(query)
	# 	permisos = cur.fetchall()
	# 	cur.close()
	# 	conn.close()
	# 	lista_permisos = [permisos[0] for permisos in permisos[1:]]
	# 	self.limpiar_lista_permisos(lista_permisos)
	
	def limpiar_lista_permisos(self, lista_permisos):
		for texto in lista_permisos:
			select_i = texto.find("SELECT")
			insert_i = texto.find("INSERT")
			update_i = texto.find("UPDATE")
			notarius_i = texto.find("notarius")
			to_i = texto.find("TO")

			nombre_tabla = texto[notarius_i+11:to_i-2]
			print("La tabla es:",nombre_tabla)
			if "SELECT" in texto:
				par_i = texto.index(')')
				subcadena_select = texto[select_i:par_i]
				subcadena_select = subcadena_select.replace("(","")
				par_i=texto.find(')', texto.find(')')+1)
				subcadena_insert = texto[insert_i:par_i]
				subcadena_insert = subcadena_insert.replace("(","")
				par_i = texto.rfind(')')
				subcadena_update = texto[update_i:par_i]
				subcadena_update = subcadena_update.replace("(","")
			else:
				par_i = texto.index(')')
				subcadena_insert = texto[insert_i:par_i]
				subcadena_insert = subcadena_insert.replace("(","")
				par_i = texto.rfind(')')
				subcadena_update = texto[update_i:par_i]
				subcadena_update = subcadena_update.replace("(","")
			permiso_select = (subcadena_select.replace(", ",",")).split(" ")
			permiso_insert = (subcadena_insert.replace(", ",",")).split(" ")
			permiso_update = (subcadena_update.replace(", ",",")).split(" ")

			permiso_select.append(nombre_tabla)
			permiso_insert.append(nombre_tabla)
			permiso_update.append(nombre_tabla)
			print(permiso_select)
			print(permiso_insert)
			print(permiso_update)

			#ya tomé ejnergias ya comi 


			


	def guardarCambios(self):
		usuario_seleccionado = self.usuarioslist.currentText()
		self.generarGrants(usuario_seleccionado)
		self.label_guardado_exitoso.setText("Guardado exitosamente")
    	

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
		# aqui se le asignan los metodos a cada checkbox y se llena el diccionario con las columnas de la tabla - Jared
		self.connectCheckboxes(self)
		self.resetCheckboxes(self)

	def generarGrants(self,nombre_usuario):
		query = f""
		conn = obtener_conexion()
		cur = conn.cursor()
		for llave,accion in self.diccionario_permisos.items():
			if llave == 'Agregar': permiso='INSERT'
			elif llave == 'Modificar': permiso='UPDATE'
			elif llave == 'Ver': permiso='SELECT'
			for nombre_tabla,columnas in accion.items():
				for nombre_columna,checked in columnas.items():
					if checked:
						query=f"GRANT {permiso} ({nombre_columna}) ON {nombre_tabla} TO '{nombre_usuario}'@'localhost';"
						cur.execute(query)
		cur.close()
		conn.close()

	def resetCombobox(self, Form):
		for obj in self.cols:
			self.gridLayout.removeWidget(obj)
			obj.deleteLater()
			del obj
		self.cols = []

	# este metodo le asigna un metodo a cada checkbox que ejecuta guardar_opcion al ser activado/desactivado - Jared
	def connectCheckboxes(self, Form):
		for obj in self.cols:
			obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	# este metodo revisa el diccionario de permisos y activa aquellas columnas que estan guardadas como true -Jared
	def resetCheckboxes(self, Form):
		for obj in self.cols:
			if self.tablaslist.currentText() not in self.diccionario_permisos[self.accioneslist.currentText()]:
				self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()] = {}
			if obj.text() in self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()]:
				obj.setChecked(self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()][obj.text()])
			else:
				obj.setChecked(False)

	'''
	En este metodo se guarda si el checkbox fue activado o no.
	El diccionario se compone por:
	Acciones (Guardar,Ver,Modificar) -> Nombre de tabla -> Columna: True/False
	-Jared
	'''
	def guardar_opcion(self, obj):
		self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()][obj.text()] = obj.isChecked()

	#este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
	def limpiarDict(self):
		self.diccionario_permisos = {'Agregar':{},
								'Modificar':{},
								'Ver':{}}
		self.resetCheckboxes(Form)



	# al seleccionar guardar se llevara a cabo el comando en la base de datos
	#	ejemplo: GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO 'someuser'@'somehost';
	# seria buena opcion que aparezca un aviso una vez que se ha guardado correctamente
