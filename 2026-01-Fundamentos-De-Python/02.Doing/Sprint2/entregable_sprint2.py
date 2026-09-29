usuarrio = input("Usuario")
contrasena = input("Contraseña")

if usuario  == "Admin":
    if contrasena == "1234":
        print("Acceso total concedido. Bienvenido administrador")
    else:
        print("Contraseña de admin incorrecta. Acceso denegado")

elif usuario == "Invitado":
    if contrasena == "1234":
        print("Bienvenido invitado. Acceso limitado")
    else:
        print("Contraseña de invitado incorrecta. Acceso denegado")
else:
    print("Usuario incorrecto. Acceso denegado")


#-------------- Arbol de decisiones de entregable_sprint2.py -----------------#

"""
Usuario ingresa nombre y contraseña
|
|-- if usuario == "admin"
|      |-- if contrasena == "1234"
|      |      |-- "Acceso total concedido"
|      |
|      |-- else
|             |-- "Contraseña incorrecta"
|
|-- elif usuario == "invitado"
|      |-- "Bienvenido, acceso limitado"
|
|-- else
       |-- "Usuario no encontrado. Acceso denegado."
"""

# ENTREGABLE SPRINT 2: SISTEMA DE LOGIN

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

# TODO 1: Escribe un if que verifique si usuario == "admin".
# Dentro de ese bloque, agrega un if anidado para revisar la contraseña.


# TODO 2: Si contrasena == "1234", imprime:
# "Acceso total concedido. Bienvenido, administrador."


# TODO 3: Si la contraseña del admin es incorrecta, imprime:
# "Contraseña incorrecta. Acceso denegado."


# TODO 4: Agrega un elif para usuario == "invitado".
# El invitado no necesita contraseña.
# Imprime: "Bienvenido, invitado. Tienes acceso limitado."

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso total concedido. Bienvenido, administrador.")
    else:
        print("Contraseña incorrecta. Acceso denegado.")

elif usuario == "invitado":
    print("Bienvenido, invitado. Tienes acceso limitado.")

else:
    print("Usuario no encontrado. Acceso denegado.")