# DRILL 1: EL REGISTRO DE BANDAS DE MATEO

# TODO 1: Usa input() para pedir el nombre de la banda
# y guárdalo en una variable llamada 'nombre_banda'.

# TODO 2: Usa input() para pedir el escenario asignado
# y guárdalo en una variable llamada 'escenario'.

# TODO 3: Usa input() para pedir el horario de prueba de sonido
# y guárdalo en una variable llamada 'horario'.

# TODO 4: Usa una f-string para imprimir un resumen de registro.
# Ejemplo de salida:
# "Registro confirmado: [nombre_banda] — Escenario [escenario] — [horario]"

nombre_banda = input("Ingrese el nombre de la banda: ") # Variable de tipo str
escenario = input("Ingrese el escenario asignado: ") # Variable de tipo str
horario = input("Ingrese el horario de prueba de sonido: ") # Variable de tipo str

print(f"Registro confirmado: {nombre_banda} — Escenario {escenario} — {horario}")