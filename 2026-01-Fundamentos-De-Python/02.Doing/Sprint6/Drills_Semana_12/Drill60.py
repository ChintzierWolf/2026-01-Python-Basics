# DRILL 5: ASOMÁNDONOS AL SISTEMA — IMPORT OS

# TODO 1: Importa el módulo os al inicio del archivo.

import os

# TODO 2: Usa os.getcwd() para obtener el directorio actual.
# Guarda el resultado en una variable llamada 'directorio'.

directorio = os.getcwd()

# TODO 3: Imprime el directorio con una f-string.
# Ejemplo:
# "El sistema está corriendo desde: [ruta]"

print(f"El sistema está corriendo desde: {directorio}")

# TODO 4: Usa os.listdir() para obtener la lista de archivos del directorio.
# Guárdala en una variable llamada 'archivos'.

archivos = os.listdir(directorio)

# TODO 5: Imprime cuántos archivos hay (con len()) y luego itera la lista
# con un for, imprimiendo cada nombre con un guión adelante:
# - archivo1.py
# - archivo2.py
# ...

print(f"Hay {len(archivos)} archivos en el directorio:")
for archivo in archivos:
    print(f"- {archivo}")