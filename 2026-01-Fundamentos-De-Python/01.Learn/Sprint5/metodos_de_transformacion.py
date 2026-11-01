# 1. Métodos de transformación

# 1.1 LOWER
texto1 = "Hola mundo"
print(texto1.lower())
# Convierte todo el texto a minúsculas
# hola mundo

# 1.2 UPPER
print(texto1.upper())
# Convierte todo el texto a mayúsculas
# HOLA MUNDO

# 1.3 CAPITALIZE
print(texto1.capitalize())
# Convierte la primera letra del texto a mayúscula
# hola mundo

# 1.4 TITLE
print(texto1.title())
# Convierte la primera letra de cada palabra a mayúscula
# Hola Mundo

# 2. Métodos de modificación o limpieza

# 2.1 REPLACE
print(texto1.replace("mundo", "Python"))
# Reemplaza una palabra por otra
# hola python

# 2.2 STRIP
texto2 = "   hola mundo   "
print(texto2.strip())
# Elimina los espacios en blanco al principio y al final
# hola mundo

# 2.2.1 LSTRIP
print(texto2.lstrip())
# Elimina los espacios en blanco al principio
# hola mundo

# 2.2.2 RSTRIP
print(texto2.rstrip())
# Elimina los espacios en blanco al final
# hola mundo

# 2.3 REMOVE
texto3 = "hola mundo"
print(texto3.remove("mundo"))
# Elimina una palabra
# hola

# 3. Métodos de división o unión

# 3.1 SPLIT
lista_texto = texto1.split()
print(lista_texto)
# Divide el texto en una lista de palabras
# ['hola', 'mundo']

# 3.2 JOIN
print(", ".join(lista_texto))
# Une los elementos de la lista en un texto
# hola, mundo

# 3.3 PARTITION
print(texto1.partition("mundo"))
# Divide el texto en 3 partes: antes del separador, el separador y después del separador
# ('hola ', 'mundo', '')

# 4. Métodos de búsqueda

# 4.1 STARTWITH
print(texto1.startswith("Hola"))
# Verifica si el texto empieza con una palabra
# True

"""
url = "https://www.google.com"
if url.startswith("https"):
    print("Es una URL segura")
else:
    print("No es una URL segura")
"""

# 4.2 ENDSWITH
print(texto1.endswith("mundo"))
# Verifica si el texto termina con una palabra
# True

"""
archivo  = "reporte_ventas_enero_2026.csv"
if archivo.endswith(".csv"):
    print("Es un archivo CSV")
else:
    print("No es un archivo CSV")
"""

# 4.3 FIND
print(texto1.find("mundo"))
# Busca la posición de una palabra

"""
texto = "Hola mundo"
if texto.find("mundo") != -1:
    print("La palabra 'mundo' se encuentra en el texto")
else:
    print("La palabra 'mundo' no se encuentra en el texto")
"""

# 4.4 COUNT
print(texto1.count("o"))
# Cuenta la cantidad de una palabra

"""
texto = "Hola mundo"
if texto.count("o") > 1:
    print("La palabra 'mundo' se encuentra en el texto")
else:
    print("La palabra 'mundo' no se encuentra en el texto")
"""

# 5. Métodos de búsqueda avanzada

# 5.1 RFIND
print(texto1.rfind("o"))
# Busca la posición de una palabra de derecha a izquierda


"""
texto = "Hola mundo"
if texto.rfind("o") != -1:
    print("La palabra 'mundo' se encuentra en el texto")
else:
    print("La palabra 'mundo' no se encuentra en el texto")
"""

# 5.2 ISNUMERIC
print(texto1.isnumeric())
# Verifica si el texto es un número
# False

"""
texto = "123"
if texto.isnumeric():
    print("El texto es un número")
else:
    print("El texto no es un número")
"""

# 5.3 ISDECIMAL
print(texto1.isdecimal())
# Verifica si el texto es un decimal
# False

"""
texto = "123"
if texto.isdecimal():
    print("El texto es un decimal")
else:
    print("El texto no es un decimal")
"""

# 5.4 ISDIGIT
print(texto1.isdigit())
# Verifica si el texto es un dígito
# False

# 5.5 ISALPHA
print(texto1.isalpha())
# Verifica si el texto es alfanumérico
# False

# 5.6 ISALNUM
print(texto1.isalnum())
# Verifica si el texto es alfanumérico
# False


