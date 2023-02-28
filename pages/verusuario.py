from PyQt5 import  uic
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QAbstractItemView,QPushButton
from bdConexion import obtener_conexion

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/verusuario.ui")))


class VerUsuario(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.setupTable(self)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		#self.modificar.clicked.connect(self.parent().findChild(EditarRegistro).usuarioslist)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self, Form):
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(0)
		print(self.parent())
		conn = obtener_conexion()
		query = f"SELECT * FROM usuario" 
		cur = conn.cursor(dictionary=True)
		cur.execute(query)
		tabla = cur.fetchall()
		cur.close()
		conn.close()
		header = ["Eliminar"]+list(tabla[0].keys())
		self.tableWidget.setColumnCount(len(header))
		self.tableWidget.setHorizontalHeaderLabels(header)
		for dic in tabla:
			col = 1
			button = self.createButton(self)
			rows = self.tableWidget.rowCount()
			self.tableWidget.setRowCount(rows + 1)
			# se agrega un boton modificar que al hacer clic mandara a la pagina modificar registro
			self.tableWidget.setCellWidget(rows,0,button)
			button.clicked.connect(lambda *args, self=self, row=rows: self.eliminarusuarios(self,row))
			for val in dic.values():
				self.tableWidget.setItem(rows, col, QTableWidgetItem(str(val)))
				col +=1
		self.tableWidget.resizeColumnsToContents()
		self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents);
	
	def createButton(self, Form):
  
		button = QPushButton(self.tableWidget)
		button.setObjectName("eliminar")
		button.setText("Eliminar")
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
	
	def eliminarusuarios(self, Form, row):
		index = self.tableWidget.item(row,1).text()
		conn = obtener_conexion()
		cur = conn.cursor()
		query = f"delete from usuario where id='{index}';"
		cur.execute(query)
		cur.close()
		conn.commit()
		conn.close()
		self.setupTable(self)