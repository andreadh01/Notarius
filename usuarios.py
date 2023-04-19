# en este archivo se van a ejecutar funciones que nos daran los permisos que tienen los usuarios,
# para poder mostrar los campos adecuados en select * y crear el dashboard adecuado para cada usuario
from bdConexion import obtener_conexion
dict_permisos = {}
usuario = {'user':'','pwd':''}
lista_tablas = []
lista_tablas_write = []
all_tablas = {}

def saveSession(user,pwd):
    global usuario
    usuario["user"] = user
    usuario["pwd"] = pwd
    listaTablas(user,pwd)
    showGrants(user, pwd)
    permisosRead()


def clearSession():
    usuario.clear()
    dict_permisos.clear()
    lista_tablas.clear()
    all_tablas.clear()
    all_tablas.clear()
    lista_tablas_write.clear()
    
def getUsuarioLogueado():
    return usuario["user"], usuario["pwd"];

def listaTablas(user,pwd):
		global lista_tablas
		conn = obtener_conexion(user, pwd)
		cur = conn.cursor()
		query = 'SHOW TABLES'
		cur.execute(query)
		tablas = cur.fetchall()
		cur.close()
		conn.close()
		lista_tablas = [tabla[0] for tabla in tablas]

# devuelve las columnas a las que el usuario tiene acceso (en select, update y insert) en la tabla indicada
def getPermisos(tabla):
    return dict_permisos[tabla]

def getListaTablas():
    return lista_tablas

def listaDescribe(tabla, columnas):
    conn = obtener_conexion(usuario["user"],usuario["pwd"])
    cur = conn.cursor()
    lista = []
    for col in columnas:
        query=f"DESCRIBE {tabla} {col}"
        cur.execute(query)
        description = cur.fetchone()
        lista.append(description)
    cur.fetchall()
    cur.close()
    conn.close()
    return lista

def permisosAdmin():
    conn = obtener_conexion(usuario["user"],usuario["pwd"])
    cur = conn.cursor()
    for tabla in lista_tablas:
        permisos = {}
        query=f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= '{tabla}' AND TABLE_SCHEMA='notarius'"
        cur.execute(query)
        columnas = cur.fetchall()
        lista_columnas = [col[0] for col in columnas]
        lista_columnas = ','.join(lista_columnas)
        permisos["read"] = lista_columnas 
        
        permisos["write"] = lista_columnas
        #permisos["UPDATE"] = lista_columnas
        dict_permisos[tabla] = permisos
        lista_tablas_write.append(tabla)

    cur.close()
    conn.close()

def showGrants(user, pwd):
	conn = obtener_conexion(user,pwd)
	cur = conn.cursor()
	query=f"SHOW GRANTS FOR '{user}'@'localhost';"
	cur.execute(query)
	permisos = cur.fetchall()
	cur.close()
	conn.close()
	lista_permisos = [permisos[0] for permisos in permisos[1:]]
	limpiar_lista_permisos(lista_permisos)

def limpiar_lista_permisos(lista_permisos):
	for texto in lista_permisos:
		subcadena_select = ''
		subcadena_insert = ''
		subcadena_update = ''
		if 'GRANT ALL PRIVILEGES' in texto: 
			permisosAdmin()
			break
		permisos = {}
		select_i = texto.find("SELECT")
		insert_i = texto.find("INSERT")
		update_i = texto.find("UPDATE")
		notarius_i = texto.find("notarius")
		to_i = texto.find("TO")
		nombre_tabla = texto[notarius_i+11:to_i-2]
		if "SELECT" in texto:
			par_i = texto.find(')')
			subcadena_select = texto[select_i:par_i]
			subcadena_select = subcadena_select.replace("(","")
			par_i=texto.find(')', texto.find(')')+1)
			subcadena_insert = texto[insert_i:par_i]
			subcadena_insert = subcadena_insert.replace("(","")
			par_i = texto.rfind(')')
			subcadena_update = texto[update_i:par_i]
			subcadena_update = subcadena_update.replace("(","")
		else:
			par_i = texto.find(')')
			subcadena_insert = texto[insert_i:par_i]
			subcadena_insert = subcadena_insert.replace("(","")
			par_i = texto.rfind(')')
			subcadena_update = texto[update_i:par_i]
			subcadena_update = subcadena_update.replace("(","")
		permiso_select = (subcadena_select.replace(", ",",")).split(" ")
		#permiso_insert = (subcadena_insert.replace(", ",",")).split(" ")
		permiso_update = (subcadena_update.replace(", ",",")).split(" ")
		#lista_columnas = lista_columnas.append('id')
		#permisos["INSERT"] = permiso_insert[1] if len(permiso_insert) > 1 else ''
		permisos["read"] = permiso_select[1] if len(permiso_select) > 1 else ''
		permisos["write"] = permiso_update[1] if len(permiso_update) > 1 else ''
		if permisos["write"] != '':
			if 'id' not in permisos["write"]: permisos["write"]=f"id,{permisos['write']}"
			lista_tablas_write.append(nombre_tabla)
			#print("el usuario puede escribir en",lista_tablas_write)
		#permisos["write"] = f"id,{str(permisos["write"])}"
		dict_permisos[nombre_tabla] = permisos
		

