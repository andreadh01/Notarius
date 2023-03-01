# en este archivo se van a ejecutar funciones que nos daran los permisos que tienen los usuarios,
# para poder mostrar los campos adecuados en select * y crear el dashboard adecuado para cada usuario
from bdConexion import obtener_conexion
dict_permisos = {}
usuario = {'user':'','pwd':''}
def saveSession(user,pwd):
    global usuario
    usuario["user"] = user
    usuario["pwd"] = pwd
    showGrants(user, pwd)

def getUsuarioLogueado():
    return usuario["user"], usuario["pwd"];

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
		if 'GRANT ALL PRIVILEGES ON `notarius`.*' in texto: 
			dict_permisos['usuario'] = {'SELECT':'','INSERT':'','UPDATE':''}
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
			par_i = texto.index(')')
			subcadena_select = texto[select_i:par_i]
			subcadena_select = subcadena_select.replace("(","")
			par_i=texto.find(')', texto.find(')')+1)
			subcadena_insert = texto[insert_i:par_i]
			subcadena_insert = subcadena_insert.replace("(","")
			par_i = texto.rfind(')')
			subcadena_update = texto[update_i:par_i]
			subcadena_update = subcadena_update.replace("(","")
		else:
			par_i = texto.index(')')
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
	
def getPermisos():
	return dict_permisos