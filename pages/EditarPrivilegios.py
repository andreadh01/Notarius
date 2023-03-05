from PyQt5 import uic,QtWidgets
import os
from bdConexion import obtener_conexion
from functools import partial

from usuarios import getListaTablas, getUsuarioLogueado

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-privilegios.ui")))


class EditarPrivilegios(Base, Form):
	cols = []
	diccionario_permisos = {'Ver':{},
							'Escritura':{},
							' ':{}}
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		# se mandan llamar los metodos al correr el programa
		self.setupUsers(self)
		self.setupTables(self)
		self.setupColumns(self)
		
		

		self.button_guardar.clicked.connect(self.guardarCambios)

		# cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
		self.usuarioslist.currentTextChanged.connect(self.limpiarDict)
		self.usuarioslist.currentTextChanged.connect(self.showGrants)
		self.tablaslist.currentTextChanged.connect(self.setupColumns)
		self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
  
	def showGrants(self):
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		usuario_seleccionado = self.usuarioslist.currentText()
		query=f"SHOW GRANTS FOR '{usuario_seleccionado}'@'localhost';"
		cur.execute(query)
		permisos = cur.fetchall()
		cur.close()
		conn.close()
		lista_permisos = [permisos[0] for permisos in permisos[1:]]
		self.limpiar_lista_permisos(lista_permisos)
	
	def limpiar_lista_permisos(self,lista_permisos):
		for texto in lista_permisos:
			subcadena_insert = ""
			subcadena_select = ""
			select_i = texto.find("SELECT")
			insert_i = texto.find("INSERT")
			notarius_i = texto.find("notarius")
			to_i = texto.find("TO")

			nombre_tabla = texto[notarius_i+11:to_i-2]
			print("La tabla es:",nombre_tabla)
			if "SELECT" in texto:
				par_i = texto.find(')')
				subcadena_select = texto[select_i:par_i]
				subcadena_select = subcadena_select.replace("(","")
				par_i=texto.find(')', texto.find(')')+1)
				subcadena_insert = texto[insert_i:par_i]
				subcadena_insert = subcadena_insert.replace("(","")
			else:
				par_i = texto.find(')')
				subcadena_insert = texto[insert_i:par_i]
				subcadena_insert = subcadena_insert.replace("(","")
	
			permiso_select = (subcadena_select.replace(", ",",")).split(" ")
			permiso_insert = (subcadena_insert.replace(", ",",")).split(" ")

			permiso_select.append(nombre_tabla)
			permiso_insert.append(nombre_tabla)
			self.ingresar_datos_diccionario(permiso_select,permiso_insert)
		print(self.diccionario_permisos)


	def ingresar_datos_diccionario(self,permiso_select,permiso_insert):
		if len(permiso_select) > 2:
			columnas = permiso_select[1].split(",")
			for columna in columnas:
				if permiso_select[2] not in self.diccionario_permisos['Ver']:
					self.diccionario_permisos['Ver'][permiso_select[2]] = {}
				self.diccionario_permisos['Ver'][permiso_select[2]][columna] = True
		if len(permiso_insert) > 2:
			columnas = permiso_insert[1].split(",")
			for columna in columnas:
				if permiso_insert[2] not in self.diccionario_permisos['Escritura']:
					self.diccionario_permisos['Escritura'][permiso_insert[2]] = {}
				self.diccionario_permisos['Escritura'][permiso_insert[2]][columna] = True

	def guardarCambios(self):
		usuario_seleccionado = self.usuarioslist.currentText()
		self.generarGrants(usuario_seleccionado)
		self.label_guardado_exitoso.setText("Guardado exitosamente")
    	

	# en esta funcion se van a cargar los usuarios de la base de datos al combobox de usuarios
	def setupUsers(self, Form):
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		query = 'SELECT nombre_usuario FROM usuario'
		cur.execute(query)
		usuarios = cur.fetchall()
		cur.close()
		conn.close()
		lista_usuarios = [usu[0] for usu in usuarios]
		self.usuarioslist.addItems(lista_usuarios)
		self.showGrants()

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
	def setupTables(self, Form):
		lista_tablas = getListaTablas()
		self.tablaslist.addItems(lista_tablas)
	
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
	def setupColumns(self, Form):
		# se eliminan los combobox anteriores
		self.resetCombobox(self)
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		tabla_seleccionada = self.tablaslist.currentText()
		query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= '{tabla_seleccionada}' AND TABLE_SCHEMA='notarius'"
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
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		query=f"REVOKE ALL PRIVILEGES, GRANT OPTION FROM '{nombre_usuario}'@'localhost';"
		cur.execute(query)
		for llave,accion in self.diccionario_permisos.items():
			for nombre_tabla,columnas in accion.items():
				for nombre_columna,checked in columnas.items():
					if checked:
						if llave == 'Ver':
							query=f"GRANT SELECT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
							cur.execute(query)
						elif llave == 'Escritura':
							query=f"GRANT INSERT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
							cur.execute(query)
							query=f"GRANT UPDATE ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
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
		for permiso in self.diccionario_permisos:
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
	Acciones (Ver, Escritura) -> Nombre de tabla -> Columna: True/False
	-Jared
	'''
	def guardar_opcion(self, obj):
		tabla = self.tablaslist.currentText()
		columna = obj.text()
		self.diccionario_permisos[self.accioneslist.currentText()][tabla][columna] = obj.isChecked()
		if self.accioneslist.currentText() == 'Escritura':
			if tabla not in self.diccionario_permisos['Ver']:
				self.diccionario_permisos['Ver'][tabla] = {}
			if columna not in self.diccionario_permisos['Ver'][tabla]:
				self.diccionario_permisos['Ver'][tabla][columna] = self.diccionario_permisos['Escritura'][tabla][columna]
			if self.diccionario_permisos['Ver'][tabla][columna] == False and self.diccionario_permisos['Escritura'][tabla][columna]:
				self.diccionario_permisos['Ver'][tabla][columna] = True
		print(self.diccionario_permisos)

	#este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
	def limpiarDict(self):
		self.diccionario_permisos = {'Ver':{},
								'Escritura':{},
								' ':{}}
		self.resetCheckboxes(Form)
		self.accioneslist.setCurrentIndex(0)



	# al seleccionar guardar se llevara a cabo el comando en la base de datos
	#	ejemplo: GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO 'someuser'@'somehost';
	# seria buena opcion que aparezca un aviso una vez que se ha guardado correctamente
