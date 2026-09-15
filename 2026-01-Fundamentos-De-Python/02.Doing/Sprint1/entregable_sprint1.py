# ENTREGABLE SPRINT 1: BIENVENIDA INTERACTIVA

print("--- SISTEMA DE INGRESO INADAPTADOS ---")

# TODO 1: Usa input() para pedir el nombre del usuario y guárdalo en una variable.

# TODO 2: Usa input() para pedir la ciudad de origen del usuario.

# TODO 3: Pide el año de nacimiento del usuario.
# ¡CUIDADO! Aplica el casting con int() envolviendo el input para que sea un número.

# TODO 4: Calcula la edad aproximada restándole el año de nacimiento a 2026.
# (Ej. edad = 2026 - año_nacimiento)

# TODO 5: Usa un print() con f-string para mostrar un resumen espectacular.
# Debe decir algo como: "Bienvenido [nombre] de [ciudad]. Tienes [edad] años, ¡a hackear!"

nombre_usuario = input("Ingrese su nombre: ") # Variable de tipo string
ciudad_usuario = input("Ingrese su ciudad de origen: ") # Variable de tipo string
anio_nacimiento = int(input("Ingrese su año de nacimiento: ")) # Variable de tipo int

edad_usuario = 2026 - anio_nacimiento # Variable de tipo int

print(f"Bienvenido {nombre_usuario} de {ciudad_usuario}. Tienes {edad_usuario} años, ¡a hackear!")

# El proceso de casting es transformar una variable de un tipo a otro. En este caso, estamos transformando una variable de tipo int a una variable de tipo float.