from functools import partial
import re
from PyQt5 import uic, QtWidgets
import os
from bdConexion import obtener_conexion
from pages.components import agregarInputsSubtabla, crearBoton, crearInput, crearRadioButton, eliminarInputsSubtabla, messageBox
from usuarios import getAllPermisos, getPermisos, getRegistro, getRegistrosSubtabla, getSubtabla, getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable
from PyQt5.QtCore import Qt
from deployment import getBaseDir
#from reportlab.pdfgen import canvas, 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from PyQt5.QtWidgets import QFileDialog


base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','editar-registro.ui'))

class EditarRegistro(Form, Base):
    listaregistros_editarregistros = []
    diccionarioregistros_editarregistros_subtablas = {}
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
        self.pushButton_pdf.clicked.connect(self.crearPDF)
	
    def crearPDF(self):
        #se abre el filechooser o ajá
        file_path, _ = QFileDialog.getSaveFileName(filter='PDF Files (*.pdf)')
        bold_style = ParagraphStyle(
        name='Bold',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.black,
        alignment=TA_LEFT,
        )
        # Create a new PDF
        if file_path != '':
            pdf = SimpleDocTemplate(file_path,pagesize=letter, topMargin=10)
            styles = getSampleStyleSheet()
            normal_style = styles["Normal"]
            parrafos = []

            logo = Image("logo.png")
            logo.hAlign = 'LEFT'
            logo.spaceBefore = 20
            logo.drawHeight = 4*inch*logo.drawHeight/logo.drawWidth
            logo.drawWidth = 4*inch
            parrafos.append(logo)

            #este for es para la informacion normal
            for element in self.listaregistros_editarregistros:
                parrafo = Paragraph(str(element[0])+': '+str(element[1]),normal_style)
                parrafos.append(parrafo)
                parrafos.append(Spacer(1,12))


            #este for es para las subtablas     
            for key, value in self.diccionarioregistros_editarregistros_subtablas.items():
                diccionario = {}
                parrafo = Paragraph(key,bold_style)
                parrafos.append(parrafo)
                parrafos.append(Spacer(1,12))
                diccionario = self.organizardiccionario(value, diccionario)
                lista = []
                for key, value in diccionario.items():
                        lista.append(value)
                for j, element in enumerate(lista[0]):
                    for k in range(0, len(diccionario)):
                        parrafo = Paragraph(str(list(diccionario.keys())[k])+': '+str(diccionario[list(diccionario.keys())[k]][j]),normal_style)
                        parrafos.append(parrafo)
                        parrafos.append(Spacer(1,12))
                    parrafos.append(Spacer(1,25))
            pdf.build(parrafos)

    def organizardiccionario(self, value, diccionario):
        for element in value:
                if element[0] not in diccionario:
                    diccionario[element[0]] = []
                    diccionario[element[0]].append(element[1])
                else:
                    diccionario[element[0]].append(element[1])
        return diccionario



    def setupInputs(self, Form, registro, subtabla=False):
        # se eliminan los inputs anteriores
        self.listaregistros_editarregistros = []
        columnas = getPermisos('tabla_final')["read"]
        columnas_write = getPermisos('tabla_final')["write"]
        #print('registroooo tabla',registro)
        lista_columnas = columnas.split(',')
        lista_columnas_write = columnas_write.split(',')
        propiedades_columnas = listaDescribe('tabla_final',lista_columnas)
        lista_write = []
        for i, col in enumerate(lista_columnas_write):
            name_input = f"input_{i}"
            lista_write.append(col)

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
            elif col in lista_write:
                widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col)
                layout.addWidget(widget)
                if 'tinyint' in tipo_dato:
                    r0,r1 = crearRadioButton(self, name_input, registro[col],col)
                    layout.addWidget(r0)
                    layout.addWidget(r1)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input, registro[col],col, enable=False)
                layout.addWidget(r0)
                layout.addWidget(r1)

            else:
                widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col, enable=False)
                layout.addWidget(widget)
                
            if registro[col] is not None:
                self.listaregistros_editarregistros.append((col,registro[col]))
                
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
        listaderegistros = []
        tablename = nombre_tabla
        if nombre_tabla == "no_facturas":
            tablename = 'facturas'
        if nombre_tabla == "no_fechas_catastro_calif":
            tablename = 'fechas_catastro_calif'
        if nombre_tabla == "no_fechas_catastro_td":
            tablename = 'fechas_catastro_td'
        if nombre_tabla == "no_fechas_rpp":
            tablename = 'fechas_rpp'
        if nombre_tabla == "no_desgloce_ppto":
            tablename = 'desgloce_ppto'
        if nombre_tabla == "bitacora_pagos":
            tablename = 'pagos'
        if nombre_tabla == "bitacora_depositos":
            tablename = 'depositos'
        columnas_write = getPermisos(nombre_tabla)["write"]
        lista_columnas_write = columnas_write.split(',')
        print(nombre_tabla,columnas_write,len(lista_columnas_write))

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
        #horizontal.addWidget(attr_label)
        #horizontal.addWidget(add_btn)
        
        if len(lista_columnas_write) > 1: 
            lastVLayout = QtWidgets.QVBoxLayout(objectName='col_eliminar')
            gridLayout.addLayout(lastVLayout,1,len(lista_columnas)+1)
            add_btn = crearBoton('+')
            add_btn.clicked.connect(partial(agregarInputsSubtabla,self,column))
            gridLayout.addWidget(add_btn,0,len(lista_columnas)+1)

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
                elif col in lista_columnas_write:
                    widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col)
                    vLayout.addWidget(widget)
                    if 'tinyint' in tipo_dato:
                        r0,r1 = crearRadioButton(self, name_input, registro[col],col)
                        vLayout.addWidget(r0)
                        vLayout.addWidget(r1)
                elif 'tinyint' in tipo_dato:
                    r0,r1 = crearRadioButton(self, name_input, registro[col],col, enable=False)
                    vLayout.addWidget(r0)
                    vLayout.addWidget(r1)
                else:
                    widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col,enable=False)
                    vLayout.addWidget(widget)
                #guardar los registros que se van a editar en una lista
                if registro[col] != '':
                    self.diccionarioregistros_editarregistros_subtablas[tablename] = []
                    listaderegistros.append((col,registro[col]))
        if listaderegistros != []:
            self.diccionarioregistros_editarregistros_subtablas[tablename] = listaderegistros

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