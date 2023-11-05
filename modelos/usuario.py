# -----------------------------------------------------------------
# Módulo de funciones sobre usuarios
# -----------------------------------------------------------------

import csv
import os

# Variables globales que usaremos en este módulo
usuarios = []
id_usuario = 1  # Variable para asignar IDs únicos a los usuarios
ruta_archivo_usuarios = 'modelos\\usuarios.csv'

def inicializar_usuarios():
    """
    Inicializa la lista de usuarios.

    Si existe un archivo CSV con datos de usuarios, los importa.
    Si no existe, agrega dos usuarios de ejemplo a la lista.
    """
    global id_usuario
    if os.path.exists(ruta_archivo_usuarios):
        importar_datos_desde_csv()
    else:
        # Agrega dos usuarios de ejemplo a la lista con IDs únicos
        usuarios.append({
            "id": id_usuario,
            "nombre de usuario": "juan",
            "contraseña": "12343",
        })
        id_usuario += 1
        usuarios.append({
            "id": id_usuario,
            "nombre de usuario": "pedro",
            "contraseña": "test-122",
        })
        id_usuario += 1

def crear_usuario(nombre_usuario, contraseña):
    """
    Crea un nuevo usuario con el nombre de usuario y contraseña especificados.

    Parameters:
    nombre_usuario (str): El nombre de usuario del nuevo usuario.
    contraseña (str): La contraseña del nuevo usuario.

    Returns:
    dict: El usuario recién creado, con un ID único.
    """
    global id_usuario
    # Agrega el usuario a la lista con un ID único
    usuarios.append({
        "id": id_usuario,
        "nombre de usuario": nombre_usuario,
        "contraseña": contraseña,
    })
    id_usuario += 1
    exportar_a_csv()
    # Devuelve el usuario recién creado
    return usuarios[-1]

def obtener_usuario_por_id(id_usuario):
    """
    Obtiene un usuario por su ID.

    Parameters:
    id_usuario (int): El ID del usuario a buscar.

    Returns:
    dict: El usuario con el ID especificado, o None si no se encuentra.
    """
    # Recorre la lista de usuarios
    for usuario in usuarios:
        # Si el ID de usuario coincide, devuelve el usuario
        if usuario["id"] == id_usuario:
            return usuario
    # Devuelve None si no se encuentra el usuario
    return None

def obtener_usuarios():
    """
    Obtiene todos los usuarios.

    Returns:
    list: La lista de todos los usuarios.
    """
    # Devuelve la lista de usuarios
    return usuarios

def editar_usuario_por_id(id_usuario, nuevo_nombre_usuario, nueva_contraseña):
    """
    Edita el nombre de usuario y contraseña de un usuario existente.

    Parameters:
    id_usuario (int): El ID del usuario a editar.
    nuevo_nombre_usuario (str): El nuevo nombre de usuario.
    nueva_contraseña (str): La nueva contraseña.

    Returns:
    dict: El usuario editado, o None si no se encuentra.
    """
    # Recorre la lista de usuarios
    for usuario in usuarios:
        # Si el ID de usuario coincide, actualiza el nombre de usuario y la contraseña
        if usuario["id"] == id_usuario:
            usuario["nombre de usuario"] = nuevo_nombre_usuario
            usuario["contraseña"] = nueva_contraseña
            exportar_a_csv()
            return usuario
    # Devuelve None si no se encuentra el usuario
    return None

def eliminar_usuario_por_id(id_usuario):
    """
    Elimina un usuario por su ID.

    Parameters:
    id_usuario (int): El ID del usuario a eliminar.
    """
    global usuarios
    # Crea una nueva lista sin el usuario a eliminar
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id_usuario]
    exportar_a_csv()

def exportar_a_csv():
    """
    Exporta los datos de usuarios a un archivo CSV.
    """
    with open(ruta_archivo_usuarios, 'w', newline='') as csvfile:
        campo_nombres = ['id', 'nombre de usuario', 'contraseña']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)

def importar_datos_desde_csv():
    """
    Importa los datos de usuarios desde un archivo CSV.
    """
    global usuarios
    global id_usuario
    usuarios = []  # Limpiamos la lista de usuarios antes de importar desde el archivo CSV
    with open(ruta_archivo_usuarios, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertimos el ID de cadena a entero
            row['id'] = int(row['id'])
            usuarios.append(row) 
    if len(usuarios)>0:
        id_usuario= usuarios[-1]["id"]+1
    else:
        id_usuario = 1