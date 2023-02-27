import mysql.connector

def obtener_conexion(user='root', pwd=''):
    return mysql.connector.connect(host='localhost',
                           user=user,
                           password=pwd,
                           database='notarius'
                           )