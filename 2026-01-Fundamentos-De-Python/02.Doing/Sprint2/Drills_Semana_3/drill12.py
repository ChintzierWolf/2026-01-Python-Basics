# DRILL 2: SENSOR DE PRESIÓN ATMOSFÉRICA — BASE ARES

# TODO 1: Usa input() con float() para pedir el nivel de presión detectado.
# Guárdalo en una variable llamada 'presion'.

# TODO 2: Crea una variable 'alerta_roja' que sea True
# si la presión supera 100 unidades.

# TODO 3: Crea una variable 'presion_ideal' que sea True
# si la presión es exactamente 50.

# TODO 4: Usa print() con f-strings para mostrar ambos resultados.
# Ejemplo de salida:
# "¿Alerta por sobrepresión?: [alerta_roja]"
# "¿Presión en nivel óptimo?: [presion_ideal]"

presion = float(input("¿Cuál es la presión detectada?: "))

alerta_roja = presion > 100
presion_ideal = presion == 50

print(f'\n\n¿Alerta por sobrepresión?: {alerta_roja}')
print(f'¿Presión en nivel óptimo?: {presion_ideal}')

print(f'\n\n ############################ Fin del programa ############################\n\n')
