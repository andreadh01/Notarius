from datetime import date
from functools import partial
from PyQt5 import uic
import pandas as pd
#python(suversion) -m pip install pandas
from PyQt5.QtWidgets import QHeaderView, QTableView, QAbstractItemView,QPushButton,QMessageBox,QScrollBar,QItemDelegate
from PyQt5.QtCore import Qt,QSortFilterProxyModel, QTimer
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from bdConexion import obtener_conexion
import os

from pages.EditarRegistro import EditarRegistro
from usuarios import getListaTablas, getPermisos, getValoresTabla
from deployment import getBaseDir

base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','ver-tabla.ui'))


headers = []

class Tablas(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		#self.setupTableList(self)
		self.setupTable(self)
		self.mensaje.hide()
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.pushButton_2.clicked.connect(self.escribirCSV)
		#self.tableslist.currentIndexChanged.connect(partial(self.setupTable,self))

	# def selectTable(self,Form,tabla):
	# 	#print("resultado")
	# 	item = self.tableslist.findText(tabla,Qt.MatchExactly)
	# 	#index =self.tableslist.row(item[0])
	# 	self.tableslist.setCurrentIndex(item)
	# 	#print(self.tableslist.row(item[0]))
	# 	#self.tableslist.setCurrentRow(0)

	# en este metodo se agregan las tablas disponibles para el usuario a una lista	
	# def setupTableList(self,Form):
	# 	lista_tablas = getListaTablas()
	# 	self.tableslist.addItems(lista_tablas)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self,Form):
		#tabla_name = self.tableslist.currentText()
		tabla_name = 'tabla_final'
		#obtener los permisos del usuario para la tabla seleccionada
		permisos = getPermisos(tabla_name)
		select = permisos["read"]
		tabla = getValoresTabla(tabla_name)
		if permisos["write"] == '': self.botonModificar.hide()
		#si puede encontrar una manera menos fea de obtener esto en ves de hacer esta variable globar que toma el dic actual dense porfavor. atte; gracida
		global Diccionario
		Diccionario = tabla
		header = select.split(',')
		model = QStandardItemModel()
		#agregar los encabezados al modelo
		for i, item in enumerate(header):
			model.setHorizontalHeaderItem(i,QStandardItem(item))		

		#agregar el modelo al widget QTableView
		self.tableView.setModel(model)
		#agregar los registros al modelo con un boton para editar el registro
		list_nested_tables = ['facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp,desgloce_ppto','pagos','depositos'] #lista de tablas que deben ser anidadas en los respectivos campos

		#crear un objeto qitemdelegate para celdas
		delegate = QItemDelegate(self)
		#agregar el objeto al widget QTableView
		self.tableView.setItemDelegate(delegate)
		
		for i, registro in enumerate(tabla):
			for j, (col, val) in enumerate(registro.items()):
				if val is None: val =''
				if col in list_nested_tables:
					#si el campo es de una de las tablas en la lista, entonces se guarda su index
					#para poder acceder a ella mas facilmente
					index = model.index(i,j)
					if col == 'pagos':
						col = 'pagos_presupuesto'
					if col == 'depositos':
						col = 'depositos_presupuesto'
					subtable = self.setupSubTable(i,j,col)
					subtable.setParent(self.tableView)
					self.tableView.setIndexWidget(index,subtable)
				else:
					model.setItem(i,j,QStandardItem(str(val)))
		
		


		#crear un filtro para el widget QTableView
		self.proxy = QSortFilterProxyModel()
		#agregar el modelo al filtro
		self.proxy.setSourceModel(model)
		#agregar el filtro al widget QTableView
		self.tableView.setModel(self.proxy)
		self.busqueda()
		#agregar un evento al filtro para cuando se escribe en el line edit
		self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
		#agregar un evento al filtro para cuando se escribe en el line edit
		self.line_edit_busqueda_presupuesto.textChanged.connect(self.proxy.setFilterRegExp)
		self.tableView.resizeColumnsToContents()
		#add horizontal scrollbar to table view widget 
		# create a scroll bar object
		scroll_bar = QScrollBar(self.tableView)
        # setting style sheet
		scroll_bar.setStyleSheet("QScrollBar:horizontal {\n"
"    border: 2px grey;\n"
"    background: white;\n"
"    height: 15px;\n"
"    margin: 0px 21px 0 21px;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"height: 0px;\n"
"width: 0px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"background: none;\n"
"height: 0px;\n"
"width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"background: none;\n"
"height: 0px;\n"
"width: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(204,204,204);\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"    border: 2px grey;\n"
"    background: white;\n"
"    height: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"    border: 2px grey;\n"
"    background: white;\n"
"    height: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: 2px grey;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:horizontal:on {\n"
"    background: rgb(102,102,102);\n"
"}")

        # setting horizontal scroll bar to it
		self.tableView.setHorizontalScrollBar(scroll_bar)
		self.tableView.horizontalHeader().setStretchLastSection(True)
	
	def setupSubTable(self,i,j,column)->QTableView:
		subtable = QTableView()
		subtable.setModel(self.setupSubTableModel(column))
		subtable.verticalHeader().setVisible(False)
		subtable.horizontalHeader().setVisible(True)
		subtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		subtable.setSelectionBehavior(QAbstractItemView.SelectRows)
		subtable.setSelectionMode(QAbstractItemView.SingleSelection)
		subtable.verticalHeader().setVisible(False)
		subtable.horizontalHeader().setVisible(False)
		subtable.horizontalHeader().setStretchLastSection(True)
		subtable.setMinimumSize(subtable.sizeHint())
		subtable.setMaximumSize(subtable.sizeHint())
		subtable.setSortingEnabled(True)
		subtable.setAlternatingRowColors(True)
		return subtable

	def setupSubTableModel(self,column)->QStandardItemModel:
		model = QStandardItemModel()
		#se ponen los headers de la tabla
		# queda pendiente model.setHorizontalHeaderLabels()
		#obtener columnas de la tabla
		tabla = getValoresTabla(column)
		#se agregan los datos de la tabla al modelo
		for i, registro in enumerate(tabla):
			model.insertRow(i)
			for j, (col, val) in enumerate(registro.items()):
				if val is None: val =''
				model.setItem(i,j,QStandardItem(str(val)))
		
		return model

	def createButton(self, Form):
		button = QPushButton(self.tableView)
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
	
	def changePage(self, Form, row,tabla):
		index = self.getIndexCell(row)
		editar = EditarRegistro()
		self.parent().addWidget(editar)
		self.parent().findChild(EditarRegistro).getRegistro(editar, index, tabla, 'id')
		self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(EditarRegistro)))
  
  #la funcion getIndexCell obtiene el valor de la celda de la tabla que se encuentra en la columna id, para luego enviarlo a la funcion getRegistro de la clase EditarRegistro
  #para obtener el registro que se desea editar y mostrarlo en el formulario de edicion de registros de la clase EditarRegistro
	def getIndexCell(self, row):
		headercount = self.tableView.model().columnCount()
		for x in range(headercount):
			headertext = self.tableView.model().headerData(x, Qt.Horizontal)
			if 'id' == headertext:
				cell = self.tableView.model().index(row, x).data()  # get cell at row, col
				return cell
	
	#esta funcion obtiene el nombre de la tabla actual seleccionada, y rellena el combobox conforme a los campos de la tabla. Después, se realiza una consulta select para obtener el contenido de la tabla y se inserta en un widget QTableView para obtener su filtrado a travez de la seleccion del campo en el combobox.
	def busqueda(self):
		self.fillCombo()
		#evento para que al presionar el botón de buscar se ejecute el metodo getTableContent()
		#self.pushButton_3.clicked.connect(self.getTableContent)
		#evento para que al presionar el boton modificar se obtenga el elemento seleccionado en el QTableView, en caso de que no se haya seleccionado ninguno, de un mensaje de error. Además, en el caso de tener seleccionado un elemento se hace un cambio de pagina para poder modificar el registro en cuestion con respecto a su id.
		self.botonModificar.clicked.connect(self.modificarRegistro)
	
	def modificarRegistro(self):
		#obtener el nombre de la tabla actual
		#tabla_name = self.tableslist.currentText()
		tabla_name = 'tabla_final'
		#obtener el id del registro seleccionado en el QTableView

		if self.tableView.selectedIndexes() == []:
			# agregar mensaje de error
			self.mensaje.show()
			self.mensaje.setText("No tiene ningun registro seleccionado para modificar")
			self.timerAndHide()
			return
		elif len(self.tableView.selectedIndexes())>1:
			self.mensaje.show()
			self.mensaje.setText("Elija solamente un campo para modificar el registro")
			self.timerAndHide()
			return
		else:
			row = self.tableView.selectedIndexes()[0].row()
			index = self.getIndexCell(row)
			#se obtiene de la lista de campos de la tabla actual
			id_name = self.tableView.model().headerData(0, Qt.Horizontal)
			#crear un objeto de la clase EditarRegistro
			editar = EditarRegistro()
			#agregar el objeto a la pila de widgets del QStackedWidget
			self.parent().addWidget(editar)
			#obtener el objeto EditarRegistro de la pila de widgets del QStackedWidget
			editar = self.parent().findChild(EditarRegistro)
			#ejecutar el metodo getRegistro del objeto EditarRegistro
			editar.getRegistro(editar, index, tabla_name, id_name)
			#hacer el cambio de pagina al objeto EditarRegistro
			self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(EditarRegistro)))

