# DRILL 2: PASES EXTRA — OMAR ACTUALIZA EL EXPEDIENTE

# TODO 1: Crea el diccionario 'periodista' con dos claves:
# "nombre" → "Ana López"
# "pases_extra" → 0

# TODO 2: Suma 1 a la clave "pases_extra" usando el operador +=.

# TODO 3: Suma otro pase más (deberían quedar 2 en total).

# TODO 4: Crea una clave NUEVA llamada "fotografo_confirmado" con valor True.

# TODO 5: Usa una f-string para imprimir un resumen.
# Ejemplo:
# "Ana López tiene 2 pases extra. Fotógrafo confirmado: True"

periodista = {
    "nombre": "Ana López",
    "pases_extra": 0
}

periodista["pases_extra"] += 1
periodista["pases_extra"] += 1
periodista["fotografo_confirmado"] = True

print(f"{periodista['nombre']} tiene {periodista['pases_extra']} pases extra. Fotógrafo confirmado: {periodista['fotografo_confirmado']}")
