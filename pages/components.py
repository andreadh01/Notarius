from functools import partial
import re
from PyQt5 import uic, QtWidgets,QtCore
# en este archivo se generan los componentes de gui que se agregaran de forma dinamica

# esta funcion devuelve un boton de dashboard
# def dashboardButton(name):

# esta funcion devuelve un input con su respectivo label, uno de los parametros es el tipo de input, 
# segun su tipo regresa un widget diferente.
def crearInput(self,tipo_dato,name_input, registro='',col='',enable=True): # <---- este sera el metodo input()
    if 'int' in tipo_dato:   
        setattr(self, name_input, QtWidgets.QSpinBox(self.scrollAreaWidgetContents))
        attr = getattr(self,name_input)
        attr.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        attr.setStyleSheet(inputStylesheet(enable))
        attr.setObjectName(name_input)
        attr.setMaximum(2147483647)
        registro = 1 if registro == '' else registro
        
        attr.valueChanged.connect(partial(self.actualizarDict, col))
        attr.setValue(registro)
        attr.setEnabled(enable)    
        return attr
    elif 'date' in tipo_dato:
        setattr(self, name_input, QtWidgets.QDateEdit(self.scrollAreaWidgetContents))
        attr = getattr(self,name_input)
        attr.setCalendarPopup(True)
        attr.setStyleSheet(inputStylesheet(enable, True))
        attr.setObjectName(name_input)
        registro = QtCore.QDate.currentDate() if registro == '' else registro
        
        attr.dateChanged.connect(partial(self.actualizarDict, col))
        attr.setDate(registro)
        attr.setEnabled(enable)    
        return attr
    elif 'varchar' in tipo_dato:
        setattr(self, name_input, QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
        attr = getattr(self,name_input)
        attr.setStyleSheet(inputStylesheet(enable))
        attr.setObjectName(name_input)
        max_value = self.limpiarString(tipo_dato)
        attr.setMaxLength(int(max_value))
        
        attr.textChanged.connect(partial(self.actualizarDict, col))
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
        
        attr.valueChanged.connect(partial(self.actualizarDict, col))
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

        attr.currentTextChanged.connect(partial(self.actualizarDict, col))
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
        registro = QtCore.QDate.currentDate() if registro == '' else registro

        
        attr.dateTimeChanged.connect(partial(self.actualizarDict, col))
        attr.setDate(registro)
        attr.setEnabled(enable)    
        return attr

def crearRadioButton(self,name_input, registro='',col=''):
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
        r1.setStyleSheet("font: 100 12pt 'Arial';\ncolor: #666666")
        r0.setStyleSheet("font: 100 12pt 'Arial';\ncolor: #666666")
        r1.toggled.connect(partial(self.actualizarDict, col, True))
        r0.toggled.connect(partial(self.actualizarDict, col, False))
        print("rad btn registro")
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
            font: 12pt "Arial";\ncolor: #666666;\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\nheight: 50px; padding:0 10px;
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
            font: 12pt "Arial";\ncolor: #666666;\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\nheight: 50px; padding:0 10px;
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
background-color: white;
}
QCalendarWidget QSpinBox {
width: 70px;
font-size:14px;
color: #957F5F;
background-color: white;
selection-background-color: #957F5F;
selection-color: white;
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
background-color: white;
selection-background-color: #957F5F;
selection-color:white;
}

/* days in other months */
/* navigation bar */
QCalendarWidget QWidget#qt_calendar_navigationbar
{
background-color: white;
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
            font: 12pt "Arial";\ncolor: #666666;\nborder-radius: 8px;\nborder: 1px solid #CCCCCC;\npadding: 10px;
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
background-color: #fff;
outline: 0px;
}

/* style for list items */
QComboBox QListView::item {
padding-left: 10px;
background-color: #fff;
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
