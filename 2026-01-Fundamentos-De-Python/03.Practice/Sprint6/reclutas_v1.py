"""
reclutas = []

print = ("==== ALTA DE RECLUTAS ====")
nombre = input("Ingrese el nombre del recluta: ")
apellido = input("Ingrese el apellido del recluta: ")
edad = int(input("Ingrese la edad del recluta: "))
division = input("Ingrese la división del recluta (Alfa/Beta/Delta): ")
rango = input("Ingrese el rango inicial del recluta (Soldado/Cabo): ")


# Más código en el menú aquí
# Imagina 50 líneas más

nuevo_recluta = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "division": division,
    "rango": rango
    }

reclutas.append(nuevo_recluta)

print(f"Recluta {nombre} agregado exitosamente a la lista {reclutas}")
"""

def pedir_datos_reclutas():

    print = ("==== ALTA DE RECLUTAS ====")
    nombre = input("Ingrese el nombre del recluta: ")
    apellido = input("Ingrese el apellido del recluta: ")
    edad = int(input("Ingrese la edad del recluta: "))
    division = input("Ingrese la división del recluta (Alfa/Beta/Delta): ")
    rango = input("Ingrese el rango inicial del recluta (Soldado/Cabo): ")
    
    return nombre, apellido, edad, division, rango

if registrar_recluta(reclutas, nombre, apellido, edad, division, rango):

    nuevo_recluta = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "division": division,
        "rango": rango
    }
    
    reclutas.append(nuevo_recluta)
    print(f"Recluta {nombre} {apellido} agregado exitosamente")

reclutas = []

def alta_recluta():
    nombre, apellido, edad, division, rango = pedir_datos_reclutas()

    registrar_reclutas(reclutas, nombre, apellido, edad, division, rango)

alta_recluta()
print(f"Recluta {nombre} {apellido} agregado exitosamente")