# DRILL 4: ELSE Y FINALLY — EL EQUIPO DE LIMPIEZA

# TODO 1: Abre un bloque try.
# Pide al usuario un número entero (cantidad de pulseras impresas)
# y guárdalo en 'pulseras'.

try:
    pulseras = int(input("Cantidad de pulseras impresas: "))

# TODO 2: Agrega un except ValueError que imprima:
# "Error: dato inválido, no se registró nada."

except ValueError:
    print("Error: dato inválido, no se registró nada.")

# TODO 3: Agrega un bloque else que imprima:
# "[pulseras] pulseras registradas correctamente."
# (Solo se ejecuta si el try terminó sin errores)

else:
    print(f"{pulseras} pulseras registradas correctamente.")

# TODO 4: Agrega un bloque finally que imprima:
# "--- Operación concluida (con o sin éxito) ---"
# (Se ejecuta siempre)

finally:
    print("--- Operación concluida (con o sin éxito) ---")

# TODO 5: Prueba dos veces:
# Caso 1: ingresa "100" → debe verse el else y luego el finally.
# Caso 2: ingresa "muchas" → debe verse el except y luego el finally.