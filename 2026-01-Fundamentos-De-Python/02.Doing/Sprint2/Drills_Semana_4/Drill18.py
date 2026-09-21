# DRILL 8: CLASIFICACIÓN DE ENERGÍA — BASE ARES

# TODO 1: Usa input() con int() para pedir el nivel de batería.
# Guárdalo en una variable llamada 'energia'.

# TODO 2: Escribe un if/elif/else con tres ramas:
# - Si energia < 18: estado Crítico
# - Si energia < 65: estado Moderado
# - En cualquier otro caso: estado Óptimo

# TODO 3: Cada rama debe imprimir un mensaje diferente con el estado correspondiente.

energia = int(input('ingresa el nivel de energia: '))

if energia < 18:
    print('estado crítico')
elif energia < 65:
    print('estado moderado')
else:
    print('estado óptimo')
