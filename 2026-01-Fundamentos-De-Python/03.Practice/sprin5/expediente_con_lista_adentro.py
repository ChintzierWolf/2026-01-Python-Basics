#Extra 1 — El expediente con lista adentro. 

# TODO 1
# Crea un diccionario donde una de las claves ("asistentes") tenga como valor una lista con tres nombres. 
# TODO 2
# Imprime solo el segundo nombre de la lista accediendo primero a la clave del diccionario y luego al índice de la lista. 
# Pista: expediente["asistentes"][1].

# Extra 2 — Conteo por zona. 

# TODO 4
# Dado un diccionario acreditaciones (nombre → zona)
# TODO 5
# Crea un nuevo diccionario conteo_zonas donde la clave sea la zona y el valor sea cuántas personas hay asignadas a ella.
# TODO 6
# Recorre con .items() y usa el patrón dict.get(clave, 0) + 1 para sumar sin reventar cuando la zona aparece por primera vez.

# Extra 1 — El expediente con lista adentro.

expediente = {
    "nombre": "Ana López",
    "medio": "Diario del Sur",
    "zona_acceso": "Carpa de prensa",
    "pases_extra": 0,
    "fotografo_confirmado": True,
    "asistentes": ["Diego Ruiz", "Mara Soto", "Elena Vega"],
    "zonas_asignadas": {
        "Carpa de prensa": True,
        "Backstage": False,
        "Zona VIP": False
    }
}

print("El segundo asistente es: ", expediente["asistentes"][1])

#Extra 2 — Conteo por zona.

acreditaciones = {
    "Ana López": "Carpa de prensa",
    "Diego Ruiz": "Backstage",
    "Mara Soto": "Zona VIP"
}

conteo_zonas = {}

for nombre, zona in acreditaciones.items():
    # Nombre es la clave, zona es el valor de el diccionario acreditaciones
    # conteo_zonas.get(zona, 0) es para que no marque error si la clave no existe
    # Y el +1 es para que sume 1 a la clave, si no existe marca 1
    # Es como un contador por zona
    conteo_zonas[zona] = conteo_zonas.get(zona, 0) + 1

print("Conteo por zona: ", conteo_zonas)
