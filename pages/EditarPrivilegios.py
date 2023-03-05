from PyQt5 import uic,QtWidgets,QtCore
import os
from bdConexion import obtener_conexion
from functools import partial

from usuarios import getListaTablas, getPermisos, getUsuarioLogueado, getValoresTabla

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-privilegios.ui")))


class EditarPrivilegios(Base, Form):
	cols = []
	diccionario_permisos = {'ver':{},
							'escritura':{}}
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		# se mandan llamar los metodos al correr el programa
		self.setupUsers(self)
		self.setupTables(self)
		self.setupColumns(self)
		
		

		self.button_guardar.clicked.connect(self.guardarCambios)
		self.pushButton_cancelar.clicked.connect(self.reset)
		# cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
		#self.usuarioslist.currentTextChanged.connect(self.limpiarDict)
		self.usuarioslist.currentTextChanged.connect(self.showGrants)
		self.tablaslist.currentTextChanged.connect(self.setupColumns)
		#self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
  
	def showGrants(self):
		self.limpiarDict()
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
				if permiso_select[2] not in self.diccionario_permisos['ver']:
					self.diccionario_permisos['ver'][permiso_select[2]] = {}
				self.diccionario_permisos['ver'][permiso_select[2]][columna] = True
		if len(permiso_insert) > 2:
			columnas = permiso_insert[1].split(",")
			for columna in columnas:
				if permiso_insert[2] not in self.diccionario_permisos['escritura']:
					self.diccionario_permisos['escritura'][permiso_insert[2]] = {}
				self.diccionario_permisos['escritura'][permiso_insert[2]][columna] = True

	def guardarCambios(self):
		usuario_seleccionado = self.usuarioslist.currentText()
		self.generarGrants(usuario_seleccionado)
		self.mensaje.setText("Guardado exitosamente")
		self.checkThreadTimer = QtCore.QTimer(self)
		self.checkThreadTimer.setInterval(3000)
		self.checkThreadTimer.start()
		self.checkThreadTimer.timeout.connect(partial(self.mensaje.setText,''))
				

	# en esta funcion se van a cargar los usuarios de la base de datos al combobox de usuarios
	def setupUsers(self, Form):
		# user, pwd = getUsuarioLogueado()
		# conn = obtener_conexion(user,pwd)
		# cur = conn.cursor()
		# query = 'SELECT nombre_usuario FROM usuario'
		# cur.execute(query)
		# usuarios = cur.fetchall()
		# cur.close()
		# conn.close()
		usuarios = getValoresTabla('usuario')
		lista_usuarios = [usu['nombre_usuario'] for usu in usuarios]

		self.usuarioslist.addItems(lista_usuarios)
		if len(lista_usuarios)>0: self.showGrants()

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
	def setupTables(self, Form):
		lista_tablas = getListaTablas()
		self.tablaslist.addItems(lista_tablas)
		self.tablaslist.setCurrentIndex(0)
	
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
	def setupColumns(self, Form):
		# se eliminan los combobox anteriores
		self.resetCombobox(self)		
		if self.tablaslist.currentIndex() == 0: return
		tabla_seleccionada = self.tablaslist.currentText()
		columnas = getPermisos(tabla_seleccionada)["ver"]
		lista_columnas = columnas.split(',')		
		# aqui se crea el widget del checkbox y se agrega al gui
		for i, col in enumerate(lista_columnas):
			name_ver = f"acceso_{i}_ver"
			name_escritura = f"acceso_{i}_escritura"
			setattr(self, name_ver, QtWidgets.QCheckBox(Form))
			setattr(self, name_escritura, QtWidgets.QCheckBox(Form))
			checkbox_ver = getattr(self,name_ver)
			checkbox_ver.setStyleSheet("\n"
			"font: 75 16pt;\n"
			"color: white;")
			checkbox_ver.setObjectName(name_ver)
			
			checkbox_escritura = getattr(self,name_ver)
			checkbox_escritura.setText(col)
			checkbox_escritura = getattr(self,name_escritura)
			checkbox_escritura.setStyleSheet("\n"
			"font: 75 16pt;\n"
			"color: white;")
			checkbox_escritura.setObjectName(name_escritura)
			checkbox_escritura.setText(col)
			# permisos de ver
			self.verLayout.addWidget(checkbox_ver)
			# permisos de escritura
			self.escribirLayout.addWidget(checkbox_escritura)
			self.cols.append(checkbox_ver)
			self.cols.append(checkbox_escritura)
		# aqui se le asignan los metodos a cada checkbox y se llena el diccionario con las columnas de la tabla - Jared
		self.connectCheckboxes(self)
		self.resetCheckboxes(self)

	def generarGrants(self,nombre_usuario):
		query = f""
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		#query=f"REVOKE ALL PRIVILEGES, GRANT OPTION FROM '{nombre_usuario}'@'localhost';"
		#cur.execute(query)
		for llave,accion in self.diccionario_permisos.items():
			for nombre_tabla,columnas in accion.items():
				for nombre_columna,checked in columnas.items():
					if checked:
						if llave == 'ver':
							query=f"GRANT SELECT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
							cur.execute(query)
						elif llave == 'escritura':
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
				permiso = obj.objectName()
				permiso = permiso.split('_')[2]
				if self.tablaslist.currentText() not in self.diccionario_permisos[permiso]:
					self.diccionario_permisos[permiso][self.tablaslist.currentText()] = {}
				if obj.text() in self.diccionario_permisos[permiso][self.tablaslist.currentText()]:
					obj.setChecked(self.diccionario_permisos[permiso][self.tablaslist.currentText()][obj.text()])
				else:
					obj.setChecked(False)

	'''
	En este metodo se guarda si el checkbox fue activado o no.
	El diccionario se compone por:
	Acciones (ver, escritura) -> Nombre de tabla -> Columna: True/False
	-Jared
	'''
	def guardar_opcion(self, obj):
		tabla = self.tablaslist.currentText()
		columna = obj.text()
		permiso = obj.objectName()
		permiso = permiso.split('_')[2]
		self.diccionario_permisos[permiso][tabla][columna] = obj.isChecked()
		if permiso == 'escritura':
			if tabla not in self.diccionario_permisos['ver']:
				self.diccionario_permisos['ver'][tabla] = {}
			if columna not in self.diccionario_permisos['ver'][tabla]:
				self.diccionario_permisos['ver'][tabla][columna] = self.diccionario_permisos['escritura'][tabla][columna]
			if self.diccionario_permisos['ver'][tabla][columna] == False and self.diccionario_permisos['escritura'][tabla][columna]:
				self.diccionario_permisos['ver'][tabla][columna] = True
		print(self.diccionario_permisos)

	#este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
	def limpiarDict(self):
		self.diccionario_permisos = {'ver':{},
								'escritura':{}}
		self.tablaslist.setCurrentIndex(0)
		self.resetCheckboxes(Form)
		#self.accioneslist.setCurrentIndex(0)

	def reset(self):
		self.diccionario_permisos = {'ver':{},
								'escritura':{}}
		self.showGrants()

	# al seleccionar guardar se llevara a cabo el comando en la base de datos
	#	ejemplo: GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO 'someuser'@'somehost';
	# seria buena opcion que aparezca un aviso una vez que se ha guardado correctamente