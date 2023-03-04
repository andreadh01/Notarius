from functools import partial
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QTableView, QAbstractItemView,QPushButton
from PyQt5.QtCore import Qt,QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from bdConexion import obtener_conexion
import os

from pages.EditarRegistro import EditarRegistro
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/ver-tabla.ui")))



class VerTabla(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.comboBox_busqueda_presupuesto.setEnabled(False)
		self.line_edit_busqueda_presupuesto.setEnabled(False)
		self.setupTableList(self)
		self.setupTable(self)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableslist.itemSelectionChanged.connect(partial(self.setupTable,self))
		self.comboBox_busqueda_presupuesto.currentTextChanged.connect(self.busqueda)
		# self.line_edit_busqueda_presupuesto.textChanged.connect(self.busqueda)


	# en este metodo se agregan las tablas disponibles para el usuario a una lista	
	def setupTableList(self,Form):
		lista_tablas = getListaTablas()
		print(lista_tablas)
		self.tableslist.addItems(lista_tablas)
		self.tableslist.setCurrentRow(0)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self,Form):
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(0)
		tabla_name = self.tableslist.currentItem().text()
		self.bloquearBusqueda(tabla_name)
		permisos = getPermisos(tabla_name)
		user, pwd = getUsuarioLogueado()
		print("COLUMNAS DICT")
		print(permisos["SELECT"])
		conn = obtener_conexion(user,pwd)
		select = permisos["SELECT"]
		query = f"SELECT {select} FROM {tabla_name}"
		cur = conn.cursor(dictionary=True)
		cur.execute(query)
		tabla = cur.fetchall()
		cur.close()
		conn.close()
		columnas = select.split(',')
		header = ["Modificar"]+columnas if permisos["UPDATE"] != '' else columnas
			
		self.tableWidget.setColumnCount(len(header))
		self.tableWidget.setHorizontalHeaderLabels(header)

		for dic in tabla:
			col = 0
			rows = self.tableWidget.rowCount()
			self.tableWidget.setRowCount(rows + 1)
			# se agrega un boton modificar que al hacer clic mandara a la pagina modificar registro
			if permisos["UPDATE"] != '':
				col = 1
				button = self.createButton(self)
				self.tableWidget.setCellWidget(rows,0,button)
				button.clicked.connect(lambda *args, self=self, row=rows, tabla=tabla_name, col=columnas[0]: self.changePage(self,row,tabla, col))
			for val in dic.values():
				self.tableWidget.setItem(rows, col, QTableWidgetItem(str(val)))
				col +=1
		self.tableWidget.resizeColumnsToContents()
		self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
	
	def createButton(self, Form):
		button = QPushButton(self.tableWidget)
		button.setObjectName("modificar")
		button.setText("Modificar")
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
	
	def changePage(self, Form, row,tabla, col):
		index = self.tableWidget.item(row,1).text()
		editar = EditarRegistro()
		self.parent().addWidget(editar)
		self.parent().findChild(EditarRegistro).getRegistro(editar, index, tabla, col)
		self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(EditarRegistro)))
  
	def bloquearBusqueda(self, table_name:str):
		if table_name == 'presupuesto' or table_name == 'escritura' or table_name == 'juridico':
			self.comboBox_busqueda_presupuesto.setEnabled(True)
			self.line_edit_busqueda_presupuesto.setEnabled(True)
		else:
			self.comboBox_busqueda_presupuesto.setEnabled(False)
			self.line_edit_busqueda_presupuesto.setEnabled(False)

	#esta función crea el table view, esta funcion se encargará de obtener el valor del combobox y de ejecutar el proceso de busqueda
	def busqueda(self):

		comboValue = self.comboBox_busqueda_presupuesto.currentText()
		tabla_name = self.tableslist.currentItem().text()
		if comboValue == "no_presupuesto":
			conn = obtener_conexion()
			curdict = conn.cursor(dictionary=True)
			cur = conn.cursor()
			query1 = f"SELECT *  FROM {tabla_name};"
			cur.execute(query1)
			contenido_tabla = cur.fetchall()
			query2 = f"DESCRIBE {tabla_name}"
			cur.execute(query2)
			headers_notFiltered = cur.fetchall()
			headers = []
			for items in headers_notFiltered:
				headers.append(items[0])

			if self.tableWidget != None:
				self.tableWidget.deleteLater()
				self.tableWidget = None

			contenido_tabla2 = contenido_tabla.copy()
			model = QStandardItemModel(len(contenido_tabla),len(contenido_tabla2.pop()))
			model.setHorizontalHeaderLabels(headers)
			for row, tupla in enumerate(contenido_tabla):
				for column, field in enumerate(tupla):
					field = str(field)
					item = QStandardItem(field)
					model.setItem(row, column, item)
			filter_proxy_model = QSortFilterProxyModel()
			filter_proxy_model.setSourceModel(model)
			filter_proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
			filter_proxy_model.setFilterKeyColumn(0)

			self.line_edit_busqueda_presupuesto.textChanged.connect(filter_proxy_model.setFilterRegExp)

			table=QTableView()
			table.setStyleSheet('font-size: 15px;')
			table.setModel(filter_proxy_model)
			
			self.horizontalLayout.addWidget(table)

		if comboValue == "":
			if self.QTableView != None:
				self.QTableView.deleteLater()
				self.QTableView = None
			self.__init__()

			

		if comboValue == "proyectista":
			conn = obtener_conexion()
			curdict = conn.cursor(dictionary=True)
			cur = conn.cursor()
			query1 = f"SELECT *  FROM {tabla_name};"
			cur.execute(query1)
			contenido_tabla = cur.fetchall()
			query2 = f"DESCRIBE {tabla_name}"
			cur.execute(query2)
			headers_notFiltered = cur.fetchall()
			headers = []
			for items in headers_notFiltered:
				headers.append(items[0])

			if self.tableWidget != None:
				self.tableWidget.deleteLater()
				self.tableWidget = None


			contenido_tabla2 = contenido_tabla.copy()
			model = QStandardItemModel(len(contenido_tabla),len(contenido_tabla2.pop()))
			model.setHorizontalHeaderLabels(headers)
			for row, tupla in enumerate(contenido_tabla):
				for column, field in enumerate(tupla):
					field = str(field)
					item = QStandardItem(field)
					model.setItem(row, column, item)
			filter_proxy_model = QSortFilterProxyModel()
			filter_proxy_model.setSourceModel(model)
			filter_proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
			filter_proxy_model.setFilterKeyColumn(1)

			self.line_edit_busqueda_presupuesto.textChanged.connect(filter_proxy_model.setFilterRegExp)

			table=QTableView()
			table.setStyleSheet('font-size: 15px;')
			table.setModel(filter_proxy_model)
			
			self.horizontalLayout.addWidget(table)
			
