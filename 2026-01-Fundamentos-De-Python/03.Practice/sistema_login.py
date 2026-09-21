# SISTEMA DE LOGIN — SonidoLibre
# El primer guardián digital del festival

# TODO 1: Pide el usuario con input() y guárdalo en una variable llamada 'usuario'.

# TODO 2: Pide la contraseña con input() y guárdala en una variable llamada 'password'.

# TODO 3: Escribe un if que verifique si usuario == "admin".
# Dentro de ese bloque (indentado), imprime "Usuario reconocido".

# TODO 4: Dentro del mismo bloque del if de usuario,
# escribe otro if que verifique si password == "1234".
# Si es correcta, imprime "Bienvenido al sistema".
# Si no (else), imprime "Contraseña incorrecta".

# TODO 5: Fuera del bloque del primer if (pegado a la izquierda),
# escribe un else que imprima "Intruso detectado: usuario no reconocido".

usuario = input('ingresa tu usuario: ')
password = input('ingresa tu contraseña: ')

if usuario == 'admin':
    print('Usuario reconocido')
    if password == '1234':
        print('Bienvenido al sistema')
    else:
        print('Contraseña incorrecta.')
else:
    print('Intruso detectado: usuario no reconocido.')