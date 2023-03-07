from functools import partial
from PyQt5 import uic,QtWidgets,QtCore
import os
import re

from bdConexion import obtener_conexion
from pages.components import crearInput, crearRadioButton
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable
from deployment import getBaseDir


base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','agregar-registros.ui'))


class AgregarRegistro(Form, Base):
    cols=[]
    camposCambiados = {}
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupTables(self)
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los labels de las columnas y se agregan sus debidos inputs
        self.tablaslist.currentTextChanged.connect(self.setupColumns)
        self.pushButton_confirmar.clicked.connect(self.guardarRegistro)
        self.pushButton_cancelar.clicked.connect(self.restartRegistro)

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
    def setupTables(self, Form):
        lista_tablas = getListaTablas()
        #print(lista_tablas)
        self.tablaslist.addItems(lista_tablas)
    
			
 	# en esta funcion se van a actualizar los labels y se agregaran los inputs segun los labels de las columnas
    def setupColumns(self, Form):
        # se eliminan los combobox anteriores
        self.camposCambiados.clear()
        self.resetCombobox(self)
        tabla = self.tablaslist.currentText()
        columnas = getPermisos(tabla)["write"]
        lista_columnas = columnas.split(',')
        propiedades_columnas = listaDescribe(tabla,lista_columnas)
        layout = self.verticalLayout
        index = getValoresTabla(tabla)[-1]['id']
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_input = f"input_{i}"
            name_label = f'label_{i}'
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            setattr(self, name_label, QtWidgets.QLabel(self.scrollAreaWidgetContents))
            # Label
            attr_label = getattr(self,name_label)
            attr_label.setStyleSheet("\n"
			"font: 75 12pt;\n"
			"color: #666666;\n" 
            "font-weight: 700;")
            attr_label.setObjectName(name_label)
            attr_label.setText(col+': ')
            layout.addWidget(attr_label)
            self.cols.append(attr_label)
            if pri == 'PRI': 
                    widget = crearInput(self, tipo_dato, name_input,registro=index+1,col=col, enable=False)
                    layout.addWidget(widget)
                    self.cols.append(widget)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input, col=col)
                layout.addWidget(r0)
                layout.addWidget(r1)
                self.cols.append(r0)
                self.cols.append(r1)
            else:
                widget = crearInput(self, tipo_dato, name_input, col=col)
                layout.addWidget(widget)
                self.cols.append(widget)


    def limpiarString(self,cadena_sucia):
        string_limpio = re.sub("[^0-9]","",cadena_sucia)
        return string_limpio


    def resetCombobox(self, Form):
        for obj in self.cols:
            self.verticalLayout.removeWidget(obj)
            obj.deleteLater()
            del obj
        self.cols.clear()
        self.camposCambiados.clear()
        
    
    def actualizarDict(self,col, val):
        tipo = str(type(val))
        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        if type(val) == bool: val = 1 if val else 0
        self.camposCambiados[col] = val
        
    def guardarRegistro(self):
        tabla = self.tablaslist.currentText()
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        query = f"INSERT INTO {tabla} (" 
        vals = "values ("

        for i, (col, val) in enumerate(self.camposCambiados.items()):
            if i+1 == len(self.camposCambiados): 
                query+= f"{col}) "
                vals+= f"'{val}');"
            else: 
                query+=f"{col},"
                vals+= f"'{val}', "
        cur.execute(query+vals)
        conn.commit()
        cur.close()
        conn.close()
        updateTable(tabla)
        self.label_exito.setText("Registro guardado exitosamente")
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(3000)
        self.checkThreadTimer.start()
        self.checkThreadTimer.timeout.connect(partial(self.label_exito.setText,''))
        self.restartRegistro()
                
        #insert into {nombre_tabla} (cols[0]) cols[1]
    def restartRegistro(self):
        self.setupColumns(self)
    
    def reject(self) -> None:
        return

	# dentro de este método se podran actualizar los campos de forma dinamica,
	# segun la tabla que se haya seleccionado	
	# def setupUi(self, Form):
		# print("agregar campos de tabla")
		# primero se obtendra la tabla seleccionada, por default sera write
		# se hara un fetch a la base de datos con todos los campos de esa tabla 
		# se debe renderizar la pantalla con los inputs de los campos a llenar
		# si es posible, que existan condiciones para poner el mejor tipo de campo
		# 	ejemplo 1, si es boolean que aparezca un radio button si y otro no
		# 	ejemplo 2, si es tipo datetime que aparezca uno de seleccionar fecha
		# al picar guardar, almacenar datos en la tabla. En caso de errores alertar al usuario
		# se redirige a la tabla
		# en caso de cancelar, redirigir a la tabla