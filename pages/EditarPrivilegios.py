from PyQt5 import uic,QtWidgets,QtCore
import os
from bdConexion import obtener_conexion
from functools import partial
from usuarios import  getPermisos, getTablaRelacionada, getUsuarioLogueado, getValoresTabla
from deployment import getBaseDir


base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','editar-privilegios.ui'))


class EditarPrivilegios(Base, Form):
	checkboxList = []
	foreign_keys = {}
	diccionario_permisos = {'read':{},
							'write':{}}
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		# se mandan llamar los metodos al correr el programa
		self.setupUsers(self)
		self.setupTables(self)
		#self.otorgarPermisosForaneas()
		self.setupColumns(self)
		self.llavesForaneas()
		self.checkBoxAllVer.stateChanged.connect(partial(self.checkAll,"read"))
		self.checkBoxAllEscribir.stateChanged.connect(partial(self.checkAll,"write"))
		self.button_guardar.clicked.connect(self.guardarCambios)
		self.pushButton_cancelar.clicked.connect(self.reset)
		# cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
		#self.usuarioslist.currentTextChanged.connect(self.limpiarDict)
		self.usuarioslist.currentTextChanged.connect(self.showGrants)
		self.tablaslist.currentTextChanged.connect(self.setupColumns)
		#self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
  

	def llavesForaneas(self):
		conn = obtener_conexion()
		cur = conn.cursor()
		cur.execute("SELECT TABLE_NAME,COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE CONSTRAINT_SCHEMA = 'notarius' AND REFERENCED_TABLE_NAME IS NOT NULL")
		for table_name, column_name, referenced_table_name, referenced_column_name in cur:
			if table_name not in self.foreign_keys:
				self.foreign_keys[table_name] = []
			self.foreign_keys[table_name].append((column_name,referenced_table_name, referenced_column_name))
		cur.close()
		conn.close()

	def showGrants(self):
		self.checkBoxAllVer.setChecked(False)
		self.checkBoxAllEscribir.setChecked(False)
		self.limpiarDict()
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		usuario_seleccionado = self.usuarioslist.currentText()
		query=f"SHOW GRANTS FOR '{usuario_seleccionado}'@'localhost';"
		if usuario_seleccionado != '': 
			cur.execute(query)
			permisos = cur.fetchall()
			lista_permisos = [permisos[0] for permisos in permisos[1:]]
			self.limpiar_lista_permisos(lista_permisos)
			cur.close()
			conn.close()
		
	
	def limpiar_lista_permisos(self,lista_permisos):
		for texto in lista_permisos:
			subcadena_insert = ""
			subcadena_select = ""
			select_i = texto.find("SELECT")
			insert_i = texto.find("INSERT")
			notarius_i = texto.find("notarius")
			to_i = texto.find("TO")

			nombre_tabla = texto[notarius_i+11:to_i-2]
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

	#PONER AQUI LO DE CHECKED BOX DE LLAVE FORANEA
	def ingresar_datos_diccionario(self,permiso_select,permiso_insert):
		
		if len(permiso_select) > 2:
			columnas = permiso_select[1].split(",")
			
			for columna in columnas:
				if permiso_select[2] not in self.diccionario_permisos['read']:
					self.diccionario_permisos['read'][permiso_select[2]] = {}
				self.diccionario_permisos['read'][permiso_select[2]][columna] = True
		if len(permiso_insert) > 2:
			columnas = permiso_insert[1].split(",")

			for columna in columnas:
				if permiso_insert[2] not in self.diccionario_permisos['write']:
					self.diccionario_permisos['write'][permiso_insert[2]] = {}
				self.diccionario_permisos['write'][permiso_insert[2]][columna] = True
				#tabla_principal = permiso_insert[2]
				#columna = columna_principal


				# #  Aquí
				# for tabla_p, lista_foreignkey in self.foreign_keys.items():
				# 	lista_tabla_col = lista_foreignkey[0]
				# 	columna_p = lista_tabla_col[0]
				# 	tabla_secundaria = lista_tabla_col[1]
				# 	columna_secundaria = lista_tabla_col[2]
				# 	if tabla_principal == tabla_p:
				# 		if columna == columna_p:
				# 			if tabla_secundaria not in self.diccionario_permisos['write']:
				# 				self.diccionario_permisos['write'][tabla_secundaria] = {}
				# 			self.diccionario_permisos['write'][tabla_secundaria][columna_secundaria] = True


	def guardarCambios(self):
		usuario_seleccionado = self.usuarioslist.currentText()
		self.generarGrants(usuario_seleccionado)
		self.checkBoxAllVer.setChecked(False)
		self.checkBoxAllEscribir.setChecked(False)
		self.mensaje.setText("Guardado exitosamente")
		self.checkThreadTimer = QtCore.QTimer(self)
		self.checkThreadTimer.setInterval(3000)
		self.checkThreadTimer.start()
		self.checkThreadTimer.timeout.connect(partial(self.mensaje.setText,''))
				
	def checkAll(self,tipo_permiso):
		for checkbox in self.checkboxList:
			permiso = checkbox.objectName()
			permiso = permiso.split('-')[1]
			if tipo_permiso == permiso:
				checkbox.setChecked(True)


	# en esta funcion se van a cargar los usuarios de la base de datos al combobox de usuarios
	def setupUsers(self, Form):
		usuarios = getValoresTabla('usuario')
		lista_usuarios = [usu['nombre_usuario'] for usu in usuarios]

		self.usuarioslist.addItems(lista_usuarios)
		if len(lista_usuarios)>0: self.showGrants()

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
	def setupTables(self, Form):
		lista_tablas = ['tabla_final','desgloce_ppto','pagos','depositos','fechas_rpp','fechas_catastro_td','fechas_catastro_calif']
		self.tablaslist.addItems(lista_tablas)
		self.tablaslist.setCurrentIndex(0)
	
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
	def setupColumns(self, Form):
		
		# se eliminan los combobox anteriores
		self.resetCombobox(self)		
		if self.tablaslist.currentIndex() == 0: return
		tabla_seleccionada = self.tablaslist.currentText()
		columnas = getPermisos(tabla_seleccionada)["read"]
		lista_columnas = columnas.split(',')		
		# aqui se crea el widget del checkbox y se agrega al gui
		for i, col in enumerate(lista_columnas):
			name_ver = f"{col}-read"
			name_escritura = f"{col}-write"
			setattr(self, name_ver, QtWidgets.QCheckBox(Form))
			setattr(self, name_escritura, QtWidgets.QCheckBox(Form))
			checkbox_ver = getattr(self,name_ver)
			checkbox_ver.setStyleSheet("\n"
			"font: 75 14pt;\n"
			"color: white;")
			checkbox_ver.setObjectName(name_ver)
			
			checkbox_escritura = getattr(self,name_ver)
			checkbox_escritura.setText(col)
			checkbox_escritura = getattr(self,name_escritura)
			checkbox_escritura.setStyleSheet("\n"
			"font: 75 14pt;\n"
			"color: white;")
			checkbox_escritura.setObjectName(name_escritura)
			checkbox_escritura.setText(col)
			# permisos de read
			self.verLayout.addWidget(checkbox_ver)
			# permisos de write
			self.escribirLayout.addWidget(checkbox_escritura)
			self.checkboxList.append(checkbox_ver)
			self.checkboxList.append(checkbox_escritura)
			
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
		query=f"SELECT rol FROM usuario WHERE nombre_usuario='{nombre_usuario}'"
		cur.execute(query)
		rol = cur.fetchall()
		rol = rol[0][0]
		for llave,accion in self.diccionario_permisos.items():
			for nombre_tabla,columnas in accion.items():
				for nombre_columna,checked in columnas.items():
					if checked:
						if llave == 'read':
							query=f"GRANT SELECT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
							cur.execute(query)
						else:
							#Aqui se puede dar el permiso
							query=f"GRANT INSERT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
							cur.execute(query)
							query=f"GRANT UPDATE ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
							cur.execute(query)

							#Aquí se le ponen los permisos de escritura a las llaves foráneas cuando se guarda
							# for tabla_principal, lista_foreignkey in self.foreign_keys.items():
							# 	lista_tabla_col = lista_foreignkey[0]
							# 	columna_principal = lista_tabla_col[0]
							# 	tabla_secundaria = lista_tabla_col[1]
							# 	columna_secundaria = lista_tabla_col[2]

							# 	if tabla_principal == nombre_tabla:
							# 		if columna_principal == nombre_columna:
							# 			query=f"GRANT INSERT ({columna_secundaria}) ON notarius.{tabla_secundaria} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
							# 			cur.execute(query)
							# 			query=f"GRANT UPDATE ({columna_secundaria}) ON notarius.{tabla_secundaria} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
							# 			cur.execute(query)	
						if rol == 'admin':
							query=f"GRANT ALL PRIVILEGES ON mysql.* TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
							cur.execute(query)

		cur.close()
		conn.close()

	def agregarLlavesForaneas(self,nombre_tabla,nombre_columna,nombre_usuario,cur):
		# subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
		try:
			lista_tabla_col = self.foreign_keys[nombre_tabla]
			for item in lista_tabla_col:
				columna_principal = item[0]
				tabla_secundaria = item[1]
				columna_secundaria = item[2]
				# if nombre_columna in subtablas.keys():
				#      subtabla = subtablas[nombre_columna]
				#      query=f"GRANT SELECT ({subtabla[1]}) ON notarius.{subtabla[0]} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
				#      cur.execute(query)
				if columna_principal == nombre_columna:
					query=f"GRANT SELECT ({columna_secundaria}) ON notarius.{tabla_secundaria} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
					cur.execute(query)
		except KeyError as error:
			#print("La tabla no tiene llaves foraneas")
			return

	def resetCombobox(self, Form):
		for obj in self.checkboxList:
			self.gridLayout.removeWidget(obj)
			obj.deleteLater()
			del obj
		self.checkboxList = []

	# este metodo le asigna un metodo a cada checkbox que ejecuta guardar_opcion al ser activado/desactivado - Jared
	def connectCheckboxes(self, Form):
		for obj in self.checkboxList:
			obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	# este metodo revisa el diccionario de permisos y activa aquellas columnas que estan guardadas como true -Jared
	def resetCheckboxes(self, Form):
		for permiso in self.diccionario_permisos:
			for obj in self.checkboxList:
				permiso = obj.objectName()
				permiso = permiso.split('-')[1]
				if self.tablaslist.currentText() not in self.diccionario_permisos[permiso]:
					self.diccionario_permisos[permiso][self.tablaslist.currentText()] = {}
				if obj.text() in self.diccionario_permisos[permiso][self.tablaslist.currentText()]:
					obj.setChecked(self.diccionario_permisos[permiso][self.tablaslist.currentText()][obj.text()])
				else:
					obj.setChecked(False)

	'''
	En este metodo se guarda si el checkbox fue activado o no.
	El diccionario se compone por:
	Acciones (read, write) -> Nombre de tabla -> Columna: True/False
	-Jared
	'''
	def guardar_opcion(self, obj):
		subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
		tablas_no_validas = ['no_facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp','desgloce_ppto','pagos','depositos','usuario']
		permiso = obj.objectName()
		permiso = permiso.split('-')[1]
		tabla = self.tablaslist.currentText()
		columna = obj.text()
		self.diccionario_permisos[permiso][tabla][columna] = obj.isChecked()
		if permiso == 'write':
			if tabla not in self.diccionario_permisos['read']:
				self.diccionario_permisos['read'][tabla] = {}
			if columna not in self.diccionario_permisos['read'][tabla]:
				self.diccionario_permisos['read'][tabla][columna] = self.diccionario_permisos['write'][tabla][columna]
			if self.diccionario_permisos['read'][tabla][columna] == False and self.diccionario_permisos['write'][tabla][columna]:
				self.diccionario_permisos['read'][tabla][columna] = True
		tabla_relacionada = getTablaRelacionada(columna)

		if columna in subtablas.keys():
			subtabla = subtablas[columna][0]
			columna_subtabla = subtablas[columna][1].split(',')
			columna_subtabla.append('id')
			if "fecha" in columna: columna_subtabla.append('id_fechas') 
			else: columna_subtabla.append('id_relacion')
			if subtabla not in self.diccionario_permisos[permiso]:
				self.diccionario_permisos[permiso][subtabla] = {}
			for col in columna_subtabla:
				if subtabla not in self.diccionario_permisos[permiso]:
					self.diccionario_permisos[permiso][subtabla] = {}
				elif col not in self.diccionario_permisos[permiso][subtabla]: 
					self.diccionario_permisos[permiso][subtabla][col] = True
				elif obj.isChecked()  and columna not in 'facturas':
					self.diccionario_permisos[permiso][subtabla][col] = self.diccionario_permisos[permiso][subtabla][col]
				else:
					self.diccionario_permisos[permiso][subtabla][col] = obj.isChecked()

		for key in subtablas:
			subtabla = subtablas[key][0]
			columna_subtabla = subtablas[key][1].split(',')
			if subtabla == tabla:
				for col in columna_subtabla:
					if self.diccionario_permisos[permiso][subtabla][col] == False:
						self.diccionario_permisos[permiso]['tabla_final'][key] = False
					else:
						self.diccionario_permisos[permiso]['tabla_final'][key] = True
						break

		for registro in tabla_relacionada:
			for tabla_val in registro.values():
				if tabla_val == tabla or tabla_val in tablas_no_validas: continue
				if tabla_val not in self.diccionario_permisos[permiso]:
					self.diccionario_permisos[permiso][tabla_val] = {}
				self.diccionario_permisos[permiso][tabla_val][columna] = obj.isChecked()
				if permiso == 'write':
					if tabla_val not in self.diccionario_permisos['read']:
						self.diccionario_permisos['read'][tabla_val] = {}
					if columna not in self.diccionario_permisos['read'][tabla_val]:
						self.diccionario_permisos['read'][tabla_val][columna] = self.diccionario_permisos['write'][tabla_val][columna]
					if self.diccionario_permisos['read'][tabla_val][columna] == False and self.diccionario_permisos['write'][tabla_val][columna]:
						self.diccionario_permisos['read'][tabla_val][columna] = obj.isChecked()
					if self.diccionario_permisos['read'][tabla_val][columna] == False and self.diccionario_permisos['write'][tabla_val][columna] == False:
						self.diccionario_permisos['read'][tabla_val][columna] = obj.isChecked()
				try:
					lista_foreignkey = self.foreign_keys[tabla_val]
					lista_tabla_col = lista_foreignkey[0]
					columna_p = lista_tabla_col[0]
					tabla_secundaria = lista_tabla_col[1]
					columna_secundaria = lista_tabla_col[2]
					if tabla_val not in self.diccionario_permisos[permiso]:
						self.diccionario_permisos[permiso][tabla_val] = {}
					self.diccionario_permisos[permiso][tabla_val][columna_p] = obj.isChecked()

					if columna == columna_p:
						if tabla_secundaria not in self.diccionario_permisos[permiso]:
							self.diccionario_permisos[permiso][tabla_secundaria] = {}
						self.diccionario_permisos[permiso][tabla_secundaria][columna_secundaria] = obj.isChecked()
				except KeyError as error:
					#print("La tabla no tiene llaves foraneas")
					return
		self.resetCheckboxes(self)

	#este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
	def limpiarDict(self):
		self.diccionario_permisos = {'read':{},
								'write':{}}
		self.tablaslist.setCurrentIndex(0)
		self.resetCheckboxes(Form)
		#self.accioneslist.setCurrentIndex(0)

	def reset(self):
		self.checkBoxAllVer.setChecked(False)
		self.checkBoxAllEscribir.setChecked(False)
		self.diccionario_permisos = {'read':{},
								'write':{}}
		self.showGrants()

	def reject(self) -> None:
		return
	# al seleccionar guardar se llevara a cabo el comando en la base de datos
	#	ejemplo: GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO 'someuser'@'somehost';
	# seria buena opcion que aparezca un aviso una vez que se ha guardado correctamente