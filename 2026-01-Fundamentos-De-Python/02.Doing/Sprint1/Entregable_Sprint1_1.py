# Definition of Done
# Lee esto antes de escribir código. Tu entregable está completo cuando puedes marcar todos los puntos:

# El programa corre sin errores de principio a fin con datos válidos
# Pide al menos 3 datos al usuario con input()
# Aplica casting correctamente en al menos un dato numérico
# Calcula la edad usando el año de nacimiento y el año actual
# El resumen final usa f-strings — no valores escritos a mano
# Los nombres de las variables son descriptivos y en snake_case
# El mensaje final se lee como una oración con sentido, no como datos sueltos

# ENTREGABLE SPRINT 1: SISTEMA DE BIENVENIDA DE SONIDOLIBRE

print("\n\n=== BIENVENIDO A SONIDOLIBRE 2026 ===\n\n")

# TODO 1: Usa input() para pedir el nombre del asistente
# y guárdalo en una variable.

# TODO 2: Usa input() para pedir la ciudad de origen del asistente.

# TODO 3: Usa input() con int() para pedir el año de nacimiento.
# Recuerda: int() convierte el texto que devuelve input() a número entero.

# TODO 4: Calcula la edad restando el año de nacimiento al año actual (2026).
# Guarda el resultado en una variable llamada 'edad'.

# TODO 5: Usa print() con f-strings para mostrar el resumen de bienvenida.
# Debe incluir el nombre, la ciudad y la edad calculada.
# Ejemplo de salida:
# "Bienvenido a SonidoLibre, [nombre] de [ciudad]. Tienes [edad] años.
# ¡Que disfrutes el festival!"

nombre_del_asistente = input("¿Cuál es tu nombre?: ")
ciudad_de_origen = input("\n¿Cuál es tu ciudad de origen?: ")
año_de_nacimiento = int(input("\n¿Cuál es tu año de nacimiento?: "))
edad = 2026 - año_de_nacimiento

print("\n\n######### CARTA DE PRESENTACIÓN ########")

print(f"\nBienvenido a SonidoLibre, {nombre_del_asistente} de {ciudad_de_origen}. Tienes {edad} años.\n")
print("¡Que disfrutes el festival!\n")

print("######### FIN DEL PROGRAMA ########\n\n")