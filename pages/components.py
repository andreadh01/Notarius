from functools import partial
import re
from PyQt5 import uic, QtWidgets,QtGui,QtCore
from PyQt5.QtCore import Qt
from bdConexion import obtener_conexion
from usuarios import getPermisos, getSubtabla, getUsuarioLogueado, listaDescribe
# en este archivo se generan los componentes de gui que se agregaran de forma dinamica

# esta funcion devuelve un boton de dashboard
# def dashboardButton(name):

# esta funcion devuelve un input con su respectivo label, uno de los parametros es el tipo de input, 
# segun su tipo regresa un widget diferente.
def crearInput(self,tipo_dato,name_input,nombre_tabla,registro='',col='',enable=True,modificar=True): # <---- este sera el metodo input()
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
        # print(lista_opciones)
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

        attr.currentTextChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla, col))
        attr.setCurrentIndex(1)
        attr.removeItem(0)
        attr.setEnabled(enable)    
        if not modificar: attr.setEditable(True)
        return attr
    else:
        if 'int' in tipo_dato:   
            setattr(self, name_input, QtWidgets.QSpinBox(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            attr.setStyleSheet(inputStylesheet(enable))
            attr.setObjectName(name_input)
            attr.setMaximum(2147483647)
            registro = 1 if registro == '' else registro
            
            attr.valueChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla,col))
            attr.setValue(registro)
            attr.setEnabled(enable)    
            return attr
        elif 'date' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateEdit(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            attr.setStyleSheet(inputStylesheet(enable, True))
            attr.setObjectName(name_input)
            registro = QtCore.QDate() if registro == '' else registro
            attr.dateChanged.connect(partial(self.actualizarDict,attr,name_input,nombre_tabla, col))
            attr.setDate(registro)
            attr.setEnabled(enable)    
            return attr
        elif 'varchar' in tipo_dato:
            widget = QtWidgets.QTextEdit(self.scrollAreaWidgetContents) if 'varchar(500)' in tipo_dato else QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            setattr(self, name_input, widget)
            attr = getattr(self,name_input)
            attr.setStyleSheet(inputStylesheet(enable))
            attr.setObjectName(name_input)
            max_value = self.limpiarString(tipo_dato)
            try:
                attr.setMaxLength(int(max_value))
                attr.textChanged.connect(partial(self.actualizarDict,attr,name_input,nombre_tabla, col))
            except:
                attr.textChanged.connect((partial(self.on_text_changed,attr,name_input,nombre_tabla, col)))
            attr.setText(registro)
            attr.setEnabled(enable)    
            return attr
        elif 'decimal' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setStyleSheet(inputStylesheet(enable))
            attr.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            attr.setObjectName(name_input)
            attr.setMaximum(99999999.99)
            registro = 0 if registro == '' else registro
            
            attr.valueChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla,col))
            attr.setValue(registro)
            attr.setEnabled(enable)    
            return attr            
        elif 'enum' in tipo_dato:
            setattr(self, name_input, QtWidgets.QComboBox(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setStyleSheet(inputStylesheet(enable,combobox=True))
            attr.setObjectName(name_input)
            re_pattern = re.compile(r"[^a-z, ()]", re.I)
            opciones = re.sub(re_pattern, "", tipo_dato)            
            opciones = opciones.replace('enum(','').replace(')','')
            opciones = opciones.split(',')
            attr.addItems(opciones)
            
            attr.view().parentWidget().setStyleSheet('background-color: white;\outline:none;')

            attr.currentTextChanged.connect(partial(self.actualizarDict, attr,name_input,nombre_tabla,col))
            attr.setCurrentText(registro)
            attr.setEnabled(enable)    
            return attr
        elif 'timestamp' in tipo_dato:
            setattr(self, name_input, QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents))
            attr = getattr(self,name_input)
            attr.setCalendarPopup(True)
            #attr.setDisplayFormat("yyyy-mm-dd HH:mm:ss")
            attr.setStyleSheet(inputStylesheet(enable, True))
            attr.setObjectName(name_input)
            registro = QtCore.QDate() if registro == '' else registro
            attr.dateTimeChanged.connect(partial(self.actualizarDict,attr,name_input,nombre_tabla, col))
            attr.setDate(registro)
            attr.setEnabled(enable)    
            return attr

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
        r1.setStyleSheet("font: 100 11pt 'Segoe UI';\ncolor: #666666")
        r0.setStyleSheet("font: 100 11pt 'Segoe UI';\ncolor: #666666")
        r1.setEnabled(enable)
        r0.setEnabled(enable)
        r1.toggled.connect(partial(self.actualizarDict, r1,name_input,nombre_tabla,col, True))
        r0.toggled.connect(partial(self.actualizarDict, r0,name_input,nombre_tabla,col, False))
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
            font: 12pt "Arial";\ncolor: #666666;\nbackground-color: """+bg+""";\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\nheight: 50px; padding:0 10px;
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
            font: 12pt "Arial";\ncolor: #666666;\nbackground-color: """+bg+""";\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\nheight: 50px; padding:0 10px;
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
font-size: 14px;
icon-size: 20px, 20px;
background-color: #957F5F;
}
QCalendarWidget QMenu {
width: 90px;
color: #957F5F;
font-size: 14px;
background-color: """+bg+""";
}
QCalendarWidget QSpinBox {
width: 70px;
font-size:14px;
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
font-size:14;
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
            font: 12pt "Arial";\ncolor: #666666;\nbackground-color: """+bg+""";\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\npadding: 10px;
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
font-size: 12px;
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
        stylesheet = f"font: 100 12pt 'Arial';\ncolor: #666666;\nbackground-color: {bg};\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\npadding: 10px;"
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
    font-size: 16px;
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
            font-size: 16px;
        }
        QMessageBox QLabel {
            color: #666666;
        }
        QMessageBox QPushButton {
            border-radius: 8px;
            background-color: #957F5F;
            color: white;
            font-size: 16px;
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
        gridLayout = self.layouts[0]
        lista_columnas = select.split(',')
        propiedades_columnas = listaDescribe(nombre_tabla,lista_columnas)
        lastVLayout = self.verticalLayouts[0]


        del_btn = crearBoton('-')
        lastVLayout.addWidget(del_btn)
        self.del_btns.append(del_btn)
        index = self.del_btns.index(del_btn)
        del_btn.clicked.connect(partial(eliminarInputsSubtabla,self,index,column))
     
        for i, col in enumerate(lista_columnas):
            name_input = f"input_{i}"
            tipo_dato = propiedades_columnas[i][1]
            auto_increment = propiedades_columnas[i][5]
            pri = propiedades_columnas[i][3]
            
            vLayout = self.verticalLayouts[i+1]
            
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
            widget_to_remove = self.del_btns[index]
            gridLayout = self.findChild(QtWidgets.QGridLayout,f'grid_layout_{nombre_tabla}')
            lastVLayout = gridLayout.findChild(QtWidgets.QVBoxLayout,'col_eliminar')
            index = lastVLayout.indexOf(widget_to_remove)
            lastVLayout.removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()
            for i, col in enumerate(lista_columnas):
                del self.camposCambiados[nombre_tabla][index][col]
                layout = self.findChild(QtWidgets.QVBoxLayout, f'layout_{col}_{i}_{nombre_tabla}')
                widget_to_remove = layout.itemAt(index).widget()
                layout.removeWidget(widget_to_remove)
                widget_to_remove.deleteLater()
            updateIndices(self,nombre_tabla)
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