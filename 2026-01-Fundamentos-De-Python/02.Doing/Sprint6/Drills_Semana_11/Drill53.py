# DRILL 3: LA VALIDACIÓN DE CREDENCIALES DE REGINA

# TODO 1: Define una función llamada 'tiene_acceso_backstage' que reciba
# un parámetro llamado 'tipo_credencial' (será un string).
# La función debe devolver True si el tipo es "staff" o "artista".
# En cualquier otro caso, debe devolver False.

def tiene_acceso_backstage(tipo_credencial):
    return tipo_credencial == "staff" or tipo_credencial == "artista"

# TODO 2: Llama la función con "artista" e imprime el resultado.

print(tiene_acceso_backstage("artista"))

# TODO 3: Llama la función con "prensa" e imprime el resultado.

print(tiene_acceso_backstage("prensa"))

# TODO 4: Usa la función dentro de un if para imprimir un mensaje legible.
# Ejemplo:
# tipo = "staff"
# if tiene_acceso_backstage(tipo):
#     print("Acceso permitido a backstage")
# else:
#     print("Acceso denegado")

tipo_credencial = "artista"

if tiene_acceso_backstage(tipo_credencial):
    print("Acceso permitido a backstage")
else:
    print("Acceso denegado")