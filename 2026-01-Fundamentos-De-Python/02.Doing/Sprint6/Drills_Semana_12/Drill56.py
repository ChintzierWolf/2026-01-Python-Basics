# DRILL 1: DIVISIÓN SEGURA — CHECO BLINDA EL PROMEDIO

# TODO 1: Crea una variable llamada 'asistentes_totales' con valor 400.
# Crea una variable llamada 'numero_escenarios' con valor 0
# (sí, cero — para forzar el error).

asistentes_totales = 400
numero_escenarios = 0

# TODO 2: Envuelve la división en un bloque try.
# Dentro del try, calcula:
# promedio = asistentes_totales / numero_escenarios
# E imprime el resultado.

try:
    promedio = asistentes_totales / numero_escenarios
    print(promedio)

# TODO 3: Agrega un bloque except ZeroDivisionError que imprima:
# "No hay escenarios registrados, no puedo calcular el promedio."

except ZeroDivisionError:
    print("No hay escenarios registrados, no puedo calcular el promedio.")

# TODO 4: Después del try/except (sin indentación adicional),
# imprime: "El programa sigue vivo."
# Si todo funciona bien, deberías ver el mensaje del except seguido de
# "El programa sigue vivo."

print("El programa sigue vivo.")