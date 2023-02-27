from functools import partial
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView,QPushButton
from bdConexion import obtener_conexion
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/ver-tabla.ui")))


class VerTabla(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.setupTableList(self)
		self.setupTable(self)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableslist.itemSelectionChanged.connect(partial(self.setupTable,self))


	# en este metodo se agregan las tablas disponibles para el usuario a una lista	
	def setupTableList(self, Form):
		conn = obtener_conexion()
		cur = conn.cursor()
		query = 'SHOW TABLES'
		cur.execute(query)
		tablas = cur.fetchall()
		cur.close()
		conn.close()
		lista_tablas = [tabla[0] for tabla in tablas]
		self.tableslist.addItems(lista_tablas)
		self.tableslist.setCurrentRow(0)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self, Form):
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(0)
		tabla_name = self.tableslist.currentItem().text()
		conn = obtener_conexion()
		query = f"SELECT * FROM {tabla_name}"
		cur = conn.cursor(dictionary=True)
		cur.execute(query)
		tabla = cur.fetchall()
		cur.close()
		conn.close()
		header = ["Modificar"]+list(tabla[0].keys())
		print(header)
		self.tableWidget.setColumnCount(len(header))
		self.tableWidget.setHorizontalHeaderLabels(header)

		for dic in tabla:
			col = 1
			button = self.createButton(self)
			rows = self.tableWidget.rowCount()
			self.tableWidget.setRowCount(rows + 1)
			# se agrega un boton modificar que al hacer clic mandara a la pagina modificar registro
			self.tableWidget.setCellWidget(rows,0,button)
			for val in dic.values():
				self.tableWidget.setItem(rows, col, QTableWidgetItem(str(val)))
				col +=1
		self.tableWidget.resizeColumnsToContents()
		self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents);
	
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
