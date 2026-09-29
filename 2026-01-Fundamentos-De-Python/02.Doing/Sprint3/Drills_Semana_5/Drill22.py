# DRILL 2: LA VALIDACIÓN OBSTINADA DE VALENTINA

# TODO 1: Pide la palabra clave con input("Palabra clave del día: ") y guárdala en 'palabra'.
# TODO 2: Usa un while que repita MIENTRAS palabra sea distinto de "area-tecnica".
# TODO 3: Dentro del bucle, vuelve a pedir la palabra con input("Incorrecto. Intenta de nuevo: ").
# TODO 4: Fuera del bucle, imprime "Acceso a zona técnica concedido.".

palabra = input("Palabra clave del día: ")
while palabra != "area-tecnica":
    palabra = input("Incorrecto. Intenta de nuevo: ")
print("Acceso a zona técnica concedido.")