from functools import partial
from PyQt5 import uic
import pandas as pd
#python(suversion) -m pip install pandas
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QTableView, QAbstractItemView,QPushButton
from PyQt5.QtCore import Qt,QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from bdConexion import obtener_conexion
import os

from pages.EditarRegistro import EditarRegistro
from usuarios import getListaTablas, getPermisos, getValoresTabla

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/ver-tabla.ui")))



class VerTabla(Base, Form):
	def __init__(self, parent=None):
		self.flag = False
		self.flagTabla = False
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.setupTableList(self)
		self.setupTable(self)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.pushButton_2.clicked.connect(self.escribirCSV)
		self.tableslist.itemSelectionChanged.connect(partial(self.setupTable,self))

	def selectTable(self,Form,tabla):
		#print("resultado")
		item = self.tableslist.findItems(tabla,Qt.MatchExactly)
		index =self.tableslist.row(item[0])
		self.tableslist.setCurrentRow(index)
		#print(self.tableslist.row(item[0]))
		#self.tableslist.setCurrentRow(0)

	# en este metodo se agregan las tablas disponibles para el usuario a una lista	
	def setupTableList(self,Form):
		lista_tablas = getListaTablas()
		self.tableslist.addItems(lista_tablas)
		if self.tableslist.currentRow() == -1: self.tableslist.setCurrentRow(0)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self,Form):
		self.tableWidget.show()
		self.deactivateLineEdit()
		#verificar si hay algún objeto QTableView en el layout
		if hasattr(self, 'tableView'):
			self.tableView.hide()
			self.flag = False

		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(0)
		tabla_name = self.tableslist.currentItem().text()
		permisos = getPermisos(tabla_name)
		select = permisos["Ver"]
		tabla = getValoresTabla(tabla_name)
		#si puede encontrar una manera menos fea de obtener esto en ves de hacer esta variable globar que toma el dic actual dense porfavor. atte; gracida
		global Diccionario
		Diccionario = tabla
		columnas = select.split(',')
		header = ["Editar"]+columnas if permisos["Escritura"] != '' else columnas
		self.tableWidget.setColumnCount(len(header))
		self.tableWidget.setHorizontalHeaderLabels(header)
		
		for dic in tabla:
			col = 0
			rows = self.tableWidget.rowCount()
			self.tableWidget.setRowCount(rows + 1)
			# se agrega un boton modificar que al hacer clic mandara a la pagina modificar registro
			if permisos["Escritura"] != '':
				col = 1
				button = self.createButton(self)
				self.tableWidget.setCellWidget(rows,0,button)
				button.clicked.connect(lambda *args, self=self, row=rows, tabla=tabla_name: self.changePage(self,row,tabla))
			for val in dic.values():
				self.tableWidget.setItem(rows, col, QTableWidgetItem(str(val)))
				col +=1
		self.tableWidget.resizeColumnsToContents()
		self.busqueda()
		# self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		#self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
		#header = self.tableWidget.horizontalHeader()       
		#header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
		#header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
		#header.setSectionResizeMode(2, QHeaderView.ResizeToContents)self.busqueda()
		
		
		
		
	
	def createButton(self, Form):
		button = QPushButton(self.tableWidget)
		button.setObjectName("editar")
		button.setText("Editar")
		button.setStyleSheet("QPushButton {\n"
"background-color: #d3c393;\n"
"color: rgb(131, 112, 82);\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(116, 91, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(103, 80, 41);\n"
"    color: rgb(255, 255, 255);\n"
"}")
		return button

	# en esta funcion se van a ordenar las columnas en el diccionario para crear diccionario de diccionarios
	# def crearDiccionario(self, diccionario:dict, tabla_seleccionada:str, campo_seleccionado:int)->dict:
	# 	# conexion a base de datos
	# 	conn = obtener_conexion()
	# 	cur = conn.cursor()
	# 	query1 = f"SELECT *  FROM {tabla_seleccionada};"
	# 	cur.execute(query1)
	# 	contenido_tabla = cur.fetchall()
	# 	for i,items in enumerate(contenido_tabla):
	# 		diccionario[contenido_tabla[i][campo_seleccionado]] = items
	# 	cur.close()
	# 	conn.close()
	# 	return diccionario
	
	def changePage(self, Form, row,tabla):
		index = self.getIndexCell(row)
		print('INDICEEEE ')
		print(index)
		editar = EditarRegistro()
		self.parent().addWidget(editar)
		self.parent().findChild(EditarRegistro).getRegistro(editar, index, tabla, 'id')
		self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(EditarRegistro)))
  
	def getIndexCell(self, row):
		headercount = self.tableWidget.columnCount()
		for x in range(headercount):
			headertext = self.tableWidget.horizontalHeaderItem(x).text()
			print('header')
			print(headertext)
			if 'id' == headertext:
				cell = self.tableWidget.item(row, x).text()  # get cell at row, col
				return cell
	
	# def bloquearBusqueda(self, table_name:str):
	# 	if table_name == 'presupuesto' or table_name == 'escritura' or table_name == 'juridico':
	# 		self.comboBox_busqueda_presupuesto.setEnabled(True)
	# 		self.line_edit_busqueda_presupuesto.setEnabled(True)
	# 	else:
	# 		self.comboBox_busqueda_presupuesto.setEnabled(False)
	# 		self.line_edit_busqueda_presupuesto.setEnabled(False)

	#esta funcion obtiene el nombre de la tabla actual seleccionada, y rellena el combobox conforme a los campos de la tabla. Después, se realiza una consulta select para obtener el contenido de la tabla y se inserta en un widget QTableView para obtener su filtrado a travez de la seleccion del campo en el combobox.
	def busqueda(self):
		self.fillCombo()
		#evento para que al presionar el botón de buscar se ejecute el metodo getTableContent()
		self.pushButton_3.clicked.connect(self.getTableContent)

	def deactivateLineEdit(self):
		#ocultar el line edit
		self.line_edit_busqueda_presupuesto.hide()

	def fillCombo(self):
		#obtener el nombre de la tabla actual
		tabla_name = self.tableslist.currentItem().text()
		#obtener la conexion a la base de datos
		conn = obtener_conexion()
		#crear un cursor para la conexion
		cur = conn.cursor()
		#crear la consulta para obtener los campos de la tabla
		query = f"DESCRIBE {tabla_name}"
		#ejecutar la consulta
		cur.execute(query)
		#obtener los campos de la tabla
		headers = cur.fetchall()
		#cerrar la conexion
		cur.close()
		conn.close()
		#limpiar el combobox
		self.comboBox_busqueda_presupuesto.clear()
		#agregar los campos al combobox
		for i in headers:
			self.comboBox_busqueda_presupuesto.addItem(i[0])

	#en el siguiente metodo se obtiene el valor del combobox para realizar una consulta que obtenga todos los registros de la tabla;
	def getTableContent(self):
		#obtener el nombre de la tabla actual
		tabla_name = self.tableslist.currentItem().text()
		#obtener el valor del combobox
		comboValue = self.comboBox_busqueda_presupuesto.currentText()
		#obtener la conexion a la base de datos
		conn = obtener_conexion()
		#crear un cursor para la conexion
		cur = conn.cursor()
		#crear la consulta para obtener todos los registros de la tabla
		query = f"SELECT *  FROM {tabla_name};"
		query2 = f"DESCRIBE {tabla_name}"
		#ejecutar la consulta
		cur.execute(query)
		#obtener los registros de la tabla
		contenido_tabla = cur.fetchall()
		#ejecutar la consulta
		cur.execute(query2)
		#obtener los encabezados de la tabla
		headers_sinFiltro = cur.fetchall()
		#cerrar la conexion
		cur.close()
		conn.close()
		#crear un modelo para el widget QTableView
		model = QStandardItemModel()
		#agregar los encabezados al modelo
		for i in headers_sinFiltro:
			model.setHorizontalHeaderItem(headers_sinFiltro.index(i),QStandardItem(i[0]))
		#agregar los registros al modelo con un boton para editar el registro
		for i,items in enumerate(contenido_tabla):
			for j in range(len(contenido_tabla[i])):
				model.setItem(i,j,QStandardItem(str(contenido_tabla[i][j])))
			model.setItem(i,len(contenido_tabla[i]),QStandardItem("Modificar"))
		
		#agregar el widget QTableView al layout
		if self.flag == False:
			#crear un nuevo widget QTableView
			self.tableView = QTableView()
			self.horizontalLayout.addWidget(self.tableView)
			self.flag=True
		#agregar el modelo al widget QTableView
		self.tableView.setModel(model)
		#agregar un evento al widget QTableView para cuando se presiona el boton de editar
		#esto lo hizo copilot y no se pa que xd o como funciona
		self.tableView.clicked.connect(lambda: self.changePage(self, self.tableWidget.currentIndex().row(), tabla_name, self.tableWidget.currentIndex().column()))
		#crear un filtro para el widget QTableView
		proxy = QSortFilterProxyModel()
		#agregar el modelo al filtro
		proxy.setSourceModel(model)
		#agregar el filtro al widget QTableView
		self.tableView.setModel(proxy)
		######Karo, ponle aqui el cambio de icono al boton de filtro######
		if self.flagTabla == False:
			self.line_edit_busqueda_presupuesto.show()
			#ocultar el widget tableWidget
			self.tableWidget.hide()
			self.tableView.show()
			self.flagTabla = True
		else:
			self.line_edit_busqueda_presupuesto.hide()
			self.tableView.hide()
			self.tableWidget.show()
			self.flagTabla = False
		#obtener una lista enumerada de los campos de la tabla
		headers = list(enumerate([i[0] for i in headers_sinFiltro]))
		print(headers)
		#agregar un evento al filtro para cuando se cambia el valor del combobox, comparar el valor del combobox con la lista de campos de la tabla para obtener el indice del campo seleccionado
		for items in headers:
			if comboValue == items[1]:
				proxy.setFilterKeyColumn(items[0])
		#agregar un evento al filtro para cuando se escribe en el line edit
		proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
		#agregar un evento al filtro para cuando se escribe en el line edit
		self.line_edit_busqueda_presupuesto.textChanged.connect(proxy.setFilterRegExp)
	def escribirCSV(self,d,b):
		print(d)
		print(b)
		print(Diccionario)
		tabla = self.tableslist.currentItem().text()
		if bool(Diccionario)==True:
			try:
				df=pd.DataFrame.from_dict(Diccionario)
				df.to_csv(rf'{tabla}',index=False,header=True)		
			except IOError:
				print("no")