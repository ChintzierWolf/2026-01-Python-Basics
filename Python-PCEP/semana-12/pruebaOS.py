# os.getcwd() -> Obtiene el directorio actual
# os.listdir('directorio') -> Lista los archivos en el directorio
# os.mkdir('directorio') -> Crea un directorio
# os.rmdir('directorio') -> Elimina un directorio
# os.remove('archivo') -> Elimina un archivo
# os.rename('archivo', 'nuevo_nombre') -> Renombra un archivo
# os.path.exists('archivo') -> Verifica si existe un archivo
# os.path.isfile('archivo') -> Verifica si es un archivo
# os.path.isdir('directorio') -> Verifica si es un directorio

import os

ruta_actual = os.getcwd() # Current Working Directory
print(f"La ruta actual es: {ruta_actual}")

nombre_archivo = "README.md"

if os.path.exists(nombre_archivo):
    if os.path.isfile(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' existe y es un archivo")
    elif os.path.isdir(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' existe y es un directorio")
else:
    print(f"El archivo '{nombre_archivo}' no existe")
    try:
        open(nombre_archivo, "w")
    except FileNotFoundError:
        print("Error: El archivo no existe")

nombre_archivo_2 = ".\Python-PCEP\semana-12\pruebaOS.py"
if os.path.exists(nombre_archivo_2):
    if os.path.isfile(nombre_archivo_2):
        print(f"El archivo '{nombre_archivo_2}' existe y es un archivo")
    elif os.path.isdir(nombre_archivo_2):
        print(f"El archivo '{nombre_archivo_2}' existe y es un directorio")
else:
    print(f"El archivo '{nombre_archivo_2}' no existe")
    try:
        open(nombre_archivo_2, "w")
    except FileNotFoundError:
        print("Error: El archivo no existe")

archivos = os.listdir(ruta_actual) # Listar archivos en el directorio actual
print(f"Los archivos en el directorio actual son: {archivos}")

os.mkdir("nuevo_directorio") # Crear un nuevo directorio
print(f"Directorio 'nuevo_directorio' creado")

os.rmdir("nuevo_directorio") # Eliminar el directorio
print(f"Directorio 'nuevo_directorio' eliminado")

os.remove("archivo.txt") # Eliminar un archivo
print(f"Archivo 'archivo.txt' eliminado")

os.rename("archivo.txt", "nuevo_nombre.txt") # Renombrar un archivo
print(f"Archivo 'archivo.txt' renombrado a 'nuevo_nombre.txt'")

os.path.exists("archivo.txt") # Verificar si existe un archivo
print(f"¿Existe el archivo 'archivo.txt'? {os.path.exists('archivo.txt')}")

os.path.isfile("archivo.txt") # Verificar si es un archivo
print(f"¿Es 'archivo.txt' un archivo? {os.path.isfile('archivo.txt')}")

os.path.isdir("directorio") # Verificar si es un directorio
print(f"¿Es 'directorio' un directorio? {os.path.isdir('directorio')}")