from functools import partial
import re
from PyQt5 import QtWidgets,QtCore
from bdConexion import obtener_conexion
from usuarios import getSubtabla, getUsuarioLogueado, listaDescribe
import secrets, numpy as np, datetime, workdays
# en este archivo se generan los componentes de gui que se agregaran de forma dinamica

# esta funcion devuelve un boton de dashboard
# def dashboardButton(name):

# esta funcion devuelve un input con su respectivo label, uno de los parametros es el tipo de input, 
# segun su tipo regresa un widget diferente.
def crearInput(self,tipo_dato,name_input,nombre_tabla,registro='',col='',enable=True): # <---- este sera el metodo input()
    
    if registro is None: registro = ''
    #checar llaves foraneas y si el campo tiene llave foranea
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor()
    query=f"SELECT REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE REFERENCED_TABLE_SCHEMA = 'notarius' AND TABLE_NAME = '{nombre_tabla}' AND COLUMN_NAME = '{col}';"
    cur.execute(query)
    foreign_key = cur.fetchall()
    if len(foreign_key) > 0:
      foreign_key = foreign_key[0]
    es_fk = False
    if len(foreign_key) > 0: es_fk = True
    if es_fk:
        #select todos los resultados de la columna de la tabla
        query = f"SELECT {foreign_key[1]} FROM {foreign_key[0]};"
        cur.execute(query)
        lista_opciones = cur.fetchall()
        if len(lista_opciones) > 0:
            opciones = ['Selecciona una opcion']
            for indice,tupla in enumerate(lista_opciones):
                temp = str(lista_opciones[indice][0])
                opciones.append(temp)
        else:
            opciones = ['No existen datos para esta columna']

        #prepara combobox
        setattr(self, name_input, QtWidgets.QComboBox(self.scrollAreaWidgetContents))
        attr = getattr(self,name_input)
        attr.setStyleSheet(inputStylesheet(enable,combobox=True))
        attr.setObjectName(name_input)
        attr.addItems(opciones)
        
        attr.view().parentWidget().setStyleSheet('background-color: white;\outline:none;')

        attr.currentTextChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla, col,enable))
        attr.setCurrentIndex(0)
        attr.setEnabled(enable)    
    else:
        if 'int' in tipo_dato:   
            setattr(self, name_input, QtWidgets.QSpinBox(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            attr.setStyleSheet(inputStylesheet(enable))
            attr.setObjectName(name_input)
            attr.setMaximum(2147483647)
            registro = 1 if registro == '' else registro
            attr.valueChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla,col,enable))
            attr.setValue(registro)
            attr.setEnabled(enable)    
        elif 'date' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateEdit(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            attr.setStyleSheet(inputStylesheet(enable, True))
            attr.setObjectName(name_input)
            registro = QtCore.QDate() if registro == '' else registro
            attr.dateChanged.connect(partial(self.actualizarDict,attr,name_input,nombre_tabla, col,enable))
            attr.setDate(registro)            
            attr.setEnabled(enable)
            
                    
        elif 'varchar' in tipo_dato:
            widget = QtWidgets.QTextEdit(self.scrollAreaWidgetContents) if 'varchar(500)' in tipo_dato else QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            setattr(self, name_input, widget)
            attr = getattr(self,name_input)
            attr.setStyleSheet(inputStylesheet(enable))
            attr.setObjectName(name_input)
            max_value = self.limpiarString(tipo_dato)
            try:
                attr.setMaxLength(int(max_value))
                attr.textChanged.connect(partial(self.actualizarDict,attr,name_input,nombre_tabla, col,enable))
            except:
                attr.textChanged.connect((partial(self.on_text_changed,attr,name_input,nombre_tabla, col,enable)))
            attr.setText(registro)
            attr.setEnabled(enable)    
        elif 'decimal' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            if col == 'saldo': attr.setMinimum(-99999999.99)
            attr.setStyleSheet(inputStylesheet(enable))
            attr.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            attr.setObjectName(name_input)
            attr.setMaximum(99999999.99)
            registro = 0 if registro == '' else registro
            
            attr.valueChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla,col,enable))
            attr.setValue(registro)
            attr.setEnabled(enable)    
        elif 'enum' in tipo_dato:
            setattr(self, name_input, QtWidgets.QComboBox(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setStyleSheet(inputStylesheet(enable,combobox=True))
            attr.setObjectName(name_input)
            re_pattern = re.compile(r"[^a-z, ()]", re.I)
            opciones = re.sub(re_pattern, "", tipo_dato)            
            opciones = opciones.replace('enum(','').replace(')','')
            opciones = opciones.split(',')
            opciones.insert(0,'Seleccionar')
            attr.addItems(opciones)
            if registro == '': attr.setCurrentIndex(0)
            attr.view().parentWidget().setStyleSheet('background-color: white;\outline:none;')

            attr.currentTextChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla,col,enable))
            attr.setCurrentText(registro)
            attr.setEnabled(enable)
        elif 'timestamp' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            #attr.setDisplayFormat("yyyy-mm-dd HH:mm:ss")
            attr.setStyleSheet(inputStylesheet(enable, True))
            attr.setObjectName(name_input)
            registro = QtCore.QDate() if registro == '' else registro
            attr.dateTimeChanged.connect(partial(self.actualizarDict,attr,name_input,nombre_tabla, col,enable))
            attr.setDate(registro)
            attr.setEnabled(enable)
        self.previous[nombre_tabla] = {}
        self.previous[nombre_tabla][col] = {}
        self.previous[nombre_tabla][col][name_input] = registro
        return attr

