from PyQt5 import QtGui, uic
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/ver-tabla.ui")))


class VerTabla(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
  
	# def setupUi(self, Form):
		# print('actualizar tabla')
		# en este metodo se debe crear el checkbox con las tablas disponibles para el usuario	
		# checar permisos de usuario, si no puede editar desactivar edicion
  
  
		# se necesita un select all que permita ver la cantidad de tablas seleccionadas
		# en el check box (dinamico), si es posible, evitar la repeticion de columnas
		# en este punto estamos considerando que con la creacion del usuario con sus permisos
		# no mostrara de forma automatica los campos que no puede ver (comprobar en tests)

		# mock up de como se actualizara ver tabla
  
		# all_data = db.fetch
		# tbl = QtGui.QTableWidget(len(all_data),X) # X is The number of columns that you need  
		# header_labels = ['Column 1', 'Column 2', 'Column 3', 'Column 4',...]  
		# tbl.setHorizontalHeaderLabels(header_labels)
		# for row in all_data:
		# 	inx = all_data.index(row)
		# 	tbl.insertRow(inx)
		# 	tbl.setItem(inx,Y,QTableWidgetItem(your data)) # Y is the column that you want to insert data  