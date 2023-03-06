from datetime import date
from functools import partial
from PyQt5 import uic
import pandas as pd
#python(suversion) -m pip install pandas
from PyQt5.QtWidgets import QHeaderView, QTableView, QAbstractItemView,QPushButton,QMessageBox
from PyQt5.QtCore import Qt,QSortFilterProxyModel, QTimer
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
		self.mensaje.hide()
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.pushButton_2.clicked.connect(self.escribirCSV)
		self.tableslist.currentIndexChanged.connect(partial(self.setupTable,self))

	def selectTable(self,Form,tabla):
		#print("resultado")
		item = self.tableslist.findText(tabla,Qt.MatchExactly)
		print(item)
		#index =self.tableslist.row(item[0])
		self.tableslist.setCurrentIndex(item)
		#print(self.tableslist.row(item[0]))
		#self.tableslist.setCurrentRow(0)

	# en este metodo se agregan las tablas disponibles para el usuario a una lista	
	def setupTableList(self,Form):
		lista_tablas = getListaTablas()
		self.tableslist.addItems(lista_tablas)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self,Form):
		tabla_name = self.tableslist.currentText()
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
		for i, registro in enumerate(tabla):
			for j, (col, val) in enumerate(registro.items()):
				model.setItem(i,j,QStandardItem(str(val)))
			
		#crear un filtro para el widget QTableView
		self.proxy = QSortFilterProxyModel()
		#agregar el modelo al filtro
		self.proxy.setSourceModel(model)
		#agregar el filtro al widget QTableView
		self.tableView.setModel(self.proxy)

		#obtener una lista enumerada de los campos de la tabla
		headers = list(enumerate([i for i in header]))
		#agregar un evento al filtro para cuando se cambia el valor del combobox, comparar el valor del combobox con la lista de campos de la tabla para obtener el indice del campo seleccionado
		self.comboBox_busqueda_presupuesto.currentIndexChanged.connect(lambda *args, headers= headers: self.setfilterKeyColumn(headers))
		#agregar un evento al filtro para cuando se escribe en el line edit
		self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
		#agregar un evento al filtro para cuando se escribe en el line edit
		self.line_edit_busqueda_presupuesto.textChanged.connect(self.proxy.setFilterRegExp)
		self.busqueda()

		self.tableView.resizeColumnsToContents();
		
		self.tableView.horizontalHeader().setStretchLastSection(True);
		
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
		tabla_name = self.tableslist.currentText()
		#obtener el id del registro seleccionado en el QTableView
		print('selected')
		print(self.tableView.selectedIndexes())

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
			print(row)
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


	def fillCombo(self):
		#obtener el nombre de la tabla actual
		tabla_name = self.tableslist.currentText()
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



	def setfilterKeyColumn(self,headers:list):
		#obtener el valor del combobox
		print()
		print("AQUI EMPIEZA EL SETFILTERKEYCOLUMN")
		print(headers)
		comboValue = self.comboBox_busqueda_presupuesto.currentText()
		for items in headers:
			print(items)
			if items[1] == comboValue:
				keyColumn = items[0]
				print(keyColumn)
				self.proxy.setFilterKeyColumn(keyColumn)
		print("AQUI TERMINA EL SETFILTERKEYCOLUMN")

	def escribirCSV(self):
		tabla = self.tableslist.currentText()
		path = os.path.expanduser(f"~/NotariusBackup/{tabla}")
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
				print("no")
			self.timerAndHide()

	def timerAndHide(self):
		self.checkThreadTimer = QTimer(self)
		self.checkThreadTimer.setInterval(5000)
		self.checkThreadTimer.start()
		self.checkThreadTimer.timeout.connect(self.mensaje.hide)
	
	def reject(self) -> None: 
		return