def actualizarFechaVencimiento(self):
    #se calcula la nueva fecha de vencimiento
    fecha = self.findChild(QtWidgets.QDateEdit, 'input_16').date().toPyDate()
    end_date, cosa_inutil = calcularDia(str(fecha))
    print(end_date)
    self.findChild(QtWidgets.QDateEdit, "input_23").setDate(end_date)

def crearRadioButton(self,name_input, nombre_tabla,registro='',col='',enable=True):
        si_radiobutton = f"{name_input}_1"
        no_radiobutton = f"{name_input}_0"
        setattr(self, si_radiobutton, QtWidgets.QRadioButton("Si"))
        setattr(self, no_radiobutton, QtWidgets.QRadioButton("No"))
        setattr(self, name_input, QtWidgets.QButtonGroup(self))
        attr=getattr(self,name_input) # Number group
        r0 = getattr(self,no_radiobutton)
        attr.addButton(r0)
        r1 = getattr(self,si_radiobutton)
        attr.addButton(r1)
        r1.setStyleSheet("font: 100 14pt 'Segoe UI';\ncolor: #666666")
        r0.setStyleSheet("font: 100 14pt 'Segoe UI';\ncolor: #666666")
        r1.setEnabled(enable)
        r0.setEnabled(enable)
        r1.toggled.connect(partial(self.actualizarDict, r1,name_input,nombre_tabla,col,enable, True))
        r0.toggled.connect(partial(self.actualizarDict, r0,name_input,nombre_tabla,col, enable,False))
        if registro == 1:
            r1.setChecked(True)
        else: 
            r0.setChecked(True)
        
        return r0, r1

def inputStylesheet(enable, date=False, combobox=False):
    bg = "white" if enable else "rgba(185, 185, 185, 0.34)"

    if date: 
        stylesheet = """
        QDateTimeEdit {
            font: 15pt "Arial";\ncolor: #666666;\nbackground-color: """+bg+""";\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\nheight: 50px; padding:0 10px;
        }
        QDateEdit::drop-down{
            background-color:#957F5F;
border-top-right-radius: 8px;
border-bottom-right-radius:8px;
            height:50px;
    width:25px;
    padding: 0 5px;
    image:url(:/resources/resources/icons/calendario.png);
        }
        QDateEdit {
            font: 15pt "Arial";\ncolor: #666666;\nbackground-color: """+bg+""";\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\nheight: 50px; padding:0 10px;
        }
        QDateTimeEdit::drop-down{
            background-color:#957F5F;
border-top-right-radius: 8px;
border-bottom-right-radius:8px;
            height:50px;
    width:25px;
    padding: 0 5px;
    image:url(:/resources/resources/icons/calendario.png);
        }
        QCalendarWidget QToolButton {
height: 30px;
width: 90px;
color: white;
font-size: 16px;
icon-size: 20px, 20px;
background-color: #957F5F;
}
QCalendarWidget QMenu {
width: 90px;
color: #957F5F;
font-size: 16px;
background-color: """+bg+""";
}
QCalendarWidget QSpinBox {
width: 70px;
font-size:16px;
color: #957F5F;
background-color: """+bg+""";
selection-background-color: #957F5F;
selection-color: """+bg+""";
}
QCalendarWidget QSpinBox::up-button { subcontrol-origin: border; subcontrol-position: top right; width:20px; }
QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right; width:20px;}
QCalendarWidget QSpinBox::up-arrow { color: #957F5F; width:20px; height:20px; }
QCalendarWidget QSpinBox::down-arrow { color: #957F5F; width:20px; height:20px; }
QCalendarWidget QToolButton#qt_calendar_prevmonth 
{
    qproperty-icon: url(:/resources/resources/icons/left-arrow.png);
}
QCalendarWidget QToolButton#qt_calendar_nextmonth 
{
    qproperty-icon: url(:/resources/resources/icons/right-arrow.png);
}
/* normal days */
QCalendarWidget QAbstractItemView:enabled
{
font-size:16;
color: #957F5F;
background-color: """+bg+""";
selection-background-color: #957F5F;
selection-color:"""+bg+""";
}

/* days in other months */
/* navigation bar */
QCalendarWidget QWidget#qt_calendar_navigationbar
{
background-color: """+bg+""";
}

QCalendarWidget QAbstractItemView:disabled
{
color: #957F5F;
}

QCalendarWidget {
    border: none;
}
"""
    elif combobox:
        stylesheet = """
        QComboBox {
            font: 15pt "Arial";\ncolor: #666666;\nbackground-color: """+bg+""";\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\npadding: 10px;
        }

/* style for drop down area */
QComboBox::drop-down{
border: 0px;
}
/* style for drop down arrow */
QComboBox::down-arrow {
image: url(:/resources/resources/icons/down-arrow-gray.png);
width: 20px;
height: 20px;
margin-right: 15px;
}
/* style for QComboBox after open selcet menu */
QComboBox:on {
border: 4px solid #c2dbfe;
}
/* style for list menu */
QComboBox QListView {
font-size: 16px;
border: 1px solid rgba(0, 0, 0, 10%);
padding: 5px;
background-color:"""+bg+""";
color: black;
outline: 0px;
}

/* style for list items */
QComboBox QListView::item {
padding-left: 10px;
background-color: """+bg+""";
color: black;
}
QComboBox QListView::item:hover {
background-color: #d3c393;
}
QComboBox QListView::item:selected {
background-color: #d3c393;
}

        """
    else:
        stylesheet = f"font: 100 15pt 'Arial';\ncolor: #666666;\nbackground-color: {bg};\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\npadding: 10px;"
    return  stylesheet
