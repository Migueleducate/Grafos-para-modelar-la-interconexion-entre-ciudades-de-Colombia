import mysql.connector

# Configuración de la conexión
db = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='GrafoColombia',
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()


def leer_conexiones(ciudad_id):
    try:
        cursor.callproc("LeerConexiones", [ciudad_id])
        
        for result in cursor.stored_results():
            conexiones = result.fetchall()
            print(f"Conexiones de la ciudad con ID {ciudad_id}:")
            for conexion in conexiones:
                print(f"  {conexion[0]} -> {conexion[1]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def crear_conexion(origen_id, destino_id):
    try:
        cursor.callproc("CrearConexion", [origen_id, destino_id])
        db.commit()
        print(f"Conexión creada: {origen_id} -> {destino_id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def actualizar_conexion(conexion_id, nuevo_destino):
    try:
        cursor.callproc("ActualizarConexion", [conexion_id, nuevo_destino])
        db.commit()  
        print(f"Conexión con ID {conexion_id} actualizada al nuevo destino: {nuevo_destino}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")



def eliminar_conexion(conexion_id):
    try:
        cursor.callproc("EliminarConexion", [conexion_id])
        db.commit() 
        print(f"Conexión con ID {conexion_id} eliminada")
    except mysql.connector.Error as err:
        print(f"Error: {err}")




leer_conexiones(1)


crear_conexion(2, 3)


actualizar_conexion(1, 4)


eliminar_conexion(2)



