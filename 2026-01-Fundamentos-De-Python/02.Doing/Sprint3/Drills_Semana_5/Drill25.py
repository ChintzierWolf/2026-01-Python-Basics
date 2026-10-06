# DRILL 5: EL FRENO DE EMERGENCIA DE REGINA

# TODO 1: Define password_correcto = "sonidolibre25".
# TODO 2: Crea un bucle infinito intencional con 'while True:'.
# TODO 3: Dentro del bucle, pide intento = input("Contraseña de la sala de comunicaciones: ").
# TODO 4: Si intento es igual a password_correcto, usa 'break' para romper el ciclo.
# TODO 5: Fuera del bucle, imprime "Acceso a comunicaciones autorizado.".

password_correcto = "sonidolibre25"

while True:
    intento = input("Contraseña de la sala de comunicaciones: ")
    if intento == password_correcto:
        break

print("Acceso a comunicaciones autorizado.")
