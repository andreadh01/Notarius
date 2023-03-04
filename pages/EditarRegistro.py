from functools import partial
import re
from PyQt5 import uic, QtWidgets
import os
from bdConexion import obtener_conexion
from usuarios import getPermisos, getUsuarioLogueado, listaDescribe, updateTable

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-registro.ui")))

class EditarRegistro(Form, Base):
    cols = []
    camposCambiados = {}
    pri_key = ()
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
            # se mandan llamar los metodos al correr el programa
        #self.setupInputs(self)
        self.pushButton_cancelar.clicked.connect(self.changePage)
        self.pushButton_confirmar.clicked.connect(self.actualizarRegistro)
			
    def setupInputs(self, Form, tabla, registro):
        # se eliminan los inputs anteriores
        self.resetCombobox(self)
        # user, pwd = getUsuarioLogueado()
        # conn = obtener_conexion(user,pwd)
        # cur = conn.cursor()
        columnas = getPermisos(tabla)["UPDATE"]
        lista_columnas = columnas.split(',')
        print(tabla)
        print(lista_columnas)
        propiedades_columnas = listaDescribe(tabla,lista_columnas)
        # query = f'DESCRIBE {tabla}'
        # cur.execute(query)
        # propiedades_columnas = cur.fetchall()
        # print(propiedades_columnas)
        # cur.close()
        # conn.close()
        
        
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_input = f"input_{i}"
            name_label = f'label_{i}'
            print(col)
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            disable = False
            if pri == 'PRI': 
                    disable = True
                    self.pri_key = (col,registro[col])
                    print(self.pri_key)
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
                widget = self.crearInput(tipo_dato, name_input, registro[col],col, disable)
                self.gridLayout.addWidget(widget, i+1, 2, 1, 1)
                self.cols.append(widget)
                
    # este metodo carga el registro seleccionado
    def getRegistro(self, Form, index, tabla, col):
        print('nombreeee '+tabla)
        self.tablaLabel.setText(tabla)
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor(dictionary=True)
        query = f"SELECT * FROM {tabla} WHERE {col}='{index}'"
        cur.execute(query)
        registro = cur.fetchone()
        cur.close()
        conn.close()
        print(registro)
        self.setupInputs(self,tabla,registro)
        
    
    def crearInput(self,tipo_dato,name_input, registro,col,disable=False):
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
            attr.setValue(registro)
            attr.valueChanged.connect(partial(self.actualizarDict, col))
        # elif 'tinyint' in tipo_dato:
        #     setattr(self, name_input, QtWidgets.QSpinBox())
        #     attr = getattr(self,name_input)
        #     attr.setStyleSheet("\n"
        #     "font: 75 16pt;\n"
        #     "color: rgb(149, 117, 61);")
        #     attr.setObjectName(name_input)
        #     if 'tinyint' in tipo_dato:
        #         attr.setMaximum(127)
        #     else:
        #         attr.setMaximum(2147483647)
        #     attr.setValue(registro)
        elif 'date' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateEdit())
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            attr.setDate(registro)
            attr.dateChanged.connect(partial(self.actualizarDict, col))
        elif 'varchar' in tipo_dato:
            setattr(self, name_input, QtWidgets.QLineEdit())
            attr = getattr(self,name_input)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            max_value = self.limpiarString(tipo_dato)
            attr.setMaxLength(int(max_value))
            attr.setText(registro)
            attr.textChanged.connect(partial(self.actualizarDict, col))
        elif 'decimal' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDoubleSpinBox())
            attr = getattr(self,name_input)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            attr.setMaximum(99999999.99)
            attr.setValue(registro)
            attr.valueChanged.connect(partial(self.actualizarDict, col))            
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
            attr.setCurrentText(registro)
            attr.currentTextChanged.connect(partial(self.actualizarDict, col))
        elif 'timestamp' in tipo_dato:
            print(Form)
            setattr(self, name_input, QtWidgets.QDateTimeEdit())
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            #attr.setDisplayFormat("yyyy-mm-dd HH:mm:ss")
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name_input)
            attr.setDateTime(registro)
            attr.dateTimeChanged.connect(partial(self.actualizarDict, col))
        if disable: attr.setEnabled(False)    
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

    def changePage(self):
        from pages.VerTabla import VerTabla
        self.camposCambiados.clear()
        self.parent().findChild(VerTabla).setupTable(self.parent().findChild(VerTabla))
        self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(VerTabla)))
        
    
    def actualizarDict(self, col,val):
        tipo = str(type(val))
        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        self.camposCambiados[col] = val
        print(self.camposCambiados)
        
    def actualizarRegistro(self):
        tabla = self.tablaLabel.text()
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        query = f"UPDATE {tabla} set "

        for i, (col, val) in enumerate(self.camposCambiados.items()):
            print(i)
            print(len(self.camposCambiados))
            if i+1 == len(self.camposCambiados): query+= f"{col}='{val}' WHERE  {self.pri_key[0]}='{self.pri_key[1]}'"
            else: query+= f"{col}='{val}', "
        print(query)
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        updateTable(tabla)
        self.changePage()
    #     print(registro)
    #     conn = obtener_conexion(self.user,self.password)
    #     cur = conn.cursor()
    #     query = 'SELECT * FROM {} WHERE {'columna_0'}='{valor_col_0}''
    #     cur.execute(query)
    #     tablas = cur.fetchall()
    #     cur.close()
    #     conn.close()
    #     lista_tablas = [tabla[0] for tabla in tablas]
        
    # este metodo le da el valor a los labels del registro a modificar
    
    # este metodo carga las tablas
    
    # este metodo carga todos los registros en un combobox (el id para seleccionar)
