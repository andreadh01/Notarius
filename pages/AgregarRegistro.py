from PyQt5 import uic,QtWidgets
import os
import re

from bdConexion import obtener_conexion
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado, listaDescribe

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/agregar-registros.ui")))


class AgregarRegistro(Form, Base):
    cols=[]
    
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupTables(self)
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los labels de las columnas y se agregan sus debidos inputs
        self.tablaslist.currentTextChanged.connect(self.setupColumns)
        self.pushButton_confirmar.clicked.connect(self.guardarRegistro)
        self.pushButton_cancelar.clicked.connect(self.cancelarRegistro)

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
    def setupTables(self, Form):
        lista_tablas = getListaTablas()
        #print(lista_tablas)
        self.tablaslist.addItems(lista_tablas)
    
			
 	# en esta funcion se van a actualizar los labels y se agregaran los inputs segun los labels de las columnas
    def setupColumns(self, Form):
        # se eliminan los combobox anteriores
        self.resetCombobox(self)
        tabla = self.tablaslist.currentText()
        columnas = getPermisos(tabla)["INSERT"]
        lista_columnas = columnas.split(',')
        print(tabla)
        print(lista_columnas)
        propiedades_columnas = listaDescribe(tabla,lista_columnas)
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_input = f"input_{i}"
            name_label = f'label_{i}'
            
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            if auto_increment != 'auto_increment':
                setattr(self, name_label, QtWidgets.QLabel(Form))
                # Label
                attr_label = getattr(self,name_label)
                attr_label.setStyleSheet("\n"
				"font: 75 16pt;\n"
				"color: rgb(149, 117, 61);")
                attr_label.setObjectName(name_label)
                attr_label.setText(col+': ')
                self.gridLayout.addWidget(attr_label, i+1, 1, 1, 1)
                self.cols.append(attr_label)
                widget = self.crearInput(tipo_dato, name_input)
                print(widget)
                self.gridLayout.addWidget(widget, i+1, 2, 1, 1)
                self.cols.append(widget)

    # Metodo para crear los input para cada columna que se necesita registrar segun la tabla seleccionada
    def crearInput(self,tipo_dato,name_input):
        if 'int' in tipo_dato:   
            setattr(self, name_input, QtWidgets.QSpinBox())
            attr = getattr(self,name_input)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            if 'tinyint' in tipo_dato:
                attr.setMaximum(127)
            else:
                attr.setMaximum(2147483647)
            return attr
        elif 'date' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateEdit())
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            return attr
        elif 'varchar' in tipo_dato:
            setattr(self, name_input, QtWidgets.QLineEdit())
            attr = getattr(self,name_input)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            max_value = self.limpiarString(tipo_dato)
            attr.setMaxLength(int(max_value))
            return attr
        elif 'decimal' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDoubleSpinBox())
            attr = getattr(self,name_input)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            attr.setMaximum(99999999.99)
            return attr
        elif 'enum' in tipo_dato:
            setattr(self, name_input, QtWidgets.QComboBox())
            attr = getattr(self,name_input)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            re_pattern = re.compile(r"[^a-z, ()]", re.I)
            opciones = re.sub(re_pattern, "", tipo_dato)            
            opciones = opciones.replace('enum(','').replace(')','')
            opciones = opciones.split(',')
            attr.addItems(opciones)
            return attr
        elif 'timestamp' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateTimeEdit())
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            #attr.setDisplayFormat("yyyy-mm-dd HH:mm:ss")
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            return attr
                    

    def limpiarString(self,cadena_sucia):
        string_limpio = re.sub("[^0-9]","",cadena_sucia)
        return string_limpio


    def resetCombobox(self, Form):
        for obj in self.cols:
            self.gridLayout.removeWidget(obj)
            obj.deleteLater()
            del obj
        self.cols = []

    def guardarRegistro(self):
        print(type(self.cols[0]))
        user, pwd = getUsuarioLogueado()
        nombre_columnas = []
        inputs = []
        tabla_seleccionada = self.tablaslist.currentText()
        query = f'INSERT INTO {tabla_seleccionada} ('
        for elemento in self.cols:
            if elemento.__class__.__name__=='QLabel':
                nombre_columnas.append(elemento.text().replace(": ",""))
            else:
                if elemento.__class__.__name__ == 'QSpinBox':
                    inputs.append(elemento.value())
                elif elemento.__class__.__name__ == 'QDateEdit':
                    inputs.append(elemento.date().toString("yyyy-MM-dd"))
                elif elemento.__class__.__name__ == 'QLineEdit':
                    inputs.append(elemento.text())
                elif elemento.__class__.__name__ == 'QDoubleSpinBox':
                    inputs.append(elemento.value())
                elif elemento.__class__.__name__ == 'QComboBox':
                    inputs.append(elemento.currentText())
                elif elemento.__class__.__name__ == 'QDateTimeEdit':
                    inputs.append(elemento.dateTime().toString("yyyy-MM-dd hh:mm:ss"))

        for columna in nombre_columnas:
            query += f"{columna},"
        query += ") VALUES ("
        for dato in inputs:
            if dato.__class__.__name__ == 'str':
                query += f"'{dato}',"
            else:
                query += f"{dato},"
        query += ");"
        query = query.replace(",)",")")
        print(query)

        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        self.label_exito.setText("Registro guardado exitosamente")
                
        #insert into {nombre_tabla} (cols[0]) cols[1]
    def cancelarRegistro(self):
        self.lineEdit_nombreusuario.setText("")
        self.lineEdit_contrasenausuario.setText("")
        self.limpiarDict()

	# dentro de este método se podran actualizar los campos de forma dinamica,
	# segun la tabla que se haya seleccionado	
	# def setupUi(self, Form):
		# print("agregar campos de tabla")
		# primero se obtendra la tabla seleccionada, por default sera escritura
		# se hara un fetch a la base de datos con todos los campos de esa tabla 
		# se debe renderizar la pantalla con los inputs de los campos a llenar
		# si es posible, que existan condiciones para poner el mejor tipo de campo
		# 	ejemplo 1, si es boolean que aparezca un radio button si y otro no
		# 	ejemplo 2, si es tipo datetime que aparezca uno de seleccionar fecha
		# al picar guardar, almacenar datos en la tabla. En caso de errores alertar al usuario
		# se redirige a la tabla
		# en caso de cancelar, redirigir a la tabla