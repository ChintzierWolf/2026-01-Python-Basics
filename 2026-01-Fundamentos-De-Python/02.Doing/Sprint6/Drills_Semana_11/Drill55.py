# DRILL 5: REFACTORIZANDO EL ESPAGUETI DE SOFÍA

# TODO 1: Define una función llamada 'pedir_dato_limpio' que reciba un parámetro
# llamado 'etiqueta' (será el mensaje que se le muestra al usuario).
# Dentro de la función:
#   - Usa input(etiqueta) para pedir el dato.
#   - Aplícale .strip() y .title() para limpiarlo.
#   - Devuelve el resultado con return.

def pedir_dato_limpio(etiqueta):
    return input(etiqueta).strip().title()

# TODO 2: Usa la función TRES veces para pedir tres datos distintos:
# 1. El nombre del artista
# 2. El nombre del medio de prensa
# 3. La zona asignada

nombre_artista = pedir_dato_limpio("Nombre del artista: ")
nombre_medio = pedir_dato_limpio("Nombre del medio de prensa: ")
zona_asignada = pedir_dato_limpio("Zona asignada: ")

# TODO 3: Imprime los tres datos limpios con f-strings.

print(f"Nombre del artista: {nombre_artista}")
print(f"Nombre del medio de prensa: {nombre_medio}")
print(f"Zona asignada: {zona_asignada}")

# TODO 4: Cuenta cuántas líneas escribiste GRACIAS a haber definido la función UNA vez,
# en lugar de repetir el bloque input + strip + title tres veces. (No hay output —
# solo es una reflexión interna).