# esta funcion devuelve un checkbox
#

def crearBoton(text):
    button = QtWidgets.QPushButton(text)
    button.setFixedSize(40,40)
    styleSheet = """
QPushButton {
    border-radius: 20px;
    background-color: #957F5F;
    color: white;
    font-size: 18px;
    padding: 10px 10px;
}

QPushButton:hover {
    background-color: rgb(116, 91, 47);
    color: rgb(255, 255, 255);
}

QPushButton:pressed {
    border-style: inset;
    background-color: rgb(103, 80, 41);
    color: rgb(255, 255, 255);
    border: 3px solid  rgb(103, 80, 41);
}
"""
    button.setStyleSheet(styleSheet)
    return button

def calcularDia(dia):
    start_date = datetime.datetime.strptime(dia, '%Y-%m-%d')
    anio = dia[:4]
    dias_festivos = [datetime.datetime.strptime(f'{anio}-01-01', '%Y-%m-%d'), datetime.datetime.strptime(f'{anio}-05-01', '%Y-%m-%d'), datetime.datetime.strptime(f'{anio}-09-16', '%Y-%m-%d'), datetime.datetime.strptime(f'{anio}-12-25', '%Y-%m-%d')]
    dias_festivos = agregarDiasFestivos(dias_festivos, anio)
    working_days = 60
    end_date = workdays.workday(start_date,working_days,dias_festivos).date()
    return end_date,dias_festivos

def agregarDiasFestivos(lista:list, anio:str) -> list:

    #agregar el primer lunes de febrero en conmemoracion del dia de la constitucion
    holiday = np.busday_offset(anio+'-02', 0, roll='forward', weekmask='Mon')
    holiday = np.datetime_as_string(holiday, unit='D')
    lista.append(datetime.datetime.strptime(holiday,'%Y-%m-%d'))

    #agregar el tercer lunes de marzo en conmemoracion del natalicio de benito juarez
    holiday = np.busday_offset(anio+'-03', 2, roll='forward', weekmask='Mon')
    holiday = np.datetime_as_string(holiday, unit='D')
    lista.append(datetime.datetime.strptime(holiday,'%Y-%m-%d'))

    #agregar el tercer lunes de noviembre en conmemoracion de la revolucion mexicana
    holiday=np.busday_offset(anio+'-11', 2, roll='forward', weekmask='Mon')
    holiday = np.datetime_as_string(holiday, unit='D')
    lista.append(datetime.datetime.strptime(holiday,'%Y-%m-%d'))
    
    return lista
def messageBox():
    custom_box = QtWidgets.QMessageBox()
    custom_box.setWindowTitle("Confirmation")
    custom_box.setText("¿Está seguro de que quiere eliminar el registro?")
    custom_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    custom_box.setDefaultButton(QtWidgets.QMessageBox.No)
    yes_button = custom_box.button(QtWidgets.QMessageBox.Yes)
    yes_button.setText("Si")    
    styleSheet = """
        QMessageBox {
            background-color: white;
            color: #666666;
            font-size: 18px;
        }
        QMessageBox QLabel {
            color: #666666;
        }
        QMessageBox QPushButton {
            border-radius: 8px;
            background-color: #957F5F;
            color: white;
            font-size: 18px;
            padding: 10px 30px;
        }
        QMessageBox QPushButton:hover {
            background-color: rgb(116, 91, 47);
            color: rgb(255, 255, 255);
        }
        QMessageBox QPushButton:pressed {
            border-style: inset;
            background-color: rgb(103, 80, 41);
            color: rgb(255, 255, 255);
        }
    """
    custom_box.setStyleSheet(styleSheet)
    result = custom_box.exec_()
    return result

