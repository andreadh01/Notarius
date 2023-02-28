from PyQt5 import uic
import os
from bdConexion import obtener_conexion

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/editar-registro.ui")))

class EditarRegistro(Form, Base):
    
    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
    
    # este metodo carga los labels
    def createLabels(self, Form, index=None):
        print(index)
    #     conn = obtener_conexion()
    #     cur = conn.cursor()
    #     query = 'SELECT * FROM {} WHERE {'columna_0'}='{valor_col_0}''
    #     cur.execute(query)
    #     tablas = cur.fetchall()
    #     cur.close()
    #     conn.close()
    #     lista_tablas = [tabla[0] for tabla in tablas]
        
    # este metodo le da el valor a los labels del registro a modificar
    
    # este metodo carga las tablas
    
    # este metodo carga todos los registros en un combobox (el id para seleccionar)