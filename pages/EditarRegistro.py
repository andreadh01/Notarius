from functools import partial
import re
from PyQt5 import uic, QtWidgets
import os
from bdConexion import obtener_conexion
from pages.components import agregarInputsSubtabla, crearBoton, crearInput, crearRadioButton, eliminarInputsSubtabla, messageBox
from usuarios import getPermisos, getRegistro, getRegistrosSubtabla, getSubtabla, getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable
from PyQt5.QtCore import Qt
from deployment import getBaseDir

base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','editar-registro.ui'))

class EditarRegistro(Form, Base):
    camposCambiados = {}
    pri_key = ()
    del_btns = []
    tabla = ''
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
            # se mandan llamar los metodos al correr el programa
        #self.setupInputs(self)
        self.pushButton_cancelar.clicked.connect(self.changePage)
        self.pushButton_confirmar.clicked.connect(self.actualizarRegistro)
			
    def setupInputs(self, Form, registro, subtabla=False):
        # se eliminan los inputs anteriores
        columnas = getPermisos('tabla_final')["write"]
        #print('registroooo tabla',registro)
        lista_columnas = columnas.split(',')
        propiedades_columnas = listaDescribe('tabla_final',lista_columnas)
        list_nested_tables = ['facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp','desgloce_ppto','pagos','depositos'] #lista de tablas que deben ser anidadas en los respectivos campos

        layout = self.verticalLayout
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_input = f"input_{i}"
            name_label = f'label_{i}'
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            if col in list_nested_tables:
                new_registro = getRegistrosSubtabla(col,registro[col])
                self.setupInputsSubtabla(col,new_registro)
                continue
            setattr(self, name_label, QtWidgets.QLabel(self.scrollAreaWidgetContents))
            # Label
            attr_label = getattr(self,name_label)
            attr_label.setStyleSheet("\n"
			"font: 75 16pt;\n"
			"color: #666666;\n" 
            "font-weight: 700;")
            attr_label.setObjectName(name_label)
            attr_label.setText(col)
            layout.addWidget(attr_label)
            
            if isinstance(tipo_dato, bytes):
                tipo_dato = tipo_dato.decode('utf-8')
            elif pri == 'PRI': 
                    self.pri_key = (col,registro[col])
                    widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col, enable=False)
                    layout.addWidget(widget)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input, registro[col],col)
                layout.addWidget(r0)
                layout.addWidget(r1)
            else:
                widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col)
                layout.addWidget(widget)
                
    # este metodo carga el registro seleccionado
    def getRegistro(self, Form, index, tabla, col):
        registro = getRegistro(tabla,col,int(index))
        self.setupInputs(self,registro)
        
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
   
    def setupInputsSubtabla(self,column,registros):
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
        #horizontal.addWidget(attr_label)
        #horizontal.addWidget(add_btn)
        
        
        for i in enumerate(registros): 
            del_btn = crearBoton('-')
            lastVLayout.addWidget(del_btn)
            self.del_btns.append(del_btn)
            index = self.del_btns.index(del_btn)
            del_btn.clicked.connect(partial(eliminarInputsSubtabla,self,index,column))
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
			"font: 75 14pt;\n"
			"color: #957F5F;\n")
            attr_label.setObjectName(name_label)
            attr_label.setText(col)
            #attr_label.setAlignment(Qt.AlignCenter)
            
            gridLayout.addWidget(attr_label,0,i)
            vLayout = QtWidgets.QVBoxLayout(objectName=f'layout_{col}_{i}_{nombre_tabla}')
            gridLayout.addLayout(vLayout,1,i)
            
            for registro in registros:
                if isinstance(tipo_dato, bytes):
                    tipo_dato = tipo_dato.decode('utf-8')
                elif pri == 'PRI': 
                        self.pri_key = (col,registro[col])
                        widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col, enable=False)
                        vLayout.addWidget(widget)
                elif 'tinyint' in tipo_dato:
                    r0,r1 = crearRadioButton(self, name_input, registro[col],col)
                    vLayout.addWidget(r0)
                    vLayout.addWidget(r1)
                else:
                    widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col)
                    vLayout.addWidget(widget)
        layout.addLayout(gridLayout)

    def changePage(self):
        from pages.Tablas import Tablas
        self.camposCambiados.clear()
        
        #obtener los permisos del usuario para la tabla seleccionada
        self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(Tablas)))
        
    
    def actualizarDict(self, col,val):
        tipo = str(type(val))
        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        if type(val) == bool: val = 1 if val else 0
        self.camposCambiados[col] = val
        
    def actualizarRegistro(self):
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        query = f"UPDATE tabla_final set "

        for i, (col, val) in enumerate(self.camposCambiados.items()):
            if i+1 == len(self.camposCambiados): query+= f"{col}='{val}' WHERE  {self.pri_key[0]}='{self.pri_key[1]}'"
            else: query+= f"{col}='{val}', "
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        from pages.Tablas import Tablas
        updateTable('tabla_final')

        self.parent().findChild(Tablas).actualizarRegistro(self.pri_key[1])
        self.changePage()

    def reject(self) -> None:
        return