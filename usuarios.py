# en este archivo se van a ejecutar funciones que nos daran los permisos que tienen los usuarios,
# para poder mostrar los campos adecuados en select * y crear el dashboard adecuado para cada usuario
from bdConexion import obtener_conexion
dict_permisos = {}
usuario = {'user':'','pwd':''}
lista_tablas = []

def saveSession(user,pwd):
    global usuario
    usuario["user"] = user
    usuario["pwd"] = pwd
    listaTablas(user,pwd)
    showGrants(user, pwd)
    print(dict_permisos)

def clearSession():
    usuario.clear()
    dict_permisos.clear()
    lista_tablas.clear()
    
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

def getPermisos(tabla):
    return dict_permisos[tabla]

def getListaTablas():
    return lista_tablas

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
        permisos["SELECT"] = lista_columnas 
        permisos["INSERT"] = lista_columnas
        permisos["UPDATE"] = lista_columnas
        dict_permisos[tabla] = permisos
        print(dict_permisos)
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
		if 'GRANT ALL' in texto: 
			permisosAdmin()
			return
		permisos = {}
		select_i = texto.find("SELECT")
		insert_i = texto.find("INSERT")
		update_i = texto.find("UPDATE")
		notarius_i = texto.find("notarius")
		to_i = texto.find("TO")
		nombre_tabla = texto[notarius_i+11:to_i-2]
		print(texto)
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
		permiso_insert = (subcadena_insert.replace(", ",",")).split(" ")
		permiso_update = (subcadena_update.replace(", ",",")).split(" ")
		permisos["INSERT"] = permiso_insert[1] if len(permiso_insert) > 1 else ''
		permisos["SELECT"] = permiso_select[1] if len(permiso_select) > 1 else ''
		permisos["UPDATE"] = permiso_update[1] if len(permiso_update) > 1 else ''
		dict_permisos[nombre_tabla] = permisos
	
def getAllPermisos():
	return dict_permisos