from PyQt5 import  uic
from bdConexion import obtener_conexion
from PyQt5.QtWidgets import QHeaderView, QTableView, QAbstractItemView,QPushButton,QMessageBox
from PyQt5.QtCore import Qt,QSortFilterProxyModel, QTimer
from resources_rc import *
from PyQt5.QtGui import QStandardItemModel,QStandardItem

import os

from pages.EditarPrivilegios import EditarPrivilegios
from usuarios import getPermisos, getUsuarioLogueado, getValoresTabla, updateTable

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/ver-usuario.ui")))


class VerUsuarios(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.setupTable(self)
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.botonEliminar.clicked.connect(self.buttonClick)

	# en este metodo se actualizan los datos de la tabla, segun la tabla seleccionada en la lista
	def setupTable(self, Form):
		permisos = getPermisos('usuario')
		select = permisos["read"]
		tabla = getValoresTabla('usuario')
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
		self.tableView.horizontalHeader().setStretchLastSection(True);
	
	def buttonClick(self):
		if self.tableView.selectedIndexes() == []:
			# agregar mensaje de error
			self.mensaje.show()
			self.mensaje.setText("No tiene ningun usuario seleccionado para eliminar")
			self.checkThreadTimer = QTimer(self)
			self.checkThreadTimer.setInterval(5000)
			self.checkThreadTimer.start()
			self.checkThreadTimer.timeout.connect(self.mensaje.hide)
			return
		elif len(self.tableView.selectedIndexes())>1:
			self.mensaje.show()
			self.mensaje.setText("Elija solamente un campo para eliminar el usuario")
			self.checkThreadTimer = QTimer(self)
			self.checkThreadTimer.setInterval(5000)
			self.checkThreadTimer.start()
			self.checkThreadTimer.timeout.connect(self.mensaje.hide)
			return
		else:
			row = self.tableView.selectedIndexes()[0].row()
			print(row)
			index = self.getIndexCell(row)
			self.eliminarusuarios(self,index)
	
	def getIndexCell(self, row):
		headercount = self.tableView.model().columnCount()
		for x in range(headercount):
			headertext = self.tableView.model().headerData(x, Qt.Horizontal)
			if 'id' == headertext:
				cell = self.tableView.model().index(row, x).data()  # get cell at row, col
				return cell

	def eliminarusuarios(self, Form, index):
		user, pwd = getUsuarioLogueado()
		conn = obtener_conexion(user,pwd)
		cur = conn.cursor()
		query = f"select nombre_usuario from usuario where id='{index}'"
		cur.execute(query)
		user = cur.fetchone()
		
		query = f"drop user '{user[0]}'@'localhost';"
		cur.execute(query)
		query = f"delete from usuario where id='{index}';"
		cur.execute(query)
		cur.close()
		conn.commit()
		conn.close()
		item = self.parent().findChild(EditarPrivilegios).usuarioslist.findText(user[0])
		self.parent().findChild(EditarPrivilegios).usuarioslist.removeItem(item)
		updateTable('usuario')
		self.setupTable(self)
	def reject(self) -> None:
		return