# Sistema de Ficha de Recluta

print("=== REGISTRO DE RECLUTA ===\n")

# TODO 1: Crea el diccionario 'recluta' con al menos 5 claves:
#   "nombre", "edad", "rango", "puntos" y "especialidad".

# TODO 2: Imprime "--- FICHA COMPLETA ---" y recorre el diccionario
# con un bucle 'for clave, valor in recluta.items():' mostrando
# cada par como "Clave: valor".

# TODO 3: Imprime "--- PROMOCIÓN ---". Cambia el "rango" a "Aprendiz"
# y suma 150 a los "puntos". Imprime el nuevo rango y los puntos totales.

# TODO 4: Agrega dos claves nuevas al diccionario:
#   "proyecto_actual" (un string) y "mentores" (una lista de nombres).

# TODO 5: Imprime "--- CAMPOS DISPONIBLES ---" y recorre solo las claves
# con recluta.keys(), imprimiendo cada una con un prefijo "- ".

# TODO 6: Usa .get("certificaciones", []) para leer un campo que puede
# no existir SIN provocar un KeyError. Imprime el resultado.

# TODO 7: Usa 'if "proyecto_actual" in recluta:' para verificar que existe
# y elimínalo con .pop(), guardando el valor devuelto. Imprime qué eliminaste.

# TODO 8: Imprime "--- FICHA FINAL ---" y vuelve a recorrer el diccionario
# con .items() para mostrar cómo quedó la ficha.

#TODO 1
recluta = {
    "nombre": "Cesar",
    "edad": 25,
    "rango": "Recluta",
    "puntos": 80,
    "especialidad": "Programación"
}

#TODO 2
print("====== FICHA COMPLETA ======")
for clave, valor in recluta.items():
    print(f"{clave}: {valor}")

#TODO 3
print("\n====== PROMOCIÓN ======")
recluta["rango"] = "Aprendiz"
recluta["puntos"] += 150
print(f"Nuevo rango: {recluta['rango']}")
print(f"Puntos totales: {recluta['puntos']}")

#TODO 4
print("\n====== NUEVOS CAMPOS ======")
recluta["proyecto_actual"] = "Calculadora Simple"
recluta["mentores"] = ["Juan", "Maria", "Pedro"]

#TODO 5
print("\n====== CAMPOS DISPONIBLES ======")
for clave in recluta.keys():
    print(f"- {clave}")

#TODO 6
print("\n====== SIN CERTIFICACIONES ======")
print(f"Certificaciones: {recluta.get('certificaciones', [])}")

#TODO 7
print("\n====== ELIMINAR PROYECTO ======")
if "proyecto_actual" in recluta:
    proyecto = recluta.pop("proyecto_actual")
    print(f"Proyecto eliminado: {proyecto}")

#TODO 8
print("\n====== FICHA FINAL ======")
for clave, valor in recluta.items():
    print(f"{clave}: {valor}")