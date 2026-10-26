persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Lima",
    "trabajo": "Programadora",
    "estado_civil": "Soltera",
    "pasatiempos": ["leer", "caminar", "cocinar"],
    "mascotas": {
        "nombre": "Firulais",
        "tipo": "Perro"
    }
}
#Acceder a los elementos por separado
print("=== Acceso a elementos por separado ===")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Ciudad: {persona['ciudad']}")
print(f"Trabajo: {persona['trabajo']}")
print(f"Estado civil: {persona['estado_civil']}")
print(f"Pasatiempos: {persona['pasatiempos']}")
print(f"Mascotas: {persona['mascotas']}")

#Iterar sobre las claves
print("\n=== Iterar sobre las claves ===")
for clave in persona.keys():
    print(clave)

#Iterar sobre los valores
print("\n=== Iterar sobre los valores ===")
for valor in persona.values():
    print(valor)

#Iterar sobre las claves y los valores
print("\n=== Iterar sobre las claves y los valores ===")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#Agregar una nueva clave y valor
print("\n=== Agregar una nueva clave y valor ===")
persona["correo"] = "[EMAIL_ADDRESS]"
print(f"Correo: {persona['correo']}")

#Actualizar un valor
print("\n=== Actualizar un valor ===")
persona["edad"] = 26
print(f"Edad: {persona['edad']}")