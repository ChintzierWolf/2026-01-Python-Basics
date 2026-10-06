# DRILL 8: EL ACUMULADOR DE CHECO

# TODO 1: Antes del bucle, crea una variable 'total_asistentes = 0'.

# TODO 2: Usa 'for hora in range(1, 6):' para recorrer del 1 al 5.
# Dentro del bucle, suma 'hora' al acumulador con +=
# e imprime el progreso: "Hora {hora}: total acumulado {total_asistentes}".

# TODO 3: Fuera del bucle, imprime:
# "Total de asistentes del día: {total_asistentes} mil asistentes"

total_asistentes = 0

for hora in range(1,6):
    total_asistentes += hora
    print(f"Hora {hora}: total acumulado {total_asistentes}")

print(f"Total de asistentes del día: {total_asistentes} mil asistentes")