from PyQt5 import uic, QtWidgets, QtCore
from pages.EditarPrivilegios import EditarPrivilegios
import os
from bdConexion import obtener_conexion
from functools import partial

from pages.VerUsuario import VerUsuario
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/agregar-usuario.ui")))

class RegistrarUsuario(Form, Base):
    cols=[]
    diccionario_permisos = {'Ver':{},
                            'Escritura':{}}
    
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupTables(self)
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
        self.tablaslist.currentTextChanged.connect(self.setupColumns)
        self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
        self.pushButton_confirmar.clicked.connect(self.crearUsuario)
        self.pushButton_cancelar.clicked.connect(self.cancelarRegistro)

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
    def setupTables(self, Form):
        # user, pwd = getUsuarioLogueado()
        # conn = obtener_conexion(user,pwd)
        # cur = conn.cursor()
        # query = 'SHOW TABLES'
        # cur.execute(query)
        # tablas = cur.fetchall()
        # cur.close()
        # conn.close()
        # lista_tablas = [tabla[0] for tabla in tablas]
        lista_tablas = getListaTablas()
        #print(lista_tablas)
        self.tablaslist.addItems(lista_tablas)
    
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
    def setupColumns(self, Form):
        # se eliminan los combobox anteriores
        self.resetCombobox(self)
        # user, pwd = getUsuarioLogueado()
        # conn = obtener_conexion(user,pwd)
        # cur = conn.cursor()
        tabla_seleccionada = self.tablaslist.currentText()
        columnas = getPermisos(tabla_seleccionada)["SELECT"]
        lista_columnas = columnas.split(',')
        # query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= '{tabla_seleccionada}' AND TABLE_SCHEMA='notarius'"
        # cur.execute(query)
        # columnas = cur.fetchall()
        # cur.close()
        # conn.close()
        # lista_columnas = [col[0] for col in columnas]
        # aqui se crea el widget del checkbox y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name = f"acceso_{i}"
            setattr(self, name, QtWidgets.QCheckBox(Form))
            attr = getattr(self,name)
            attr.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: rgb(149, 117, 61);")
            attr.setObjectName(name)
            attr.setText(col)
            self.gridLayout.addWidget(attr, i+1, 2, 1, 1)
            self.cols.append(attr)
        # aqui se le asignan los metodos a cada checkbox y se llena el diccionario con las columnas de la tabla - Jared
        self.connectCheckboxes(self)
        self.resetCheckboxes(self)

    def resetCombobox(self, Form):
        for obj in self.cols:
            self.gridLayout.removeWidget(obj)
            obj.deleteLater()
            del obj
        self.cols = []

	# este metodo le asigna un metodo a cada checkbox que ejecuta guardar_opcion al ser activado/desactivado - Jared
    def connectCheckboxes(self, Form):
        for obj in self.cols:
            obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	# este metodo revisa el diccionario de permisos y activa aquellas columnas que estan guardadas como true -Jared
    def resetCheckboxes(self, Form):
        for permiso in self.diccionario_permisos:
            for obj in self.cols:
                if self.tablaslist.currentText() not in self.diccionario_permisos[self.accioneslist.currentText()]:
                    self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()] = {}
                if obj.text() in self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()]:
                    obj.setChecked(self.diccionario_permisos[self.accioneslist.currentText()][self.tablaslist.currentText()][obj.text()])
                else:
                    obj.setChecked(False)

    '''
    En este metodo se guarda si el checkbox fue activado o no.
    El diccionario se compone por:
    Acciones (Ver, Escritura) -> Nombre de tabla -> Columna: True/False
    -Jared
    '''
    def guardar_opcion(self, obj):
        tabla = self.tablaslist.currentText()
        columna = obj.text()
        self.diccionario_permisos[self.accioneslist.currentText()][tabla][columna] = obj.isChecked()
        if self.accioneslist.currentText() == 'Escritura':
            if tabla not in self.diccionario_permisos['Ver']:
                self.diccionario_permisos['Ver'][tabla] = {}
            if columna not in self.diccionario_permisos['Ver'][tabla]:
                self.diccionario_permisos['Ver'][tabla][columna] = self.diccionario_permisos['Escritura'][tabla][columna]
            if self.diccionario_permisos['Ver'][tabla][columna] == False and self.diccionario_permisos['Escritura'][tabla][columna]:
                self.diccionario_permisos['Ver'][tabla][columna] = True
 

    #este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
    def limpiarDict(self):
        self.diccionario_permisos = {'Ver':{},
                                'Escritura':{}}
        self.resetCheckboxes(Form)

    def crearUsuario(self):
        nombre_usuario = self.lineEdit_nombreusuario.text()
        contrasena = self.lineEdit_contrasenausuario.text()
        rol = self.formatRol(self.comboBox_roles.currentText())
        if len(nombre_usuario) > 100:
            self.label_error.setText("El nombre de usuario no debe superar 100 caracteres")
            self.label_exito.setText("")
        elif len(contrasena) > 300:
            self.label_error.setText("La contraseña no debe superar los 300 caracteres")
            self.label_exito.setText("")
        elif len(contrasena)==0 or len(nombre_usuario)==0:
            self.label_error.setText("Por favor ingrese datos en ambas casillas")
            self.label_exito.setText("")
        else:
            user, pwd = getUsuarioLogueado()
            conn = obtener_conexion(user,pwd)
            cur = conn.cursor()
            if self.isUsuarioRepetido(nombre_usuario, cur):
                self.label_error.setText("El usuario ingresado ya existe")
                self.label_exito.setText("")
            else:
                query = f"INSERT INTO usuario(nombre_usuario,contrasena,rol) VALUES('{nombre_usuario}','{contrasena}','{rol}')"
                cur.execute(query)
                query = f"CREATE USER '{nombre_usuario}'@'localhost' IDENTIFIED BY '{contrasena}'"
                cur.execute(query)
                self.generarGrants(nombre_usuario)
                cur.close()
                conn.close()
                
                self.lineEdit_nombreusuario.setText("")
                self.lineEdit_contrasenausuario.setText("")
                self.label_error.setText("")
                self.label_exito.setText("Usuario registrado exitosamente")
                timer = QtCore.QTimer()
                timer.timeout.connect(partial(self.label_exito.setText,''))
                timer.start(1000)
                self.parent().findChild(EditarPrivilegios).usuarioslist.addItem(nombre_usuario)
                self.parent().findChild(VerUsuario).setupTable(self.parent().findChild(VerUsuario))
                self.limpiarDict()

    def generarGrants(self,nombre_usuario):
        query = f""
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        for llave,accion in self.diccionario_permisos.items():
            for nombre_tabla,columnas in accion.items():
                for nombre_columna,checked in columnas.items():
                    if checked:
                        if llave == 'Ver':
                            query=f"GRANT SELECT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
                            cur.execute(query)
                        else:
                            query=f"GRANT INSERT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
                            cur.execute(query)
                            query=f"GRANT UPDATE ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost';"
                            cur.execute(query)
                        
        cur.close()
        conn.close()
    
    def cancelarRegistro(self):
        self.lineEdit_nombreusuario.setText("")
        self.lineEdit_contrasenausuario.setText("")
        self.limpiarDict()

    def formatRol(self,rol_unformat):
        if rol_unformat == 'Administrador':
            return 'admin'
        elif rol_unformat == 'Empleado':
            return 'empleado'
        elif rol_unformat == 'Proyectista':
            return 'proyectista'
        elif rol_unformat == 'Armadores':
            return 'armadores'
        else:
            return 'otro' 

    def isUsuarioRepetido(self,nombre_usuario,cur):
        query = f"SELECT * FROM usuario WHERE nombre_usuario ='{nombre_usuario}'"
        cur.execute(query)
        usuarios = cur.fetchall()
        if len(usuarios) == 0:
            repetido = False
        else:
            repetido = True
        return repetido
