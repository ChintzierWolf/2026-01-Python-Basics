# DRILL 5: SISTEMA DE ALERTA INVERSA — BASE ARES

# TODO 1: Usa input() con float() para pedir la temperatura del módulo.
# Guárdala en una variable llamada 'temperatura'.

# TODO 2: Crea una variable 'temperatura_normal' que sea True
# si la temperatura está entre 15 y 30 grados (inclusive en ambos extremos).
# Usa AND para combinar las dos condiciones.

# TODO 3: Crea una variable 'alerta_termica' usando NOT
# para invertir el valor de temperatura_normal.

# TODO 4: Usa print() con f-strings para mostrar ambos resultados.
# "¿Temperatura en rango seguro?: [temperatura_normal]"
# "¿Alerta térmica activa?: [alerta_termica]"

temperatura = float(input("¿Cuál es la temperatura del módulo?: "))
temperatura_normal = 15 <= temperatura <= 30
alerta_termica = not temperatura_normal
print(f"¿Temperatura en rango seguro?: {temperatura_normal}")
print(f"¿Alerta térmica activa?: {alerta_termica}")
