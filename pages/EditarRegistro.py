from functools import partial
import re
from PyQt5 import uic, QtWidgets
import os
from bdConexion import obtener_conexion
from pages.components import agregarInputsSubtabla, crearBoton, crearInput, crearRadioButton, eliminarInputsSubtabla, messageBox
from usuarios import getAllPermisos, getAutoIncrement, getPermisos, getRegistro, getRegistroBD, getRegistrosSubtabla, getSubtabla, getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable
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
    pri_key = {}
    del_btns = []
    tabla = ''
    layouts={}
    tablas_agregar = {}
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
        registros_id = {'id_cc':'cc_fechas_cc','id_ctd':'ctd_fechas_ctd','id_rpp':'rpp_fechas_rpp'}
        

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
                    if col in registros_id.keys(): self.pri_key[registros_id[col]] = (col,registro[col])
                    else: self.pri_key['tabla_final'] = (col,registro[col])
                    widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col, enable=False)
                    layout.addWidget(widget)
            elif col in lista_columnas_write:
                widget = crearInput(self, tipo_dato, name_input,'tabla_final', registro[col],col)
                layout.addWidget(widget)
                if 'tinyint' in tipo_dato:
                    r0,r1 = crearRadioButton(self, name_input, 'tabla_final',registro[col],col)
                    layout.addWidget(r0)
                    layout.addWidget(r1)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input, 'tabla_final',registro[col],col, enable=False)
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

    def on_text_changed(self,attr,name_input,tabla, col):
        # Get the current text in the QTextEdit
        current_text = attr.toPlainText()

        # Check if the current text length is greater than 500
        if len(current_text) > 500:
            # Truncate the text to 500 characters
            truncated_text = current_text[:500]

            # Update the QTextEdit with the truncated text
            attr.setPlainText(truncated_text)
        self.actualizarDict(attr,name_input,tabla,col,attr.toPlainText())
   
    def setupInputsSubtabla(self,column,registros):
        nombre_tabla,select = getSubtabla(column)
        listaderegistros = []
        relacionadas = {'no_facturas':'facturas','fechas_catastro_calif':'cc_fechas_cc','fechas_catastro_td':'ctd_fechas_ctd','fechas_rpp':'rpp_fechas_rpp','desgloce_ppto':'desgloce_ppto_presupuesto','pagos':'pagos_presupuesto','depositos':'depositos_presupuesto'}

        columnas_write = getPermisos(nombre_tabla)["write"]
        lista_columnas_write = columnas_write.split(',')

        lista_columnas = select.split(',')
        propiedades_columnas = listaDescribe(nombre_tabla,lista_columnas)
        layout = self.verticalLayout
        gridLayout = QtWidgets.QGridLayout()
        self.layouts[f'grid_layout_{nombre_tabla}'] = {}
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
            lastVLayout = QtWidgets.QVBoxLayout()
            self.layouts[f'grid_layout_{nombre_tabla}']['col_eliminar'] = lastVLayout
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
            vLayout = QtWidgets.QVBoxLayout()
            self.layouts[f'grid_layout_{nombre_tabla}'][f'layout_{col}_{i}_{nombre_tabla}'] = vLayout
            gridLayout.addLayout(vLayout,1,i)
            
            for registro in registros:
                if isinstance(tipo_dato, bytes):
                    tipo_dato = tipo_dato.decode('utf-8')
                elif pri == 'PRI': 
                    widget = crearInput(self, tipo_dato, name_input,nombre_tabla, registro[col],col, enable=False)
                    vLayout.addWidget(widget)
                elif col in lista_columnas_write:
                    widget = crearInput(self, tipo_dato, name_input,nombre_tabla, registro[col],col)
                    vLayout.addWidget(widget)
                    if 'tinyint' in tipo_dato:
                        r0,r1 = crearRadioButton(self, name_input,nombre_tabla, registro[col],col)
                        vLayout.addWidget(r0)
                        vLayout.addWidget(r1)
                elif 'tinyint' in tipo_dato:
                    r0,r1 = crearRadioButton(self, name_input, nombre_tabla,registro[col],col, enable=False)
                    vLayout.addWidget(r0)
                    vLayout.addWidget(r1)
                else:
                    widget = crearInput(self, tipo_dato, name_input,nombre_tabla, registro[col],col,enable=False)
                    vLayout.addWidget(widget)
                #guardar los registros que se van a editar en una lista
                if registro[col] != '':
                    self.diccionarioregistros_editarregistros_subtablas[nombre_tabla] = []
                    listaderegistros.append((col,registro[col]))
               
                       
        if listaderegistros != []:
            self.diccionarioregistros_editarregistros_subtablas[nombre_tabla] = listaderegistros

        layout.addLayout(gridLayout)

    def changePage(self):
        from pages.Tablas import Tablas
        self.camposCambiados.clear()
        
        #obtener los permisos del usuario para la tabla seleccionada
        self.parent().setCurrentIndex(self.parent().indexOf(self.parent().findChild(Tablas)))
        
    
    def actualizarDict(self,widget,name_input,tabla,col, val):
        relacionadas = {'no_facturas':'facturas','fechas_catastro_calif':'cc_fechas_cc','fechas_catastro_td':'ctd_fechas_ctd','fechas_rpp':'rpp_fechas_rpp','desgloce_ppto':'desgloce_ppto_presupuesto','pagos':'pagos_presupuesto','depositos':'depositos_presupuesto'}
        #subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
        #relacionadas={'facturas':'no_presupuesto,escritura_id','cc_fechas_cc':'catastro_calificacion,id_cc','ctd_fechas_ctd':'catastro_td,id_ctd','rpp':'rpp_fechas_rpp,id_rpp','desgloce_ppto_presupuesto':'no_presupuesto','pagos_presupuesto':'no_presupuesto','depositos_presupuesto':'no_presupuesto'}
        
        
        
        
        if tabla not in self.pri_key: self.pri_key[tabla] = {}
        if tabla not in self.tablas_agregar: self.tablas_agregar[tabla] = {}
        
        tipo = str(type(val))
        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        if type(val) == bool: val = 1 if val else 0
        if val is None: val = ''
        if tabla in relacionadas.keys():
            i = name_input.split('_')[1]
            vLayout = self.layouts[f'grid_layout_{tabla}'][f'layout_{col}_{i}_{tabla}']
            index = 'id_fechas' if 'fecha' in tabla else 'id_relacion'
            col_name = tabla if tabla != 'no_facturas' else 'facturas'
            if vLayout.indexOf(widget) != -1: key = vLayout.indexOf(widget) 
            else: return
            id_col = self.pri_key['tabla_final'][0]
            id_val = self.pri_key['tabla_final'][1]
            registro_id = getRegistro('tabla_final',id_col,id_val)[col_name]
            if registro_id is None: 
                relacion = relacionadas[tabla]
                value = getAutoIncrement(relacion)
                if tabla not in self.tablas_agregar:
                    self.tablas_agregar[tabla] = {}
                if key not in self.tablas_agregar[tabla]: self.tablas_agregar[tabla][key] = {}
                if index not in self.tablas_agregar[tabla][key]: self.tablas_agregar[tabla][key][index] = getAutoIncrement(relacion)
                self.tablas_agregar[tabla][key][col] = val
                if relacion not in self.tablas_agregar:
                    self.tablas_agregar[relacion] = {}
                cols_rel = getPermisos(relacion)['read'].split(',')
                # estas son las columnas de las tablas que se tienen que agregar NO UPDATE
                for col_rel in cols_rel:
                    if col_rel == 'id': continue
                    if col_rel == 'no_presupuesto':  
                        self.tablas_agregar[relacion][col_rel] =  self.camposCambiados['tabla_final']['no_presupuesto']
                    else: 
                        self.tablas_agregar[relacion][col_rel] = value
            else: 
                # si ya existe un registro en la columna, se puede hace update
                self.pri_key[relacionadas[tabla]] = ('id',registro_id)
                if tabla not in self.camposCambiados:
                    self.camposCambiados[tabla] = {}
                if key not in self.camposCambiados[tabla]:
                    self.camposCambiados[tabla][key] = {}
                if index not in self.camposCambiados[tabla][key]: 
                    id_col = self.pri_key['tabla_final'][0]
                    id_val = self.pri_key['tabla_final'][1]
                    registro = getRegistro('tabla_final',id_col,id_val)[col_name]
                    if registro is None:registro = getAutoIncrement(relacionadas[tabla])                    
                    self.camposCambiados[tabla][key][index] = registro
                self.camposCambiados[tabla][key][col] = val
        else:
            if tabla not in self.camposCambiados:
                self.camposCambiados[tabla] = {}
            self.camposCambiados[tabla][col] = val                    
        
        for subtabla, relacion in relacionadas.items():
            if relacion not in self.camposCambiados: 
                self.camposCambiados[relacion] = {}
            cols_rel = getPermisos(relacion)['read'].split(',')
            col_name = subtabla if subtabla != 'no_facturas' else 'facturas'
            print(cols_rel)
            for col_rel in cols_rel:
                id_col = self.pri_key['tabla_final'][0]
                id_val = self.pri_key['tabla_final'][1]
                value = getRegistro('tabla_final',id_col,id_val)[col_name]
                if value is None: value = getAutoIncrement(relacion)
                if col_rel == 'id': continue
                if col_rel == 'no_presupuesto':  
                    if 'no_presupuesto' in  self.camposCambiados['tabla_final']:
                        self.camposCambiados[relacion][col_rel] =  self.camposCambiados['tabla_final']['no_presupuesto']
                        self.camposCambiados['tabla_final'][col_name] = value
                else: 
                    self.camposCambiados[relacion][col_rel] = value
                    self.camposCambiados['tabla_final'][col_rel] = value
                    self.camposCambiados['tabla_final'][col_name] = value
                    

        
    def actualizarRegistro(self):
        subtablas = ['no_facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp','desgloce_ppto','pagos','depositos']

        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")

        print("TABLAS DE INSERT",self.tablas_agregar)
        print("CAMPOS CAMBIADOS",self.camposCambiados)
        print("LLAVES PRIMARIAS",self.pri_key)
        
        for tabla, registro in self.tablas_agregar.items():
            query = f"INSERT INTO {tabla} (" 
            vals = "values ("
            execute = True
            if not registro: execute = False
            for i, (col,val) in enumerate(registro.items()):
                if i+1 == len(dicc): 
                    query+= f"{col}) "
                    vals+= f"'{val}');"
                else: 
                    query+=f"{col},"
                    vals+= f"'{val}', "
            if execute:
                print(query+vals)
                cur.execute(query+vals)
                conn.commit()
                    
        for tabla, dicc in self.camposCambiados.items():
            query = f"UPDATE {tabla} set " 
            subtabla = False
            execute = True
            if not dicc: execute = False
            if tabla in subtablas: 
                subtabla = True
                continue
            for i, (col, val) in enumerate(dicc.items()):
                id_col = self.pri_key[tabla][0]
                id_value = self.pri_key[tabla][1]
                if i+1 == len(dicc): query+= f"{col}='{val}' WHERE  {id_col}='{id_value}'"
                else: query+= f"{col}='{val}', "
            print(query)
            if execute and not subtabla: 
                cur.execute(query)
                conn.commit()


        for tabla in subtablas:
            if tabla in self.camposCambiados:
                for dicc in self.camposCambiados[tabla].values():
                    execute = True
                    query = f"UPDATE {tabla} set "
                    if not dicc: execute = False
                    for i, (col,val) in enumerate(dicc.items()):
                        id_col = self.pri_key[tabla][0]
                        id_value = self.pri_key[tabla][1]
                        if col == 'id': continue
                        if i+1 == len(dicc): query+= f"{col}='{val}' WHERE  {id_col}='{id_value}'"
                        else: query+= f"{col}='{val}', "
                    print(query)
                    if execute:
                        cur.execute(query)
                        conn.commit()

                    
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        cur.close()
        conn.close()
        registro = getRegistroBD('tabla_final','id',self.pri_key['tabla_final'][1])
        from pages.Tablas import Tablas
        updateTable('tabla_final')

        self.parent().findChild(Tablas).actualizarRegistro(registro)
        self.changePage()

    def reject(self) -> None:
        return