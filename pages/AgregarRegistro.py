from functools import partial
from PyQt5 import uic,QtWidgets,QtCore
import os
import re

from bdConexion import obtener_conexion
from pages.Tablas import Tablas
from pages.components import agregarInputsSubtabla, crearBoton, crearInput, crearRadioButton, eliminarInputsSubtabla
from usuarios import getListaTablas, getListaTablasWrite, getPermisos, getRegistrosSubtabla, getSubtabla, getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable
from deployment import getBaseDir


base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','agregar-registros.ui'))


class AgregarRegistro(Form, Base):
    del_btns = []
    cols=[]
    camposCambiados = {}
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los labels de las columnas y se agregan sus debidos inputs
        self.pushButton_confirmar.clicked.connect(self.guardarRegistro)
        self.pushButton_cancelar.clicked.connect(self.restartRegistro)
			
 	# en esta funcion se van a actualizar los labels y se agregaran los inputs segun los labels de las columnas
    def setupColumns(self, Form):
        list_nested_tables = ['facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp','desgloce_ppto','pagos','depositos'] #lista de tablas que deben ser anidadas en los respectivos campos
        # se eliminan los combobox anteriores
        self.camposCambiados.clear()
        self.resetCombobox(self)
        tabla = 'tabla_final'
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
            if col in list_nested_tables:
                self.setupInputsSubtabla(col)
                continue
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
            if isinstance(tipo_dato, bytes):
                tipo_dato = tipo_dato.decode('utf-8')
            if pri == 'PRI': 
                    widget = crearInput(self, tipo_dato, name_input,tabla,registro=index+1,col=col, enable=False)
                    layout.addWidget(widget)
                    self.cols.append(widget)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input, col=col)
                layout.addWidget(r0)
                layout.addWidget(r1)
                self.cols.append(r0)
                self.cols.append(r1)
            else:
                widget = crearInput(self, tipo_dato, name_input,tabla, col=col)
                layout.addWidget(widget)
                self.cols.append(widget)

    def setupInputsSubtabla(self,column):
        nombre_tabla,select = getSubtabla(column)
        columnas = getPermisos(nombre_tabla)["write"]
        lista_columnas = select.split(',')
        propiedades_columnas = listaDescribe(nombre_tabla,lista_columnas)
        layout = self.verticalLayout
        gridLayout = QtWidgets.QGridLayout(objectName=f'grid_layout_{nombre_tabla}')

        name_label = f"label_{column}"
        setattr(self, name_label, QtWidgets.QLabel(self.scrollAreaWidgetContents))
            # Label
        attr_label = getattr(self,name_label)
        attr_label.setStyleSheet("\n"
		"font: 75 16pt;\n"
		"color: #957F5F;\n" 
        "font-weight: 700;")
        attr_label.setObjectName(name_label)
        attr_label.setText(column)
        #horizontal = QtWidgets.QHBoxLayout()
        layout.addWidget(attr_label)
        lastVLayout = QtWidgets.QVBoxLayout(objectName='col_eliminar')
        gridLayout.addLayout(lastVLayout,1,len(lista_columnas)+1)
        add_btn = crearBoton('+')
        add_btn.clicked.connect(partial(agregarInputsSubtabla,self,column))
        gridLayout.addWidget(add_btn,0,len(lista_columnas)+1)
        layout.addLayout(gridLayout)
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_label = f'label_{i}'
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            setattr(self, name_label, QtWidgets.QLabel(self.scrollAreaWidgetContents))
            # Label
            attr_label = getattr(self,name_label)
            attr_label.setStyleSheet("\n"
			"font: 75 14pt;\n"
			"color: #957F5F;\n")
            attr_label.setObjectName(name_label)
            attr_label.setText(col)
            #attr_label.setAlignment(Qt.AlignCenter)
            
            gridLayout.addWidget(attr_label,0,i)
            vLayout = QtWidgets.QVBoxLayout(objectName=f'layout_{col}_{i}_{nombre_tabla}')
            gridLayout.addLayout(vLayout,1,i)
            
        agregarInputsSubtabla(self,column)
            
        
        
    def limpiarString(self,cadena_sucia):
        string_limpio = re.sub("[^0-9]","",cadena_sucia)
        return string_limpio

    def on_text_changed(self,attr):
        # Get the current text in the QTextEdit
        current_text = attr.toPlainText()

        # Check if the current text length is greater than 500
        if len(current_text) > 500:
            # Truncate the text to 500 characters
            truncated_text = current_text[:500]

            # Update the QTextEdit with the truncated text
            attr.setPlainText(truncated_text)
    def resetCombobox(self, Form):
         
        for obj in self.cols:
            try: 
                self.verticalLayout.removeWidget(obj)
                obj.deleteLater()
                del obj
            except RuntimeError:
                return
        self.cols.clear()
        self.camposCambiados.clear()

    
    def actualizarDict(self,col, val):
        tipo = str(type(val))
        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        if type(val) == bool: val = 1 if val else 0
        self.camposCambiados[col] = val
        
    def guardarRegistro(self):
        tabla = 'tabla_final'
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
        #updateTable(tabla)
        self.parent().findChild(Tablas).agregarRegistro(self.camposCambiados['id'])
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