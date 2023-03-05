from PyQt5 import uic, QtWidgets, QtCore
from pages.EditarPrivilegios import EditarPrivilegios
import os
from bdConexion import obtener_conexion
from functools import partial

from pages.VerUsuario import VerUsuario
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado, updateTable

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/registrar-usuario.ui")))

class RegistrarUsuario(Form, Base):
    checkboxList=[]
    diccionario_permisos = {'read':{},
                            'write':{}}
    
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupTables(self)
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
        self.tablaslist.currentTextChanged.connect(self.setupColumns)
        #self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
        self.button_guardar.clicked.connect(self.crearUsuario)
        self.pushButton_cancelar.clicked.connect(self.cancelarRegistro)
        self.checkBoxAllVer.stateChanged.connect(partial(self.checkAll,"read"))
        self.checkBoxAllEscribir.stateChanged.connect(partial(self.checkAll,"write"))

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
    def setupTables(self, Form):
        lista_tablas = getListaTablas()
        self.tablaslist.addItems(lista_tablas)
    
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
    def setupColumns(self, Form):
        # se eliminan los combobox anteriores
        self.resetCombobox(self)
        self.checkBoxAllVer.setChecked(False)
        self.checkBoxAllEscribir.setChecked(False)
        tabla_seleccionada = self.tablaslist.currentText()
        columnas = getPermisos(tabla_seleccionada)["read"]
        lista_columnas = columnas.split(',')
        
        # aqui se crea el widget del checkbox y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_ver = f"acceso_{i}_read"
            name_escritura = f"acceso_{i}_write"
            setattr(self, name_ver, QtWidgets.QCheckBox(Form))
            setattr(self, name_escritura, QtWidgets.QCheckBox(Form))
            checkbox_ver = getattr(self,name_ver)
            checkbox_ver.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: white;")
            checkbox_ver.setObjectName(name_ver)
            
            checkbox_escritura = getattr(self,name_ver)
            checkbox_escritura.setText(col)
            checkbox_escritura = getattr(self,name_escritura)
            checkbox_escritura.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: white;")
            checkbox_escritura.setObjectName(name_escritura)
            checkbox_escritura.setText(col)
            # permisos de read
            self.verLayout.addWidget(checkbox_ver)
            # permisos de write
            self.escribirLayout.addWidget(checkbox_escritura)
            self.checkboxList.append(checkbox_ver)
            self.checkboxList.append(checkbox_escritura)
        # aqui se le asignan los metodos a cada checkbox y se llena el diccionario con las columnas de la tabla - Jared
        self.connectCheckboxes(self)
        self.resetCheckboxes(self)

    def checkAll(self,tipo_permiso):
        for checkbox in self.checkboxList:
            permiso = checkbox.objectName()
            permiso = permiso.split('_')[2]
            if tipo_permiso == permiso:
                checkbox.setChecked(not checkbox.isChecked())

    def resetCombobox(self, Form):
        for obj in self.checkboxList:
            permiso = obj.objectName()
            permiso = permiso.split('_')[2]
            if 'read' in permiso: self.verLayout.removeWidget(obj)
            else: self.escribirLayout.removeWidget(obj)
            obj.deleteLater()
            del obj
        self.checkboxList = []

	# este metodo le asigna un metodo a cada checkbox que ejecuta guardar_opcion al ser activado/desactivado - Jared
    def connectCheckboxes(self, Form):
        for obj in self.checkboxList:
            obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	# este metodo revisa el diccionario de permisos y activa aquellas columnas que estan guardadas como true -Jared
    def resetCheckboxes(self, Form):
        
        for permiso in self.diccionario_permisos:
            for obj in self.checkboxList:
                permiso = obj.objectName()
                permiso = permiso.split('_')[2]
                if self.tablaslist.currentText() not in self.diccionario_permisos[permiso]:
                    self.diccionario_permisos[permiso][self.tablaslist.currentText()] = {}
                if obj.text() in self.diccionario_permisos[permiso][self.tablaslist.currentText()]:
                    obj.setChecked(self.diccionario_permisos[permiso][self.tablaslist.currentText()][obj.text()])
                else:
                    obj.setChecked(False)

    '''
    En este metodo se guarda si el checkbox fue activado o no.
    El diccionario se compone por:
    Acciones (Guardar,read,Modificar) -> Nombre de tabla -> Columna: True/False
    -Jared
    '''
    def guardar_opcion(self, obj):
        permiso = obj.objectName()
        permiso = permiso.split('_')[2]
        tabla = self.tablaslist.currentText()
        columna = obj.text()
        self.diccionario_permisos[permiso][tabla][columna] = obj.isChecked()
        if permiso == 'write':
            if tabla not in self.diccionario_permisos['read']:
                self.diccionario_permisos['read'][tabla] = {}
            if columna not in self.diccionario_permisos['read'][tabla]:
                self.diccionario_permisos['read'][tabla][columna] = self.diccionario_permisos['write'][tabla][columna]
            if self.diccionario_permisos['read'][tabla][columna] == False and self.diccionario_permisos['write'][tabla][columna]:
                self.diccionario_permisos['read'][tabla][columna] = True
        print(self.diccionario_permisos)
 

    #este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
    def limpiarDict(self):
        self.diccionario_permisos = {'read':{},
                                'write':{}}
        self.resetCheckboxes(Form)

    def crearUsuario(self):
        nombre_usuario = self.lineEdit_nombreusuario.text()
        contrasena = self.lineEdit_contrasenausuario.text()
        rol = self.formatRol(self.comboBox_roles.currentText())
        if len(nombre_usuario) > 100:
            self.label_error.setText("El nombre de usuario no debe superar 100 caracteres")
            self.mensaje.setText("")
        elif len(contrasena) > 300:
            self.label_error.setText("La contraseña no debe superar los 300 caracteres")
            self.mensaje.setText("")
        elif len(contrasena)==0 or len(nombre_usuario)==0:
            self.label_error.setText("Por favor ingrese datos en ambas casillas")
            self.mensaje.setText("")
        else:
            user, pwd = getUsuarioLogueado()
            conn = obtener_conexion(user,pwd)
            cur = conn.cursor()
            if self.isUsuarioRepetido(nombre_usuario, cur):
                self.label_error.setText("El usuario ingresado ya existe")
                self.mensaje.setText("")
            else:
                print('permisossss')
                print(self.diccionario_permisos.values())
                query = f"INSERT INTO usuario(nombre_usuario,contrasena,rol) VALUES('{nombre_usuario}','{contrasena}','{rol}')"
                cur.execute(query)
                query = f"CREATE USER '{nombre_usuario}'@'localhost' IDENTIFIED BY '{contrasena}'"
                cur.execute(query)
                self.generarGrants(nombre_usuario)
                cur.close()
                conn.close()
                
                self.lineEdit_nombreusuario.setText("")
                self.lineEdit_contrasenausuario.setText("")
                self.mensaje.setText("Usuario registrado exitosamente")
                self.checkThreadTimer = QtCore.QTimer(self)
                self.checkThreadTimer.setInterval(3000)
                self.checkThreadTimer.start()
                self.checkThreadTimer.timeout.connect(partial(self.mensaje.setText,''))
                updateTable('usuario')
                self.checkBoxAllVer.setChecked(False)
                self.checkBoxAllEscribir.setChecked(False)
                self.parent().findChild(EditarPrivilegios).usuarioslist.addItem(nombre_usuario)
                self.parent().findChild(VerUsuario).setupTable(self.parent().findChild(VerUsuario))
                self.limpiarDict()
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(3000)
        self.checkThreadTimer.start()
        self.checkThreadTimer.timeout.connect(partial(self.label_error.setText,''))

    def generarGrants(self,nombre_usuario):
        query = f""
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        for llave,accion in self.diccionario_permisos.items():
            for nombre_tabla,columnas in accion.items():
                for nombre_columna,checked in columnas.items():
                    if checked:
                        if llave == 'read':
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
        self.checkBoxAllVer.setChecked(False)
        self.checkBoxAllEscribir.setChecked(False)
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
