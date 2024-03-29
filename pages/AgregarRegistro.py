from functools import partial
from PyQt5 import uic,QtWidgets,QtCore
import os
import mysql.connector
import datetime
import re

from bdConexion import obtener_conexion
from pages.Tablas import Tablas
from pages.components import agregarInputsSubtabla, calcularDia, crearBoton, crearInput, crearRadioButton, actualizarFechaVencimiento
from usuarios import getAutoIncrement,  getListaTablasWrite, getNombreCompleto, getNombreCompletoSubtabla, getPermisos,  getSubtabla,  getUsuarioLogueado, getValoresTabla, listaDescribe, updateTable
from deployment import getBaseDir

base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','agregar-registros.ui'))


class AgregarRegistro(Form, Base):
    del_btns = []
    previous = {}
    cols=[]
    layouts={}
    widgetLayout=[]
    camposCambiados = {}
    saldo = 0
    cols_auto = {}
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los labels de las columnas y se agregan sus debidos inputs
        self.pushButton_confirmar.clicked.connect(self.guardarRegistro)
        self.combobox_colores.currentTextChanged.connect(self.cargarColores)
        self.pushButton_cancelar.clicked.connect(self.restartRegistro)
        if self.findChild(QtWidgets.QDateEdit, 'input_16') != None:
            print('agregar',self.findChild(QtWidgets.QDateEdit, 'input_16'))
            self.findChild(QtWidgets.QDateEdit, 'input_16').dateChanged.connect(partial(actualizarFechaVencimiento,self))
			
    def cargarColores(self):
        if 'tabla_final' not in self.camposCambiados:
            self.camposCambiados['tabla_final']={}
        
        propiedades = self.propiedadesComboBox()
        #id = self.pri_key['tabla_final'][1]
        option = self.combobox_colores.currentText()
        color = ''
        agregar_color = ''
        id = getAutoIncrement('tabla_final')
        if option == 'Trámites y pagos finalizados':
            color = '#09E513'
            color = 'green'
            
            #self.temp_dicc_colores[id] = color
            agregar_color = ("\n"
			"QComboBox {\n"
			"background-color:#09E513;\n" 
            "}")
            #self.temp_dicc_colores[id].insert(1, (propiedades + agregar_color))
        elif option == 'Tramites pendientes':
            color = '#FFFF00'
            color = 'yellow'
            #self.temp_dicc_colores[id] = color
            agregar_color = ("\n"
			"QComboBox {\n"
			"background-color: #FFFF00;\n" 
            "}")
        elif option == 'Pagos pendientes':
            color = '#FF0000'
            color = 'red'
            #self.temp_dicc_colores[id] = color
            agregar_color = ("\n"
			"QComboBox {\n"
			"background-color: #FF0000;\n" 
            "}")
        else:
            color = '#B9B9B9'
            color = 'gray'
            #self.temp_dicc_colores[id] = color
            agregar_color = ("\n"
			"QComboBox {\n"
			"background-color: #B9B9B9;\n" 
            "}")
        self.camposCambiados['tabla_final']['color'] = color
        self.combobox_colores.setStyleSheet(propiedades + agregar_color)


    
 	# en esta funcion se van a actualizar los labels y se agregaran los inputs segun los labels de las columnas
    def setupColumns(self, Form):
        registros_id = {'id_cc':'cc_fechas_cc','id_ctd':'ctd_fechas_ctd','id_rpp':'rpp_fechas_rpp'}
        columnas_val_automatico = ['saldo','fecha_vence_td','fecha_vence']
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
        restart_color = self.propiedadesComboBox()
        self.combobox_colores.setStyleSheet(restart_color)
        self.combobox_colores.setCurrentIndex(0)
        
        # aqui se crea los widgets del label con sus input y se agrega al gui
        for i, col in enumerate(lista_columnas):
            
            enable = True
            name_input = f"input_{i}"
            name_label = f'label_{i}'
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            if pri == 'PRI' or col in registros_id.keys() or col == 'color' or col == 'vencimiento_color':
                    # if col in registros_id.keys(): index = getAutoIncrement(registros_id[col])
                    # else: index = getAutoIncrement('tabla_final')
                    # widget = crearInput(self, tipo_dato, name_input,tabla,registro=index,col=col, enable=False)
                    # layout.addWidget(widget)
                    # self.cols.append(widget)
                    continue
            if col in list_nested_tables:
                self.setupInputsSubtabla(col)
                continue
            if col in columnas_val_automatico: enable=False
            setattr(self, name_label, QtWidgets.QLabel(self.scrollAreaWidgetContents))
            # Label
            attr_label = getattr(self,name_label)
            attr_label.setStyleSheet("\n"
			"font: 75 18pt;\n"
			"color: #666666;\n" 
            "font-weight: 700;")
            attr_label.setObjectName(name_label)
            attr_label.setText(getNombreCompleto(col)+': ')
            layout.addWidget(attr_label)
            self.cols.append(attr_label)
            if isinstance(tipo_dato, bytes):
                tipo_dato = tipo_dato.decode('utf-8')
            
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input,tabla, col=col,enable=enable)
                layout.addWidget(r0)
                layout.addWidget(r1)
                self.cols.append(r0)
                self.cols.append(r1)
            else:
                widget = crearInput(self, tipo_dato, name_input,tabla, col=col, enable=enable)
                if col in columnas_val_automatico: self.cols_auto[col] = widget
                layout.addWidget(widget)
                self.cols.append(widget)

    def propiedadesComboBox(self):
        css_code = ("\n"
            "QComboBox {\n"
            "    width: 30px;\n"
            "    height: 30px;\n"
            "    border-radius: 15px;\n"
            "    border: 1px solid;\n"
            "    background-color: rgb(185, 185, 185);\n"
            "    font: 75 12pt \"MS Sans Serif\";\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    border-left-width: 0px;\n"
            "    border-top-right-radius: 15px;\n"
            "    border-bottom-right-radius: 15px;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    min-width: 250px;\n"
            "    border-radius: 6px;\n"
            "    background-color: rgb(255, 255, 255);\n"
            "    padding: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView::item:hover {\n"
            "    background-color: #f0f0f0;\n"
            "}\n")
        return css_code
    
    def setupInputsSubtabla(self,column):
        nombre_tabla,select = getSubtabla(column)
        columnas = getPermisos(nombre_tabla)["write"]
        lista_columnas = select.split(',')
        propiedades_columnas = listaDescribe(nombre_tabla,lista_columnas)
        layout = self.verticalLayout
        gridLayout = QtWidgets.QGridLayout()
        self.widgetLayout.append(gridLayout)
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
        attr_label.setText(getNombreCompleto(column))
        self.cols.append(attr_label)
        #horizontal = QtWidgets.QHBoxLayout()
        layout.addWidget(attr_label)
        lastVLayout = QtWidgets.QVBoxLayout()
        self.layouts[f'grid_layout_{nombre_tabla}']['col_eliminar'] = lastVLayout
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
			"font: 75 16pt;\n"
			"color: #957F5F;\n")
            attr_label.setObjectName(name_label)
            attr_label.setText(getNombreCompletoSubtabla(nombre_tabla,col))
            #attr_label.setAlignment(Qt.AlignCenter)
            
            gridLayout.addWidget(attr_label,0,i)
            vLayout = QtWidgets.QVBoxLayout()
            self.layouts[f'grid_layout_{nombre_tabla}'][f'layout_{col}_{i}_{nombre_tabla}'] = vLayout
            gridLayout.addLayout(vLayout,1,i)
            
            
        
        
    def limpiarString(self,cadena_sucia):
        string_limpio = re.sub("[^0-9]","",cadena_sucia)
        return string_limpio

    def on_text_changed(self,attr,name_input,tabla, col,enable):
        # Get the current text in the QTextEdit
        current_text = attr.toPlainText()

        # Check if the current text length is greater than 500
        if len(current_text) > 500:
            # Truncate the text to 500 characters
            truncated_text = current_text[:500]

            # Update the QTextEdit with the truncated text
            attr.setPlainText(truncated_text)
        self.actualizarDict(attr,name_input,tabla,col,enable,attr.toPlainText())
    def resetCombobox(self, Form):

        for dicc in self.layouts.values():
            for layout in dicc.values():
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        widget = child.widget()
                        widget.deleteLater()
                        del widget
        for layout in self.widgetLayout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    widget = child.widget()
                    widget.deleteLater()
                    del widget
        for obj in self.cols:
            try: 
                self.verticalLayout.removeWidget(obj)
                obj.deleteLater()
                del obj
            except RuntimeError:
                return
        self.widgetLayout.clear()
        self.layouts.clear()
        self.cols.clear()
        self.camposCambiados.clear()

    
    def actualizarDict(self,widget,name_input,tabla,col, enable,val):
        relacionadas = {'no_facturas':'facturas','fechas_catastro_calif':'cc_fechas_cc','fechas_catastro_td':'ctd_fechas_ctd','fechas_rpp':'rpp_fechas_rpp','desgloce_ppto':'desgloce_ppto_presupuesto','pagos':'pagos_presupuesto','depositos':'depositos_presupuesto'}
        columnas_write = getPermisos(tabla)['write'].split(',')
        columnas_write_tf = getPermisos('tabla_final')['write'].split(',')
        #subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
        #relacionadas={'facturas':'no_presupuesto,escritura_id','cc_fechas_cc':'catastro_calificacion,id_cc','ctd_fechas_ctd':'catastro_td,id_ctd','rpp':'rpp_fechas_rpp,id_rpp','desgloce_ppto_presupuesto':'no_presupuesto','pagos_presupuesto':'no_presupuesto','depositos_presupuesto':'no_presupuesto'}
        tipo = str(type(val))

        if 'QDate' in tipo: val = val.toString("yyyy-MM-dd")
        if type(val) == bool: val = 1 if val else 0

        
        if tabla in relacionadas.keys():
            i = name_input.split('_')[1]
            vLayout = self.layouts[f'grid_layout_{tabla}'][f'layout_{col}_{i}_{tabla}']
            index = 'id_fechas' if 'fecha' in tabla else 'id_relacion'
            col_name = tabla if tabla != 'no_facturas' else 'facturas'
            if vLayout.indexOf(widget) != -1: key = vLayout.indexOf(widget) 
            else: return
            if tabla not in self.camposCambiados:
                self.camposCambiados[tabla] = {}
            if key not in self.camposCambiados[tabla]:
                self.camposCambiados[tabla][key] = {}
            if index not in self.camposCambiados[tabla][key]: self.camposCambiados[tabla][key][index] = getAutoIncrement(relacionadas[tabla])
            if col in columnas_write: self.camposCambiados[tabla][key][col] = val
        else:
            if tabla not in self.camposCambiados:
                self.camposCambiados[tabla] = {}
            if col in columnas_write: self.camposCambiados[tabla][col] = val                    
        
        for tabla, relacion in relacionadas.items():
            if relacion or tabla not in getListaTablasWrite(): continue
            if relacion not in self.camposCambiados: 
                self.camposCambiados[relacion] = {}
            cols_rel = getPermisos(relacion)['write'].split(',')
            col_name = tabla if tabla != 'no_facturas' else 'facturas'
            for col_rel in cols_rel:
                value = getAutoIncrement(relacion)
                if col_rel == 'id': continue
                if col_rel == 'no_presupuesto':  
                    if 'no_presupuesto' in  self.camposCambiados['tabla_final']:
                        self.camposCambiados[relacion][col_rel] =  self.camposCambiados['tabla_final']['no_presupuesto']
                        if col_name in columnas_write_tf: self.camposCambiados['tabla_final'][col_name] = value
                else: 
                    self.camposCambiados[relacion][col_rel] = value
                    if col_rel in columnas_write_tf: self.camposCambiados['tabla_final'][col_rel] = value
                    if col_name in columnas_write_tf: self.camposCambiados['tabla_final'][col_name] = value
        
        if col == 'cantidad':
            self.saldo = 0
            if 'pagos' in self.camposCambiados:
                
                for index,dicc in self.camposCambiados['pagos'].items():
                    self.saldo = self.saldo - dicc['cantidad']
            if 'depositos' in self.camposCambiados:
                for index,dicc in self.camposCambiados['depositos'].items():
                    self.saldo = self.saldo + dicc['cantidad']
            if 'saldo' in self.cols_auto:
                self.cols_auto['saldo'].setEnabled(True)
                self.cols_auto['saldo'].setValue(self.saldo)
                self.cols_auto['saldo'].setEnabled(False)
        if col == 'fecha_escritura':
            fecha_vencimiento,algoinservible = calcularDia(val)
            self.camposCambiados['tabla_final']['fecha_vence_td'] = fecha_vencimiento
            print(fecha_vencimiento)
            if 'fecha_vence_td' in self.cols_auto:
                self.cols_auto['fecha_vence_td'].setEnabled(True)
                self.cols_auto['fecha_vence_td'].setDate(fecha_vencimiento)
                self.cols_auto['fecha_vence_td'].setEnabled(False)
        if col == 'fecha_presentado':
            date_obj = datetime.datetime.strptime(val, '%Y-%m-%d')
            fecha_vencimiento2=date_obj+datetime.timedelta(days=90)
            tiempoactual=datetime.date.today()
            datetime_obj = datetime.datetime.combine(tiempoactual, datetime.datetime.min.time())
            diferencia = fecha_vencimiento2-datetime_obj
            diferencia = diferencia.days
            if(diferencia<7 and diferencia>0):
                    self.camposCambiados['tabla_final']['vencimiento_color'] = 'yellow'
            elif(diferencia<=0):
                    self.camposCambiados['tabla_final']['vencimiento_color'] = 'red'
            else:
                    self.camposCambiados['tabla_final']['vencimiento_color'] = 'grey'
            new_date_str = fecha_vencimiento2.strftime('%Y-%m-%d')
            self.camposCambiados['tabla_final']['fecha_vence'] = new_date_str
            if 'fecha_vence' in self.cols_auto:
                self.cols_auto['fecha_vence'].setEnabled(True)
                self.cols_auto['fecha_vence'].setDate(fecha_vencimiento2)
                self.cols_auto['fecha_vence'].setEnabled(False)
        
    def guardarRegistro(self):
        #key_id = list(self.temp_dicc_colores.keys())[0]
        lista_pagos = []
        
        tabla = 'tabla_final'
        subtablas = ['no_facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp','desgloce_ppto','pagos','depositos']

        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        tablas_con_fk = []
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        
        for tabla, dicc in self.camposCambiados.items():
            
            query = f"INSERT INTO {tabla} (" 
            vals = "values ("
            subtabla = False
            if tabla in subtablas: 
                subtabla = True
                continue
            for i, (col, val) in enumerate(dicc.items()):
                if i+1 == len(dicc): 
                    query+= f"{col}) "
                    vals+= f"'{val}');"
                else: 
                    query+=f"{col},"
                    vals+= f"'{val}', "
            if not subtabla: 
                try:
                    cur.execute(query+vals)
                    conn.commit()
                except mysql.connector.errors.IntegrityError as error:
                    self.label_exito.setStyleSheet("color:red")
                    if error.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                        self.label_exito.setText("Ese registro ya existe, búsquelo en la tabla y haga doble clic para modificarlo")
                    else:
                        self.label_exito.setText("Ha ocurrido un error, consulte al administrador")
                        print("MySQL Error: {}".format(error))
                    
                    self.checkThreadTimer = QtCore.QTimer(self)
                    self.checkThreadTimer.setInterval(10000)
                    self.checkThreadTimer.start()
                    self.checkThreadTimer.timeout.connect(partial(self.label_exito.setText,''))
                    #self.restartRegistro()
                    return

        for tabla in subtablas:
            if tabla in self.camposCambiados:
                for dicc in self.camposCambiados[tabla].values():
                    query = f"INSERT INTO {tabla} (" 
                    vals = "values ("
                    for i, (col,val) in enumerate(dicc.items()):
                        if i+1 == len(dicc): 
                            query+= f"{col}) "
                            vals+= f"'{val}');"
                        else: 
                            query+=f"{col},"
                            vals+= f"'{val}', "
                    
                    cur.execute(query+vals)
                    conn.commit()
                                
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
        #cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()

        #registro = getRegistroBD('tabla_final','id',self.camposCambiados['tabla_final']['id'])[0]
        updateTable('tabla_final')
        self.label_exito.setStyleSheet("color:green")
        self.label_exito.setText("Registro guardado exitosamente")
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(10000)
        self.checkThreadTimer.start()
        self.checkThreadTimer.timeout.connect(partial(self.label_exito.setText,''))
        self.parent().findChild(Tablas).tabla(self.parent().findChild(Tablas))
        self.restartRegistro()
                
        #insert into {nombre_tabla} (cols[0]) cols[1]
        # Aquí se ponen los colores en la base de datos pero con el root para q no haya pedos
        # conn = obtener_conexion('root','')
        # cur = conn.cursor()
        # color_status = self.temp_dicc_colores[key_id]
        # query = f"UPDATE tabla_final SET color = '{color_status}' WHERE id = {key_id}"
        # cur.execute(query)
        # conn.commit()
        # cur.close()
        # conn.close()
        
        #registro = getRegistroBD('tabla_final','id',self.camposCambiados['tabla_final']['id'])[0]
        updateTable('tabla_final')
        self.label_exito.setStyleSheet("color:green")
        self.label_exito.setText("Registro guardado exitosamente")
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(10000)
        self.checkThreadTimer.start()
        self.checkThreadTimer.timeout.connect(partial(self.label_exito.setText,''))
        self.parent().findChild(Tablas).tabla(self.parent().findChild(Tablas))
        self.restartRegistro()
                
        #insert into {nombre_tabla} (cols[0]) cols[1]
        #self.temp_dicc_colores.clear()

    def restartRegistro(self):
        propiedades = self.propiedadesComboBox()
        agregar_color = ("\n"
			"QComboBox {\n"
			"background-color: #B9B9B9;\n" 
            "}")
        self.combobox_colores.setStyleSheet(propiedades + agregar_color)
        self.combobox_colores.setCurrentText('Ninguno')
        self.setupColumns(self)
    
    def reject(self) -> None:
        return

    def llavesForaneas(self):
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT TABLE_NAME,COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE CONSTRAINT_SCHEMA = 'notarius' AND REFERENCED_TABLE_NAME IS NOT NULL")
        foreign_keys = {}
        for table_name, column_name, referenced_table_name, referenced_column_name in cur:
            if table_name not in foreign_keys:
                foreign_keys[table_name] = []
            foreign_keys[table_name].append((column_name, referenced_table_name, referenced_column_name)) # agregar los valores en una tupla
        cur.close()
        conn.close()
        return foreign_keys