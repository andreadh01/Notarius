from functools import partial
import re
from PyQt5 import uic, QtWidgets
import os
from bdConexion import obtener_conexion
from pages.components import crearInput, crearRadioButton
from usuarios import getPermisos, getRegistro, getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-registro.ui")))

class EditarRegistro(Form, Base):
    camposCambiados = {}
    pri_key = ()
    tabla = ''
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
            # se mandan llamar los metodos al correr el programa
        #self.setupInputs(self)
        self.pushButton_cancelar.clicked.connect(self.changePage)
        self.pushButton_confirmar.clicked.connect(self.actualizarRegistro)
			
    def setupInputs(self, Form, tabla, registro):
        # se eliminan los inputs anteriores
        self.tabla = tabla
        columnas = getPermisos(tabla)["write"]
        lista_columnas = columnas.split(',')
        print(tabla)
        print(lista_columnas)
        propiedades_columnas = listaDescribe(tabla,lista_columnas)
        print(registro['id'])
        print(registro)
        layout = self.verticalLayout
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_input = f"input_{i}"
            name_label = f'label_{i}'
             
            print(col)
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            setattr(self, name_label, QtWidgets.QLabel(self.scrollAreaWidgetContents))
            # Label
            attr_label = getattr(self,name_label)
            attr_label.setStyleSheet("\n"
			"font: 75 16pt;\n"
			"color: #666666;\n" 
            "font-weight: 700;")
            attr_label.setObjectName(name_label)
            attr_label.setText(col+': ')
            layout.addWidget(attr_label)
            if pri == 'PRI': 
                    self.pri_key = (col,registro[col])
                    widget = crearInput(self, tipo_dato, name_input, registro[col],col, enable=False)
                    layout.addWidget(widget)
                    print(self.pri_key)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input, registro[col],col)
                layout.addWidget(r0)
                layout.addWidget(r1)
            else:
                widget = crearInput(self, tipo_dato, name_input, registro[col],col)
                layout.addWidget(widget)
                
    # este metodo carga el registro seleccionado
    def getRegistro(self, Form, index, tabla, col):
        self.label_tabla.setText(f"Tabla: {tabla}")
        registro = getRegistro(tabla,col,int(index))
        print(registro)
        self.setupInputs(self,tabla,registro)
        
    def limpiarString(self,cadena_sucia):
        string_limpio = re.sub("[^0-9]","",cadena_sucia)
        return string_limpio



    def changePage(self):
        from pages.Tablas import Tablas
        self.camposCambiados.clear()
        print(self.tabla)
        self.parent().findChild(Tablas).selectTable(self.parent().findChild(Tablas),self.tabla)
        self.parent().findChild(Tablas).setupTable(self.parent().findChild(Tablas))
        self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(Tablas)))
        
    
    def actualizarDict(self, col,val):
        tipo = str(type(val))
        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        if type(val) == bool: val = 1 if val else 0
        self.camposCambiados[col] = val
        print(self.camposCambiados)
        
    def actualizarRegistro(self):
        tabla = self.label_tabla.text().split(": ")
        tabla = tabla[1]
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

    def reject(self) -> None:
        return