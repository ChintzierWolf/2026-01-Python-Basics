# DRILL 6: VERIFICACIÓN DE COMANDANTE — BASE ARES

# TODO 1: Usa input() para pedir el rango del usuario.
# Guárdalo en una variable llamada 'rango'.

# TODO 2: Escribe un if que verifique si el rango es exactamente "comandante".
# Si es True, imprime un mensaje de bienvenida.
# Si es False, el programa no debe imprimir nada.

rango = input('ingresa el rango de usuario: ')

if rango == 'comandante':
    print('Bienvenido al sistema')