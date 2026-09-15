# Este archivo es para conocer los diferentes tipos de errores en Python.

# --- ERROR 1: NameError ---
# Se produce cuando intentamos usar una variable que no ha sido definida.
# print(mensaje_secreto)

# --- CORRECCIÓN ---
mensaje_secreto = "El código no miente"
print(mensaje_secreto)

# --- ERROR 2: SyntaxError ---
# Se produce cuando el código no sigue las reglas de Python.
# print(f"El código no miente" # Falta el paréntesis de cierre

# --- CORRECCIÓN ---
print(f"El código no miente")

# --- ERROR 3: TypeError ---
# Se produce cuando intentamos realizar una operación entre tipos incompatibles.
# edad = "25"
# print(edad + 5) # No se puede sumar un string y un int

# --- CORRECCIÓN ---
edad = "25"
print(int(edad) + 5)

# --- ERROR 4: ZeroDivisionError ---
# Se produce cuando intentamos dividir por cero.
# print(10 / 0)

# --- CORRECCIÓN ---
print(10 / 2)

# --- ERROR 5: IndexError ---
# Se produce cuando intentamos acceder a un índice que no existe en una lista.
# lista_numeros = [1, 2, 3]
# print(lista_numeros[3]) # El último índice es 2, no 3

# --- CORRECCIÓN ---
lista_numeros = [1, 2, 3]
print(lista_numeros[2])

# --- ERROR 6: KeyError ---
# Se produce cuando intentamos acceder a una clave que no existe en un diccionario.
# diccionario = {"nombre": "Juan", "edad": 25}
# print(diccionario["apellido"]) # La clave "apellido" no existe

# --- CORRECCIÓN ---
diccionario = {"nombre": "Juan", "edad": 25}
print(diccionario["nombre"])