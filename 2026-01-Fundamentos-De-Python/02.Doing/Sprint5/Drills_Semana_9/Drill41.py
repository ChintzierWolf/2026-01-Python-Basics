# DRILL 1: EL PRIMER EXPEDIENTE DE OMAR

# TODO 1: Crea un diccionario llamado 'periodista' con tres pares clave-valor:
# "nombre" → "Ana López"
# "medio" → "Diario del Sur"
# "zona_acceso" → "Carpa de prensa"

# TODO 2: Imprime el diccionario completo con un solo print().

# TODO 3: Imprime SOLO el nombre del periodista usando la clave entre corchetes.
# Ejemplo de salida:
# "Acreditado: Ana López"

periodista = {
    "nombre": "Ana López",
    "medio": "Diario del Sur",
    "zona_acceso": "Carpa de prensa"
}

print("Diccionario del periodista: ",periodista)

print("Acreditado: ",periodista["nombre"])