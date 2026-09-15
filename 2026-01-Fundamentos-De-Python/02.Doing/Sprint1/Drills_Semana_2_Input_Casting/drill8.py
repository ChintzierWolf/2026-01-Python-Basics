# DRILL 3: LOS AÑOS DEL FESTIVAL DE DON BETO

# TODO 1: Usa input() con int() para pedir el año de la primera edición
# del festival y guárdalo en una variable llamada 'anio_fundacion'.

# TODO 2: Calcula cuántos años lleva el festival en pie
# restando el año de fundación al año actual (2026).
# Guarda el resultado en una variable llamada 'anos_activo'.

# TODO 3: Usa una f-string para imprimir el mensaje del cartel.
# Ejemplo de salida:
# "SonidoLibre: [anos_activo] años de música independiente."

anio_fundacion = int(input("Ingrese el año de la primera edición del festival: ")) # Variable de tipo int
anos_activo = 2026 - anio_fundacion # Variable de tipo int
print(f"SonidoLibre: {anos_activo} años de música independiente.")

# ¿Qué fue difícil de programar?

# Fue fácil de programar. Solo tuve que usar input() con int() para pedir el año de la primera edición 
# del festival, luego restarle el año actual (2026) para obtener los años activos, y finalmente 
# usar una f-string para imprimir el mensaje del cartel.