def getAllPermisos():
	return dict_permisos

def tablaToDict(user, pwd):
    dict_permisos = getAllPermisos()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    for tabla, permisos in dict_permisos.items():
        select = permisos["read"]
        if tabla == 'tabla_final': query = f"SELECT {select} FROM {tabla} order by no_escritura asc"
        else: query = f"SELECT {select} FROM {tabla}"
        cur.execute(query)
        valores = cur.fetchall()
        all_tablas[tabla] = valores
    cur.close()
    conn.close()

def updateTable(tabla):
    permisos = getPermisos(tabla)
    conn = obtener_conexion(usuario["user"],usuario["pwd"])
    cur = conn.cursor(dictionary=True)
    select = permisos["read"]
    if tabla == 'tabla_final': query = f"SELECT {select} FROM {tabla} order by no_escritura asc"
    else: query = f"SELECT {select} FROM {tabla}"
    cur.execute(query)
    valores = cur.fetchall()
    all_tablas[tabla] = valores
    cur.close()
    conn.close()

def getValoresTabla(tabla):
    return all_tablas[tabla]

def getListaTablasWrite():
    return lista_tablas_write
def getRegistro(tabla, col, value):
    for registro in all_tablas[tabla]:
        if registro[col] == value: 
            return registro

def getRegistroBD(tabla,col,value):
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    select = dict_permisos[tabla]["read"]
    cur.execute(f'SELECT {select} FROM {tabla} WHERE {col}="{value}"')
    registro = cur.fetchall()
    cur.close()
    conn.close()
    return registro
def getLastElement(tabla):
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    select = dict_permisos[tabla]["read"]
    cur.execute(f"SELECT {select} FROM {tabla} ORDER BY id DESC LIMIT 1")
    registro = cur.fetchone()
    cur.close()
    conn.close()
    return registro

# este metodo va a regresar en orden las columnas de una tabla que el usuario va a visualizat
def permisosRead():
    user, pwd = getUsuarioLogueado()
    tablas = getListaTablas()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    for tabla in tablas:
        query = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabla}' and TABLE_SCHEMA='NOTARIUS'"
        cur.execute(query)
        valores = cur.fetchall()
        valores_read = generarString(valores)
        valores_write = ordenarPermisosWrite(valores,tabla)
        dict_permisos[tabla]['read'] = valores_read
        dict_permisos[tabla]['write'] = valores_write
        
    cur.close()
    conn.close()

def getAutoIncrement(tabla):
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    select = dict_permisos[tabla]["read"]
    cur.execute(f"SHOW TABLE STATUS LIKE '{tabla}'")
    result = cur.fetchone()
    next_auto_increment = result['Auto_increment']
    cur.close()
    conn.close()
    return next_auto_increment
def ordenarPermisosWrite(lista,tabla):
        values = []
        for i, dicc in enumerate(lista):
            for value in dicc.values():
                if value in dict_permisos[tabla]['write']:
                    values.append(value)
                    
        return ','.join(values)        
def generarString(lista):
        st = []
        for dicc in lista:
            for value in dicc.values():
                st.append(value)
        return ','.join(st)

def getSubtabla(col):
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)

    subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
    nombre_tabla = subtablas[col][0]
    select = subtablas[col][1].split(',')
    select_permisos = []
    query = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{nombre_tabla}' and TABLE_SCHEMA='NOTARIUS'"
    cur.execute(query)
    valores = cur.fetchall()
    cur.close()
    conn.close()
    #aqui se eliminan aquellas columnas que el usuario no tiene permitido visualizar
    for dicc in valores:
        for value in dicc.values():
            if value in select: select_permisos.append(value)
    
    
    
    return nombre_tabla, ','.join(select_permisos)
def getRegistrosSubtabla(col,id_registro):
    index = 'id_fechas' if "fecha" in col else 'id_relacion'
    nombre_tabla, select = getSubtabla(col)
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    query = f"SELECT {select} FROM {nombre_tabla} WHERE {index} = '{id_registro}'"
    #print(query)
    cur.execute(query)
    valores = cur.fetchall()
    cur.close()
    conn.close()
    return valores

def getTablaRelacionada(col):
    user, pwd = getUsuarioLogueado()
    conn = obtener_conexion(user,pwd)
    cur = conn.cursor(dictionary=True)
    query = f" SELECT DISTINCT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME IN ('{col}') AND TABLE_SCHEMA='notarius' AND TABLE_NAME != 'tabla_final'"
    cur.execute(query)
    valores = cur.fetchall()
    cur.close()
    conn.close()
    return valores