def agregarInputsSubtabla(self,column):
        nombre_tabla,select = getSubtabla(column)
        gridLayout = self.layouts[f'grid_layout_{nombre_tabla}']
        lista_columnas = select.split(',')
        propiedades_columnas = listaDescribe(nombre_tabla,lista_columnas)
        lastVLayout = gridLayout['col_eliminar']

        del_btn = crearBoton('-')
        lastVLayout.addWidget(del_btn)
        self.del_btns.append(del_btn)
        index = self.del_btns.index(del_btn)
        #index = len(lastVLayout)-1 if modificar else index
        del_btn.clicked.connect(partial(eliminarInputsSubtabla,self,index,column))
     
        for i, col in enumerate(lista_columnas):
            key = generate_unique_key(self)
            name_input = f"input_{i}_{key}"
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            
            vLayout = gridLayout[f'layout_{col}_{i}_{nombre_tabla}']
            
            if isinstance(tipo_dato, bytes):
                tipo_dato = tipo_dato.decode('utf-8')
            elif pri == 'PRI':
                    widget = crearInput(self, tipo_dato, name_input,nombre_tabla, '',col, enable=False)
                    vLayout.addWidget(widget)
            elif 'tinyint' in tipo_dato:
                r0,r1 = crearRadioButton(self, name_input,nombre_tabla, '',col)
                vLayout.addWidget(r0)
                vLayout.addWidget(r1)

            else:
                widget = crearInput(self, tipo_dato, name_input,nombre_tabla, '',col)
                vLayout.addWidget(widget)

            
def eliminarInputsSubtabla(self,index,column):
        result = messageBox()
        
        if result == QtWidgets.QMessageBox.Yes:
            nombre_tabla,select = getSubtabla(column)
            lista_columnas = select.split(',')
            
            gridLayout = self.layouts[f'grid_layout_{nombre_tabla}']
            lastVLayout = gridLayout['col_eliminar']
            widget_to_remove =  self.del_btns[index]
            widget_index = lastVLayout.indexOf(widget_to_remove)
            lastVLayout.removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()
            for i, col in enumerate(lista_columnas):
                if nombre_tabla in self.camposCambiados: 
                    if widget_index in self.camposCambiados[nombre_tabla]: 
                        if col in self.camposCambiados[nombre_tabla][widget_index]: 
                            del self.camposCambiados[nombre_tabla][widget_index][col]
                print(self.diccionarioregistros_editarregistros_subtablas[nombre_tabla])
                print('elemento a eliminar',widget_index,col)
                if nombre_tabla in self.diccionarioregistros_editarregistros_subtablas:
                    if widget_index in self.diccionarioregistros_editarregistros_subtablas[nombre_tabla]:
                        if col in self.diccionarioregistros_editarregistros_subtablas[nombre_tabla][widget_index]:
                            print('eliminado',self.diccionarioregistros_editarregistros_subtablas[nombre_tabla][widget_index][col])
                            del self.diccionarioregistros_editarregistros_subtablas[nombre_tabla][widget_index][col]
                layout = gridLayout[f'layout_{col}_{i}_{nombre_tabla}']
                widget_to_remove = layout.itemAt(widget_index).widget()
                layout.removeWidget(widget_to_remove)
                widget_to_remove.deleteLater()
            if nombre_tabla in self.camposCambiados: updateIndices(self,nombre_tabla)
            print("Confirmed")
        else:
            print("Not confirmed")
            
def updateIndices(self,nombre_tabla):
    new_dict = {}
    for i, (key, dicc) in enumerate(self.camposCambiados[nombre_tabla].items()):
        if len(dicc) > 0: 
            if i-1 == -1: new_dict[i]=dicc
            else: new_dict[i-1]=dicc
    del self.camposCambiados[nombre_tabla]
    self.camposCambiados[nombre_tabla] = {}
    self.camposCambiados[nombre_tabla] = new_dict
    
def generate_unique_key(self,length=5):
    while True:
        key = secrets.token_hex(length)
        # Check if the key is already in use
        if not is_key_in_use(self,key):
            return key

def is_key_in_use(self,key):
    if not self.previous: return False
    for col in self.previous.values():
        for used_key in col.keys():
            if key == used_key: return True
    return False  # Replace with your implementation