#la funcion fillcombo obtiene los campos de la tabla actual y los agrega al combobox para que el usuario pueda seleccionar el campo por el cual desea filtrar la tabla	
	def fillCombo(self):
		#obtener el nombre de la tabla actual
		#tabla_name = self.tableslist.currentText()
		tabla_name = 'tabla_final'
		#obtener la conexion a la base de datos
		conn = obtener_conexion()
		#crear un cursor para la conexion
		cur = conn.cursor()
		#crear la consulta para obtener los campos de la tabla
		query = f"DESCRIBE {tabla_name}"
		#ejecutar la consulta
		cur.execute(query)
		#obtener los campos de la tabla
		vals = cur.fetchall()
		#cerrar la conexion
		cur.close()
		conn.close()
		headers  = []
		#limpiar el combobox
		self.comboBox_busqueda_presupuesto.clear()
		#agregar los campos al combobox
		for i, item in enumerate(vals):
			if item[0] in ['no_presupuesto','no_escritura','proyectista','adquiriente']:
				headers.append((i,item[0]))
				self.comboBox_busqueda_presupuesto.addItem(item[0])
		if len(headers) > 0: self.proxy.setFilterKeyColumn(headers[0][0])
		#agregar un evento al filtro para cuando se cambia el valor del combobox, comparar el valor del combobox con la lista de campos de la tabla para obtener el indice del campo seleccionado
		self.comboBox_busqueda_presupuesto.currentIndexChanged.connect(lambda *args, headers= headers: self.setfilterKeyColumn(headers))

	def setfilterKeyColumn(self,headers:list):
		#obtener el valor del combobox
		comboValue = self.comboBox_busqueda_presupuesto.currentText()
		for items in headers:
			if items[1] == comboValue:
				keyColumn = items[0]
				self.proxy.setFilterKeyColumn(keyColumn)

	def escribirCSV(self):
		#tabla = self.tableslist.currentText()
		path = os.path.expanduser(f"~/NotariusBackup/")
		if not os.path.exists(path): os.makedirs(path)

		path = f"{path}/{date.today()}.csv"
		if bool(Diccionario)==True:
			try:
				df=pd.DataFrame.from_dict(Diccionario)
				df.to_csv(path,index=False,header=True)
				self.mensaje.show()
				self.mensaje.setText(f"Exportado con éxito, en la ruta \"{path}\"")
			except IOError:
				self.mensaje.show()
				self.mensaje.setStyleSheet("color:red;")
				self.mensaje.setText(f"Hubo un error al exportar la tabla")
			self.timerAndHide()

	def timerAndHide(self):
		self.checkThreadTimer = QTimer(self)
		self.checkThreadTimer.setInterval(5000)
		self.checkThreadTimer.start()
		self.checkThreadTimer.timeout.connect(self.mensaje.hide)
	
	def reject(self) -> None: 
		return